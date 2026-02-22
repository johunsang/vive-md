#!/usr/bin/env python3
"""
Fetch original papers (best-effort) and generate 1:1 translation documents.

Input:
  docs/vibe-coding-ontology-research-synthesis.md (section 8 table rows)

Output:
  docs/ontology-papers/originals/
  docs/ontology-papers/translations/
  docs/ontology-papers/meta/manifest.csv
  docs/ontology-papers/meta/manifest.json
"""

from __future__ import annotations

import csv
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MD = ROOT / "docs" / "vibe-coding-ontology-research-synthesis.md"
BASE_DIR = ROOT / "docs" / "ontology-papers"
ORIGINALS_DIR = BASE_DIR / "originals"
TRANSLATIONS_DIR = BASE_DIR / "translations"
META_DIR = BASE_DIR / "meta"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)

MAX_TRANSLATE_CHARS = 12000
REQUEST_TIMEOUT = 30
RETRY_COUNT = 2


def slugify(text: str, max_len: int = 80) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    if not s:
        s = "paper"
    return s[:max_len].rstrip("-")


def parse_table_rows(md_text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in md_text.splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 6:
            continue
        try:
            no = int(parts[0])
            year = int(parts[1])
        except ValueError:
            continue
        rows.append(
            {
                "no": no,
                "year": year,
                "title_en": parts[2],
                "title_ko": parts[3],
                "summary_ko": parts[4],
                "link": parts[5],
            }
        )
    return sorted(rows, key=lambda x: x["no"])


def extract_doi(link: str) -> str | None:
    m = re.search(r"doi\.org/(.+)$", link, re.IGNORECASE)
    if not m:
        return None
    doi = m.group(1).strip().strip("/")
    doi = doi.replace("arXiv.", "arxiv.")
    return doi or None


def invert_abstract(inv: dict[str, list[int]] | None) -> str:
    if not inv:
        return ""
    max_pos = -1
    for pos_list in inv.values():
        if pos_list:
            max_pos = max(max_pos, max(pos_list))
    if max_pos < 0:
        return ""
    words = [""] * (max_pos + 1)
    for word, pos_list in inv.items():
        for pos in pos_list:
            if 0 <= pos < len(words):
                words[pos] = word
    return " ".join(w for w in words if w).strip()


def http_get_json(session: requests.Session, url: str) -> dict[str, Any] | None:
    for _ in range(RETRY_COUNT + 1):
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT)
            if resp.status_code == 200:
                return resp.json()
        except requests.RequestException:
            pass
        time.sleep(1)
    return None


def fetch_openalex_record(
    session: requests.Session, title_en: str, doi: str | None
) -> dict[str, Any] | None:
    if doi:
        doi_url = f"https://api.openalex.org/works/https://doi.org/{quote(doi, safe='')}"
        data = http_get_json(session, doi_url)
        if data and data.get("id"):
            return data

    search_url = (
        "https://api.openalex.org/works?"
        f"search={quote(title_en)}&per-page=1"
        "&select=id,title,doi,ids,abstract_inverted_index,"
        "primary_location,open_access,best_oa_location,content_urls,publication_year"
    )
    data = http_get_json(session, search_url)
    if not data:
        return None
    results = data.get("results") or []
    return results[0] if results else None


def is_pdf_bytes(content: bytes) -> bool:
    return content.startswith(b"%PDF")


def pick_candidate_urls(record: dict[str, Any], source_link: str, doi: str | None) -> list[str]:
    best_oa = record.get("best_oa_location") or {}
    primary = record.get("primary_location") or {}
    open_access = record.get("open_access") or {}
    content_urls = record.get("content_urls") or {}

    urls: list[str] = []
    for u in [
        source_link,
        best_oa.get("pdf_url"),
        best_oa.get("landing_page_url"),
        primary.get("pdf_url"),
        primary.get("landing_page_url"),
        open_access.get("oa_url"),
        content_urls.get("pdf"),
    ]:
        if u and isinstance(u, str):
            urls.append(u)
    if doi:
        urls.append(f"https://doi.org/{doi}")

    deduped: list[str] = []
    seen: set[str] = set()
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        deduped.append(u)
    return deduped


