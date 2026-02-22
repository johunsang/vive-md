# Ontology Papers Archive

- 총 논문 수: 58
- PDF 저장 성공: 7
- HTML 저장 성공: 34
- 원문 미확보: 17

## 강화 요약

- **Coverage(범위):** 고전 이론(1993~)부터 LLM 기반 온톨로지 학습/정렬(2023~2025)까지 포함
- **Usability(활용성):** 58편 전부 1:1 번역 문서 생성 완료
- **Risk(리스크):** 미확보 17편은 라이선스/접근 제한으로 전문 정독 불가

## 품질 등급 가이드

| 등급 | 기준 | 권장 사용 |
|---|---|---|
| A | `pdf_saved` + 번역 `ok` | 정밀 정독, 인용 후보, 구현 근거 문서화 |
| B | `pdf_saved` + 번역 `partial_translated` 또는 `html_saved` + 번역 `ok` | 설계 참고, 빠른 스캐닝, 2차 검증 전제 |
| C | `html_saved` + `partial_translated` 또는 `not_downloaded` | 탐색적 참고, 원문 재확보 후 재검증 필요 |

## 빠른 읽기 트랙

1. **입문 트랙 (원칙/방법론):** 1, 2, 3, 5, 9
2. **실무 구축 트랙 (표준/추론/운영):** 7, 21, 26, 27, 32, 33
3. **도메인 확장 트랙 (KG/바이오/IoT):** 35, 36, 40, 41, 42
4. **LLM 전환 트랙 (최신):** 44, 45, 48, 51, 52, 54

## 경로

- 원문: `docs/ontology-papers/originals/`
- 번역: `docs/ontology-papers/translations/`
- 메타: `docs/ontology-papers/meta/manifest.csv`, `docs/ontology-papers/meta/manifest.json`
- 미확보 원문 목록: `docs/ontology-papers/meta/missing-originals.md`

## 메타 파일 읽는 법

- `manifest.csv`의 `download_status`: `pdf_saved` / `html_saved` / `not_downloaded`
- `manifest.csv`의 `translation_status`: `ok` / `partial_translated`
- `used_abstract_fallback=true`: 원문 추출 대신 OpenAlex 초록 기반 번역

## 다음 강화 우선순위

1. 미확보 17편 원문 재수집 (기관 인증/대체 저장소 확인)
2. `partial_translated` 17편 전체 분량 번역 확장
3. A등급 논문 중심으로 “정밀 리뷰(기여/한계/재현성)” 문서 추가

## 주의

- 저작권/접근 제한으로 일부 논문은 PDF가 아닌 HTML 메타 페이지만 저장되거나 미확보 상태일 수 있습니다.
- 번역은 자동 번역 결과이며, 원문 추출 실패 시 OpenAlex 초록 기반으로 생성됩니다.
