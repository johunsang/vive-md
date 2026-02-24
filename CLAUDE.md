# vive-md 프로젝트 가이드

## 프로젝트 개요
바이브코딩용 개발 가이드 & 방법론 산출물 템플릿 프로젝트. Claude Code가 각 기술 스택에 맞게 바로 코딩하거나, **초기 개발은 워터폴**, **유지보수/운영은 칸반** 방법론에 따른 산출물을 생성할 수 있도록 상세한 가이드를 제공한다.


## 구조
```
├── docs/                                       # 문서 모음
│   ├── research/                               # 논문 & 연구
│   │   ├── multi-agent-orchestration-papers-guide.md
│   │   ├── vibe_coding_orchestration_papers_2025_2026_comprehensive_review.md
│   │   ├── vibe-coding-ontology-research-synthesis.md
│   │   └── debate-2026-02-18T17-43-36.md
│   ├── guides/                                 # 가이드
│   │   └── 문서-기반-프로젝트-설정-가이드.md
│   ├── reports/                                # 보고서
│   │   └── orchestra-report.md
│   ├── octo/                                   # 오케스트레이션 도구
│   └── scrum/                                  # 스크럼 기록
│
├── vibe-coding/                                # 바이브코딩 가이드
│   ├── README.md
│   ├── mcp/                                    # MCP 지식 센터
│   │   ├── README.md                           # MCP 종합 가이드 (아키텍처, Transport, 설정, 프리미티브)
│   │   ├── 01-MCP-서버-개발-가이드.md           # 커스텀 서버 개발 (TS/Python SDK)
│   │   ├── 02-MCP-보안-인증-가이드.md           # OAuth 2.0, 엔터프라이즈 보안
│   │   ├── 03-MCP-실전-패턴-모음.md             # DB, GitHub, 모니터링 통합 패턴
│   │   ├── 04-MCP-서버-카탈로그.md              # 인기 MCP 서버 설정 레시피
│   │   └── Awesome-MCP-Servers-한국어-가이드.md  # 2596개+ MCP 서버 한국어 카탈로그
│   ├── skills/                                 # Skills 지식 센터
│   │   ├── README.md                           # Skills 종합 가이드 (SKILL.md, Frontmatter, 스코프)
│   │   ├── 01-Skills-생성-실전-가이드.md         # 스킬 생성 스텝바이스텝
│   │   ├── 02-Skills-고급-패턴.md               # 동적 컨텍스트, 서브에이전트, Hooks
│   │   └── 03-Skills-실전-예시-모음.md           # PR 리뷰, 배포, 코드 분석 등 실전 예시
│   ├── tools/                                  # 도구별 가이드
│   │   ├── Claude-Code-바이브코딩-가이드.md
│   │   └── Kimi-바이브코딩-가이드.md
│   ├── papers/                                 # 논문 분석
│   │   ├── README.md
│   │   └── multi-agent-orchestration-papers.md
│   ├── prompts/                                # 프롬프트 모음
│   │   ├── README.md
│   │   └── 예시-프롬프트-모음.md
│   └── resources/                              # 추가 자료
│       ├── README.md
│       └── Awesome-Claude-Skills-한국어-가이드.md  # 380개+ Skills 한국어 카탈로그
│
└── templates/                                  # 개발 가이드 & 산출물 템플릿
    ├── spring-boot/Spring-Boot-개발가이드.md   # Spring Boot 3.x (3000줄+)
    ├── vue/Vue3-개발가이드.md                   # Vue 3 + TypeScript (3000줄+)
    ├── react/React-개발가이드.md                # React 18+ + TypeScript (3000줄+)
    ├── nextjs/NextJS-개발가이드.md              # Next.js 14+ App Router (2600줄+)
    ├── design-system/디자인시스템-가이드.md      # UI/UX, 접근성, 다크모드 (2500줄+)
    ├── security/보안-가이드.md                   # OWASP, 인증/인가, API 보안 (2900줄+)
    ├── waterfall/                                # 워터폴 방법론 산출물 템플릿 (초기 개발)
    │   ├── 00-기획/
    │   │   ├── 서비스기획서.md
    │   │   └── 비즈니스정책서.md
    │   ├── 01-요구사항분석/
    │   │   ├── 요구사항명세서-SRS.md
    │   │   ├── 유스케이스명세서.md
    │   │   └── 요구사항추적매트릭스-RTM.md
    │   ├── 02-시스템설계/
    │   │   ├── 시스템아키텍처설계서-SAD.md
    │   │   ├── 데이터베이스설계서.md
    │   │   ├── API설계서.md
    │   │   └── 화면설계서.md
    │   ├── 03-상세설계/
    │   │   └── 상세설계서.md
    │   ├── 05-테스트/
    │   │   ├── 테스트계획서.md
    │   │   ├── 테스트케이스.md
    │   │   └── 테스트결과보고서.md
    │   ├── 06-배포/
    │   │   ├── 배포계획서.md
    │   │   └── 운영가이드.md
    │   ├── 07-유지보수/
    │   │   └── 유지보수계획서.md
    │   └── 08-검토/
    │       ├── 단계별검토-체크리스트.md
    │       ├── UX검토서.md
    │       └── 프로젝트관리-산출물.md
    │
    └── kanban/                                  # 칸반 방법론 산출물 템플릿 (유지보수/운영)
        ├── CLAUDE.md                            # 칸반 종합 가이드
        ├── 01-칸반-보드-설계서.md                 # 보드 구조, WIP, Swimlane, Class of Service
        ├── 02-서비스-수준-협약-SLA.md              # SLA/SLE, 장애등급별 대응시간
        ├── 03-변경요청-관리-프로세스.md             # CR 프로세스, 승인체계, 칸반 연동
        ├── 04-장애-대응-절차서.md                  # 장애 분류, Runbook, Post-mortem
        ├── 05-기술부채-관리대장.md                  # 부채 분류/등록/해소 전략
        ├── 06-릴리스-관리-절차서.md                 # 정기/긴급/핫픽스, 롤백
        ├── 07-운영-모니터링-대시보드-설계서.md       # 시스템/앱/비즈니스/칸반 메트릭
        ├── 08-회고-및-개선-보고서.md                # 칸반 4가지 리뷰, KPT, 개선 추적
        └── 09-인수인계-문서.md                     # 시스템 구성, 운영 정보, KT 계획
```