def try_download_original(
    session: requests.Session, urls: list[str], file_stem: str
) -> tuple[str, str | None, str]:
    """
    Returns:
      (download_status, saved_file_path, source_url_used)
    """
    html_fallback: tuple[str | None, str] = (None, "")
    for url in urls:
        for _ in range(RETRY_COUNT + 1):
            try:
                resp = session.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
                if resp.status_code >= 400:
                    time.sleep(0.7)
                    continue
                content = resp.content or b""
                ctype = (resp.headers.get("content-type") or "").lower()

                if "application/pdf" in ctype or is_pdf_bytes(content):
                    out = ORIGINALS_DIR / f"{file_stem}.pdf"
                    out.write_bytes(content)
                    return ("pdf_saved", str(out), url)

                if "text/html" in ctype or b"<html" in content[:500].lower():
                    out = ORIGINALS_DIR / f"{file_stem}.html"
                    out.write_bytes(content)
                    if html_fallback[0] is None:
                        html_fallback = (str(out), url)
            except requests.RequestException:
                pass
            time.sleep(0.7)

    if html_fallback[0]:
        return ("html_saved", html_fallback[0], html_fallback[1])
    return ("not_downloaded", None, "")


def extract_text_from_file(path_str: str | None) -> str:
    if not path_str:
        return ""
    path = Path(path_str)
    if not path.exists():
        return ""

    try:
        if path.suffix.lower() == ".pdf":
            reader = PdfReader(str(path))
            chunks: list[str] = []
            for page in reader.pages:
                txt = page.extract_text() or ""
                if txt.strip():
                    chunks.append(txt.strip())
            return "\n\n".join(chunks).strip()
        if path.suffix.lower() == ".html":
            html = path.read_text(encoding="utf-8", errors="ignore")
            soup = BeautifulSoup(html, "lxml")
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()
            text = soup.get_text("\n")
            lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
            return "\n".join(lines).strip()
    except Exception:
        return ""
    return ""