## 문서 카테고리

### 기술 스택 가이드 (6개)
개발 가이드 문서. 프로젝트에 복사하면 Claude Code가 보안/생산성/성능 모범 사례를 적용.
- 각 문서 2500~3200줄 분량
- 6개 섹션: 프로젝트 개요, 코딩 컨벤션, 보안 필수사항, 생산성 가이드, 성능 최적화, Gotchas

### 워터폴 산출물 템플릿 (14개+) — 초기 개발
워터폴 방법론 각 단계별 산출물의 표준 템플릿. Claude Code에게 "SRS 작성해줘" 요청 시 해당 템플릿 기반으로 산출물 생성.
- [placeholder] 표시로 프로젝트별 내용을 채울 위치 명시
- Mermaid 다이어그램 포함 (flowchart, sequenceDiagram, erDiagram, classDiagram, gantt)
- **적용 단계**: Phase 0(기획) ~ Phase 6(배포)

### 칸반 산출물 템플릿 (9개+) — 유지보수/운영
워터폴 Phase 6(배포) 완료 후 칸반으로 전환하여 유지보수/운영 단계의 산출물을 관리. Claude Code에게 "칸반 보드 설계해줘", "SLA 작성해줘" 요청 시 해당 템플릿 기반으로 산출물 생성.
- 플랫 구조 (숫자 접두사): 칸반은 순차 단계가 없으므로 폴더 중첩 불필요
- 각 문서는 독립적인 Living Document로 지속 갱신
- 워터폴 산출물(유지보수계획서, 운영가이드)의 내용을 계승하되 칸반 고유 개념(SLE, Post-mortem, 흐름 메트릭) 추가
- **적용 단계**: Phase 7(유지보수) 이후 지속

### 검토 문서 (3개)
단계별 검토 체크리스트, UX 검토서, 프로젝트 관리 산출물.
- 닐슨의 10가지 휴리스틱 평가
- WCAG 2.1 AA 접근성 체크리스트
- 위험 관리, WBS, 변경 관리

### 연구 & 논문 문서 (docs/research/)
멀티에이전트 오케스트레이션 및 바이브코딩 관련 논문 분석.
- 2025-2026년 주요 논문 종합 리뷰
- 바이브코딩 온톨로지 연구 종합
- ChatDev, MetaGPT, HyperAgent 등 심층 분석

### 바이브코딩 라이브러리 (vibe-coding/)
바이브코딩 & 멀티에이전트 오케스트레이션 종합 가이드.
- 도구별 바이브코딩 가이드 (Claude Code, Kimi)
- 논문 분석 및 실전 프롬프트 모음
- 추가 자료 및 리소스

### MCP 지식 센터 (vibe-coding/mcp/)
MCP(Model Context Protocol) 종합 가이드. 아키텍처, Transport, 서버 설정/개발/보안부터 실전 패턴과 서버 카탈로그까지.
- 6개 문서, 약 9,700줄 분량
- 커스텀 서버 개발 (TypeScript SDK, Python FastMCP)
- OAuth 2.0 인증, 엔터프라이즈 보안 체크리스트
- DB/GitHub/모니터링 통합 패턴, 공식+커뮤니티 서버 카탈로그
- **2596개+ MCP 서버 한국어 종합 카탈로그** (32개 카테고리, 4개 출처 통합)

### Skills 지식 센터 (vibe-coding/skills/)
Claude Code Skills 종합 가이드. SKILL.md 구조, Frontmatter 레퍼런스, 스킬 생성/고급 패턴/실전 예시.
- 4개 문서, 약 5,300줄 분량
- User-Invocable/Agent 스킬 튜토리얼
- 동적 컨텍스트, String Substitution, CI/CD 통합
- PR 리뷰, 배포 자동화, 보안 스캔 등 8개+ 완전한 예시

## 작성 원칙
- 한국어로 작성, 기술 용어는 영어 유지
- 마크다운 형식, `##` / `###` / `####`로 섹션 구분
- 코드 예시는 실무에서 바로 복사해서 쓸 수 있는 완전한 형태
- 각 스택 고유의 패턴에 집중 (일반적인 소프트웨어 상식은 생략)

## 새 템플릿 추가 시
1. `templates/{category}/` 디렉토리 생성
2. 의미 있는 한국어 파일명으로 `.md` 작성
3. `README.md`의 지원 템플릿 테이블에 추가