def split_for_translation(text: str, max_chars: int = 1200) -> list[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    if not paras:
        paras = [text.strip()] if text.strip() else []
    chunks: list[str] = []
    cur = ""
    for p in paras:
        if not cur:
            cur = p
            continue
        if len(cur) + 2 + len(p) <= max_chars:
            cur += "\n\n" + p
        else:
            chunks.append(cur)
            cur = p
    if cur:
        chunks.append(cur)
    return chunks


def translate_chunk_via_google(session: requests.Session, text: str) -> str:
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "ko",
        "dt": "t",
        "q": text,
    }
    resp = session.get(url, params=params, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    segments = data[0] if isinstance(data, list) and data else []
    out = []
    for seg in segments:
        if isinstance(seg, list) and seg:
            out.append(seg[0] or "")
    return "".join(out).strip()


def translate_text_ko(text: str, session: requests.Session) -> tuple[str, str]:
    if not text.strip():
        return "", "no_source_text"
    clipped = text[:MAX_TRANSLATE_CHARS]
    chunks = split_for_translation(clipped, max_chars=1000)

    out_chunks: list[str] = []
    failed = 0
    for ch in chunks:
        ok = False
        for _ in range(RETRY_COUNT + 1):
            try:
                out_chunks.append(translate_chunk_via_google(session, ch))
                ok = True
                time.sleep(0.15)
                break
            except Exception:
                time.sleep(0.35)
        if not ok:
            failed += 1
            out_chunks.append("")
    merged = "\n\n".join([c for c in out_chunks if c.strip()]).strip()
    if not merged:
        return "", "translation_failed"
    status = "ok"
    if len(text) > MAX_TRANSLATE_CHARS:
        status = "partial_translated"
    if failed:
        status = f"{status}_with_{failed}_failed_chunks"
    return merged, status


def build_translation_doc(
    row: dict[str, Any],
    manifest_entry: dict[str, Any],
    source_text: str,
    translated_text: str,
) -> str:
    src_preview = source_text[:MAX_TRANSLATE_CHARS].strip()
    return (
        f"# [{row['no']:02d}] {row['title_ko']}\n\n"
        f"- 영문 제목: {row['title_en']}\n"
        f"- 연도: {row['year']}\n"
        f"- 원문 링크: {row['link']}\n"
        f"- DOI: {manifest_entry.get('doi') or 'N/A'}\n"
        f"- 원문 저장 상태: {manifest_entry.get('download_status')}\n"
        f"- 원문 파일: {manifest_entry.get('original_file') or 'N/A'}\n"
        f"- 번역 상태: {manifest_entry.get('translation_status')}\n\n"
        "## 원문(추출 텍스트)\n\n"
        f"{src_preview or '[원문 텍스트를 추출하지 못했습니다. OpenAlex 초록만 확보된 경우 메타에 기록됨]'}\n\n"
        "## 한국어 번역\n\n"
        f"{translated_text or '[자동 번역 실패]'}\n"
    )


def main() -> None:
    ORIGINALS_DIR.mkdir(parents=True, exist_ok=True)
    TRANSLATIONS_DIR.mkdir(parents=True, exist_ok=True)
    META_DIR.mkdir(parents=True, exist_ok=True)

    md_text = SOURCE_MD.read_text(encoding="utf-8")
    rows = parse_table_rows(md_text)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})

    manifest: list[dict[str, Any]] = []

    for row in rows:
        no = row["no"]
        stem = f"{no:02d}_{slugify(row['title_en'])}"
        doi = extract_doi(row["link"])

        openalex = fetch_openalex_record(session, row["title_en"], doi) or {}
        if not doi:
            doi = openalex.get("doi")
            if isinstance(doi, str):
                doi = doi.replace("https://doi.org/", "")
        abstract_en = invert_abstract(openalex.get("abstract_inverted_index"))

        candidate_urls = pick_candidate_urls(openalex, row["link"], doi)
        download_status, original_file, source_url_used = try_download_original(
            session, candidate_urls, stem
        )

        extracted_text = extract_text_from_file(original_file)
        source_text_for_translation = extracted_text or abstract_en
        translated_ko, translation_status = translate_text_ko(
            source_text_for_translation, session
        )

        translation_file = TRANSLATIONS_DIR / f"{stem}.md"
        entry = {
            "no": no,
            "year": row["year"],
            "title_en": row["title_en"],
            "title_ko": row["title_ko"],
            "link": row["link"],
            "doi": doi or "",
            "openalex_id": openalex.get("id", ""),
            "download_status": download_status,
            "original_file": original_file or "",
            "source_url_used": source_url_used,
            "text_chars": len(source_text_for_translation or ""),
            "translation_chars": len(translated_ko or ""),
            "translation_status": translation_status,
            "translation_file": str(translation_file),
            "used_abstract_fallback": bool(abstract_en and not extracted_text),
        }

        doc_text = build_translation_doc(
            row=row,
            manifest_entry=entry,
            source_text=source_text_for_translation,
            translated_text=translated_ko,
        )
        translation_file.write_text(doc_text, encoding="utf-8")
        manifest.append(entry)
        print(
            f"[{no:02d}/58] {download_status} | {translation_status} | {row['title_en']}",
            flush=True,
        )

    json_out = META_DIR / "manifest.json"
    csv_out = META_DIR / "manifest.csv"
    json_out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    with csv_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(manifest[0].keys()))
        writer.writeheader()
        writer.writerows(manifest)

    readme = BASE_DIR / "README.md"
    pdf_cnt = sum(1 for m in manifest if m["download_status"] == "pdf_saved")
    html_cnt = sum(1 for m in manifest if m["download_status"] == "html_saved")
    miss_cnt = sum(1 for m in manifest if m["download_status"] == "not_downloaded")
    readme.write_text(
        (
            "# Ontology Papers Archive\n\n"
            f"- 총 논문 수: {len(manifest)}\n"
            f"- PDF 저장 성공: {pdf_cnt}\n"
            f"- HTML 저장 성공: {html_cnt}\n"
            f"- 원문 미확보: {miss_cnt}\n\n"
            "## 경로\n\n"
            "- 원문: `docs/ontology-papers/originals/`\n"
            "- 번역: `docs/ontology-papers/translations/`\n"
            "- 메타: `docs/ontology-papers/meta/manifest.csv`, `docs/ontology-papers/meta/manifest.json`\n\n"
            "## 주의\n\n"
            "- 저작권/접근 제한으로 일부 논문은 PDF가 아닌 HTML 메타 페이지만 저장되거나 미확보 상태일 수 있습니다.\n"
            "- 번역은 자동 번역 결과이며, 원문 추출 실패 시 OpenAlex 초록 기반으로 생성됩니다.\n"
        ),
        encoding="utf-8",
    )

    print("\nDone.")
    print(f"PDF: {pdf_cnt}, HTML: {html_cnt}, Missing: {miss_cnt}")


if __name__ == "__main__":
    main()
