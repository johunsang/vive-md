# Awesome MCP Servers 한국어 종합 가이드

> **2596개+ MCP 서버**를 32개 카테고리로 정리한 한국어 종합 가이드
>
> 출처: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (공식), [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers), [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers), [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)
>
> 최종 갱신: 2026-02-25

## 목차

- [🔧 공식 레퍼런스 서버](#공식-레퍼런스-서버) (7개)
- [📦 아카이브 (공식 이전 서버)](#아카이브-(공식-이전-서버)) (13개)
- [🤖 AI 플랫폼 & 모델](#ai-플랫폼--모델) (146개)
- [🗄️ 데이터베이스](#데이터베이스) (163개)
- [☁️ 클라우드 & 인프라](#클라우드--인프라) (119개)
- [🌐 브라우저 & 웹](#브라우저--웹) (84개)
- [📝 소스 제어 & 코드 관리](#소스-제어--코드-관리) (31개)
- [📋 프로젝트 관리](#프로젝트-관리) (64개)
- [📊 모니터링 & 옵저버빌리티](#모니터링--옵저버빌리티) (78개)
- [📈 마케팅 & CRM](#마케팅--crm) (30개)
- [🔒 보안](#보안) (66개)
- [🧪 테스팅 & QA](#테스팅--qa) (8개)
- [📉 데이터 분석 & BI](#데이터-분석--bi) (44개)
- [🔗 API & 통합](#api--통합) (38개)
- [⚡ 자동화 & 워크플로우](#자동화--워크플로우) (70개)
- [🔍 검색 엔진](#검색-엔진) (57개)
- [📁 파일 & 문서 관리](#파일--문서-관리) (170개)
- [🎨 디자인 & UI](#디자인--ui) (18개)
- [💬 커뮤니케이션](#커뮤니케이션) (77개)
- [📱 소셜미디어](#소셜미디어) (56개)
- [🎮 미디어 & 엔터테인먼트](#미디어--엔터테인먼트) (53개)
- [💰 금융 & 커머스](#금융--커머스) (189개)
- [🗺️ 지도 & 위치 & 여행](#지도--위치--여행) (36개)
- [🔌 IoT & 하드웨어](#iot--하드웨어) (25개)
- [🏥 헬스 & 의료](#헬스--의료) (32개)
- [⚖️ 법률 & 계약](#법률--계약) (7개)
- [🎓 교육 & 연구](#교육--연구) (82개)
- [🌤️ 날씨 & 시간](#날씨--시간) (18개)
- [🖥️ 시스템 & 데스크톱](#시스템--데스크톱) (36개)
- [💻 코드 실행 & 개발](#코드-실행--개발) (48개)
- [📚 리소스 & 도구](#리소스--도구) (54개)
- [🔗 SaaS & 플랫폼 통합](#saas--플랫폼-통합) (677개)

---

## 🔧 공식 레퍼런스 서버

> Anthropic이 제공하는 MCP 레퍼런스 구현체

| 서버 | 설명 |
|------|------|
| [**Everything**](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) | 프롬프트, 리소스, 도구를 포함한 레퍼런스/테스트 서버 |
| [**Fetch**](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | LLM 효율적 사용을 위한 웹 콘텐츠 가져오기 및 변환 |
| [**Filesystem**](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 설정 가능한 접근 제어를 통한 안전한 파일 작업 |
| [**Git**](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Git 저장소 읽기, 검색, 조작 도구 |
| [**Memory**](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | 지식 그래프 기반의 영구 메모리 시스템 |
| [**Sequential Thinking**](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) | 사고 시퀀스를 통한 동적이고 반성적인 문제 해결 |
| [**Time**](https://github.com/modelcontextprotocol/servers/tree/main/src/time) | 시간 및 타임존 변환 기능 |

---

## 📦 아카이브 (공식 이전 서버)

> 공식 레포에서 아카이브된 서버 (커뮤니티에서 유지보수 중)

| 서버 | 설명 |
|------|------|
| [**AWS KB Retrieval**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/aws-kb-retrieval-server) | Bedrock Agent Runtime을 사용한 AWS Knowledge Base 검색 |
| [**Brave Search**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search) | Brave Search API를 사용한 웹 및 로컬 검색. 공식 서버로 대체됨 |
| [**EverArt**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/everart) | 다양한 모델을 사용한 AI 이미지 생성 |
| [**GitHub**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) | 저장소 관리, 파일 작업, GitHub API 통합 |
| [**GitLab**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab) | GitLab API를 통한 프로젝트 관리 |
| [**Google Drive**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gdrive) | Google Drive 파일 접근 및 검색 기능 |
| [**Google Maps**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) | 위치 서비스, 길찾기, 장소 상세 정보 |
| [**PostgreSQL**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) | 스키마 검사를 포함한 읽기 전용 데이터베이스 접근 |
| [**Puppeteer**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer) | 브라우저 자동화 및 웹 스크래핑 |
| [**Redis**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/redis) | Redis 키-값 저장소와 상호작용 |
| [**Sentry**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sentry) | Sentry.io에서 이슈 조회 및 분석 |
| [**Slack**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack) | 채널 관리 및 메시징 기능. 현재 Zencoder에서 유지보수 |
| [**SQLite**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite) | 데이터베이스 상호작용 및 비즈니스 인텔리전스 기능 |

---

## 🤖 AI 플랫폼 & 모델

> OpenAI, Ollama, HuggingFace 등 AI/ML 서비스 연동

| 서버 | 설명 |
|------|------|
| [**0x1abin/matter-controller-mcp**](https://github.com/0x1abin/matter-controller-mcp) | Matter Controller용 MCP 서버. AI 에이전트가 Matter 디바이스를 제어하고 상호작용 |
| [**2niuhe/plantuml_web**](https://github.com/2niuhe/plantuml_web) | MCP 서버 통합을 갖춘 웹 기반 PlantUML 프론트엔드. PlantUML 이미지 생성 및 구문 검증 지원 |
| [**82ch/MCP-Dandan**](https://github.com/82ch/MCP-Dandan) | MCP 서버용 실시간 보안 프레임워크. 도구 호출 패턴과 의도를 분석하여 악성 AI 에이전트 행위 감지 및 차단 |
| [**Aganium/agenium**](https://github.com/Aganium/agenium) | MCP 서버를 agent:// 네트워크에 연결. AI 에이전트를 위한 DNS 유사 ID, 발견, 신뢰 체계. mTLS, 신뢰 점수, 기능 검색을 통한 도구 공개 |
| [**Agentic Framework**](https://github.com/Piotr1215/mcp-agentic-framework) | AI 에이전트 등록, 상호 발견, HTTP를 통한 비동기 메시지 교환, 영구 메시지 기록을 통한 멀티에이전트 협업 프레임워크 |
| [**agentmail-toolkit/mcp**](https://github.com/agentmail-to/agentmail-toolkit/tree/main/mcp) | 즉석에서 인박스를 생성하여 이메일을 보내고, 받고, 작업을 수행하는 MCP 서버. AI 에이전트를 위한 이메일 인프라 |
| [**AIM-Intelligence/AIM-Guard-MCP**](https://github.com/AIM-Intelligence/AIM-MCP) | AI 에이전트를 위한 안전 가이드라인 및 콘텐츠 분석을 제공하는 보안 중심 MCP 서버 |
| [**aktsmm/skill-ninja-mcp-server**](https://github.com/aktsmm/skill-ninja-mcp-server) | MCP용 Agent Skill Ninja: GitHub 저장소에서 AI 에이전트 스킬(SKILL.md) 검색, 설치, 관리. 140개 이상 사전 색인 스킬 지원 |
| [**AllVoiceLab**](https://www.allvoicelab.com/mcp) | TTS, 음성 복제, 비디오 번역 기능을 갖춘 AI 음성 툴킷. 스마트 에이전트 통합을 위한 MCP 서버로 제공 |
| [**Allyson**](https://github.com/isaiahbjork/allyson-mcp) | Allyson 플랫폼을 사용하여 정적 파일을 애니메이션 SVG 컴포넌트로 변환하는 AI 기반 SVG 애니메이션 생성기 |
| [**Amazon Bedrock Nova Canvas**](https://github.com/zxkane/mcp-server-amazon-bedrock) | Amazon Nova Canvas 모델을 사용한 이미지 생성 기능을 제공합니다. |
| [**andybrandt/mcp-simple-openai-assistant**](https://github.com/andybrandt/mcp-simple-openai-assistant) | OpenAI Assistants와 대화하는 MCP. Claude가 GPT 모델을 어시스턴트로 활용 가능 |
| [**APT MCP**](https://github.com/GdMacmillan/apt-mcp-server) | AI 에이전트를 사용하여 Debian 패키지 매니저(apt) 명령을 실행하는 MCP 서버 |
| [**Atla**](https://github.com/atla-ai/atla-mcp-server) | AI 에이전트가 Atla API를 통해 최신 LLM 평가를 수행할 수 있도록 지원 |
| [**Atlan**](https://github.com/atlanhq/agent-toolkit/tree/main/modelcontextprotocol) | Atlan 서비스와 다양한 도구를 통해 상호작용할 수 있는 MCP 서버 |
| [**Atlassian**](https://github.com/sooperset/mcp-atlassian) | Atlassian Cloud 제품(Confluence, Jira)과 상호작용. Confluence 페이지 검색/읽기, Jira 이슈 접근, 프로젝트 메타데이터 조회 |
| [**Atlassian Server (by phuc-nt)**](https://github.com/phuc-nt/mcp-atlassian-server) | AI 에이전트(Cline, Claude Desktop, Cursor 등)를 Atlassian Jira & Confluence에 연결하는 MCP 서버 |
| [**austenstone/myinstants-mcp**](https://github.com/austenstone/myinstants-mcp) | myinstants.com의 수백만 밈 사운드를 제공하는 사운드보드 MCP 서버. 검색, 재생, 카테고리 탐색 지원 |
| [**awkoy/replicate-flux-mcp**](https://github.com/awkoy/replicate-flux-mcp) | Replicate API를 통해 이미지를 생성하는 기능을 제공하는 MCP 서버. |
| [**AWS Bedrock KB Retrieval**](https://github.com/awslabs/mcp/tree/main/src/bedrock-kb-retrieval-mcp-server) | 자연어를 사용하여 Amazon Bedrock Knowledge Base에서 데이터 소스의 관련 정보를 검색 |
| [**aymericzip/intlayer**](https://github.com/aymericzip/intlayer) | Intlayer i18n/CMS 도구의 AI 기반 IDE 지원 MCP 서버. 스마트 CLI 접근, 버전 관리 문서 제공 |
| [**Azure OpenAI DALL-E 3 MCP Server**](https://github.com/jacwu/mcp-server-aoai-dalle3) | 텍스트로부터 이미지를 생성하는 Azure OpenAI DALL-E 3 서비스용 MCP 서버 |
| [**back1ply/agent-skill-loader**](https://github.com/back1ply/agent-skill-loader) | 파일 복사 없이 Claude Code 스킬을 AI 에이전트에 동적 로드. 스킬 검색, 읽기, 온디맨드 설치 |
| [**billster45/mcp-chatgpt-responses**](https://github.com/billster45/mcp-chatgpt-responses) | Claude가 ChatGPT와 대화하고 ChatGPT의 웹 검색 기능을 활용할 수 있도록 하는 MCP 서버입니다. |
| [**BlockRunAI/x-grow**](https://github.com/BlockRunAI/x-grow) | X/Twitter 알고리즘 최적화 도구. 게시물 작성, 리뷰 점수, AI 이미지 생성으로 참여도 극대화 |
| [**bolivian-peru/baozi-mcp**](https://github.com/bolivian-peru/baozi-mcp) | Baozi.bet에서 Solana 예측 시장과 상호작용하는 68개 도구. 마켓 탐색, 베팅, 상금 수령, 마켓 생성 지원 |
| [**Buildable**](https://github.com/chunkydotdev/bldbl-mcp) | Buildable AI 기반 개발 플랫폼의 공식 MCP 서버. 작업 관리, 진행 추적, 프로젝트 컨텍스트 조회, 소프트웨어 프로젝트 협업 지원 |
| [**Cartesia**](https://github.com/cartesia-ai/cartesia-mcp) | Cartesia 음성 플랫폼에 연결하여 TTS, 음성 복제 등 수행 |
| [**Chimera-Protocol/csl-core**](https://github.com/Chimera-Protocol/csl-core) | Z3 형식 검증을 사용한 결정론적 AI 안전 정책 엔진. MCP를 통해 기계 검증 가능한 AI 에이전트 제약 조건 작성 및 시행 |
| [**CircleCI**](https://github.com/CircleCI-Public/mcp-server-circleci) | AI 에이전트가 CircleCI 빌드 실패를 수정할 수 있도록 지원 |
| [**CLDGeminiPDF Analyzer**](https://github.com/tfll37/CLDGeminiPDF-Analyzer) | 대용량 PDF 파일을 API를 통해 Google LLM에 공유하여 추가 분석 및 Claude Desktop으로의 응답 검색을 가능하게 하는 MCP 서버 도구. |
| [**Computer-Use - Remote MacOS Use**](https://github.com/baryhuang/mcp-remote-macos-use) | OpenAI Operator의 오픈소스 대안. 원격 macOS 머신을 자율 AI 에이전트로 활용하는 풀 데스크톱 경험 제공 |
| [**cqfn/aibolit-mcp-server**](https://github.com/cqfn/aibolit-mcp-server) | AI 에이전트의 리팩토링 핫스팟 식별 지원. AI가 '코드 개선 방법'을 이해하도록 돕는 도구 |
| [**Currents**](https://github.com/currents-dev/currents-mcp) | Currents에 보고된 Playwright 테스트 실패를 AI 에이전트가 수정할 수 있도록 지원 |
| [**cyclops-ui/mcp-cyclops**](https://github.com/cyclops-ui/mcp-cyclops) | Cyclops 추상화를 통해 AI 에이전트가 Kubernetes 리소스를 관리할 수 있는 MCP 서버 |
| [**DAISYS**](https://github.com/daisys-ai/daisys-mcp) | DAISYS 플랫폼을 사용한 고품질 TTS 및 음성 출력 생성 |
| [**debtstack-ai/debtstack-python**](https://github.com/debtstack-ai/debtstack-python) | AI 에이전트용 기업 부채 구조 데이터. 250개 이상 발행사, 5,000개 이상 채권의 레버리지 비율, 선순위, 약관, FINRA TRACE 가격 정보 검색 |
| [**DeepL**](https://github.com/DeepLcom/deepl-mcp-server) | DeepL API를 사용하여 DeepL의 AI 모델로 텍스트 번역 및 재작성 |
| [**DeepSeek MCP Server**](https://github.com/DMontgomery40/deepseek-mcp-server) | DeepSeek의 고급 언어 모델과 기타 유용한 API 엔드포인트를 통합하는 MCP 서버 |
| [**deepseek-thinker-mcp**](https://github.com/ruixingshi/deepseek-thinker-mcp) | DeepSeek의 추론 콘텐츠를 Claude Desktop 등 MCP 지원 AI 클라이언트에 제공하는 MCP 서버 |
| [**Deepseek_R1**](https://github.com/66julienmartin/MCP-server-Deepseek_R1) | Claude Desktop과 DeepSeek 언어 모델(R1/V3)을 연결하는 MCP 서버 구현 |
| [**DINO-X**](https://github.com/IDEA-Research/DINO-X-MCP) | Dino-X 기반의 고급 컴퓨터 비전 및 객체 감지 MCP 서버. 이미지 분석, 객체 감지, 키포인트 식별, 시각적 이해 작업 지원 |
| [**dorukardahan/domain-search-mcp**](https://github.com/dorukardahan/domain-search-mcp) | 가격 포함 빠른 도메인 가용성 집계. Porkbun, Namecheap, GoDaddy, RDAP & WHOIS 확인. 대량 검색, 등록기관 비교, AI 추천 지원 |
| [**duaraghav8/MCPJungle**](https://github.com/duaraghav8/MCPJungle) | 엔터프라이즈 AI 에이전트를 위한 자체 호스팅 MCP 서버 레지스트리 |
| [**dune-analytics-mcp**](https://github.com/kukapay/dune-analytics-mcp) | Dune Analytics 데이터를 AI 에이전트에 연결하는 MCP 서버 |
| [**edgarriba/prolink**](https://github.com/edgarriba/prolink) | 에이전트 간 마켓플레이스 미들웨어 — MCP 네이티브 발견, 협상, AI 에이전트 간 거래 |
| [**effytech/freshdesk-mcp**](https://github.com/effytech/freshdesk_mcp) | Freshdesk와 통합하여 AI 모델이 Freshdesk 모듈과 상호작용하고 다양한 지원 작업을 수행하는 MCP 서버 |
| [**ElevenLabs**](https://github.com/mamertofabian/elevenlabs-mcp-server) | ElevenLabs TTS API와 통합하여 다양한 음성으로 보이스오버를 생성하는 서버 |
| [**ElevenLabs**](https://github.com/elevenlabs/elevenlabs-mcp) | ElevenLabs 공식 MCP 서버. |
| [**espadaw/Agent47**](https://github.com/espadaw/Agent47) | 9개 이상 플랫폼(x402, RentAHuman, Virtuals 등)에 걸친 AI 에이전트 통합 작업 수집기 |
| [**Gemini Bridge**](https://github.com/eLyiN/gemini-bridge) | 공식 CLI를 통해 Claude가 Google의 Gemini AI와 상호작용할 수 있게 하는 경량 MCP 서버. API 비용 없음, 상태 비저장 아키텍처. |
| [**GetCacheOverflow/CacheOverflow**](https://github.com/GetCacheOverflow/CacheOverflow) | AI 에이전트 지식 마켓플레이스. 솔루션 공유 및 토큰 획득. 기존 해결된 문제를 검색하여 토큰 및 연산 비용 절감 |
| [**ggRMCP**](https://github.com/aalobaidi/ggRMCP) | gRPC 서비스를 MCP 호환 도구로 변환하는 Go 게이트웨이. Claude 같은 AI 모델이 gRPC 서비스를 직접 호출 가능 |
| [**gNucleus Text-To-CAD**](https://github.com/gNucleus/text-to-cad-mcp) | gNucleus AI 모델을 사용하여 텍스트로부터 CAD 부품 및 어셈블리 생성 |
| [**Google Vertex AI Search**](https://github.com/ubie-oss/mcp-vertexai-search) | Gemini 모델을 사용자의 프라이빗 데이터로 그라운딩하여 Google Vertex AI Search 결과를 제공합니다. |
| [**gregm711/agent-domain-service-mcp**](https://github.com/gregm711/agent-domain-service-mcp) | AgentDomainService.com을 통한 AI 기반 도메인 브레인스토밍, 분석, 가용성 확인. API 키 불필요 |
| [**hamflx/imagen3-mcp**](https://github.com/hamflx/imagen3-mcp) | Google Imagen 3.0 API를 사용한 강력한 이미지 생성 도구. 고급 사진, 예술적, 포토리얼리스틱 제어를 통한 고품질 이미지 생성 |
| [**harrison/ai-counsel**](https://github.com/harrison/ai-counsel) | AI 모델 간 다라운드 토론을 가능하게 하는 숙의 합의 엔진. 구조화된 투표, 수렴 감지, 영구 결정 그래프 메모리 |
| [**hashgraph-online/hashnet-mcp-js**](https://github.com/hashgraph-online/hashnet-mcp-js) | Registry Broker용 MCP 서버. Hashgraph 네트워크에서 AI 에이전트 발견, 등록, 채팅 |
| [**Hugging Face**](https://huggingface.co/settings/mcp) | Hugging Face Hub API에 프로그래밍 방식으로 연결합니다: Spaces와 논문의 시맨틱 검색, 데이터셋과 모델 탐색, 호환 MCP Gradio 도구 Spaces에 접근합니다. |
| [**HuggingFace Spaces**](https://github.com/evalstate/mcp-hfspace) | HuggingFace Spaces를 사용하여 오픈소스 이미지, 오디오, 텍스트 모델 등을 지원하는 MCP 서버. Claude Desktop 모드 간편 통합. |
| [**Image Generation**](https://github.com/GongRzhe/Image-Generation-MCP-Server) | Replicate Flux 모델을 사용한 이미지 생성 기능을 제공하는 MCP 서버 |
| [**Intelligent Image Generator**](https://github.com/shinpr/mcp-image) | AI 향상을 통해 간단한 프롬프트를 전문가 수준 이미지로 변환 |
| [**isaac-levine/forage**](https://github.com/isaac-levine/forage) | AI 에이전트를 위한 자가 개선 도구 발견. 레지스트리 검색, MCP 서버 서브프로세스 설치, 세션 간 도구 지식 유지 |
| [**it-tools-mcp**](https://github.com/wrenchpilot/it-tools-mcp) | CorentinTh it-tools 유틸리티를 AI 에이전트용으로 재구현한 MCP 서버. 인코딩, 디코딩, 변환 등 다양한 개발자 도구 제공 |
| [**JamesANZ/cross-llm-mcp**](https://github.com/JamesANZ/cross-llm-mcp) | 서로 다른 AI 모델 간 대화 및 메모리 공유를 가능하게 하는 크로스 LLM 통신 MCP 서버 |
| [**janreges/ai-distiller-mcp**](https://github.com/janreges/ai-distiller) | 대규모 코드베이스에서 핵심 코드 구조를 AI가 소화 가능한 형태로 추출. 기존 API를 올바르게 사용하는 코드 작성 지원 |
| [**jaspertvdm/mcp-server-gemini-bridge**](https://github.com/jaspertvdm/mcp-server-gemini-bridge) | Google Gemini API 브릿지. MCP를 통해 Gemini Pro 및 Flash 모델에 접근합니다. |
| [**jaspertvdm/mcp-server-inject-bender**](https://github.com/jaspertvdm/mcp-server-inject-bender) | AI 기반 유머 방어로 SQL 인젝션 및 XSS 시도를 무해한 코미디 응답으로 변환하는 보안 도구 |
| [**jaspertvdm/mcp-server-ollama-bridge**](https://github.com/jaspertvdm/mcp-server-ollama-bridge) | 로컬 Ollama LLM 서버 브릿지. MCP를 통해 Llama, Mistral, Qwen 등 로컬 모델 실행 |
| [**jaspertvdm/mcp-server-openai-bridge**](https://github.com/jaspertvdm/mcp-server-openai-bridge) | OpenAI API 브릿지. MCP를 통해 GPT-4, GPT-4o 등 OpenAI 모델 접근 |
| [**joinly**](https://github.com/joinly-ai/joinly) | 브라우저 기반 미팅 플랫폼(Zoom, Teams, Google Meet)과 상호작용하는 MCP 서버. 실시간 트랜스크립트, 텍스트 발화, 메시지 전송 지원 |
| [**K-Dense-AI/claude-skills-mcp**](https://github.com/K-Dense-AI/claude-skills-mcp) | 모든 모델과 클라이언트가 [Claude Agent Skills](https://www.anthropic.com/news/skills)를 네이티브처럼 사용할 수 있게 해주는 지능형 검색 기능. |
| [**kiarash-portfolio-mcp**](https://kiarash-adl.pages.dev/.well-known/mcp.llmfeed.json) | Ed25519 서명 발견이 포함된 WebMCP 지원 포트폴리오. AI 에이전트가 프로젝트, 스킬 조회 및 터미널 명령 실행 가능 |
| [**Kiln**](https://github.com/Kiln-AI/Kiln) | 프로덕션 수준의 AI 시스템 구축을 위한 무료 오픈소스 플랫폼. RAG 파이프라인, AI 에이전트, MCP 도구 호출, 평가, 합성 데이터 생성, 파인튜닝을 통합 지원 |
| [**KirokuForms**](https://www.kirokuforms.com/ai/mcp) | AI 기반 폼 플랫폼으로 전문 폼 빌더와 HITL(Human-in-the-Loop) 기능을 결합. 커스텀 폼 생성, 제출 수집, 사람의 감독 통합 |
| [**kj455/mcp-kibela**](https://github.com/kj455/mcp-kibela) | AI 모델이 Kibela와 상호작용할 수 있도록 지원 |
| [**Kokoro TTS**](https://github.com/mberg/kokoro-tts-mcp) | Kokoro TTS를 사용하여 텍스트를 MP3로 변환. S3 자동 업로드 옵션 지원 |
| [**Kubeflow Spark History MCP Server**](https://github.com/kubeflow/mcp-apache-spark-history-server) | AI 에이전트가 Spark 작업 성능을 분석하고 병목 현상을 식별하며 인사이트를 제공 |
| [**kukapay/dex-pools-mcp**](https://github.com/kukapay/dex-pools-mcp) | AI 에이전트에 실시간 DEX 유동성 풀 데이터 접근을 제공하는 MCP 서버 |
| [**kukapay/etf-flow-mcp**](https://github.com/kukapay/etf-flow-mcp) | AI 에이전트의 의사결정을 위한 암호화폐 ETF 유입/유출 데이터 제공 |
| [**kukapay/raydium-launchlab-mcp**](https://github.com/kukapay/raydium-launchlab-mcp) | AI 에이전트가 Raydium Launchpad(LaunchLab)에서 토큰을 출시, 매수, 매도할 수 있는 MCP 서버 |
| [**kukapay/web3-jobs-mcp**](https://github.com/kukapay/web3-jobs-mcp) | AI 에이전트에 큐레이션된 Web3 채용 정보를 실시간으로 제공하는 MCP 서버 |
| [**KYC-mcp-server**](https://github.com/vishnurudra-ai/KYC-mcp-server) | Claude Desktop 호환 KYC(Know Your Computer) MCP 서버. Windows, macOS, Linux에 대한 종합 시스템 진단 및 AI 기반 권장사항 제공 |
| [**Lingo.dev**](https://github.com/lingodotdev/lingo.dev/blob/main/mcp.md) | Lingo.dev 로컬라이제이션 엔진을 사용하여 AI 에이전트가 모든 언어를 지원하도록 설정 |
| [**LlamaCloud**](https://github.com/run-llama/mcp-server-llamacloud) | LlamaCloud MCP 서버. LlamaCloud의 관리형 인덱스에 연결하는 TypeScript 기반 MCP 서버. |
| [**louis030195/gptzero-mcp**](https://github.com/louis030195/gptzero-mcp) | GPTZero API를 사용한 텍스트 콘텐츠 AI 감지. AI 생성 텍스트 감지, 신뢰도 점수, 다국어 지원(프랑스어/스페인어), 상세 확률 분석을 제공합니다. |
| [**MasterGo**](https://github.com/mastergo-design/mastergo-magic-mcp) | MasterGo 디자인 도구와 AI 모델을 연결하는 서버. AI 모델이 MasterGo 디자인 파일에서 DSL 데이터를 직접 검색 가능 |
| [**Mastra/mcp**](https://github.com/mastra-ai/mastra/tree/main/packages/mcp) | Mastra 클라이언트 구현. MCP 호환 AI 모델 및 도구와의 원활한 통합 제공 |
| [**mbailey/voice-mcp**](https://github.com/mbailey/voice-mcp) | STT, TTS, 실시간 음성 대화를 지원하는 완전한 음성 상호작용 서버. 로컬 마이크, OpenAI 호환 API, LiveKit 통합 |
| [**MCP Context Provider**](https://github.com/doobidoo/MCP-Context-Provider) | AI 모델에 영구적인 도구별 컨텍스트와 규칙을 제공하는 정적 서버. 채팅 세션 간 컨텍스트 손실 방지 |
| [**MCPfinder**](https://github.com/mcpfinder/server) | AI 에이전트의 "App Store": MCP 생태계 내에서 AI 기능을 검색, 설치, 수익화 |
| [**MCPJungle**](https://github.com/mcpjungle/MCPJungle) | 엔터프라이즈 AI 에이전트를 위한 자체 호스팅 MCP 레지스트리 및 게이트웨이 |
| [**mercurialsolo/counsel-mcp**](https://github.com/mercurialsolo/counsel-mcp) | 전략적 추론, 다관점 토론 분석, 대화형 자문 세션을 위해 AI 에이전트를 Counsel API에 연결 |
| [**Modao Proto MCP**](https://github.com/modao-dev/modao-proto-mcp) | 자연어 설명을 완전한 HTML 코드로 변환하는 AI 기반 프로토타입 생성 서버. 모던 디자인 및 반응형 레이아웃 지원 |
| [**Multi-Model Advisor**](https://github.com/YuChenSSR/multi-ai-advisor-mcp) | 여러 Ollama 모델에 쿼리를 분배하고 인사이트를 종합하여 다각적인 AI 관점을 제공하는 MCP 서버입니다. |
| [**mzxrai/mcp-openai**](https://github.com/mzxrai/mcp-openai) | OpenAI의 최신 모델과 대화 |
| [**Nanana**](https://github.com/nanana-app/mcp-server-nano-banana) | Google Gemini Nano Banana 기반의 AI 텍스트-이미지 생성기 및 이미지-이미지 편집기를 제공하는 MCP |
| [**OctoMind-dev/octomind-mcp**](https://github.com/OctoMind-dev/octomind-mcp) | AI 에이전트가 코드베이스 또는 Jira, Slack, TestRail 등에서 Octomind E2E 테스트를 생성 및 실행 |
| [**oerc-s/primordia**](https://github.com/oerc-s/primordia) | AI 에이전트 경제 정산. 영수증 확인, 미터 발행(무료). 순정산, 크레딧 라인, 감사 등급 대차대조표(유료/402) |
| [**OpenAI**](https://github.com/pierrebrunelle/mcp-server-openai) | MCP 프로토콜을 사용하여 Claude에서 OpenAI 모델을 직접 쿼리 |
| [**OpenAI GPT Image**](https://github.com/SureScaleAI/openai-gpt-image-mcp) | OpenAI GPT 이미지 생성/편집 MCP 서버 |
| [**OpenAI WebSearch MCP**](https://github.com/ConechoAI/openai-websearch-mcp) | OpenAI `web_search` 내장 도구를 제공하는 Python 기반 MCP 서버 |
| [**OpenSearch**](https://github.com/opensearch-project/opensearch-mcp-server-py) | OpenSearch에 저장된 데이터에 대해 AI 에이전트가 검색 및 분석을 수행할 수 있는 MCP 서버 |
| [**Osseni94/keyneg-mcp**](https://github.com/Osseni94/keyneg-mcp) | 95개 이상 레이블의 엔터프라이즈급 감성 분석, 키워드 추출, AI 에이전트용 배치 처리 |
| [**OthmaneBlial/term_mcp_deepseek**](https://github.com/OthmaneBlial/term_mcp_deepseek) | 터미널용 DeepSeek MCP 유사 서버 |
| [**ovlabs/mcp-server-originalvoices**](https://github.com/ovlabs/mcp-server-originalvoices) | 1:1 디지털 트윈 네트워크를 조회하여 실제 사용자의 생각과 이유를 즉시 파악. AI 에이전트에 진정한 인간 컨텍스트 제공 |
| [**oxgeneral/agentnet**](https://github.com/oxgeneral/agentnet) | AI 에이전트가 서로 발견, 추천, 소개하는 에이전트 간 추천 네트워크. 양방향 신뢰 모델, 크레딧 경제, 7개 MCP 도구 제공 |
| [**PandaDoc**](https://developers.pandadoc.com/docs/use-pandadoc-mcp-server) | PandaDoc MCP 서버에 AI 개발 도구를 연결하여 AI 기반 PandaDoc 통합 활용 |
| [**Patronus AI**](https://github.com/patronus-ai/patronus-mcp-server) | AI 에이전트 및 RAG 앱 테스트, 평가, 최적화 |
| [**Pearl**](https://github.com/Pearl-com/pearl_mcp_server) | Pearl API와 상호작용하는 공식 MCP 서버. AI 에이전트를 12,000명 이상의 인증 전문가와 즉시 연결 |
| [**Pearl**](https://mcp.pearl.com) | Pearl API와 상호작용하는 공식 MCP 서버. AI 에이전트를 12,000명 이상의 인증 전문가와 즉시 연결 |
| [**Perplexity**](https://github.com/tanigami/mcp-server-perplexity) | Perplexity와 상호작용 |
| [**Perplexity**](https://github.com/ppl-ai/modelcontextprotocol) | Perplexity의 Sonar API에 연결하여 대화형 AI에서 실시간 웹 전체 리서치를 가능하게 하는 MCP 서버입니다. |
| [**pgtuner_mcp**](https://github.com/isdaniel/pgtuner_mcp) | AI 기반 PostgreSQL 성능 튜닝 기능 제공 |
| [**phisanti/MCPR**](https://github.com/phisanti/MCPR) | R 언어용 MCP: AI 에이전트가 대화형 라이브 R 세션에 참여 가능 |
| [**poll-the-people/customgpt-mcp**](https://github.com/Poll-The-People/customgpt-mcp) | CustomGPT.ai의 환각 방지 RAG-as-a-service API 엔드포인트에 접근하는 MCP 서버입니다. |
| [**Postman**](https://github.com/postmanlabs/postman-mcp-server) | Postman의 원격 MCP 서버로 AI 에이전트, 어시스턴트, 챗봇을 Postman의 API에 직접 연결 |
| [**predictive-maintenance-mcp**](https://github.com/LGDiMaggio/predictive-maintenance-mcp) | AI 기반 예측 유지보수 및 고장 진단. 진동 분석, 베어링 진단, ISO 20816-3 준수, 산업 기계용 ML 이상 감지 |
| [**Qwen_Max**](https://github.com/66julienmartin/MCP-server-Qwen_Max) | Qwen 모델을 위한 MCP 서버 구현입니다. |
| [**RAD Security**](https://github.com/rad-security/mcp-server) | Kubernetes 및 클라우드 환경에 대한 AI 기반 보안 인사이트를 제공하는 RAD Security 플랫폼과 상호작용 |
| [**Replicate**](https://github.com/deepfates/mcp-replicate) | 간단한 도구 기반 인터페이스를 통해 Replicate에서 머신러닝 모델을 검색, 실행, 관리합니다. 모델 탐색, 예측 생성, 상태 추적, 생성된 이미지 처리를 지원합니다. |
| [**Retio-ai/pagemap**](https://github.com/Retio-ai/Retio-pagemap) | ~100K 토큰 HTML을 2-5K 토큰 구조화 맵으로 압축. AI 에이전트가 97% 적은 토큰으로 웹 페이지를 읽고 상호작용 |
| [**rsdouglas/janee**](https://github.com/rsdouglas/janee) | 런타임에 자체 도구를 생성하고 개선하는 자기 진화 MCP 서버. LLM 기반 도구 생성으로 AI 에이전트가 자체 기능을 동적으로 확장 |
| [**sim-xia/skill-cortex-server**](https://github.com/Sim-xia/skill-cortex-server) | 모든 IDE/CLI에서 Claude Code Skills 기능에 접근할 수 있게 하는 MCP 서버입니다. |
| [**ssatama/rescuedogs-mcp-server**](https://github.com/ssatama/rescuedogs-mcp-server) | 유럽 및 영국 단체의 구조견을 AI 기반 성격 매칭과 상세 프로필로 검색 및 발견 |
| [**stape-io/stape-mcp-server**](https://github.com/stape-io/stape-mcp-server) | Stape 플랫폼용 MCP 서버. Claude 또는 Cursor 같은 AI 기반 IDE에서 Stape API와 상호작용 |
| [**Strata**](https://www.klavis.ai/) | 수천 개의 도구를 점진적으로 안내하는 MCP 서버. 컨텍스트 과부하를 제거하고 정확한 도구 선택을 보장 |
| [**Sunra AI**](https://github.com/sunra-ai/sunra-clients/tree/main/mcp-server) | Sunra.ai에서 AI 모델 검색 및 실행. 비디오, 이미지, 3D 모델 콘텐츠 생성 및 관리 |
| [**TcpSocketMCP**](https://github.com/SpaceyKasey/TcpSocketMCP/) | 원시 TCP 소켓 접근을 제공하는 MCP 서버. AI 모델이 네트워크 서비스와 직접 상호작용 가능. 다중 동시 연결 지원 |
| [**Thena**](https://mcp.thena.ai) | Thena 서비스와 상호작용하고 Slack, Email, Web, Discord 등 다양한 채널에서 고객을 관리하는 MCP 서버 |
| [**Ticket-Generator MCP**](https://github.com/trycon/ticket-generator-mcp) | Streamable HTTP 전송으로 구현된 MCP 서버. AI 모델이 Ticket Generator API와 상호작용하여 이벤트 목록 조회 및 티켓 생성 |
| [**Ticketmaster MCP Server**](https://github.com/mochow13/ticketmaster-mcp-server) | Streamable HTTP 전송으로 구현된 MCP 서버. AI 모델이 Ticketmaster Discovery API를 통해 이벤트, 장소, 어트랙션 검색 |
| [**Tldv**](https://gitlab.com/tldv/tldv-mcp-server) | tl;dv를 통해 AI 에이전트를 Google Meet, Zoom, Microsoft Teams에 연결 |
| [**tubasasakunn/context-apps-mcp**](https://github.com/tubasasakunn/context-apps-mcp) | MCP를 통해 Claude와 Todo, Idea, Journal, Timer 앱을 연결하는 AI 기반 생산성 도구 모음 |
| [**vectorize-io/hindsight**](https://github.com/vectorize-io/hindsight) | Hindsight: 인간 기억처럼 작동하는 에이전트 메모리. AI 에이전트의 장기 메모리 관리용 |
| [**Voice Status Report**](https://github.com/tomekkorbak/voice-status-report-mcp-server) | OpenAI TTS API를 사용하여 음성 상태 업데이트를 제공하는 MCP 서버. Cursor 또는 Claude Code와 함께 사용 |
| [**VoiceMode**](https://github.com/mbailey/voicemode) | OpenAI 호환 STT/TTS 서비스를 사용하여 Claude와 음성 대화 지원 |
| [**vscode-ai-model-detector**](https://github.com/thisis-romar/vscode-ai-model-detector) | VS Code Copilot에서 실시간 AI 모델 감지. Chat Participant API를 통해 활성 모델(Claude, GPT, Gemini)을 식별하여 Git 기여자 표시 지원 |
| [**Wanaku MCP Router**](https://github.com/wanaku-ai/wanaku/) | 엔터프라이즈 시스템을 AI 에이전트와 통합할 수 있는 SSE 기반 확장 가능 라우팅 엔진을 제공하는 MCP 서버 |
| [**WaveSpeed**](https://github.com/WaveSpeedAI/mcp-server) | AI 에이전트에 이미지 및 비디오 생성 기능을 제공하는 WaveSpeed MCP 서버 |
| [**WordPress MCP**](https://github.com/Automattic/wordpress-mcp) | WordPress 사이트를 간단한 MCP 서버로 변환하여 LLM 및 AI 에이전트에 기능 노출 |
| [**Wren Engine**](https://github.com/Canner/wren-engine) | MCP 클라이언트 및 AI 에이전트를 위한 시맨틱 엔진 |
| [**x51xxx/codex-mcp-tool**](https://github.com/x51xxx/codex-mcp-tool) | IDE 또는 AI 어시스턴트를 Codex CLI에 연결하여 다중 모델(gpt-5-codex, o3, codex-1) 지원 코드 분석 및 편집을 제공하는 MCP 서버. |
| [**x51xxx/copilot-mcp-server**](https://github.com/x51xxx/copilot-mcp-server) | IDE 또는 AI 어시스턴트를 GitHub Copilot CLI에 연결하여 코드 분석, 리뷰, 배치 처리를 수행하는 MCP 서버입니다. |
| [**yuvalsuede/agent-media**](https://github.com/yuvalsuede/agent-media) | 7개 모델(Kling, Veo, Sora, Seedance, Flux, Grok Imagine)에 통합 접근하는 AI 비디오/이미지 생성 CLI 및 MCP 서버 |

---

## 🗄️ 데이터베이스

> PostgreSQL, MongoDB, Redis 등 DB 연동 및 벡터 스토어

| 서버 | 설명 |
|------|------|
| [**AgentMode**](https://www.agentmode.app) | 단일 MCP 서버에서 수십 개의 데이터베이스, 데이터 웨어하우스, GitHub 등에 연결. Docker 이미지를 로컬, 클라우드, 온프레미스에서 실행 |
| [**Airtable**](https://github.com/domdomegg/airtable-mcp-server) | 스키마 검사를 포함한 Airtable 데이터베이스 읽기/쓰기 접근 |
| [**Airtable**](https://github.com/felores/airtable-mcp) | Airtable MCP 서버 |
| [**Aiven**](https://github.com/Aiven-Open/mcp-aiven) | Aiven 프로젝트 탐색 및 PostgreSQL, Apache Kafka, ClickHouse, OpenSearch 서비스와 상호작용 |
| [**alexanderzuev/supabase-mcp-server**](https://github.com/alexander-zuev/supabase-mcp-server) | SQL 쿼리 실행 및 데이터베이스 탐색 도구를 지원하는 Supabase MCP 서버 |
| [**Alibaba Cloud AnalyticDB for MySQL**](https://github.com/aliyun/alibabacloud-adb-mysql-mcp-server) | AnalyticDB for MySQL 클러스터에 연결하여 데이터베이스/테이블 메타데이터 조회, 데이터 쿼리 및 분석 |
| [**Alibaba Cloud AnalyticDB for PostgreSQL**](https://github.com/aliyun/alibabacloud-adbpg-mcp-server) | AnalyticDB for PostgreSQL 인스턴스에 연결하여 데이터 쿼리 및 분석하는 MCP 서버 |
| [**Apache Doris**](https://github.com/apache/doris-mcp-server) | MPP 기반 실시간 데이터 웨어하우스인 Apache Doris용 MCP 서버 |
| [**Apache Pinot**](https://github.com/startreedata/mcp-pinot) | 고처리량, 저지연 실시간 애플리케이션을 위한 오픈소스 OLAP 데이터베이스 Apache Pinot에서 실시간 분석 쿼리 실행 |
| [**ArangoDB**](https://github.com/ravenwits/mcp-server-arangodb) | ArangoDB를 통한 데이터베이스 상호작용 기능을 제공하는 MCP 서버 |
| [**Astra DB**](https://github.com/datastax/astra-db-mcp) | DataStax Astra DB NoSQL 데이터베이스에서 컬렉션 및 문서 관리를 위한 종합 도구. 생성, 수정, 삭제, 검색 및 벌크 작업 지원 |
| [**Azure ADX**](https://github.com/pab1it0/adx-mcp-server) | Azure Data Explorer 데이터베이스 쿼리 및 분석 |
| [**Baserow**](https://gitlab.com/baserow/baserow/-/tree/develop/backend/src/baserow/api/mcp) | MCP 통합을 사용하여 Baserow 자체 호스팅 또는 SaaS 데이터베이스에서 데이터 쿼리 |
| [**benborla29/mcp-server-mysql**](https://github.com/benborla/mcp-server-mysql) | Node.js로 설정 가능한 접근 제어 및 스키마 검사를 갖춘 MySQL 데이터베이스 통합 |
| [**bram2w/baserow**](https://github.com/bram2w/baserow) | Baserow 데이터베이스 통합. 테이블 검색, 목록, 행 CRUD 기능 제공 |
| [**c4pt0r/mcp-server-tidb**](https://github.com/c4pt0r/mcp-server-tidb) | 스키마 검사 및 쿼리 기능을 갖춘 TiDB 데이터베이스 통합 |
| [**Chroma**](https://github.com/chroma-core/chroma-mcp) | 오픈소스 AI 애플리케이션 데이터베이스로 임베딩, 벡터 검색, 문서 저장, 전문 검색 제공 |
| [**Chroma**](https://github.com/privetin/chroma) | Chroma 기반 시맨틱 문서 검색 및 메타데이터 필터링을 위한 벡터 데이터베이스 서버 |
| [**Chroma Package Search**](https://trychroma.com/package-search) | Claude 또는 Cursor 같은 코딩 에이전트에 추가하여 수천 개의 의존성을 이해하고 효과적으로 사용 가능 |
| [**ClickHouse**](https://github.com/ClickHouse/mcp-clickhouse) | ClickHouse 데이터베이스 서버 쿼리 |
| [**CloudBase**](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit) | Tencent CloudBase의 서버리스 클라우드 함수와 데이터베이스를 통한 위챗 미니프로그램 및 풀스택 앱 원스톱 백엔드 서비스 |
| [**Cloudera Iceberg**](https://github.com/cloudera/iceberg-mcp-server) | Open Data Lakehouse에서 AI 활용 지원 |
| [**cobanov/teslamate-mcp**](https://github.com/cobanov/teslamate-mcp) | TeslaMate 데이터베이스에 접근하여 AI 어시스턴트가 Tesla 차량 데이터 및 분석을 쿼리하는 MCP 서버 |
| [**CockroachDB**](https://github.com/amineelkouhen/mcp-cockroachdb) | 자연어를 사용하여 AI 에이전트와 LLM이 CockroachDB를 관리, 모니터링, 쿼리하는 MCP 서버 |
| [**CockroachDB MCP Server**](https://github.com/viragtripathi/cockroachdb-mcp-server) | FastAPI와 CockroachDB로 구축된 완전한 MCP 구현. 스키마 부트스트래핑, JSONB 스토리지, LLM 지원 CLI 제공 |
| [**context-portal**](https://github.com/GreatScottyMac/context-portal) | Context Portal(ConPort)은 프로젝트별 지식 그래프를 구축하는 메모리 뱅크 데이터베이스 시스템. 결정, 진행 상황, 아키텍처 등 엔티티 캡처 |
| [**davewind/mysql-mcp-server**](https://github.com/dave-wind/mysql-mcp-server) | Cursor 및 n8n용 사용자 친화적 읽기 전용 MySQL MCP 서버 |
| [**DBHub**](https://github.com/bytebase/dbhub/) | MySQL, MariaDB, PostgreSQL, SQL Server에 연결하는 범용 데이터베이스 MCP 서버 |
| [**DBUtils**](https://github.com/donghao1393/mcp-dbutils) | PostgreSQL과 SQLite를 깔끔한 추상화 레이어로 원활하게 통합하는 MCP용 통합 데이터베이스 접근 서비스 |
| [**deadletterq/mcp-opennutrition**](https://github.com/deadletterq/mcp-opennutrition) | OpenNutrition 데이터베이스에서 30만 개 이상의 식품, 영양 정보, 바코드를 검색하는 로컬 MCP 서버 |
| [**DevDb**](https://github.com/damms005/devdb-vscode?tab=readme-ov-file#mcp-configuration) | IDE 내에서 실행되는 MCP 서버. MySQL, Postgres, SQLite, MSSQL 데이터베이스 연결 |
| [**Dolt**](https://github.com/dolthub/dolt-mcp) | 버전 관리 Dolt 데이터베이스용 공식 MCP 서버 |
| [**Dot (GetDot.ai)**](https://docs.getdot.ai/dot/integrations/mcp) | Dot AI 데이터 분석가로 데이터베이스/데이터 웨어하우스(Snowflake, BigQuery, Redshift 등)의 데이터를 가져오기, 분석, 시각화 |
| [**DPLP**](https://github.com/szeider/mcp-dblp) | DBLP 컴퓨터 과학 서지 데이터베이스 검색 |
| [**drakonkat/wizzy-mcp-tmdb**](https://github.com/drakonkat/wizzy-mcp-tmdb) | AI 어시스턴트가 영화, TV 프로그램, 인물 정보를 검색하고 조회할 수 있는 TMDB API용 MCP 서버 |
| [**DreamFactory**](https://github.com/dreamfactorysoftware/df-mcp/) | RBAC를 통해 온프레미스 및 클라우드 MS SQL Server, MySQL, PostgreSQL 데이터베이스에 안전하게 접근하는 MCP 서버 |
| [**Druid MCP Server**](https://github.com/iunera/druid-mcp-server) | Apache Druid 클러스터 관리 및 분석을 위한 도구, 리소스, 프롬프트를 제공하는 STDIO/SSE MCP 서버 |
| [**DynamoDB-Toolbox**](https://www.dynamodbtoolbox.com/docs/databases/actions/mcp-toolkit) | 스키마와 접근 패턴을 활용하여 자연어로 DynamoDB 데이터베이스와 상호작용 |
| [**Elasticsearch**](https://github.com/elastic/mcp-server-elasticsearch) | Elasticsearch에서 데이터 쿼리 |
| [**Elasticsearch**](https://github.com/cr7258/elasticsearch-mcp-server) | Elasticsearch 상호작용을 제공하는 MCP 서버 구현 |
| [**Elasticsearch Memory**](https://github.com/fredac100/elasticsearch-memory-mcp) | 계층적 분류, 시맨틱 검색, 지능형 자동 감지를 갖춘 영구 메모리. PyPI를 통해 설치 |
| [**ergut/mcp-bigquery-server**](https://github.com/ergut/mcp-bigquery-server) | Google BigQuery에 직접 접근하여 데이터베이스 쿼리를 수행하는 서버 구현 |
| [**erikhoward/adls-mcp-server**](https://github.com/erikhoward/adls-mcp-server) | Azure Data Lake Storage용 MCP 서버. 컨테이너 관리, 파일 읽기/쓰기/업로드/다운로드, 파일 메타데이터 관리 |
| [**f4ww4z/mcp-mysql-server**](https://github.com/f4ww4z/mcp-mysql-server) | 안전한 MySQL 데이터베이스 작업을 제공하는 Node.js 기반 MySQL 통합 |
| [**FalkorDB**](https://github.com/FalkorDB/FalkorDB-MCPServer) | FalkorDB 그래프 데이터베이스 서버. 스키마 조회 및 Cypher 읽기/쓰기 |
| [**Fireproof**](https://github.com/fireproof-storage/mcp-database-server) | 실시간 동기화를 갖춘 불변 원장 데이터베이스 |
| [**FreePeak/db-mcp-server**](https://github.com/FreePeak/db-mcp-server) | Golang으로 구축된 고성능 멀티 데이터베이스 MCP 서버. MySQL & PostgreSQL 지원. 쿼리 실행, 트랜잭션 관리, 스키마 탐색, 성능 분석 도구 내장 |
| [**GibsonAI**](https://github.com/GibsonAI/mcp) | AI 기반 클라우드 데이터베이스: AI로 데이터베이스 인스턴스 구축, 마이그레이션, 배포 |
| [**gogabrielordonez/mcp-ragchat**](https://github.com/gogabrielordonez/mcp-ragchat) | 단일 명령으로 웹사이트에 RAG 기반 AI 채팅 추가. 로컬 벡터 스토어, 멀티 프로바이더 LLM(OpenAI/Anthropic/Gemini), 임베딩 가능 위젯 |
| [**Gralio SaaS Database**](https://github.com/tymonTe/gralio-mcp) | Gralio MCP 서버를 사용하여 G2 리뷰, Trustpilot, Crunchbase, LinkedIn 등의 데이터로 SaaS 제품 검색 및 비교 |
| [**GreptimeDB**](https://github.com/GreptimeTeam/greptimedb-mcp-server) | GreptimeDB의 데이터를 안전하고 구조화된 방식으로 탐색 및 분석하는 기능을 AI 어시스턴트에 제공 |
| [**hannesrudolph/imessage-query-fastmcp-mcp-server**](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) | MCP를 통해 iMessage 데이터베이스에 안전하게 접근하는 서버. 전화번호 유효성 검사와 첨부 파일 처리를 포함한 iMessage 대화 쿼리 및 분석 |
| [**hannesrudolph/sqlite-explorer-fastmcp-mcp-server**](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) | FastMCP 프레임워크로 구축된 SQLite 데이터베이스 안전 읽기 전용 접근 MCP 서버. 내장 안전 기능 및 쿼리 유효성 검사 포함 |
| [**HaroldFinchIFT/vuln-nist-mcp-server**](https://github.com/HaroldFinchIFT/vuln-nist-mcp-server) | NIST NVD(국가 취약점 데이터베이스) API 엔드포인트를 쿼리하는 MCP 서버 |
| [**Heroku**](https://github.com/heroku/heroku-mcp-server) | LLM 기반 도구를 통해 Heroku 플랫폼과 상호작용. 앱, 애드온, Dyno, 데이터베이스 관리 |
| [**hifriendbot/cogmemai-mcp**](https://github.com/hifriendbot/cogmemai-mcp) | Claude Code용 영구 인지 메모리. 시맨틱 검색, AI 기반 추출, 프로젝트 스코핑을 갖춘 클라우드 우선 접근. 로컬 데이터베이스 불필요 |
| [**Himalayas-App/himalayas-mcp**](https://github.com/Himalayas-App/himalayas-mcp) | 수만 건의 원격 채용 공고 및 기업 정보에 접근. Himalayas 원격 채용 데이터베이스에 실시간 접근 제공 |
| [**InfluxData/influxdb3_mcp_server**](https://github.com/influxdata/influxdb3_mcp_server) | InfluxDB 3 Core/Enterprise/Cloud Dedicated 공식 MCP 서버 |
| [**InfluxDB**](https://github.com/idoru/influxdb-mcp-server) | InfluxDB OSS API v2에 대한 쿼리 실행 |
| [**InsForge/insforge-mcp**](https://github.com/InsForge/insforge-mcp) | AI 에이전트가 풀스택 애플리케이션을 구축 및 관리할 수 있는 AI 네이티브 BaaS 플랫폼. Auth, 데이터베이스(PostgreSQL), 스토리지, 함수를 프로덕션급 인프라로 제공 |
| [**JaviMaligno/postgres_mcp**](https://github.com/JaviMaligno/postgres_mcp) | 14개 도구를 갖춘 PostgreSQL MCP 서버. 쿼리, 스키마 탐색, 테이블 분석 지원. SQL 인젝션 방지, 기본 읽기 전용 보안 우선 설계 |
| [**JDBC**](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) | JDBC 호환 데이터베이스에 연결하여 쿼리, 삽입, 수정, 삭제 등 수행. MySQL, PostgreSQL, Oracle, SQL Server, SQLite 등 지원 |
| [**joshuarileydev/supabase-mcp-server**](https://github.com/joshuarileydev/supabase) | Supabase에서 프로젝트 및 조직을 관리하고 생성하는 MCP 서버 |
| [**jovezhong/mcp-timeplus**](https://github.com/jovezhong/mcp-timeplus) | Apache Kafka 및 Timeplus용 MCP 서버. Kafka 토픽 목록, 메시지 폴링, 데이터 로컬 저장, Timeplus를 통한 SQL 스트리밍 데이터 쿼리 |
| [**jparkerweb/mcp-sqlite**](https://github.com/jparkerweb/mcp-sqlite) | 포괄적인 SQLite 데이터베이스 상호작용 기능을 제공하는 MCP 서버 |
| [**julien040/anyquery**](https://github.com/julien040/anyquery) | 하나의 바이너리로 SQL을 사용하여 40개 이상의 앱을 쿼리. PostgreSQL, MySQL, SQLite 호환 데이터베이스에도 연결. 로컬 우선, 프라이버시 중심 설계 |
| [**Kafka**](https://github.com/tuannvm/kafka-mcp-server) | franz-go를 활용하여 Go로 구현된 Apache Kafka용 MCP 서버 |
| [**KashiwaByte/vikingdb-mcp-server**](https://github.com/KashiwaByte/vikingdb-mcp-server) | VikingDB 통합. 컬렉션 및 인덱스 소개, 벡터 저장 및 검색 기능 |
| [**ktanaka101/mcp-server-duckdb**](https://github.com/ktanaka101/mcp-server-duckdb) | 스키마 검사 및 쿼리 기능을 갖춘 DuckDB 데이터베이스 통합 |
| [**Kuzu**](https://github.com/kuzudb/kuzu-mcp-server) | LLM이 Kuzu 그래프 데이터베이스에서 스키마를 검사하고 쿼리를 실행할 수 있도록 지원 |
| [**KWDB**](https://github.com/KWDB/kwdb-mcp-server) | KWDB 데이터베이스에서 데이터 읽기, 쓰기, 쿼리, 수정 및 DDL 작업 수행 |
| [**libSQL by xexr**](https://github.com/Xexr/mcp-libsql) | libSQL 데이터베이스용 MCP 서버. 파일, 로컬 HTTP, 원격 Turso 데이터베이스 지원. 커넥션 풀링, 트랜잭션 지원, 6개 전문 도구 포함 |
| [**longevity-genie/synergy-age-mcp**](https://github.com/longevity-genie/synergy-age-mcp) | 장수 관련 시너지 및 길항 유전자 상호작용의 SynergyAge 데이터베이스용 MCP 서버 |
| [**louis030195/apollo-io-mcp**](https://github.com/louis030195/apollo-io-mcp) | Apollo.io를 통한 B2B 영업 인텔리전스 및 잠재고객 발굴. 2억 7,500만 이상 연락처 데이터베이스 접근, 이메일/전화번호 보강 |
| [**LucasHild/mcp-server-bigquery**](https://github.com/LucasHild/mcp-server-bigquery) | 스키마 검사 및 쿼리 기능을 갖춘 BigQuery 데이터베이스 통합 |
| [**mac-messages-mcp**](https://github.com/carterlasalle/mac_messages_mcp) | MCP를 통해 iMessage 데이터베이스에 안전하게 접근하는 서버. LLM이 iMessage 대화를 쿼리하고 분석 가능 |
| [**MariaDB**](https://github.com/mariadb/mcp) | MariaDB 데이터베이스 관리 및 쿼리를 위한 표준 인터페이스. 표준 SQL 작업과 고급 벡터/임베딩 기반 검색 지원 |
| [**MariaDB**](https://github.com/abel9851/mcp-server-mariadb) | Python으로 설정 가능한 접근 제어를 갖춘 MariaDB 데이터베이스 통합 |
| [**mbentham/SqlAugur**](https://github.com/mbentham/SqlAugur) | AST 기반 쿼리 유효성 검사, 읽기 전용 안전, 스키마 탐색, ER 다이어그램 생성, DBA 도구 통합을 갖춘 SQL Server MCP 서버 |
| [**MCP Toolbox for Databases**](https://github.com/googleapis/genai-toolbox) | 데이터베이스를 위한 쉽고, 빠르고, 안전한 도구를 전문으로 하는 오픈소스 MCP 서버. AlloyDB, BigQuery, MySQL, Neo4j, Postgres 등 지원 |
| [**MCP-Database-Server**](https://github.com/executeautomation/mcp-database-server) | SQL Server, SQLite, PostgreSQL 등 데이터베이스와 가장 빠르게 상호작용하는 방법 |
| [**MCP-PostgreSQL-Ops**](https://github.com/call518/MCP-PostgreSQL-Ops) | Apache Ambari API 통합을 위한 MCP 서버. Hadoop 클러스터 관리, 서비스 운영, 구성 관리, 상태 모니터링 도구 제공 |
| [**Memgraph**](https://github.com/memgraph/ai-toolkit/tree/main/integrations/mcp-memgraph) | Memgraph 그래프 데이터베이스에서 데이터 쿼리 |
| [**Milvus**](https://github.com/zilliztech/mcp-server-milvus) | Milvus 벡터 데이터베이스에서 데이터 검색, 쿼리, 상호작용 |
| [**mindsdb/mindsdb**](https://github.com/mindsdb/mindsdb) | MindsDB를 단일 MCP 서버로 사용하여 다양한 플랫폼 및 데이터베이스의 데이터를 연결 및 통합 |
| [**Mongo**](https://github.com/QuantGeekDev/mongo-mcp) | LLM이 MongoDB 데이터베이스와 직접 상호작용할 수 있도록 지원하는 MCP 서버 |
| [**MongoDB**](https://github.com/mongodb-js/mongodb-mcp-server) | MongoDB Community Server 및 MongoDB Atlas 모두 지원 |
| [**MongoDB**](https://github.com/kiliczsh/mcp-mongo-server) | MongoDB용 MCP 서버 |
| [**MongoDB & Mongoose**](https://github.com/nabid-pf/mongo-mongoose-mcp) | Mongoose 스키마 및 유효성 검사를 포함한 MongoDB MCP 서버 |
| [**MongoDB Lens**](https://github.com/furey/mongodb-lens) | MongoDB 데이터베이스용 풀 기능 MCP 서버 |
| [**montumodi/mongodb-atlas-mcp-server**](https://github.com/montumodi/mongodb-atlas-mcp-server) | MongoDB Atlas API에 접근하는 MCP. `mongodb-atlas-api-client` 패키지를 래핑하여 MCP 도구를 통해 MongoDB Atlas 기능 노출 |
| [**Moorcheh**](https://github.com/moorcheh-ai/moorcheh-mcp) | Moorcheh의 임베딩, 벡터 스토어, 검색, 생성형 AI 답변 서비스와의 원활한 통합 제공 |
| [**MSSQL**](https://github.com/aekanun2020/mcp-server/) | 설정 가능한 접근 제어 및 스키마 검사를 갖춘 MSSQL 데이터베이스 통합 |
| [**MySQL**](https://github.com/designcomputer/mysql_mcp_server) | 설정 가능한 접근 제어 및 스키마 검사를 갖춘 MySQL 데이터베이스 통합 |
| [**Neo4j**](https://github.com/neo4j-contrib/mcp-neo4j/) | Neo4j 그래프 데이터베이스 서버(스키마 + Cypher 읽기/쓰기) 및 별도의 그래프 데이터베이스 기반 메모리 |
| [**Neo4j**](https://github.com/da-okazaki/mcp-neo4j-server) | Neo4j 그래프 데이터베이스와 상호작용하는 커뮤니티 제작 서버 |
| [**Neo4j Agent Memory**](https://github.com/knowall-ai/mcp-neo4j-agent-memory) | Neo4j 지식 그래프를 사용한 AI 에이전트 메모리 관리 |
| [**Neo4j GDS**](https://github.com/neo4j-contrib/gds-agent) | 종합적인 그래프 알고리즘을 갖춘 Neo4j 그래프 데이터 사이언스 서버. 복잡한 그래프 추론 및 Q&A 지원 |
| [**Neon**](https://github.com/neondatabase/mcp-server-neon) | Neon 서버리스 Postgres 플랫폼과 상호작용 |
| [**Nile**](https://github.com/niledatabase/nile-mcp-server) | B2B 앱을 위해 재설계된 Nile Postgres와 통신하는 MCP 서버. LLM으로 데이터베이스, 테넌트, 사용자, 인증 관리 |
| [**NocoDB**](https://github.com/edwinbernadus/nocodb-mcp-server) | NocoDB 데이터베이스 읽기/쓰기 접근 |
| [**nonatofabio/local-faiss-mcp**](https://github.com/nonatofabio/local_faiss_mcp) | RAG용 로컬 FAISS 벡터 데이터베이스. 문서 수집(PDF/TXT/MD/DOCX), 시맨틱 검색, 리랭킹, 색인/쿼리용 CLI 도구 |
| [**OceanBase**](https://github.com/oceanbase/mcp-oceanbase) | OceanBase 데이터베이스 및 도구용 MCP 서버 |
| [**OceanBase**](https://github.com/yuanoOo/oceanbase_mcp_server) | (yuanoOo 제작) OceanBase 데이터베이스와 안전하게 상호작용하는 MCP 서버 |
| [**OpenLink Generic Java Database Connectivity**](https://github.com/OpenLinkSoftware/mcp-jdbc-server) | ODBC 커넥터(드라이버)를 통한 범용 DBMS 접근 |
| [**OpenLink Generic Open Database Connectivity**](https://github.com/OpenLinkSoftware/mcp-odbc-server) | ODBC 커넥터(드라이버)를 통한 범용 DBMS 접근 |
| [**OpenLink Generic Python Open Database Connectivity**](https://github.com/OpenLinkSoftware/mcp-pyodbc-server) | PyODBC용 ODBC 커넥터(드라이버)를 통한 범용 DBMS 접근 |
| [**OpenLink Generic SQLAlchemy Object-Relational Database Connectivity for PyODBC**](https://github.com/OpenLinkSoftware/mcp-sqlalchemy-server) | SQLAlchemy(PyODBC) 커넥터(드라이버)를 통한 범용 DBMS 접근 |
| [**Optimade MCP**](https://github.com/dianfengxiaobo/optimade-mcp-server) | Optimade 데이터베이스를 통한 실시간 재료 과학 데이터 쿼리(원소 조성, 결정 구조 등) |
| [**Oracle**](https://docs.oracle.com/en/database/oracle/sql-developer-command-line/25.2/sqcug/starting-and-managing-sqlcl-mcp-server.html#GUID-5F916B5D-8670-42BD-9F8B-D3D2424EC47E) | SQLcl의 네이티브 MCP 지원을 통해 모든 Oracle Database에 접근할 수 있는 공식 MCP 서버 |
| [**OSV**](https://github.com/StacklokLabs/osv-mcp) | OSV(오픈소스 취약점) 데이터베이스에서 취약점 정보 접근. 패키지 버전 또는 커밋별 쿼리, 배치 쿼리, 상세 취약점 정보 조회 |
| [**pfillion42/memviz**](https://github.com/pfillion42/memviz) | MCP Memory Service SQLite-vec 데이터베이스용 시각적 탐색기. 대시보드, 타임라인, UMAP 투영, 시맨틱 클러스터링, 중복 감지, 연관 그래프로 메모리 탐색/검색/편집 |
| [**pilat/mcp-datalink**](https://github.com/pilat/mcp-datalink) | 매개변수화된 쿼리 및 스키마 검사를 갖춘 안전한 데이터베이스 접근(PostgreSQL, MySQL, SQLite) MCP 서버 |
| [**Pinecone**](https://github.com/pinecone-io/pinecone-mcp) | 개발 환경 내에서 문서 검색 및 데이터 관리를 지원하는 Pinecone 개발자용 MCP 서버 |
| [**Pinecone**](https://github.com/sirmews/mcp-pinecone) | Pinecone에 레코드 검색 및 업로드하는 MCP 서버. Pinecone Inference API를 활용한 간단한 RAG 기능 제공 |
| [**Pinecone Assistant**](https://github.com/pinecone-io/assistant-mcp) | Pinecone Assistant 지식 베이스에서 컨텍스트 검색 |
| [**planetscale/mcp**](https://github.com/planetscale/cli?tab=readme-ov-file#mcp-server-integration) | PlanetScale CLI에 포함된 MCP 서버. AI 도구가 PlanetScale 데이터베이스에 직접 접근 |
| [**PostgreSQL**](https://github.com/ahmedmustahid/postgres-mcp-server) | HTTP/Stdio 이중 전송을 제공하는 PostgreSQL MCP 서버. 스키마 검사, 읽기 전용 쿼리 실행, 세션 관리, Podman/Docker 지원 |
| [**PostgreSQL**](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | 스키마 검사 및 쿼리 기능을 갖춘 PostgreSQL 데이터베이스 통합 |
| [**Prisma**](https://www.prisma.io/docs/postgres/integrations/mcp-server) | Prisma Postgres 데이터베이스 생성 및 관리 |
| [**Prisma Postgres**](https://github.com/prisma/mcp) | LLM이 Prisma Postgres 데이터베이스를 관리(새 데이터베이스 생성, 마이그레이션 실행, 쿼리 등)할 수 있도록 지원 |
| [**Qdrant**](https://github.com/qdrant/mcp-server-qdrant/) | Qdrant 벡터 검색 엔진 위에 시맨틱 메모리 레이어 구현 |
| [**rashidazarang/airtable-mcp**](https://github.com/rashidazarang/airtable-mcp) | AI 도구를 Airtable에 직접 연결. 자연어로 레코드 쿼리, 생성, 수정, 삭제. 베이스 관리, 테이블 작업, 스키마 조작, 데이터 마이그레이션 지원 |
| [**Redis**](https://github.com/redis/mcp-redis/) | Redis 공식 MCP 서버. Redis 데이터 관리 및 검색 인터페이스 제공 |
| [**Redis**](https://github.com/GongRzhe/REDIS-MCP-Server) | 키-값 작업, 만료 관리, 패턴 기반 키 목록을 지원하는 Redis 데이터베이스 작업 및 캐싱 마이크로서비스 서버 |
| [**Redis Cloud API**](https://github.com/redis/mcp-redis-cloud/) | 자연어를 사용하여 Redis Cloud 리소스를 관리하는 MCP 서버 |
| [**Render**](https://render.com/docs/mcp-server) | Render 공식 MCP 서버: 새 서비스 생성, 데이터베이스 쿼리 실행, 서비스 메트릭 및 로그에 직접 접근하여 빠른 디버깅 |
| [**run-sql-connectorx**](https://github.com/gigamori/mcp-run-sql-connectorx) | ConnectorX를 통해 SQL(PostgreSQL, MariaDB, BigQuery, MS SQL Server 등) 실행 및 결과를 CSV/Parquet로 스트리밍 |
| [**runekaagaard/mcp-alchemy**](https://github.com/runekaagaard/mcp-alchemy) | PostgreSQL, MySQL, MariaDB, SQLite, Oracle, MS SQL Server 등을 지원하는 범용 SQLAlchemy 기반 데이터베이스 통합. 스키마/관계 검사 및 대규모 데이터셋 분석 기능 |
| [**SchemaCrawler**](https://github.com/schemacrawler/SchemaCrawler-MCP-Server-Usage) | 관계형 데이터베이스에 연결하여 유효한 SQL을 얻고, 특정 컬럼 접두사의 의미 등을 질문 |
| [**SchemaFlow**](https://github.com/CryptoRadi/schemaflow-mcp-server) | MCP를 통한 AI-IDE용 실시간 PostgreSQL & Supabase 데이터베이스 스키마 접근. 보안 SSE 연결로 라이브 데이터베이스 컨텍스트 제공 |
| [**shashankss1205/codegraphcontext**](https://github.com/Shashankss1205/CodeGraphContext) | 로컬 코드를 그래프 데이터베이스에 색인화하여 AI 어시스턴트에 컨텍스트를 제공하는 MCP 서버. 그래픽 코드 시각화 포함 |
| [**SingleStore**](https://github.com/singlestore-labs/mcp-server-singlestore) | SingleStore 데이터베이스 플랫폼과 상호작용 |
| [**sirmews/apple-notes-mcp**](https://github.com/sirmews/apple-notes-mcp) | 로컬 Apple Notes 데이터베이스에서 AI가 읽을 수 있도록 지원(macOS 전용) |
| [**Snowflake**](https://github.com/Snowflake-Labs/mcp) | Snowflake-Labs 공식 오픈소스 MCP 서버. Cortex Agents 프롬프트, 구조화/비구조화 데이터 쿼리, SQL 실행, 시맨틱 뷰 쿼리 지원 |
| [**Snowflake**](https://github.com/isaacwasserman/mcp-snowflake-server) | LLM이 Snowflake 데이터베이스와 안전하고 제어된 데이터 작업을 수행할 수 있도록 지원하는 MCP 서버 |
| [**Snowflake Cortex MCP Server**](https://github.com/thisisbhanuj/Snowflake-Cortex-MCP-Server) | Snowflake Cortex AI 기능을 MCP 생태계에 제공하는 Snowflake MCP 서버. Claude Desktop 등 MCP 클라이언트와 연결 |
| [**SQL Server**](https://github.com/Azure-Samples/SQL-AI-samples/tree/main/MssqlMcp) | Microsoft SQL Server 공식 MCP 서버 |
| [**SQLite**](https://github.com/panasenco/mcp-sqlite) | SQLite 파일용 MCP 서버. Datasette 호환 메타데이터 지원 |
| [**SQLite**](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | 내장 분석 기능을 갖춘 SQLite 데이터베이스 작업 |
| [**subnetmarco/pgmcp**](https://github.com/subnetmarco/pgmcp) | 자연어 PostgreSQL 쿼리. 자동 스트리밍, 읽기 전용 안전, 범용 데이터베이스 호환 |
| [**Supabase**](https://github.com/supabase-community/supabase-mcp) | Supabase와 상호작용: 테이블 생성, 데이터 쿼리, Edge Function 배포 등 |
| [**Teradata**](https://github.com/arturborycki/mcp-teradata) | LLM이 Teradata 데이터베이스와 상호작용할 수 있도록 지원. 멀티 태스크 데이터 분석용 도구 및 프롬프트 포함 |
| [**Thales CDSP CAKM MCP Server**](https://github.com/sanyambassi/thales-cdsp-cakm-mcp-server) | Thales CipherTrust CDSP CAKM 커넥터용 MCP 서버. MS SQL 및 Oracle 데이터베이스 지원 |
| [**TheRaLabs/legion-mcp**](https://github.com/TheRaLabs/legion-mcp) | PostgreSQL, Redshift, CockroachDB, MySQL, BigQuery, Oracle, SQLite 등 다중 데이터베이스를 지원하는 범용 데이터베이스 MCP 서버 |
| [**TiDB**](https://github.com/pingcap/pytidb) | TiDB 데이터베이스 플랫폼과 상호작용하는 MCP 서버 |
| [**TigerGraph**](https://github.com/custom-discoveries/TigerGraph_MCP) | TigerGraph 그래프 데이터베이스와 상호작용하는 커뮤니티 제작 MCP 서버 |
| [**TMDB**](https://github.com/Laksh-star/mcp-server-tmdb) | TMDB API와 통합하여 영화 정보, 검색, 추천 기능을 제공하는 MCP 서버 |
| [**topoteretes/cognee**](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) | 다양한 그래프 및 벡터 스토어를 사용한 AI 앱 및 에이전트용 메모리 매니저. 30개 이상 데이터 소스에서 수집 |
| [**tradercjz/dolphindb-mcp-server**](https://github.com/tradercjz/dolphindb-mcp-server) | 스키마 검사 및 쿼리 기능을 갖춘 DolphinDB 데이터베이스 통합 |
| [**Upstash**](https://github.com/upstash/mcp-server) | 자연어로 Upstash의 Redis 데이터베이스 관리 및 Redis 명령 실행 |
| [**Vertica**](https://github.com/nolleh/mcp-vertica) | Python으로 설정 가능한 접근 제어 및 스키마 검사를 갖춘 Vertica 데이터베이스 통합 |
| [**vulnicheck**](https://github.com/andrasfe/vulnicheck) | OSV 및 NVD 데이터베이스에 대해 의존성을 검사하는 실시간 Python 패키지 취약점 스캐너. CVE 상세정보, 락 파일 지원 제공 |
| [**weaviate/mcp-server-weaviate**](https://github.com/weaviate/mcp-server-weaviate) | Weaviate 컬렉션을 지식 베이스로 연결하고 Weaviate를 채팅 메모리 스토어로 사용하는 MCP 서버 |
| [**wenb1n-dev/mysql_mcp_server_pro**](https://github.com/wenb1n-dev/mysql_mcp_server_pro) | SSE, STDIO 지원. MySQL CRUD 외에 데이터베이스 예외 분석, 역할 기반 권한 제어, 개발자용 도구 확장 기능 포함 |
| [**wenerme/wener-mssql-mcp**](https://github.com/wenerme/wode/tree/develop/packages/wener-mssql-mcp) | 스키마 검사 및 쿼리 기능을 갖춘 MSSQL 데이터베이스 통합 |
| [**XiYan**](https://github.com/XGenerationLab/xiyan_mcp_server) | XiyanSQL 텍스트-SQL LLM 기반으로 자연어 쿼리를 사용하여 데이터베이스에서 데이터를 가져오는 MCP 서버 |
| [**yannbrrd/simple_snowflake_mcp**](https://github.com/YannBrrd/simple_snowflake_mcp) | 기업 프록시 뒤에서 작동하는 간단한 Snowflake MCP 서버. 읽기 및 쓰기(선택) 작업 지원 |
| [**YDB**](https://github.com/ydb-platform/ydb-mcp) | YDB 데이터베이스 쿼리 |
| [**YepCode**](https://github.com/yepcode/mcp-server-js) | YepCode 기반 안전하고 확장 가능한 샌드박스 환경에서 코드 실행. 의존성, 시크릿, 로그, API/데이터베이스 접근 완전 지원 |
| [**yincongcyincong/VictoriaMetrics-mcp-server**](https://github.com/yincongcyincong/VictoriaMetrics-mcp-server) | VictoriaMetrics 데이터베이스와 상호작용하는 MCP 서버 |
| [**YugabyteDB**](https://github.com/yugabyte/yugabytedb-mcp-server) | YugabyteDB 데이터베이스와 상호작용하는 MCP 서버 |
| [**Zhwt/go-mcp-mysql**](https://github.com/Zhwt/go-mcp-mysql) | Golang으로 구축된 의존성 없는 간편한 MySQL MCP 서버. 설정 가능한 읽기 전용 모드 및 스키마 검사 |

---

## ☁️ 클라우드 & 인프라

> AWS, Azure, GCP, Docker, Kubernetes 등 클라우드 플랫폼 연동

| 서버 | 설명 |
|------|------|
| [**4everland/4everland-hosting-mcp**](https://github.com/4everland/4everland-hosting-mcp) | AI가 생성한 코드를 Greenfield, IPFS, Arweave 등 탈중앙화 스토리지 네트워크에 즉시 배포할 수 있는 4EVERLAND Hosting MCP 서버 |
| [**aashari/mcp-server-aws-sso**](https://github.com/aashari/mcp-server-aws-sso) | AWS Single Sign-On(SSO) 통합으로 AI 시스템이 SSO 로그인 시작, 계정/역할 목록 조회, 임시 자격 증명을 사용한 AWS CLI 명령 실행을 통해 AWS 리소스와 안전하게 상호작용 |
| [**AgentBay**](https://github.com/Michael98671/agentbay) | AI 에이전트를 위한 서버리스 클라우드 인프라를 제공하는 MCP 서버 |
| [**alexei-led/aws-mcp-server**](https://github.com/alexei-led/aws-mcp-server) | AI 어시스턴트가 안전한 Docker 환경에서 AWS CLI 명령 실행, Unix 파이프 사용, 일반 AWS 작업용 프롬프트 템플릿을 적용할 수 있는 경량 고성능 서버. 멀티 아키텍처 지원 |
| [**alexei-led/k8s-mcp-server**](https://github.com/alexei-led/k8s-mcp-server) | AI 어시스턴트가 안전한 Docker 환경에서 kubectl, helm, istioctl, argocd 등 Kubernetes CLI 명령을 Unix 파이프와 함께 실행할 수 있는 경량 고성능 서버. 멀티 아키텍처 지원 |
| [**Alibaba Cloud DataWorks**](https://github.com/aliyun/alibabacloud-dataworks-mcp-server) | AI가 표준화된 인터페이스를 통해 DataWorks Open API와 상호작용할 수 있는 MCP 서버. Alibaba Cloud 기반 구현 |
| [**Alibaba Cloud OpenSearch**](https://github.com/aliyun/alibabacloud-opensearch-mcp-server) | AI Agent가 표준화되고 확장 가능한 인터페이스를 통해 OpenSearch와 상호작용할 수 있는 도구를 제공하는 MCP 서버 |
| [**Alibaba Cloud OPS**](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) | CloudOps Orchestration Service와 Alibaba Cloud OpenAPI를 사용하여 Alibaba Cloud 리소스의 전체 라이프사이클을 관리 |
| [**Alibaba Cloud RDS**](https://github.com/aliyun/alibabacloud-rds-openapi-mcp-server) | LLM을 통해 Alibaba Cloud RDS 리소스를 프로그래밍 방식으로 관리할 수 있는 MCP 서버 |
| [**AlibabaCloud DevOps MCP**](https://github.com/aliyun/alibabacloud-devops-mcp-server) | AI 어시스턴트가 Yunxiao(운효) 플랫폼과 상호작용할 수 있는 Yunxiao MCP Server |
| [**aliyun/alibabacloud-tablestore-mcp-server**](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) | Tablestore용 MCP 서비스. 문서 추가, 벡터 및 스칼라 기반 시맨틱 검색, RAG 친화적, 서버리스 지원 |
| [**ariekogan/ateam-mcp**](https://github.com/ariekogan/ateam-mcp) | ADAS 플랫폼에서 멀티 에이전트 AI 솔루션을 빌드, 검증 및 배포. 도구가 포함된 스킬 설계, 솔루션 라이프사이클 관리, stdio 또는 HTTP를 통한 연결 지원 |
| [**avisangle/jenkins-mcp-server**](https://github.com/avisangle/jenkins-mcp-server) | 멀티 티어 캐싱, 파이프라인 모니터링, 아티팩트 관리, 배치 작업을 갖춘 엔터프라이즈급 Jenkins CI/CD 통합. 작업 관리, 빌드 상태 추적, 큐 관리를 위한 21개 MCP 도구 제공 |
| [**AWS**](https://github.com/awslabs/mcp) | AWS 모범 사례를 개발 워크플로에 직접 제공하는 전문 MCP 서버 |
| [**AWS**](https://github.com/rishikavikondala/mcp-server-aws) | LLM을 사용하여 AWS 리소스에 대한 작업 수행 |
| [**AWS Athena**](https://github.com/lishenxydlgzs/aws-athena-mcp) | Glue Catalog에서 SQL 쿼리를 실행할 수 있는 AWS Athena용 MCP 서버 |
| [**AWS CDK**](https://github.com/awslabs/mcp/tree/main/src/cdk-mcp-server) | CDK 처방적 조언 제공, CDK Nag 규칙 설명, 억제 확인, Bedrock Agent 스키마 생성, AWS Solutions Constructs 패턴 탐색 |
| [**AWS Cognito**](https://github.com/gitCarrot/mcp-server-aws-cognito) | AWS Cognito에 연결하여 인증 및 사용자 관리를 수행하는 MCP 서버 |
| [**AWS Core**](https://github.com/awslabs/mcp/tree/main/src/core-mcp-server) | 프롬프트 이해 및 서버 관리 기능을 제공하는 핵심 AWS MCP 서버 |
| [**AWS Cost Analysis**](https://github.com/awslabs/mcp/tree/main/src/cost-analysis-mcp-server) | CDK 프로젝트를 분석하여 사용된 AWS 서비스를 식별하고 AWS 요금 웹페이지 및 API에서 가격 정보를 조회 |
| [**AWS Cost Explorer**](https://github.com/aarora79/aws-cost-explorer-mcp-server) | 리전, 서비스, 인스턴스 유형, Foundation Model별 지출을 분석하여 AWS 비용(Amazon Bedrock 포함)을 최적화하는 MCP 서버 |
| [**AWS Documentation**](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server) | AWS 문서 페이지를 가져오고, 변환하고, 검색하며 관련 콘텐츠를 추천 |
| [**AWS EC2 Pricing**](https://github.com/trilogy-group/aws-pricing-mcp) | 한 번의 호출로 최신 EC2 가격 정보를 조회. 사전 파싱된 AWS 가격 카탈로그로 빠른 응답 |
| [**AWS Nova Canvas**](https://github.com/awslabs/mcp/tree/main/src/nova-canvas-mcp-server) | 텍스트 프롬프트와 색상 가이드를 사용하여 Amazon Nova Canvas로 이미지 생성 |
| [**AWS Open Data**](https://github.com/domdomegg/aws-open-data-mcp) | 퍼지 매칭과 상세 데이터셋 정보를 제공하는 AWS Open Data Registry 검색 및 탐색 |
| [**AWS Resources Operations**](https://github.com/baryhuang/mcp-server-aws-resources-python) | 생성된 Python 코드를 실행하여 boto3가 지원하는 모든 AWS 리소스를 안전하게 쿼리하거나 수정 |
| [**AWS S3**](https://github.com/aws-samples/sample-mcp-server-s3) | S3에서 PDF 문서 등의 객체를 유연하게 가져올 수 있는 AWS S3 샘플 MCP 서버 |
| [**Azure**](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server) | MCP 클라이언트에 Azure Storage, Cosmos DB, Azure CLI 등 주요 Azure 서비스 및 도구에 대한 접근을 제공하는 서버 |
| [**Azure DevOps**](https://github.com/microsoft/azure-devops-mcp) | 리포지토리, 작업 항목, 빌드, 릴리스, 테스트 계획, 코드 검색 등 Azure DevOps 서비스와 상호작용 |
| [**Azure DevOps**](https://github.com/Vortiago/mcp-azure-devops) | AI 어시스턴트가 작업 항목을 쿼리하고 관리할 수 있도록 Azure DevOps 서비스와 연결하는 MCP 서버 |
| [**Azure MCP Hub**](https://github.com/Azure-Samples/mcp) | Azure 개발자를 위한 MCP 서버 및 관련 리소스 큐레이션 목록 |
| [**Azure Wiki Search**](https://github.com/coder-linping/azure-wiki-search-server) | AI가 Azure DevOps Wiki에 호스팅된 위키를 쿼리할 수 있는 MCP 서버 |
| [**Azure/azure-mcp**](https://github.com/Azure/azure-mcp) | Storage, Cosmos DB, Azure Monitor를 포함한 Azure 서비스용 Microsoft 공식 MCP 서버 |
| [**Cloudflare**](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare 개발자 플랫폼(Workers/KV/R2/D1 등)에서 리소스를 배포, 설정 및 조회 |
| [**Convex**](https://stack.convex.dev/convex-mcp-server) | Convex에 배포된 앱을 검사하고 쿼리 |
| [**Cronlytic**](https://github.com/Cronlytic/cronlytic-mcp-server) | Cronlytic MCP Server를 통해 서버리스 크론 작업에 대한 CRUD 작업 수행 |
| [**CTERA Portal**](https://github.com/ctera/mcp-ctera-core) | 페타바이트 규모의 분산 콘텐츠에 대해 글로벌 네임스페이스와 통합 관리를 제공하는 멀티 테넌트, 멀티 클라우드 플랫폼 |
| [**dagger/container-use**](https://github.com/dagger/container-use) | 코딩 에이전트를 위한 컨테이너화된 환경. 여러 에이전트가 독립적으로 격리된 컨테이너와 Git 브랜치에서 작업. 전체 실행 이력, 터미널 접근, Git 워크플로 제공 |
| [**Daghis/teamcity-mcp**](https://github.com/Daghis/teamcity-mcp) | 빌드, 테스트, 에이전트, CI/CD 파이프라인 관리를 위한 87개 도구를 갖춘 JetBrains TeamCity MCP 서버. 이중 모드(dev/full) 작동 및 런타임 모드 전환 지원 |
| [**Daytona**](https://github.com/daytonaio/daytona/tree/main/apps/cli/mcp) | Daytona 샌드박스에서 AI 생성 코드를 빠르고 안전하게 실행 |
| [**Defang**](https://github.com/DefangLabs/defang/blob/main/src/pkg/mcp/README.md) | IDE를 벗어나지 않고 Defang 플랫폼을 통해 프로젝트를 클라우드에 원활하게 배포 |
| [**DefangLabs/defang**](https://github.com/DefangLabs/defang) | Docker Compose 호환 프로젝트를 AWS, GCP 또는 DigitalOcean 계정에 빌드하고 배포하는 CLI 및 MCP 서버 |
| [**deploy-mcp**](https://github.com/alexpota/deploy-mcp) | 실시간 상태 배지와 배포 모니터링을 제공하는 AI 어시스턴트용 범용 배포 추적기 |
| [**DeployHQ**](https://github.com/deployhq/deployhq-mcp-server) | AI 어시스턴트가 배포 관리, 프로젝트 목록 조회, 배포 상태 모니터링을 수행할 수 있는 DeployHQ API 연동 MCP 서버 |
| [**DesktopCommander**](https://github.com/wonderwhy-er/DesktopCommanderMCP) | AI가 컴퓨터의 파일을 편집/관리하고, 터미널 명령을 실행하며, SSH로 원격 서버에 접속할 수 있는 인기 로컬 MCP 서버 |
| [**Devcontainer**](https://github.com/AI-QL/mcp-devcontainers) | Devcontainer 설정 파일로부터 개발 컨테이너를 직접 생성하고 구성하는 MCP 서버 |
| [**DigitalOcean MCP Server**](https://github.com/rohit-kaundal/digitalocean-mcp-server) | DigitalOcean API에 대한 프로그래밍 방식 접근을 제공하는 MCP 서버. Droplet, Kubernetes 클러스터, 컨테이너 레지스트리 관리 도구 제공 |
| [**Docker**](https://github.com/ckreiling/mcp-server-docker) | Docker와 통합하여 컨테이너, 이미지, 볼륨, 네트워크를 관리 |
| [**Docker**](https://github.com/0xshariq/docker-mcp-server) | CLI 및 MCP 워크플로를 통해 컨테이너, 이미지, 볼륨, 네트워크, 오케스트레이션을 지원하는 고급 통합 Docker 관리 MCP 서버 |
| [**Docker**](https://github.com/QuantGeekDev/docker-mcp) | Docker 컨테이너, Docker Compose, 로그를 실행하고 관리 |
| [**docker/hub-mcp**](https://github.com/docker/hub-mcp) | 리포지토리, Hub 검색, Docker Hardened Images에 접근할 수 있는 Docker Hub 공식 MCP 서버 |
| [**E2B**](https://github.com/e2b-dev/mcp-server) | E2B가 호스팅하는 보안 샌드박스에서 코드 실행 |
| [**Edgee**](https://github.com/edgee-cloud/mcp-server-edgee) | Edgee 컴포넌트 및 프로젝트를 배포하고 관리 |
| [**EdgeOne Pages MCP**](https://github.com/TencentEdgeOne/edgeone-pages-mcp) | HTML 콘텐츠를 EdgeOne Pages에 배포하고 공개 접근 가능한 URL을 생성하는 MCP 서비스 |
| [**endorhq/cli**](https://github.com/endorhq/cli) | AI 에이전트가 MariaDB, Postgres, Redis, Memcached, Alpine, Valkey 등의 서비스를 격리된 샌드박스에서 실행. 5초 이내 부팅되는 사전 구성 애플리케이션 제공 |
| [**ForeverVM**](https://github.com/jamsocket/forevervm/tree/main/javascript/mcp-server) | 코드 샌드박스에서 Python 실행 |
| [**Gcore**](https://github.com/G-Core/gcore-mcp-server) | LLM 어시스턴트를 통해 CDN, GPU Cloud, AI Inference, 비디오 스트리밍, WAAP, 인스턴스 및 네트워크 등 Gcore 플랫폼 서비스와 상호작용 |
| [**GitLab**](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) | 프로젝트 관리 및 CI/CD 작업을 위한 GitLab 플랫폼 통합 |
| [**Google Cloud Run**](https://github.com/GoogleCloudPlatform/cloud-run-mcp) | Google Cloud Run에 코드를 배포 |
| [**Gru Sandbox**](https://github.com/babelcloud/gru-sandbox) | MCP 통합 또는 기타 AI 에이전트 사용 사례를 위한 자체 호스팅 가능한 오픈소스 샌드박스 |
| [**hardik-id/azure-resource-graph-mcp-server**](https://github.com/hardik-id/azure-resource-graph-mcp-server) | Azure Resource Graph를 사용하여 대규모 Azure 리소스를 쿼리하고 분석하는 MCP 서버. AI 어시스턴트가 Azure 인프라를 탐색하고 모니터링 가능 |
| [**HatmanStack/ragstack-mcp**](https://github.com/HatmanStack/RAGStack-Lambda/tree/main/src/ragstack-mcp) | RAGStack 서버리스 지식 베이스용 MCP 서버. AWS 기반 RAG 파이프라인(Lambda, Bedrock, S3, DynamoDB)을 통한 검색, AI 답변 대화, 문서/미디어 업로드, 웹사이트 스크래핑, 메타데이터 분석 |
| [**HOPX**](https://github.com/hopx-ai/mcp) | 150ms 이하의 시작 시간으로 격리된 클라우드 컨테이너에서 Python, JavaScript, Bash, Go 코드를 실행. pandas, numpy, matplotlib 등 데이터 과학 라이브러리 사전 설치 |
| [**IBM wxflows**](https://github.com/IBM/wxflows/tree/main/examples/mcp/javascript) | 모든 데이터 소스에 대한 도구를 빌드, 테스트, 배포할 수 있는 IBM 도구 플랫폼 |
| [**Inspektor Gadget MCP server**](https://github.com/inspektor-gadget/ig-mcp-server) | eBPF 기반 AI 인터페이스로 컨테이너 및 Kubernetes 워크로드를 디버그 |
| [**Inspizzz/jetbrains-datalore-mcp**](https://github.com/inspizzz/jetbrains-datalore-mcp) | JetBrains Datalore 플랫폼의 클라우드 배포와 상호작용하는 MCP 서버. Datalore API 완전 통합(실행, 대화형 실행, 실행 데이터 조회, 파일 가져오기) |
| [**inventer-dev/mcp-internet-speed-test**](https://github.com/inventer-dev/mcp-internet-speed-test) | 다운로드/업로드 속도, 지연 시간, 지터 분석, CDN 서버 감지 및 지리적 매핑을 포함한 네트워크 성능 메트릭의 인터넷 속도 테스트 |
| [**IO-Aerospace-software-community/mcp-server**](https://github.com/IO-Aerospace-software-engineering/mcp-server) | 항공우주 및 천체역학용 .NET 기반 MCP 서버. 천체력, 궤도 변환, DSS 도구, 시간 변환, 단위/수학 유틸리티 제공. STDIO 및 SSE 전송, Docker 및 .NET 배포 지원 |
| [**ipybox**](https://github.com/gradion-ai/ipybox) | IPython과 Docker 기반의 Python 코드 실행 샌드박스. 상태 유지 코드 실행, 호스트-컨테이너 간 파일 전송, 네트워크 접근 설정 가능 |
| [**IvanAmador/vercel-ai-docs-mcp**](https://github.com/IvanAmador/vercel-ai-docs-mcp) | Vercel AI SDK 문서에 대한 AI 기반 검색 및 쿼리 기능을 제공하는 MCP 서버 |
| [**JaviMaligno/mcp-server-bitbucket**](https://github.com/JaviMaligno/mcp-server-bitbucket) | 리포지토리 관리, PR, 파이프라인, 브랜치, 커밋, 배포, 웹훅, 태그, 브랜치 제한, 소스 탐색을 위한 58개 도구를 갖춘 Bitbucket MCP 서버 |
| [**jdubois/azure-cli-mcp**](https://github.com/jdubois/azure-cli-mcp) | Azure CLI 명령줄을 감싸서 Azure와 직접 대화할 수 있는 래퍼 |
| [**Jenkins**](https://plugins.jenkins.io/mcp-server/) | AI 어시스턴트가 표준 MCP 인터페이스를 통해 빌드 관리, 작업 상태 확인, 로그 조회 및 CI/CD 파이프라인과 통합할 수 있는 공식 Jenkins MCP Server 플러그인 |
| [**Jupyter MCP Server**](https://github.com/datalayer/jupyter-mcp-server) | Jupyter Notebook과 실시간으로 상호작용하여 AI가 데이터 분석, 시각화 등의 코드를 편집, 문서화, 실행. 모든 Jupyter 배포(로컬, JupyterHub 등)와 호환 |
| [**k8s-multicluster-mcp**](https://github.com/razvanmacovei/k8s-multicluster-mcp) | 여러 kubeconfig 파일을 사용하여 여러 Kubernetes 클러스터와 동시에 상호작용하는 MCP 서버 |
| [**Kubernetes**](https://github.com/Flux159/mcp-server-kubernetes) | Kubernetes 클러스터에 연결하여 Pod, Deployment, Service를 관리 |
| [**Kubernetes and OpenShift**](https://github.com/manusa/kubernetes-mcp-server) | OpenShift도 추가 지원하는 강력한 Kubernetes MCP 서버. 모든 Kubernetes 리소스에 대한 CRUD 작업과 클러스터 상호작용을 위한 전문 도구 제공 |
| [**liquidmetal-ai/raindrop-mcp**](https://docs.liquidmetal.ai/tutorials/claude-code-mcp-setup/) | Claude Code와 MCP를 사용하여 클라우드 인프라를 배포하는 최적의 방법 |
| [**localstack/localstack-mcp-server**](https://github.com/localstack/localstack-mcp-server) | 라이프사이클 관리, 인프라 배포, 로그 분석, 장애 주입, 상태 관리 등 로컬 AWS 환경을 관리하는 LocalStack용 MCP 서버 |
| [**mcp-containerd**](https://github.com/jokemanfire/mcp-containerd) | Rust로 구현된 containerd MCP. CRI 인터페이스 작업 지원 |
| [**mcp-k8s-go**](https://github.com/strowk/mcp-k8s-go) | Golang 기반 Kubernetes MCP 서버. Pod 및 로그, 이벤트, 네임스페이스 등을 탐색 가능. 확장성을 고려하여 설계 |
| [**meal-inc/bonnard-cli**](https://github.com/meal-inc/bonnard-cli) | 초고속 배포 가능한 에이전트 우선 MCP 지원 시맨틱 레이어 |
| [**megberts/mcp-websitepublisher-ai**](https://github.com/megberts/mcp-websitepublisher-ai) | AI 대화를 통해 웹사이트를 빌드하고 게시. 페이지, 에셋, 엔티티, 레코드, 통합을 위한 27개 MCP 도구. OAuth 2.1 자동 탐색을 지원하는 원격 서버 |
| [**Microsandbox**](https://github.com/microsandbox/microsandbox) | AI 코드의 안전한 실행을 위한 자체 호스팅 플랫폼. Code Interpreter, 데이터 분석, Browser Use에 적합 |
| [**Mulesoft**](https://www.npmjs.com/package/@mulesoft/mcp-server) | 호환 IDE 내에서 자연어로 MuleSoft 애플리케이션을 빌드, 배포 및 관리 |
| [**NanoVMs**](https://github.com/nanovms/ops-mcp) | 모든 클라우드에 Unikernel을 손쉽게 빌드하고 배포 |
| [**Netdata**](https://github.com/netdata/netdata/blob/master/src/web/mcp/README.md) | 메트릭, 로그, 시스템, 컨테이너, 프로세스, 네트워크 연결 등 모든 관찰 가능성 데이터를 활용한 탐색, 보고 및 근본 원인 분석 |
| [**Netlify**](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/) | Netlify 웹 플랫폼으로 웹사이트를 생성, 빌드, 배포 및 관리 |
| [**Node Code Sandbox**](https://github.com/alfonsograziano/node-code-sandbox-mcp) | 격리된 Docker 기반 샌드박스에서 npm 의존성을 즉시 설치하여 JavaScript 코드를 실행하는 Node.js MCP 서버 |
| [**ocireg**](https://github.com/StacklokLabs/ocireg-mcp) | LLM 기반 애플리케이션이 OCI 레지스트리와 상호작용할 수 있는 SSE 기반 MCP 서버. 컨테이너 이미지 정보 조회, 태그 목록 조회 등 지원 |
| [**Octopus Deploy**](https://github.com/OctopusDeploy/mcp-server) | Octopus Deploy 인스턴스를 쿼리, 검사 및 관리할 수 있는 공식 MCP 서버 |
| [**Onyx MCP Sandbox**](https://github.com/avd1729/Onyx) | 격리된 Docker 샌드박스에서 코드를 안전하게 실행하는 MCP 서버. Python, Java, C, C++, JavaScript, Rust 지원. CPU/메모리 제한 적용 |
| [**Pinner MCP**](https://github.com/safedep/pinner-mcp) | 공급망 공격을 방지하기 위해 GitHub Actions와 컨테이너 베이스 이미지를 불변 SHA 해시로 고정하는 MCP 서버 |
| [**portainer/portainer-mcp**](https://github.com/portainer/portainer-mcp) | AI 어시스턴트가 Portainer 인스턴스와 원활하게 상호작용할 수 있는 강력한 MCP 서버. 컨테이너 관리, 배포 작업, 인프라 모니터링에 대한 자연어 접근 제공 |
| [**Pulumi**](https://github.com/pulumi/mcp-server) | Pulumi를 사용하여 클라우드 인프라를 배포하고 관리 |
| [**Pulumi**](https://github.com/dogukanakkaya/pulumi-mcp-server) | Pulumi API와 상호작용하여 Stack을 생성하고 목록을 조회하는 MCP 서버 |
| [**pydantic/pydantic-ai/mcp-run-python**](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) | Deno와 Pyodide를 활용하여 MCP 도구 호출을 통해 보안 샌드박스에서 Python 코드 실행 |
| [**pythonanywhere/pythonanywhere-mcp-server**](https://github.com/pythonanywhere/pythonanywhere-mcp-server) | PythonAnywhere 클라우드 플랫폼용 MCP 서버 구현 |
| [**Qiniu MCP Server**](https://github.com/qiniu/qiniu-mcp-server) | Qiniu Cloud 제품 기반 MCP 서버. Qiniu Cloud Storage, 지능형 멀티미디어 서비스 등에 접근 가능 |
| [**r33drichards/mcp-js**](https://github.com/r33drichards/mcp-js) | V8을 사용하여 AI 생성 JavaScript를 안전하게 로컬 실행하는 코드 실행 샌드박스. 힙 스냅샷으로 영구 세션 지원 |
| [**reza-gholizade/k8s-mcp-server**](https://github.com/reza-gholizade/k8s-mcp-server) | 표준화된 인터페이스를 통해 Kubernetes 클러스터와 상호작용하는 MCP 서버. API 리소스 탐색, 리소스 관리, Pod 로그, 메트릭, 이벤트 지원 |
| [**s2-streamstore/s2-sdk-typescript**](https://github.com/s2-streamstore/s2-sdk-typescript) | S2.dev 서버리스 스트림 플랫폼의 공식 MCP 서버 |
| [**samvas-codes/dawshund_mcp**](https://github.com/samvas-codes/dawshund_mcp) | AWS IAM 데이터를 열거하고, 유효 권한을 분석하며, 사용자/역할/리소스 간 접근 관계를 시각화하는 dAWShund 기반 MCP 서버. 클라우드 보안 엔지니어를 위한 AWS ID 위험 인사이트 제공 |
| [**Shadcn Registry Manager**](https://github.com/reuvenaor/shadcn-registry-manager) | 로컬 또는 원격 레지스트리를 통해 자동화된 원격 또는 컨테이너화된 프로젝트 관리를 가능하게 하는 Shadcn UI용 MCP 서버 |
| [**silenceper/mcp-k8s**](https://github.com/silenceper/mcp-k8s) | 자연어로 Kubernetes 클러스터의 모든 리소스(Deployment, Service 등 네이티브 리소스 및 CRD)를 관리하는 AI 기반 도구. 복잡한 명령어 없이 AI가 정확히 실행 |
| [**skysqlinc/skysql-mcp**](https://github.com/skysqlinc/skysql-mcp) | 서버리스 MariaDB Cloud DB MCP 서버. 실행, 삭제, SQL 실행 및 정확한 text-to-SQL과 대화를 위한 DB 수준 AI 에이전트 작업 지원 |
| [**softvoyagers/pagedrop-api**](https://github.com/softvoyagers/pagedrop-api) | 붙여넣기, 파일 업로드, ZIP 배포를 지원하는 무료 즉시 HTML 호스팅 API. API 키 불필요 |
| [**Svelte Documentation**](https://github.com/khromov/llmctx) | 최신 Svelte 및 SvelteKit 문서를 제공하는 원격 서버(SSE/Streamable) |
| [**Tencent Cloud COS MCP**](https://github.com/Tencent/cos-mcp) | Tencent Cloud Storage(COS) 및 데이터 처리(CI) 기능과 빠르게 통합 |
| [**Terraform**](https://github.com/hashicorp/terraform-mcp-server) | Terraform 생태계와 원활하게 통합하여 Infrastructure as Code(IaC) 개발을 위한 고급 자동화 및 상호작용 기능을 제공 |
| [**Terraform-Cloud**](https://github.com/severity1/terraform-cloud-mcp) | AI 어시스턴트를 Terraform Cloud API와 통합하여 자연어 대화로 인프라를 관리하는 MCP 서버 |
| [**theonedev/tod**](https://github.com/theonedev/tod/blob/main/mcp.md) | CI/CD 파이프라인 편집, 이슈 워크플로 자동화, Pull Request 리뷰를 위한 OneDev MCP 서버 |
| [**Tianji**](https://github.com/msgbyte/tianji/tree/master/apps/mcp-server) | 자체 호스팅 또는 클라우드 플랫폼에서 Tianji 플랫폼과 상호작용 |
| [**Tiberriver256/mcp-server-azure-devops**](https://github.com/Tiberriver256/mcp-server-azure-devops) | 리포지토리 관리, 작업 항목, 파이프라인을 위한 Azure DevOps 통합 |
| [**Tinybird**](https://github.com/tinybirdco/mcp-tinybird) | Tinybird 서버리스 ClickHouse 플랫폼과 상호작용 |
| [**use_aws_mcp**](https://github.com/runjivu/use_aws_mcp) | amazon-q-cli의 use_aws 도구를 독립 MCP로 추출. 범용 AWS API 사용 지원 |
| [**Verbwire**](https://github.com/verbwire/verbwire-mcp-server) | Verbwire API를 통해 스마트 컨트랙트 배포, NFT 발행, IPFS 스토리지 관리 등을 수행 |
| [**Vercel**](https://vercel.com/docs/mcp/vercel-mcp) | 로그 접근, 문서 검색, 프로젝트 및 배포 관리 |
| [**vercel/next-devtools-mcp**](https://github.com/vercel/next-devtools-mcp) | 코딩 에이전트를 위한 공식 Next.js MCP 서버. 런타임 진단, 라우트 검사, 개발 서버 로그, 문서 검색, 업그레이드 가이드 제공. 전체 런타임 기능을 사용하려면 Next.js 16+ 개발 서버 필요 |

---

## 🌐 브라우저 & 웹

> Puppeteer, Playwright 등 브라우저 자동화 및 웹 스크래핑

| 서버 | 설명 |
|------|------|
| [**agent-infra/mcp-server-browser**](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) | Puppeteer를 사용한 브라우저 자동화 기능. 로컬 및 원격 브라우저 연결 모두 지원 |
| [**AgentQL**](https://github.com/tinyfish-io/agentql-mcp) | AI 에이전트가 AgentQL을 사용하여 비정형 웹에서 정형 데이터를 추출 |
| [**ananddtyagi/webpage-screenshot-mcp**](https://github.com/ananddtyagi/webpage-screenshot-mcp) | UI 개발 중 피드백으로 활용할 수 있는 웹페이지 스크린샷 캡처 MCP 서버 |
| [**Android MCP**](https://github.com/minhalvp/android-mcp-server) | ADB를 통해 Android 디바이스를 제어하는 MCP 서버. 디바이스 스크린샷 캡처, UI 레이아웃 분석, 패키지 관리, ADB 명령 실행 지원 |
| [**AnyCrawl**](https://github.com/any4ai/anycrawl-mcp-server) | Cursor, Claude 등 LLM 클라이언트를 위한 MCP를 통한 강력한 웹 스크래핑 및 크롤링 |
| [**apify/mcp-server-rag-web-browser**](https://github.com/apify/mcp-server-rag-web-browser) | Apify의 오픈소스 RAG Web Browser Actor로 웹 검색, URL 스크래핑, Markdown 콘텐츠 반환을 수행하는 MCP 서버 |
| [**automatalabs/mcp-server-playwright**](https://github.com/Automata-Labs-team/MCP-Server-Playwright) | Playwright를 사용한 브라우저 자동화 MCP 서버 |
| [**BB-fat/browser-use-rs**](https://github.com/BB-fat/browser-use-rs) | 의존성 제로의 Rust 경량 브라우저 자동화 MCP 서버 |
| [**Bing Webmaster Tools**](https://github.com/isiahw1/mcp-server-bing-webmaster) | 검색 분석, 사이트 관리, URL 제출, SEO 인사이트를 제공하는 Bing Webmaster Tools API 통합 MCP 서버 |
| [**blackwhite084/playwright-plus-python-mcp**](https://github.com/blackwhite084/playwright-plus-python-mcp) | LLM에 더 적합한 Playwright를 사용한 브라우저 자동화 Python MCP 서버 |
| [**Browser MCP**](https://github.com/browsermcp/mcp) | 로컬 브라우저 자동화 |
| [**BrowserLoop**](https://github.com/mattiasw/browserloop) | Playwright를 사용하여 웹 페이지 스크린샷을 캡처하는 MCP 서버. 설정 가능한 형식, 뷰포트 크기, 쿠키 기반 인증, 전체 페이지 및 요소 캡처 지원 |
| [**BrowserStack**](https://github.com/browserstack/mcp-server) | BrowserStack 테스트 플랫폼에 접근하여 디버그, 테스트 작성 및 수정, 접근성 테스트 등을 수행 |
| [**brutalzinn/simple-mcp-selenium**](https://github.com/brutalzinn/simple-mcp-selenium) | Cursor IDE에서 자연어로 브라우저를 제어하는 MCP Selenium Server. 테스트, 자동화, 다중 사용자 시나리오에 적합 |
| [**BurtTheCoder/mcp-maigret**](https://github.com/BurtTheCoder/mcp-maigret) | 다양한 공개 소스에서 사용자 계정 정보를 수집하는 강력한 OSINT 도구 maigret용 MCP 서버. 소셜 네트워크 사용자명 검색 및 URL 분석 도구 제공 |
| [**BurtTheCoder/mcp-virustotal**](https://github.com/BurtTheCoder/mcp-virustotal) | VirusTotal API를 쿼리하는 MCP 서버. URL 스캔, 파일 해시 분석, IP 주소 보고서 검색 도구 제공 |
| [**chasesaurabh/mcp-page-capture**](https://github.com/chasesaurabh/mcp-page-capture) | 뷰포트 또는 전체 페이지 옵션과 base64 PNG 출력을 지원하는 웹페이지 스크린샷 캡처 MCP 서버 |
| [**Chrome DevTools**](https://github.com/ChromeDevTools/chrome-devtools-mcp) | AI 코딩 어시스턴트가 Chrome에서 직접 웹 페이지를 디버그하여 런타임 인사이트와 디버깅 기능을 제공 |
| [**Chrome history**](https://github.com/vincent-pli/chrome-history-mcp) | AI와 브라우저 히스토리에 대해 대화 |
| [**co-browser/browser-use-mcp-server**](https://github.com/co-browser/browser-use-mcp-server) | SSE 전송을 지원하는 MCP 서버로 패키징된 browser-use. Docker에서 Chromium 실행 + VNC 서버를 위한 Dockerfile 포함 |
| [**Code Screenshot Generator**](https://github.com/MoussaabBadla/code-screenshot-mcp) | Claude에서 직접 전문적인 테마의 구문 강조 코드 스크린샷을 생성. 파일 읽기, 줄 선택, Git diff 시각화, 배치 처리 지원 |
| [**Crawlbase MCP**](https://github.com/crawlbase/crawlbase-mcp) | HTML, Markdown, 스크린샷을 지원하는 실시간 웹 데이터에 AI 에이전트가 접근 가능. Node.js, Python, Java, PHP, .NET SDK 제공 |
| [**Creatify**](https://github.com/TSavo/creatify-mcp) | 아바타 비디오, URL-to-비디오 변환, TTS, AI 편집 도구 등 Creatify AI API 기능을 제공하는 MCP 서버 |
| [**Decodo**](https://github.com/Decodo/decodo-mcp-server) | 쉬운 웹 데이터 접근. 웹사이트와 온라인 소스에서 정보를 간편하게 검색 |
| [**Defuddle Fetch**](https://github.com/domdomegg/defuddle-fetch-mcp-server) | Defuddle을 사용하여 웹 콘텐츠를 가져오고 깔끔한 Markdown으로 변환. 표준 HTML-to-Markdown 변환기보다 우수한 결과 |
| [**deusXmachina-dev/memorylane**](https://github.com/deusXmachina-dev/memorylane) | 이벤트 기반 스크린샷으로 화면 활동을 캡처하고, AI 생성 요약과 OCR 텍스트를 SQLite에 로컬 저장하며, 시맨틱 검색, 타임라인 탐색, 이벤트 상세 조회를 MCP로 AI 어시스턴트에 노출하는 데스크톱 앱 |
| [**DropBin**](https://dropbin.org/mcp) | 인증 없이 임시 URL을 통해 HTML 웹페이지를 호스팅하고 콘텐츠를 공유하는 원격 SSE MCP 서버 |
| [**Dumpling AI**](https://github.com/Dumpling-AI/mcp-server-dumplingai) | Dumpling AI의 데이터, 웹 스크래핑, 문서 변환 API에 접근 |
| [**eyalzh/browser-control-mcp**](https://github.com/eyalzh/browser-control-mcp) | LLM 클라이언트가 사용자의 브라우저(Firefox)를 제어할 수 있도록 브라우저 확장과 연동되는 MCP 서버 |
| [**Firecrawl**](https://github.com/firecrawl/firecrawl-mcp-server) | Firecrawl로 웹 데이터 추출 |
| [**Firecrawl**](https://github.com/mendableai/firecrawl-mcp-server) | Firecrawl로 웹 데이터 추출 |
| [**freema/firefox-devtools-mcp**](https://github.com/freema/firefox-devtools-mcp) | WebDriver BiDi를 통한 Firefox 브라우저 자동화. 스냅샷/UID 기반 상호작용, 네트워크 모니터링, 콘솔 캡처, 스크린샷 지원 |
| [**gridinsoft/mcp-inspector**](https://github.com/gridinsoft/mcp-inspector) | GridinSoft Inspector 기반의 도메인 및 URL 보안 분석 MCP 서버. AI 에이전트가 웹사이트 및 링크 안전성을 검증 가능 |
| [**hanselhansel/aeo-cli**](https://github.com/hanselhansel/aeo-cli) | AI 크롤러 준비 상태를 감사하는 URL 검사 도구. robots.txt, llms.txt, JSON-LD 스키마, 콘텐츠 밀도를 0-100 AEO 점수로 평가 |
| [**HTML to Markdown**](https://github.com/levz0r/html-to-markdown-mcp) | 웹 페이지를 가져와 HTML을 깔끔하게 정돈된 Markdown으로 변환. 대용량 페이지의 경우 토큰 제한 우회를 위한 자동 파일 저장 지원 |
| [**Hyperbrowser**](https://github.com/hyperbrowserai/mcp) | AI 에이전트를 지원하고 손쉬운 확장 가능한 브라우저 자동화를 가능하게 하는 차세대 플랫폼 |
| [**imprvhub/mcp-browser-agent**](https://github.com/imprvhub/mcp-browser-agent) | Claude Desktop에 자율 브라우저 자동화 기능을 제공하는 MCP 통합 |
| [**jae-jae/fetcher-mcp**](https://github.com/jae-jae/fetcher-mcp) | Playwright 헤드리스 브라우저로 웹 페이지 콘텐츠를 가져오는 MCP 서버. JavaScript 렌더링 및 지능형 콘텐츠 추출을 지원하며 Markdown 또는 HTML 형식으로 출력 |
| [**jimfilippou/things-mcp**](https://github.com/jimfilippou/things-mcp) | Things 생산성 앱과의 원활한 통합을 제공하는 MCP 서버. AI 어시스턴트가 Things의 할 일과 프로젝트를 생성, 수정, 관리 가능 |
| [**Jina Reader**](https://github.com/wong2/mcp-jina-reader) | Jina Reader를 사용하여 원격 URL의 콘텐츠를 Markdown으로 가져오기 |
| [**JSON to Excel by WTSolutions**](https://github.com/he-yang/json-to-excel-mcp) | JSON 데이터 또는 공개 .json 파일의 URL에서 CSV 형식 문자열로 변환 |
| [**kimdonghwi94/Web-Analyzer-MCP**](https://github.com/kimdonghwi94/web-analyzer-mcp) | RAG를 위한 깔끔한 웹 콘텐츠 추출 및 웹 페이지에 대한 Q&A 제공 |
| [**kukapay/chainlist-mcp**](https://github.com/kukapay/chainlist-mcp) | AI 에이전트에게 RPC URL, 체인 ID, 익스플로러, 네이티브 토큰 등 검증된 EVM 체인 정보에 대한 빠른 접근을 제공하는 MCP 서버 |
| [**lightpanda-io/gomcp**](https://github.com/lightpanda-io/gomcp) | 웹 자동화를 위해 설계된 초고속 헤드리스 브라우저 Lightpanda용 Go MCP 서버 |
| [**louis030195/terminator-mcp-agent**](https://github.com/mediar-ai/terminator/tree/main/terminator-mcp-agent) | 접근성 API를 사용한 데스크톱 GUI 자동화. 비전 모델이나 스크린샷 없이 Windows, macOS, Linux 앱을 제어. 워크플로 녹화, 구조화된 데이터 추출, 브라우저 DOM 검사 지원 |
| [**mcp-read-website-fast**](https://github.com/just-every/mcp-read-website-fast) | 웹사이트를 깔끔한 Markdown으로 변환하는 빠르고 토큰 효율적인 웹 콘텐츠 추출. Mozilla Readability, 스마트 캐싱, robots.txt 준수, 동시 페칭 지원 |
| [**mcp-screenshot-website-fast**](https://github.com/just-every/mcp-screenshot-website-fast) | Claude Vision API에 최적화된 고품질 스크린샷 캡처. 전체 페이지를 1072x1072 청크로 자동 타일링하며 설정 가능한 뷰포트 및 동적 콘텐츠 대기 전략 제공 |
| [**modelcontextprotocol/server-fetch**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/fetch) | AI 활용을 위한 효율적인 웹 콘텐츠 가져오기 및 처리 |
| [**ndthanhdev/mcp-browser-kit**](https://github.com/ndthanhdev/mcp-browser-kit) | AI 어시스턴트가 로컬 브라우저와 상호작용할 수 있게 하는 MCP 서버 |
| [**nguyenvanduocit/all-in-one-model-context-protocol**](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) | 개발자를 위한 종합 도구 모음. Confluence, Jira, YouTube, 스크립트 실행, 지식 베이스 RAG, URL 가져오기, 이메일, 캘린더, GitLab 등 엔지니어에게 필요한 거의 모든 기능 제공 |
| [**Notte**](https://github.com/nottelabs/notte/tree/main/packages/notte-mcp) | Notte Web AI 에이전트 및 클라우드 브라우저 세션을 활용한 확장 가능한 브라우저 자동화 및 스크래핑 워크플로 |
| [**Pantheon-Security/chrome-mcp-secure**](https://github.com/Pantheon-Security/chrome-mcp-secure) | 포스트 양자 암호화(ML-KEM-768 + ChaCha20-Poly1305), 보안 자격 증명 저장소, 메모리 스크러빙, 감사 로깅을 갖춘 보안 강화 Chrome 자동화. 22개 도구 제공 |
| [**Peekaboo**](https://github.com/steipete/Peekaboo) | AI 에이전트가 애플리케이션 또는 전체 시스템의 스크린샷을 캡처할 수 있는 macOS 전용 MCP 서버 |
| [**PhungXuanAnh/selenium-mcp-server**](https://github.com/PhungXuanAnh/selenium-mcp-server) | Selenium WebDriver를 통한 웹 자동화 기능을 제공하는 MCP 서버 |
| [**Playwright**](https://github.com/microsoft/playwright-mcp) | Playwright를 사용한 브라우저 자동화 MCP 서버. 테스트 실행, 페이지 탐색, 스크린샷 캡처, 콘텐츠 스크래핑, 웹 상호작용 자동화 |
| [**Playwright**](https://github.com/executeautomation/mcp-playwright) | Playwright를 사용한 브라우저 자동화 및 웹 스크래핑 MCP 서버 |
| [**Playwright Wizard**](https://github.com/oguzc/playwright-wizard-mcp) | 모범 사례를 적용한 Playwright E2E 테스트 생성 단계별 마법사 |
| [**pragmar/mcp-server-webcrawl**](https://github.com/pragmar/mcp-server-webcrawl) | 웹 크롤러 데이터에 대한 고급 검색 및 검색. WARC, wget, Katana, SiteOne, InterroBot 크롤러 지원 |
| [**pskill9/website-downloader**](https://github.com/pskill9/website-downloader) | wget을 사용하여 전체 웹사이트를 다운로드하는 MCP 서버입니다. 웹사이트 구조를 보존하고 링크를 로컬에서 작동하도록 변환합니다. |
| [**Puppeteer**](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | 웹 스크래핑 및 상호작용을 위한 브라우저 자동화 |
| [**Puppeteer vision**](https://github.com/djannot/puppeteer-vision-mcp) | Puppeteer로 웹 페이지를 탐색하여 고품질 Markdown을 반환. AI 비전 기능으로 쿠키, CAPTCHA 등 인터랙티브 요소를 자동 처리 |
| [**Pure.md**](https://github.com/puremd/puremd-mcp) | pure.md로 웹 콘텐츠를 Markdown 형식으로 안정적으로 접근 (봇 감지 우회, 프록시 순환, 헤드리스 JS 렌더링 내장) |
| [**qa-use**](https://github.com/desplega-ai/qa-use) | 브라우저 자동화 및 QA 테스트 기능. desplega.ai와 통합하여 자동 테스트, 세션 모니터링, 배치 테스트 실행, 지능형 테스트 가이드를 제공 |
| [**ScrAPI**](https://github.com/DevEnterpriseSoftware/scrapi-mcp) | ScrAPI를 사용한 웹 스크래핑. 봇 감지, CAPTCHA, 지역 제한으로 접근이 어려운 웹사이트 콘텐츠 추출 |
| [**ScreenshotMCP**](https://github.com/upnorthmedia/ScreenshotMCP/) | 전체 페이지, 요소, 디바이스 크기 기능을 갖춘 웹사이트 스크린샷 캡처용 MCP 서버 |
| [**ScreenshotOne**](https://github.com/screenshotone/mcp/) | ScreenshotOne으로 웹사이트 스크린샷 렌더링 |
| [**Screeny**](https://github.com/rohanrav/screeny) | 프라이버시 우선의 macOS 전용 MCP 서버. 윈도우 스크린샷을 통해 AI 에이전트에 시각적 컨텍스트 제공 |
| [**SearXNG**](https://github.com/erhwenkuo/mcp-searxng) | SearXNG를 통한 웹 검색 및 URL의 Markdown 변환을 제공하는 MCP 서버 |
| [**serkan-ozal/browser-devtools-mcp**](https://github.com/serkan-ozal/browser-devtools-mcp) | AI 어시스턴트가 웹 애플리케이션을 자율적으로 테스트, 디버그, 검증할 수 있는 MCP 서버 |
| [**ShopSavvy**](https://github.com/shopsavvy/shopsavvy-mcp-server) | AI 어시스턴트를 위한 완전한 제품 및 가격 데이터 솔루션. 바코드/ASIN/URL로 제품 검색, 상세 메타데이터 접근, 수천 개 리테일러의 포괄적 가격 데이터 접근 |
| [**softvoyagers/linkmeta-api**](https://github.com/softvoyagers/linkmeta-api) | Open Graph, Twitter Cards, 파비콘, JSON-LD 등 무료 URL 메타데이터 추출 API. API 키 불필요 |
| [**softvoyagers/linkshrink-api**](https://github.com/softvoyagers/linkshrink-api) | 분석 및 링크 관리를 갖춘 프라이버시 우선 무료 URL 단축 API. API 키 불필요 |
| [**softvoyagers/pageshot-api**](https://github.com/softvoyagers/pageshot-api) | 형식, 뷰포트, 다크 모드 옵션을 지원하는 무료 웹페이지 스크린샷 캡처 API. API 키 불필요 |
| [**softvoyagers/pdfspark-api**](https://github.com/softvoyagers/pdfspark-api) | Playwright 기반의 무료 HTML/URL-to-PDF 변환 API. API 키 불필요 |
| [**sonnyflylock/voxie-ai-directory-mcp**](https://github.com/sonnyflylock/voxie-ai-directory-mcp) | 웹챗을 통해 AI 서비스에 접근할 수 있는 AI 전화번호부. Voxie AI 페르소나 및 ChatGPT 등 서드파티 서비스를 쿼리하고 무료 웹챗 URL을 즉시 제공 |
| [**Supadata**](https://github.com/supadata-ai/mcp) | YouTube, TikTok, X, 웹 데이터를 제공하는 Supadata 공식 MCP 서버 |
| [**urlDNA**](https://github.com/urldna/mcp) | urlDNA를 사용하여 잠재적으로 악성인 URL을 동적으로 스캔하고 분석 |
| [**WebDataSource**](https://webdatasource.com/releases/latest/mcp/index.html) | AI 에이전트용 웹 크롤러. MCP 지원 웹 크롤러로 웹과 개인 지식 베이스에서 실시간 인사이트를 제공하여 AI 에이전트를 강화 |
| [**webpeel/webpeel**](https://github.com/webpeel/webpeel) | HTTP에서 헤드리스 브라우저, 스텔스 모드로 자동 에스컬레이션되는 AI 에이전트용 스마트 웹 페처. fetch, search, crawl 등 9개 MCP 도구 포함. 30개 URL 벤치마크에서 100% 성공률 달성 |
| [**WebScraping.AI**](https://github.com/webscraping-ai/webscraping-ai-mcp-server) | WebScraping.AI와 연동하여 웹 데이터 추출 및 스크래핑 수행 |
| [**wishfinity/wishfinity-mcp-plusw**](https://github.com/wishfinity/wishfinity-mcp-plusw) | AI 쇼핑 경험을 위한 범용 위시리스트. 모든 스토어의 제품 URL을 위시리스트에 저장. Claude, ChatGPT, LangChain, n8n 등 모든 MCP 클라이언트와 호환 |
| [**YetiBrowser MCP**](https://github.com/yetidevworks/yetibrowser-mcp) | 최적화된 스크린샷, DOM diff, 콘솔 접근, 멀티 WebSocket 지원 등을 갖춘 완전 오픈소스 Browser MCP 워크플로 구현 |
| [**zboralski/ida-headless-mcp**](https://github.com/zboralski/ida-headless-mcp) | MCP를 통한 헤드리스 IDA Pro 바이너리 분석. Go 오케스트레이션과 Python 워커를 사용한 멀티 세션 동시 처리. Unity 및 Flutter 리버스 엔지니어링을 위한 Il2CppDumper 및 Blutter 메타데이터 임포트 지원 |
| [**zcaceres/markdownify-mcp**](https://github.com/zcaceres/markdownify-mcp) | 거의 모든 파일이나 웹 콘텐츠를 Markdown으로 변환하는 MCP 서버 |

---

## 📝 소스 제어 & 코드 관리

> GitHub, GitLab, Bitbucket 등 소스 코드 관리

| 서버 | 설명 |
|------|------|
| [**aashari/mcp-server-atlassian-bitbucket**](https://github.com/aashari/mcp-server-atlassian-bitbucket) | Atlassian Bitbucket Cloud 통합. AI 시스템이 리포지토리, Pull Request, 워크스페이스, 코드와 실시간으로 상호작용 가능 |
| [**AtomGit**](https://atomgit.com/atomgit-open-source-ecosystem/atomgit-mcp-server) | 리포지토리 관리, PR, 이슈, 브랜치, 라벨 등을 위한 AtomGit 공식 서버 |
| [**Codacy**](https://github.com/codacy/codacy-mcp-server/) | Codacy API와 상호작용하여 코드 품질 이슈, 취약점, 커버리지 인사이트를 쿼리 |
| [**Cursor MCP Installer**](https://github.com/matthewdcage/cursor-mcp-installer) | Cursor IDE 내에서 다른 MCP 서버를 쉽게 설치하고 구성하는 도구. npm 패키지, 로컬 디렉토리, Git 리포지토리 지원 |
| [**Digma**](https://github.com/digma-ai/digma-mcp-server) | OTEL/APM 데이터 기반 동적 코드 분석을 수행하는 코드 관찰 가능성 MCP. 코드 리뷰, 이슈 식별 및 수정, 위험 코드 강조 등을 지원 |
| [**Git**](https://github.com/geropl/git-mcp-go) | LLM이 로컬 Git 리포지토리와 상호작용할 수 있도록 지원. 선택적 Push 기능 포함 |
| [**Gitea**](https://gitea.com/gitea/gitea-mcp) | MCP를 통해 Gitea 인스턴스와 상호작용 |
| [**Gitee**](https://github.com/oschina/mcp-gitee) | Gitee API 통합, 리포지토리, 이슈, Pull Request 관리 등 |
| [**GitHub**](https://github.com/github/github-mcp-server) | GitHub 공식 MCP Server |
| [**Github**](https://github.com/0xshariq/github-mcp-server) | AI 어시스턴트와 개발자를 위한 29개 Git 작업 + 11개 워크플로 조합을 제공하는 MCP 서버. 포괄적인 Git 리포지토리 관리 기능 노출 |
| [**GitHub Actions**](https://github.com/ko1ynnky/github-actions-mcp-server) | GitHub Actions와 상호작용하기 위한 MCP 서버 |
| [**GitHub Enterprise MCP**](https://github.com/ddukbg/github-enterprise-mcp) | GitHub Enterprise와 상호작용하기 위한 MCP 서버 |
| [**GitHub GraphQL**](https://github.com/QuentinCody/github-graphql-mcp-server) | GitHub GraphQL API에 접근하여 리포지토리 데이터, 이슈, Pull Request 등에 대해 더 강력하고 유연한 쿼리를 가능하게 하는 비공식 GitHub MCP 서버 |
| [**GitHub Projects**](https://github.com/redducklabs/github-projects-mcp) | 아이템, 필드, 마일스톤을 포함한 전체 GraphQL API 접근으로 GitHub Projects를 관리 |
| [**GitHub Repos Manager MCP Server**](https://github.com/kurdin/github-repos-manager-mcp) | 토큰 기반 GitHub 자동화 관리. Docker 불필요, 유연한 구성, 직접 API 통합으로 80개 이상의 도구 제공 |
| [**GitKraken**](https://github.com/gitkraken/gk-cli?tab=readme-ov-file#mcp-server) | GitKraken API와 상호작용하는 CLI. `gk mcp`로 GitKraken API뿐만 아니라 Jira, GitHub, GitLab 등도 지원하는 MCP 서버 포함 |
| [**GitKraken**](https://github.com/gitkraken/gk-cli) | GitKraken API와 상호작용하는 CLI. `gk mcp`로 GitKraken API뿐만 아니라 Jira, GitHub, GitLab 등도 지원하는 MCP 서버 포함 |
| [**GitLab**](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) | AI 도구가 OAuth 2.0을 통해 GitLab 프로젝트 데이터에 안전하게 접근하고, 이슈를 관리하며, 리포지토리 작업을 수행할 수 있는 GitLab 공식 MCP 서버 |
| [**HainanZhao/mcp-gitlab-jira**](https://github.com/HainanZhao/mcp-gitlab-jira) | GitLab과 Jira를 위한 통합 MCP 서버. AI 에이전트로 프로젝트, Merge Request, 파일, 릴리스, 티켓을 관리 |
| [**JFrog**](https://github.com/jfrog/mcp-jfrog) | 리포지토리 관리, 빌드 추적, 릴리스 라이프사이클 관리 등을 지원하는 JFrog Platform API용 MCP 서버 |
| [**kaiyuanxiaobing/atomgit-mcp-server**](https://github.com/kaiyuanxiaobing/atomgit-mcp-server) | 리포지토리 관리, PR, 이슈, 브랜치, 라벨 등을 위한 AtomGit 공식 서버 |
| [**kopfrechner/gitlab-mr-mcp**](https://github.com/kopfrechner/gitlab-mr-mcp) | GitLab 프로젝트의 이슈 및 Merge Request와 원활하게 상호작용 |
| [**modelcontextprotocol/server-git**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git) | 로컬 리포지토리의 읽기, 검색, 분석을 포함한 직접적인 Git 리포지토리 작업 |
| [**narumiruna/gitingest-mcp**](https://github.com/narumiruna/gitingest-mcp) | gitingest를 사용하여 모든 Git 리포지토리를 간단한 코드베이스 텍스트 요약으로 변환하는 MCP 서버 |
| [**religa/multi-mcp**](https://github.com/religa/multi_mcp) | ChatGPT, Claude, Gemini를 활용한 병렬 멀티 모델 코드 리뷰, 보안 분석, AI 토론. 비교, 합의, OWASP Top 10 보안 검사를 위한 다중 LLM 오케스트레이션 |
| [**ryan0204/github-repo-mcp**](https://github.com/Ryan0204/github-repo-mcp) | AI 어시스턴트가 GitHub 리포지토리를 탐색하고, 디렉토리를 탐험하며, 파일 내용을 확인할 수 있는 GitHub Repo MCP |
| [**selvage-lab/selvage**](https://github.com/selvage-lab/selvage) | AST 기반 스마트 컨텍스트 추출을 갖춘 LLM 기반 코드 리뷰 MCP 서버. Claude, GPT, Gemini 및 OpenRouter를 통한 20개 이상 모델 지원 |
| [**Sonatype MCP Server**](https://github.com/brianveltman/sonatype-mcp) | Sonatype Nexus Repository Manager 및 Sonatype Repository Firewall용 MCP. AI 지원 워크플로를 통한 DevSecOps 관행 관리 |
| [**spyrae/claude-concilium**](https://github.com/spyrae/claude-concilium) | Claude Code용 멀티 에이전트 AI 자문 프레임워크. CLI 도구(Codex, Gemini, Qwen)를 래핑하는 3개 MCP 서버로 병렬 코드 리뷰와 문제 해결 수행. 폴백 체인 및 오류 감지 포함 |
| [**TamarEngel/jira-github-mcp**](https://github.com/TamarEngel/jira-github-mcp) | Jira와 GitHub를 통합하여 이슈 추적부터 브랜치, 커밋, Pull Request, 머지까지 엔드투엔드 개발 워크플로를 IDE 내에서 자동화하는 MCP 서버 |
| [**TamiShaks-2/git-context-mcp**](https://github.com/TamiShaks-2/git-context-mcp) | AI 코딩 에이전트를 위한 구조화된 Git 리포지토리 분석(프로젝트 상태, 최근 활동, 코드 맵, 위험 핫스팟)을 제공하는 로컬 MCP 서버 |

---

## 📋 프로젝트 관리

> Jira, Linear, Trello 등 프로젝트/일정/캘린더 관리

| 서버 | 설명 |
|------|------|
| [**aashari/mcp-server-atlassian-jira**](https://github.com/aashari/mcp-server-atlassian-jira) | Atlassian Jira Cloud 연동. AI 시스템이 Jira 프로젝트, 이슈, 코멘트 및 관련 개발 정보와 실시간 상호작용 |
| [**Agile Luminary**](https://github.com/AgileLuminary/mcp-agile-luminary) | 간편한 프로젝트 관리 — Agile Luminary 스토리를 IDE로 직접 전송 |
| [**AI Tasks**](https://github.com/jbrinkman/valkey-ai-tasks) | AI가 통합 태스크 관리 및 추적 도구로 복잡한 계획을 관리. STDIO, SSE, Streamable HTTP 트랜스포트 지원 |
| [**Apple Calendar**](https://github.com/Omar-v2/mcp-ical) | 자연어로 macOS 캘린더와 상호작용. 이벤트 생성, 수정, 일정 조회, 빈 시간 찾기 등 지원 |
| [**Apple Shortcuts**](https://github.com/recursechat/mcp-server-apple-shortcuts) | Apple Shortcuts와 통합하는 MCP 서버 |
| [**Atlassian**](https://www.atlassian.com/platform/remote-mcp-server) | Jira 작업 항목 및 Confluence 페이지와 안전하게 상호작용하고 통합 검색 제공 |
| [**Atono**](https://docs.atono.io/docs/mcp-server-for-atono/) | AI 어시스턴트를 Atono에 연결하여 스토리, 버그, 할당, 수정 사항을 생성 및 업데이트 |
| [**CalDAV MCP**](https://github.com/dominik1001/caldav-mcp) | CalDAV 프로토콜 기반 캘린더 작업을 AI 어시스턴트 도구로 제공하는 MCP 서버 |
| [**Calendly-mcp-server**](https://github.com/meAmitPatil/calendly-mcp-server) | 오픈소스 Calendly MCP 서버 |
| [**cjo4m06/mcp-shrimp-task-manager**](https://github.com/cjo4m06/mcp-shrimp-task-manager) | 프로그래밍 중심 태스크 관리 시스템. Cursor AI 같은 코딩 에이전트에 고급 태스크 메모리, 자기 성찰, 의존성 관리 제공 |
| [**Dart**](https://github.com/its-dart/dart-mcp-server) | AI 네이티브 프로젝트 관리 도구 Dart에서 태스크, 문서, 프로젝트 데이터와 상호작용 |
| [**DevOps-MCP**](https://github.com/wangkanai/devops-mcp) | 디렉토리 기반 인증 전환을 지원하는 동적 Azure DevOps MCP 서버. 작업 항목, 리포지토리, 빌드, 파이프라인, 멀티 프로젝트 관리 지원 |
| [**eyaltoledano/claude-task-master**](https://github.com/eyaltoledano/claude-task-master) | AI 기반 태스크 관리 시스템. PRD 파싱, 태스크 확장, 멀티 프로바이더 지원(Claude, OpenAI, Gemini, Perplexity, xAI), 선택적 도구 로딩 |
| [**Fastmail MCP**](https://github.com/MadLlama25/fastmail-mcp) | JMAP을 통한 Fastmail 접근: 이메일 목록/검색, 발송, 이동, 첨부파일/스레드 처리, 연락처 및 캘린더 도구 제공 |
| [**Fibery**](https://github.com/Fibery-inc/fibery-mcp-server) | Fibery 워크스페이스에서 쿼리 및 엔티티 작업 수행 |
| [**foxintheloop/UpTier**](https://github.com/foxintheloop/UpTier) | 깔끔한 To Do 스타일 UI의 데스크톱 태스크 매니저. 우선순위 관리, 목표 추적, 멀티 프로필 워크플로우용 25개 이상 MCP 도구 제공 |
| [**Google Calendar**](https://github.com/v-3/google-calendar) | Google Calendar 연동으로 일정 확인, 시간 찾기, 이벤트 추가/삭제 |
| [**Google Calendar**](https://github.com/nspady/google-calendar-mcp) | Google Calendar 이벤트 관리용 MCP 서버. 제목, 위치 등 속성으로 이벤트 검색도 지원 |
| [**Jira Context MCP**](https://github.com/rahulthedevil/Jira-Context-MCP) | Cursor 같은 AI 코딩 에이전트에 Jira 티켓 정보를 제공하는 MCP 서버 |
| [**khaoss85/mcp-orchestro**](https://github.com/khaoss85/mcp-orchestro) | Claude Code용 Trello: AI 기반 태스크 관리, 60개 MCP 도구, 시각적 칸반 보드, 지능형 오케스트레이션 제공 |
| [**KS-GEN-AI/jira-mcp-server**](https://github.com/KS-GEN-AI/jira-mcp-server) | JQL 및 API를 통한 Jira 데이터 조회, 티켓 생성·편집 요청 실행 |
| [**Leximo-AI/leximo-ai-call-assistant-mcp-server**](https://github.com/Leximo-AI/leximo-ai-call-assistant-mcp-server) | AI 기반 전화 대행 — 예약, 일정 잡기, 통화 트랜스크립트 조회 |
| [**Linear**](https://linear.app/docs/mcp) | Linear 이슈, 프로젝트, 코멘트 검색·생성·업데이트 |
| [**Linear**](https://github.com/tacticlaunch/mcp-linear) | Linear 프로젝트 관리 시스템과 상호작용 |
| [**Linear**](https://github.com/jerhadf/linear-mcp-server) | LLM이 Linear API와 상호작용하여 이슈 검색, 생성, 업데이트 등 프로젝트 관리 수행 |
| [**Linear (Go)**](https://github.com/geropl/linear-mcp-go) | 단일 정적 바이너리로 LLM이 Linear API와 상호작용 |
| [**Linear MCP**](https://github.com/anoncam/linear-mcp) | Linear SDK 전체 구현으로 프로젝트, 이니셔티브, 이슈, 사용자, 팀, 상태를 종합적으로 관리 |
| [**madbonez/caldav-mcp**](https://github.com/madbonez/caldav-mcp) | 범용 CalDAV 프로토콜 MCP 서버. Yandex, Google Calendar, Nextcloud, iCloud 등 모든 CalDAV 호환 서버 지원. 반복 이벤트, 카테고리, 참석자, 알림 등 포함 |
| [**MCP ProjectManage OpenProject**](https://github.com/boma086/mcp-projectmanage-openproject) | OpenProject에서 프로젝트 관리 정보를 가져와 주간 보고서를 생성하는 MCP 서비스 |
| [**MCP Toolz**](https://github.com/taylorleese/mcp-toolz) | Claude Code용 컨텍스트 관리, TODO 영속화, AI 세컨드 오피니언. 세션 간 컨텍스트·코드 스니펫·TODO 리스트 저장/복원 및 ChatGPT, Claude, Gemini 등에서 피드백 수신 |
| [**mmntm/weblate-mcp**](https://github.com/mmntm/weblate-mcp) | Weblate 번역 관리용 종합 MCP 서버. AI 어시스턴트가 번역 작업, 프로젝트 관리, 콘텐츠 검색을 스마트 형식 변환과 함께 수행 |
| [**Monday.com**](https://github.com/mondaycom/mcp) | Monday.com 보드, 아이템, 계정 및 워크 폼과 상호작용 |
| [**Monday.com (unofficial)**](https://github.com/sakce/mcp-server-monday) | Monday.com 보드 및 아이템과 상호작용하는 MCP 서버 |
| [**moro3k/mcp-altegio**](https://github.com/moro3k/mcp-altegio) | Altegio API용 MCP 서버 — 살롱/스파/클리닉 관리를 위한 예약, 고객, 서비스, 직원 스케줄. 18개 도구와 Docker 지원 |
| [**Nextcloud Calendar**](https://github.com/Cheffromspace/mcp-nextcloud-calendar) | CalDAV 기반 Nextcloud 캘린더 연동. 캘린더, 이벤트, 참석자 등 관리 |
| [**nguyenvanduocit/jira-mcp**](https://github.com/nguyenvanduocit/jira-mcp) | Go 기반 Jira MCP 커넥터. AI 어시스턴트가 이슈 관리, 스프린트 계획, 워크플로우 전환 등 일반적인 Jira 작업을 수행 |
| [**PagerDuty**](https://github.com/PagerDuty/pagerduty-mcp-server) | PagerDuty 계정과 연동하여 인시던트, 서비스, 스케줄 등을 MCP 클라이언트에서 직접 관리 |
| [**Plane**](https://github.com/makeplane/plane-mcp-server) | Plane 공식 MCP 서버. Plane API 연동으로 프로젝트, 작업 항목, 사이클 등의 AI 자동화 지원 |
| [**Project Manager**](https://github.com/croffasia/mcp-project-manager) | 계층형 태스크 관리(아이디어 → 에픽 → 태스크)와 CLI 대시보드 제공 |
| [**rinadelph/Agent-MCP**](https://github.com/rinadelph/Agent-MCP) | MCP를 활용한 멀티 에이전트 시스템 프레임워크. 태스크 관리, 공유 컨텍스트, RAG 기능으로 조율된 AI 협업 지원 |
| [**Routine**](https://github.com/routineco/mcp-server) | Routine의 캘린더, 태스크, 노트 등과 상호작용하는 MCP 서버 |
| [**roychri/mcp-server-asana**](https://github.com/roychri/mcp-server-asana) | Asana API와 MCP 클라이언트(Claude Desktop 등)를 연결하는 MCP 서버 구현 |
| [**Shortcut**](https://github.com/useshortcut/mcp-server-shortcut) | Shortcut의 프로젝트 및 태스크(Stories)에 접근하고 구현 |
| [**Siri Shortcuts**](https://github.com/dvcrn/mcp-server-siri-shortcuts) | macOS의 Siri Shortcuts와 상호작용. 모든 단축어를 MCP 도구로 노출 |
| [**snyk/studio-mcp**](https://github.com/snyk/studio-mcp) | Snyk 보안 엔진을 에이전트 워크플로우에 내장. AI 생성 코드를 실시간 보안 검사하고 취약점 백로그 해소 가속화 |
| [**Sugar**](https://github.com/cdnsteve/sugar) | Claude Code용 자율 AI 개발 플랫폼. 태스크 관리, 특화 에이전트, 워크플로우 자동화 제공 |
| [**takumi0706/google-calendar-mcp**](https://github.com/takumi0706/google-calendar-mcp) | Google Calendar API와 연동하는 TypeScript 기반 MCP 서버 |
| [**Tasks**](https://github.com/flesler/mcp-tasks) | 효율적인 태스크 매니저. LLM 토큰 효율을 극대화하면서 강력한 검색, 필터링, 정리 기능을 다양한 파일 형식으로 제공 |
| [**Things3 MCP**](https://github.com/urbanogardun/things3-mcp) | macOS용 Things3 태스크 관리 연동. TODO, 프로젝트, 태그 종합 관리 지원 |
| [**TickTick**](https://github.com/alexarevalo9/ticktick-mcp-server) | TickTick 태스크 관리 플랫폼과 연동하여 지능형 컨텍스트 인식 태스크 작업 및 자동화 지원 |
| [**Todoist**](https://github.com/doist/todoist-ai) | Todoist 태스크, 프로젝트, 섹션, 코멘트 등을 검색·추가·업데이트 |
| [**Todoist**](https://github.com/abhiz123/todoist-mcp-server) | Todoist와 연동하여 태스크 관리 |
| [**Todoist**](https://github.com/stanislavlysenko0912/todoist-mcp-server) | Todoist Rest API 전체 구현 MCP 서버 |
| [**Todos**](https://github.com/tomelliot/todos-mcp) | 챗봇과 함께 사용하는 실용적인 TODO 리스트 매니저 |
| [**tom28881/mcp-jira-server**](https://github.com/tom28881/mcp-jira-server) | 종합 TypeScript Jira MCP 서버. 이슈 CRUD, 스프린트 관리, 코멘트/이력, 첨부파일, 배치 작업 등 20개 이상 도구 제공 |
| [**Trello**](https://github.com/m0xai/trello-mcp-server) | Trello 보드, 리스트, 카드와 상호작용하는 연동 서버 |
| [**Trello MCP**](https://github.com/kocakli/Trello-Desktop-MCP) | Claude Desktop에서 자연어 명령으로 Trello 보드, 카드, 리스트, 팀원과 상호작용하는 MCP 서버 |
| [**Trello MCP Server**](https://github.com/lioarce01/trello-mcp-server) | 프롬프트를 통해 사용자 Trello 보드와 상호작용하고 수정하는 MCP 서버 |
| [**universalamateur/reclaim-mcp-server**](https://github.com/universalamateur/reclaim-mcp-server) | Reclaim.ai 캘린더 연동. 태스크, 습관, 집중 시간, 스케줄링 링크, 생산성 분석용 40개 도구 제공 |
| [**wyattjoh/calendar-mcp**](https://github.com/wyattjoh/calendar-mcp) | macOS 캘린더 이벤트에 접근하는 MCP 서버 |
| [**ybouhjira/claude-code-tts**](https://github.com/ybouhjira/claude-code-tts) | Claude Code용 텍스트 음성 변환 MCP 서버 플러그인. OpenAI TTS API 활용, 6가지 음성, 워커 풀 아키텍처, 크로스 플랫폼 지원 |
| [**YouTrack**](https://github.com/tonyzorin/youtrack-mcp) | JetBrains YouTrack 이슈 추적 시스템과 AI 어시스턴트가 상호작용할 수 있는 MCP 서버 |
| [**Yuga Planner**](https://github.com/blackopsrepl/yuga-planner) | LlamaIndex와 Timefold를 활용한 AI 태스크 스케줄 플래닝. 태스크를 분해하고 기존 캘린더에 맞춰 일정 배치 |
| [**yuvalsuede/claudia**](https://github.com/yuvalsuede/claudia) | Claude 에이전트용 AI 네이티브 태스크 관리 시스템. 계층형 태스크, 의존성, 스프린트, 인수 기준, 멀티 에이전트 조율, MCP 서버 통합 |

---

## 📊 모니터링 & 옵저버빌리티

> Sentry, Datadog, Grafana 등 시스템 모니터링 및 로깅

| 서버 | 설명 |
|------|------|
| [**Agent Mindshare**](https://agentmindshare.com) | 플랫폼 전반의 AI 에이전트 마인드셰어를 추적·모니터링 — AI 대화에서의 브랜드 가시성 측정 |
| [**AgentOps**](https://github.com/AgentOps-AI/agentops-mcp) | AgentOps API를 활용한 AI 에이전트 디버깅용 옵저버빌리티 및 트레이싱 제공 |
| [**AI Agent Marketplace Index**](https://github.com/AI-Agent-Hub/ai-agent-marketplace-index-mcp) | AI Agent Marketplace Index에서 5,000개 이상 AI 에이전트와 도구를 검색하고 AI 에이전트 트래픽 모니터링 |
| [**Alog/alog-mcp**](https://github.com/saikiyusuke/alog-mcp) | AI 에이전트 활동 로거 & 모니터 MCP 서버. 20개 도구로 로그 게시, 아티클 작성, 소셜 상호작용 관리, Alog 플랫폼에서 AI 에이전트 활동 모니터링 |
| [**alpadalar/netops-mcp**](https://github.com/alpadalar/netops-mcp) | 종합 DevOps 및 네트워킹 MCP 서버. 네트워크 모니터링, 시스템 진단, 자동화 워크플로우, 인프라 관리와 AI 기반 운영 인사이트 제공 |
| [**Arize Phoenix**](https://github.com/Arize-ai/phoenix/tree/main/js/packages/phoenix-mcp) | 오픈소스 AI/LLM 옵저버빌리티 도구 Arize Phoenix로 트레이스 검사, 프롬프트 관리, 데이터셋 큐레이션, 실험 실행 |
| [**avivsinai/langfuse-mcp**](https://github.com/avivsinai/langfuse-mcp) | Langfuse 트레이스 쿼리, 예외 디버깅, 세션 분석, 프롬프트 관리. LLM 애플리케이션용 완전한 옵저버빌리티 툴킷 |
| [**Axiom**](https://github.com/axiomhq/mcp-server-axiom) | 자연어로 Axiom 로그, 트레이스 및 모든 이벤트 데이터를 쿼리·분석 |
| [**ClearML MCP**](https://github.com/prassanna-ravishankar/clearml-mcp) | AI 대화에서 ClearML의 ML 실험 컨텍스트와 분석을 직접 가져와 활용 |
| [**conarti/mattermost-mcp**](https://github.com/conarti/mattermost-mcp) | Mattermost API용 MCP 서버. 채널 목록, 메시지 읽기/게시, 스레드·리액션 관리, 토픽 모니터링. CLI 인자, 환경 변수, 설정 파일로 유연한 구성 |
| [**Console Automation**](https://github.com/ooples/mcp-console-automation) | AI 기반 콘솔 자동화 및 모니터링용 프로덕션 레디 MCP 서버. 세션 관리, SSH, 테스팅, 모니터링, 백그라운드 작업 등 40개 도구 제공 |
| [**CrowdStrike Falcon**](https://github.com/CrowdStrike/falcon-mcp) | AI 에이전트를 CrowdStrike Falcon 플랫폼에 연결하여 탐지, 인시던트, 위협 인텔리전스, 호스트, 취약점 등에 프로그래밍 방식으로 접근 |
| [**Dash0**](https://github.com/dash0hq/mcp-dash0) | Dash0에서 OpenTelemetry 리소스 탐색, 인시던트 조사, 메트릭·로그·트레이스 쿼리 |
| [**Datadog**](https://github.com/GeLi2001/datadog-mcp-server) | 공식 Datadog API 기반 애플리케이션 트레이싱, 모니터링, 대시보드, 인시던트 쿼리용 MCP 서버 |
| [**Debugg.AI**](https://github.com/debugg-ai/debugg-ai-mcp) | Debugg.AI 원격 브라우저 테스트 에이전트를 통한 제로 설정, AI 완전 관리형 End-to-End 테스팅 |
| [**Deebo**](https://github.com/snagasuri/deebo-prototype) | AI 코딩 에이전트가 격리된 멀티 에이전트 가설 테스트를 통해 어려운 버그를 위임·수정하는 에이전틱 디버깅 MCP 서버 |
| [**DevCycle**](https://docs.devcycle.com/cli-mcp/mcp-getting-started) | AI 코딩 어시스턴트에서 자연어로 Feature Flag 생성 및 모니터링 |
| [**Diffusion**](https://github.com/diffusiondata/diffusion-mcp-server) | Diffusion 서버에 연결하여 토픽 탐색, 토픽 생성/업데이트, 세션 관리, 토픽 뷰·메트릭 등 기능 설정 및 서버 모니터링 |
| [**Downdetector**](https://github.com/domdomegg/downdetector-mcp) | Downdetector에서 서비스 상태 및 장애 정보를 확인하여 다양한 플랫폼과 지역의 서비스 가용성을 실시간 모니터링 |
| [**Dynatrace**](https://github.com/dynatrace-oss/dynatrace-mcp) | Dynatrace 플랫폼과 연동하여 실시간 옵저버빌리티 및 모니터링 관리 |
| [**fastn.ai – Unified API MCP Server**](https://github.com/fastnai/mcp-fastn) | 1,000개 이상 도구, 액션, 워크플로우에 연결되는 통합 API 원격 동적 MCP 서버. 빌트인 인증 및 모니터링 포함 |
| [**Fleet**](https://github.com/SimplyMinimal/fleet-mcp) | 디바이스 관리, 보안 모니터링, 컴플라이언스 적용을 위한 완전한 Fleet 연동. 호스트 관리, 라이브 쿼리, 정책 관리, 소프트웨어 인벤토리, 취약점 추적 지원 |
| [**gbrigandi/mcp-server-thehive**](https://github.com/gbrigandi/mcp-server-thehive) | Rust 기반 TheHive 연동 MCP 서버. AI를 통한 협업 보안 인시던트 대응 및 케이스 관리 지원 |
| [**GDB**](https://github.com/pansila/mcp_server_gdb) | MCP 프로토콜 기반 GDB/MI 프로토콜 서버. AI 어시스턴트를 통한 원격 애플리케이션 디버깅 기능 제공 |
| [**girste/mcp-cybersec-watchdog**](https://github.com/girste/mcp-cybersec-watchdog) | 89개 CIS Benchmark 통제, NIST 800-53, PCI-DSS 컴플라이언스 점검을 포함한 종합 Linux 서버 보안 감사. 방화벽, SSH, Docker, CVE, SSL/TLS 등 23개 분석기의 실시간 모니터링 및 이상 탐지 |
| [**Godot**](https://github.com/Coding-Solo/godot-mcp) | Godot 엔진 종합 연동 MCP 서버. 프로젝트 편집, 디버깅, 씬 관리 지원 |
| [**Grafana**](https://github.com/grafana/mcp-grafana) | Grafana 인스턴스에서 대시보드 검색, 인시던트 조사, 데이터소스 쿼리 |
| [**Graylog**](https://github.com/Pranavj17/mcp-server-graylog) | 절대/상대 타임스탬프로 Graylog 로그 검색, 스트림별 필터링, Claude Desktop에서 직접 프로덕션 이슈 디버깅 |
| [**hechtcarmel/jetbrains-debugger-mcp-plugin**](https://github.com/hechtcarmel/jetbrains-debugger-mcp-plugin) | JetBrains IDE 플러그인으로 MCP 서버를 노출하여 AI 코딩 어시스턴트가 디버거를 완전히 프로그래밍 방식으로 제어 |
| [**hiroata/meltbook-mcp-server**](https://github.com/hiroata/meltbook) | AI 에이전트 정치 토론 게시판 meltbook용 MCP 서버. 50개 AI 에이전트가 자율적으로 일본 정치에 대해 게시, 투표, 토론. 스레드 생성, 게시, 투표, 모니터링용 11개 도구 |
| [**hyperb1iss/droidmind**](https://github.com/hyperb1iss/droidmind) | MCP를 통해 AI로 Android 디바이스 제어. 디바이스 제어, 디버깅, 시스템 분석, UI 자동화와 종합 보안 프레임워크 제공 |
| [**imprvhub/mcp-status-observer**](https://github.com/imprvhub/mcp-status-observer) | Claude Desktop에서 주요 디지털 플랫폼의 운영 상태를 모니터링하는 MCP 서버 |
| [**inkbytefo/screenmonitormcp**](https://github.com/inkbytefo/screenmonitormcp) | 실시간 화면 분석, 컨텍스트 인식 녹화, UI 모니터링 MCP 서버. AI 비전, 이벤트 훅, 멀티모달 에이전트 워크플로우 지원 |
| [**itemit MCP**](https://github.com/umin-ai/itemit-mcp) | 300개 이상 조직이 사용하는 자산 추적 MCP. 인벤토리 관리, 모니터링, 위치 추적 제공 |
| [**iTerm MCP**](https://github.com/ferrislucas/iterm-mcp) | macOS iTerm2 터미널 에뮬레이터 연동으로 LLM이 터미널 명령을 실행하고 모니터링 |
| [**jasonjmcghee/claude-debugs-for-you**](https://github.com/jasonjmcghee/claude-debugs-for-you) | 브레이크포인트와 표현식 평가를 통한 언어 무관 자동 디버깅을 지원하는 MCP 서버 및 VS Code 확장 |
| [**jaspertvdm/mcp-server-tibet**](https://github.com/jaspertvdm/mcp-server-tibet) | AI 결정에 대한 TIBET 출처 추적. 컴플라이언스를 위한 암호학적 감사 추적 및 의도 로깅 제공 |
| [**jtang613/GhidrAssistMCP**](https://github.com/jtang613/GhidrAssistMCP) | Ghidra용 네이티브 MCP 서버. GUI 설정·로깅, 31개 강력한 도구, 외부 의존성 없음 |
| [**Langfuse Prompt Management**](https://github.com/langfuse/mcp-server-langfuse) | 프롬프트의 협업 편집, 버전 관리, 평가, 릴리스를 위한 오픈소스 도구 |
| [**lldb-mcp**](https://github.com/stass/lldb-mcp) | LLM 기반 디버깅을 제공하는 LLDB용 MCP 서버 |
| [**MCP-Ambari-API**](https://github.com/call518/MCP-Ambari-API) | Apache Ambari API 연동 MCP 서버. 서비스 운영, 설정 관리, 상태 모니터링 등 Hadoop 클러스터 관리 도구 제공 |
| [**mcp-n8n**](https://github.com/gomakers-ai/mcp-n8n) | 워크플로우 관리, 실행 모니터링, 크리덴셜, 100개 이상 사전 구축 템플릿 등 41개 도구의 완전한 n8n API 연동. AI 대화로 전체 n8n 자동화 인프라 제어 |
| [**MCP-OpenStack-Ops**](https://github.com/call518/MCP-OpenStack-Ops) | MCP 서버를 통한 전문 OpenStack 운영 자동화. 클러스터 모니터링, 인스턴스 관리, 볼륨 제어, 네트워크 분석을 위한 특화 도구 제공 |
| [**metorial/metorial**](https://github.com/metorial/metorial) | 단일 인터페이스로 AI 에이전트를 600개 이상 통합에 연결 — OAuth, 스케일링, 모니터링 포함 |
| [**Metoro**](https://github.com/metoro-io/metoro-mcp-server) | Metoro로 모니터링되는 Kubernetes 환경을 쿼리하고 상호작용 |
| [**Mux**](https://github.com/muxinc/mux-node-sdk/tree/master/packages/mcp-server) | 개발자용 비디오 API Mux. 공식 MCP로 비디오 업로드, 라이브 스트림 생성, 썸네일 생성, 캡션 추가, 재생 정책 관리, 참여 데이터 분석, 모니터링 |
| [**n8n**](https://github.com/leonardsellem/n8n-mcp-server) | AI 어시스턴트가 n8n 워크플로우와 실행을 관리하는 MCP 서버. 워크플로우 목록 조회, 생성, 업데이트, 삭제 및 실행 모니터링 포함 |
| [**Nango**](https://nango.dev/docs/guides/use-cases/ai-tool-calling) | AI 에이전트를 500개 이상 API와 통합: 인증, 커스텀 도구, 옵저버빌리티. 오픈소스 |
| [**nesquikm/mcp-rubber-duck**](https://github.com/nesquikm/mcp-rubber-duck) | 여러 OpenAI 호환 LLM에 브리지하는 MCP 서버 — 다양한 AI '러버덕'에게 문제를 설명하고 다른 관점의 피드백 수신 |
| [**ooples/token-optimizer-mcp**](https://github.com/ooples/token-optimizer-mcp) | 캐싱, 압축, 80개 이상 스마트 도구로 95% 이상 토큰 절감을 달성하는 지능형 토큰 최적화. API 최적화, 코드 분석, 실시간 모니터링 지원 |
| [**operative_sh/web-eval-agent**](https://github.com/Operative-Sh/web-eval-agent) | browser-use 브라우저 에이전트로 웹 애플리케이션을 자율적으로 디버깅하는 MCP 서버 |
| [**Plugged.in**](https://github.com/VeriTeknik/pluggedin-mcp) | 여러 MCP 서버를 하나로 통합하는 종합 프록시. 서버 간 도구, 프롬프트, 리소스, 템플릿의 검색·관리 및 디버그 플레이그라운드 제공 |
| [**Plugged.in**](https://github.com/VeriTeknik/pluggedin-mcp-proxy) | 여러 MCP 서버를 하나로 통합하는 종합 프록시. 서버 간 도구, 프롬프트, 리소스, 템플릿의 검색·관리 및 디버그 플레이그라운드 제공 |
| [**PostHog**](https://github.com/posthog/mcp) | 공식 PostHog MCP 서버로 PostHog 분석, Feature Flag, 오류 추적 등과 상호작용 |
| [**Pratyay/mac-monitor-mcp**](https://github.com/Pratyay/mac-monitor-mcp) | macOS에서 리소스 집약적 프로세스를 식별하고 성능 개선 제안 제공 |
| [**Prometheus**](https://github.com/pab1it0/prometheus-mcp-server) | 오픈소스 모니터링 시스템 Prometheus 쿼리 및 분석 |
| [**Prometheus (Golang)**](https://github.com/tjhop/prometheus-mcp-server/) | 전체 API 지원으로 Prometheus와 심층 상호작용하는 MCP 서버. Go로 작성된 단일 바이너리 설치 |
| [**Prometheus (TypeScript)**](https://github.com/yanmxa/prometheus-mcp-server) | TypeScript 구현으로 AI 어시스턴트가 자연어로 Prometheus를 쿼리 |
| [**Raygun**](https://github.com/MindscapeHQ/mcp-server-raygun) | Raygun 계정의 크래시 리포팅 및 실사용 모니터링 데이터와 상호작용 |
| [**Rootly-AI-Labs/Rootly-MCP-server**](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) | 인시던트 관리 플랫폼 Rootly용 MCP 서버 |
| [**Salesforce MCP Server**](https://github.com/tsmztech/mcp-server-salesforce) | 종합 Salesforce 연동. 레코드 쿼리, Apex 실행, 필드/오브젝트 관리, 디버그 로그 처리 도구 포함 |
| [**Secureframe**](https://github.com/secureframe/secureframe-mcp-server) | Secureframe에서 SOC 2, ISO 27001, CMMC, FedRAMP 등 프레임워크의 보안 통제 쿼리, 컴플라이언스 테스트 모니터링, 감사 데이터 접근 |
| [**seekrays/mcp-monitor**](https://github.com/seekrays/mcp-monitor) | MCP를 통해 시스템 메트릭을 노출하는 시스템 모니터링 도구. CPU, 메모리, 디스크, 네트워크, 호스트, 프로세스 정보를 LLM이 실시간 조회 |
| [**Sentry**](https://github.com/getsentry/sentry-mcp) | Sentry 공식 MCP 서버 |
| [**Sentry**](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) | 오류 추적 및 성능 모니터링을 위한 Sentry.io 연동 |
| [**spre-sre/lumino-mcp-server**](https://github.com/spre-sre/lumino-mcp-server) | Kubernetes 및 OpenShift용 AI 기반 SRE 옵저버빌리티. Tekton 파이프라인 디버깅, 로그 분석, 근본 원인 분석, 예측적 모니터링 등 40개 이상 도구 제공 |
| [**sslmon**](https://github.com/firesh/sslmon-mcp) | 도메인 등록 정보 및 SSL 인증서 모니터링. 도메인 등록/만료 정보, SSL 인증서 정보 및 유효성 상태 조회 |
| [**SystemSage**](https://github.com/Tarusharma1/SystemSage) | Windows, Linux, macOS를 지원하는 강력한 크로스 플랫폼 시스템 관리 및 모니터링 도구 |
| [**TANTIOPE/datadog-mcp-server**](https://github.com/TANTIOPE/datadog-mcp-server) | AI 어시스턴트용 종합 Datadog 옵저버빌리티 접근 MCP 서버. grep 스타일 로그 검색, APM 트레이스 필터링, 토큰 효율을 위한 스마트 샘플링, 로그·트레이스·메트릭 간 교차 상관 지원 |
| [**testdino-hq/testdino-mcp**](https://github.com/testdino-hq/testdino-mcp) | TestDino 테스트 실행/테스트 케이스 데이터를 AI 에이전트에 연결하여 자연어로 실행 리뷰, 실패 디버깅, 수동 테스트 케이스 관리 |
| [**TheHive MCP Server**](https://github.com/redwaysecurity/the-hive-mcp-server) | 보안 인시던트 대응 플랫폼 TheHive용 MCP 서버 |
| [**Tideways**](https://github.com/abuhamza/tideways-mcp-server) | AI 어시스턴트가 Tideways 성능 모니터링 데이터를 쿼리하여 PHP 애플리케이션의 대화형 성능 인사이트 제공 |
| [**TMD Earthquake**](https://github.com/amornpan/tmd-earthquake-server-1.0) | 태국 기상청의 실시간 지진 모니터링. 규모 필터링, 위치 기반 검색(태국어/영어), 위험 지진 알림 등 지원 |
| [**tumf/grafana-loki-mcp**](https://github.com/tumf/grafana-loki-mcp) | Grafana API를 통해 Loki 로그를 쿼리하는 MCP 서버 |
| [**txn2/kubefwd**](https://github.com/txn2/kubefwd) | Kubernetes 대량 포트 포워딩. 서비스 디스커버리, /etc/hosts 관리, 트래픽 모니터링, Pod 로그 스트리밍 제공 |
| [**Unity Engine**](https://github.com/codemaestroai/advanced-unity-mcp) | Code Maestro의 고급 Unity MCP. 자연어로 MCP를 통해 빌드, 디버그, 프로파일링, 에셋·씬·스크립트 관리 |
| [**utapyngo/sentry-mcp-rs**](https://github.com/utapyngo/sentry-mcp-rs) | Rust로 작성된 빠르고 경량의 Sentry MCP 서버 |
| [**weibaohui/k8m**](https://github.com/weibaohui/k8m) | MCP 멀티 클러스터 Kubernetes 관리 및 운영. 관리 인터페이스, 로깅, 일반적인 DevOps/개발 시나리오를 커버하는 약 50개 빌트인 도구. 표준 및 CRD 리소스 지원 |

---

## 📈 마케팅 & CRM

> Salesforce, HubSpot 등 CRM/마케팅/HR 플랫폼 연동

| 서버 | 설명 |
|------|------|
| [**Ads MCP**](https://github.com/amekala/ads-mcp) | 크로스 플랫폼 광고 캠페인 생성(Google Ads Search & PMax, TikTok)용 원격 MCP 서버. OAuth 2.1 인증 및 장기 실행 작업용 프로그레스 스트리밍 지원 |
| [**Amplitude**](https://amplitude.com/docs/analytics/amplitude-mcp) | Amplitude MCP 서버로 AI 어시스턴트와 제품 데이터를 연결. 차트, 대시보드, 실험, Feature Flag, 메트릭 검색·분석·쿼리 |
| [**Audiense Insights**](https://github.com/AudienseCo/mcp-audiense-insights) | Audiense 리포트 기반 마케팅 인사이트 및 오디언스 분석. 인구통계, 문화, 인플루언서, 콘텐츠 참여 분석 포함 |
| [**avisangle/method-crm-mcp**](https://github.com/avisangle/method-crm-mcp) | Method CRM API 연동 프로덕션 레디 MCP 서버. 테이블, 파일, 사용자, 이벤트, API 키 관리용 20개 종합 도구. 속도 제한, 재시도 로직, 듀얼 트랜스포트(stdio/HTTP) 지원 |
| [**BambooHR MCP**](https://github.com/encoreshao/bamboohr-mcp) | BambooHR API 연동 MCP 서버. 직원 데이터, 근태 관리, HR 관리 기능 접근 제공 |
| [**bluzername/lennys-quotes**](https://github.com/bluzername/lennys-quotes) | Lenny's Podcast 269개 에피소드에서 제품 관리 지혜를 검색. 51,000개 이상 트랜스크립트 세그먼트를 YouTube 타임스탬프와 함께 검색. PRD, 전략, PM 커리어 조언에 활용 |
| [**CallHub**](https://github.com/callhub/callhub-mcp) | Python 기반 MCP 도구. CallHub의 연락처, 전화번호부, 에이전트, 팀, 캠페인 및 기타 리소스를 관리하는 종합 기능 세트 제공 |
| [**CB Insights**](https://github.com/cbinsights/cbi-mcp-server) | CB Insights MCP 서버로 ChatCBI에 연결 |
| [**Customer.io**](https://docs.customer.io/ai/mcp-server/) | LLM이 Customer.io 워크스페이스와 직접 작업. 세그먼트 생성, 사용자 프로필 검사, 고객 검색, 워크스페이스 데이터 접근, 고객 속성 분석, 오디언스 타겟팅 관리 |
| [**Explorium**](https://github.com/explorium-ai/mcp-explorium) | AI SDR 및 GTM 에이전트를 위한 Explorium B2B 데이터 및 인프라 |
| [**fetchSERP**](https://github.com/fetchSERP/fetchserp-mcp-server-node) | fetchSERP 올인원 SEO 및 웹 인텔리전스 툴킷 API |
| [**Google Analytics**](https://github.com/surendranb/google-analytics-mcp) | LLM 분석을 위해 200개 이상 차원 및 메트릭의 데이터를 가져오는 Google Analytics MCP 서버 |
| [**Google Analytics 4**](https://github.com/gomakers-ai/mcp-google-analytics) | 리포트 조회 및 이벤트 전송을 위한 Google Analytics Data API 및 Measurement Protocol MCP 서버 |
| [**hmk/attio-mcp-server**](https://github.com/hmk/attio-mcp-server) | AI 클라이언트가 Attio CRM에서 레코드와 노트를 관리 |
| [**HubSpot**](https://developer.hubspot.com/mcp) | HubSpot CRM 데이터 연결, 관리, 상호작용 |
| [**HubSpot**](https://github.com/buryhuang/mcp-hubspot) | HubSpot CRM 연동으로 연락처 및 회사 관리. Claude 채팅에서 직접 CRM 데이터 생성 및 조회 |
| [**Keywords Everywhere**](https://api.keywordseverywhere.com/docs/#/mcp_integration) | 공식 Keywords Everywhere API MCP 서버를 통한 SEO 데이터 접근 |
| [**Klaviyo**](https://developers.klaviyo.com/en/docs/klaviyo_mcp_server) | Klaviyo 마케팅 데이터와 상호작용 |
| [**Mailjet**](https://github.com/mailgun/mailjet-mcp-server) | AI 에이전트가 Sinch Mailjet의 연락처, 캠페인, 세그먼테이션, 통계, 워크플로우 등 API와 상호작용하는 공식 MCP 서버 |
| [**MatiousCorp/google-ad-manager-mcp**](https://github.com/MatiousCorp/google-ad-manager-mcp) | Google Ad Manager API 연동. 캠페인, 주문, 라인 아이템, 크리에이티브, 광고주 관리와 대량 업로드 지원 |
| [**mcp-salesforce**](https://github.com/lciesielski/mcp-salesforce-example) | Salesforce 인스턴스와의 기본적인 상호작용을 시연하는 MCP 서버 |
| [**Mixpanel**](https://docs.mixpanel.com/docs/features/mcp) | 자연어로 제품 분석 데이터 쿼리·분석. Mixpanel MCP로 AI 어시스턴트가 워크스페이스에 연결되어 사용자 행동 인사이트, 퍼널 등에 대화형 접근 |
| [**MonadsAG/capsulecrm-mcp**](https://github.com/MonadsAG/capsulecrm-mcp) | AI 클라이언트가 Capsule CRM에서 연락처, 기회, 태스크를 관리. Claude Desktop 전용 DTX 파일 포함 |
| [**nicolascroce/keepsake-mcp**](https://github.com/nicolascroce/keepsake-mcp) | 개인용 CRM — 42개 MCP 도구로 연락처, 상호작용, 태스크, 노트, 일일 저널, 태그 관리 |
| [**Open Strategy Partners Marketing Tools**](https://github.com/open-strategy-partners/osp_marketing_tools) | 제품 마케팅을 위한 콘텐츠 편집 코드, 가치 맵, 포지셔닝 도구 |
| [**Salesforce MCP**](https://github.com/smn2gnt/MCP-Salesforce) | Salesforce 데이터 및 메타데이터와 상호작용 |
| [**Semilattice**](https://github.com/semilattice-research/mcp) | 정확한 오디언스 예측으로 콘텐츠 테스트, 기능 개인화, A/B 테스트 의사결정 |
| [**SEO MCP**](https://github.com/cnych/seo-mcp) | Ahrefs 데이터 기반 무료 SEO 도구 MCP 서비스. 백링크, 키워드 아이디어 등 기능 포함 |
| [**TalentoHQ**](https://hr.talentohq.com/mcp) | MCP를 통해 TalentoHQ HR 소프트웨어에 연결. AI 퍼스트 HR 소프트웨어로 조직을 혁신 |
| [**tianqitang1/enrichr-mcp-server**](https://github.com/tianqitang1/enrichr-mcp-server) | Enrichr API를 활용한 유전자 세트 강화 분석을 제공하는 MCP 서버 |

---

## 🔒 보안

> Auth0, Snyk 등 인증/인가, 취약점 스캔, 시크릿 관리

| 서버 | 설명 |
|------|------|
| [**20alexl/mini_claude**](https://github.com/20alexl/mini_claude) | Claude Code용 영속적 메모리 및 가드레일. 실수 추적, 루프 감지, 스코프 가드, 위험한 편집을 차단하는 Hooks 제공. Ollama로 로컬 실행 |
| [**Archestra.AI**](https://github.com/archestra-ai/archestra) | 오픈소스 엔터프라이즈급 MCP 게이트웨이, 레지스트리, 오케스트레이터, 크리덴셜 관리, LLM 비용 관리 및 채팅 플랫폼 |
| [**Asgardeo**](https://github.com/asgardeo/asgardeo-mcp-server) | LLM 도구를 통해 Asgardeo 조직과 상호작용하는 MCP 서버 |
| [**Auth0**](https://github.com/auth0/auth0-mcp-server) | Auth0 테넌트와 상호작용하는 MCP 서버. 액션, 애플리케이션, 폼, 로그, 리소스 서버 등의 생성 및 수정 지원 |
| [**Authenticator App · 2FA**](https://github.com/firstorderai/authenticator_mcp) | AI 에이전트가 Authenticator App과 상호작용할 수 있는 보안 MCP 서버 |
| [**behrensd/mcp-firewall**](https://github.com/behrensd/mcp-firewall) | MCP용 iptables 같은 결정론적 보안 프록시. 도구 호출 인터셉트, YAML 정책 적용, 시크릿 유출 스캔, 전체 로깅. AI 없음, 클라우드 없음 |
| [**BoostSecurity**](https://github.com/boost-community/boost-mcp) | BoostSecurity 기반 MCP 가드레일로 코딩 에이전트가 취약점, 멀웨어, 타이포스쿼팅이 있는 의존성 도입을 방지 |
| [**Burp Suite**](https://github.com/PortSwigger/mcp-server) | AI 클라이언트가 Burp Suite에 연결할 수 있는 MCP 서버 확장 |
| [**BurtTheCoder/mcp-shodan**](https://github.com/BurtTheCoder/mcp-shodan) | Shodan API 및 Shodan CVEDB 쿼리 MCP 서버. IP 조회, 디바이스 검색, DNS 조회, 취약점 쿼리, CPE 조회 등 도구 제공 |
| [**Cheqd**](https://github.com/cheqd/mcp-toolkit) | cheqd의 Trust Registry와 Credentials를 통해 AI 에이전트의 신뢰·검증, 사기 방지, 평판 보호 등 지원 |
| [**conan-io/conan-mcp**](https://github.com/conan-io/conan-mcp) | Conan C/C++ 패키지 매니저 공식 MCP 서버. 프로젝트 생성, 의존성 관리, 라이선스 확인, 보안 취약점 스캔 |
| [**Construe**](https://github.com/mattjoyce/mcp-construe) | Obsidian 볼트의 지능형 컨텍스트 관리 FastMCP 서버. Frontmatter 필터링, 자동 청킹, 안전한 양방향 지식 작업 제공 |
| [**Contrast Security**](https://github.com/Contrast-Security-OSS/mcp-contrast) | Contrast의 취약점 및 SCA 데이터를 코딩 에이전트에 가져와 취약점을 빠르게 수정 |
| [**CTERA Edge Filer**](https://github.com/ctera/mcp-ctera-edge) | CTERA Edge Filer로 지능형 엣지 캐싱 및 멀티 프로토콜 파일 접근 제공. 코어 및 원격 사이트 전반에서 빠르고 안전한 파일 접근 |
| [**Cycode**](https://github.com/cycodehq/cycode-cli#mcp-command-experiment) | Cycode로 SAST, SCA, Secrets, IaC 스캐닝을 통해 개발 라이프사이클 보안 강화 |
| [**Descope**](https://github.com/descope-sample-apps/descope-mcp-server) | Descope 연동 MCP 서버. 감사 로그 검색, 사용자 관리 등 지원 |
| [**dkvdm/onepassword-mcp-server**](https://github.com/dkvdm/onepassword-mcp-server) | 에이전트 AI가 사용할 수 있도록 1Password에서 안전하게 크리덴셜을 조회하는 MCP 서버 |
| [**Elastic Email**](https://github.com/ElasticEmail/elasticemail-mcp-server) | 차세대 AI 에이전트 및 MCP 호환 환경에 완전한 이메일 기능을 제공하는 Elastic Email MCP 서버 |
| [**Endor Labs**](https://docs.endorlabs.com/deployment/ide/mcp/) | 코드의 보안 위험 발견 및 수정. Endor Labs 연동으로 취약점 및 시크릿 유출로부터 코드 스캔·보호 |
| [**Fluid Attacks**](https://github.com/fluidattacks/mcp) | Fluid Attacks API와 상호작용하여 취약점 관리, 조직 인사이트, GraphQL 쿼리 실행 |
| [**forest6511/secretctl**](https://github.com/forest6511/secretctl) | MCP 통합 AI 안전 시크릿 매니저. 크리덴셜을 환경 변수로 주입하여 명령 실행 — AI 에이전트는 평문 시크릿을 볼 수 없음. 출력 새니타이징, AES-256-GCM 암호화, Argon2id 키 유도 |
| [**FPE Demo MCP**](https://github.com/Horizon-Digital-Engineering/fpe-demo-mcp) | LLM 워크플로우에서 안전한 데이터 보호를 위한 FF3 형식 보존 암호화 및 인증 패턴 |
| [**Gaffx/volatility-mcp**](https://github.com/Gaffx/volatility-mcp) | Volatility 3.x용 MCP 서버. AI 어시스턴트로 메모리 포렌식 분석 수행. pslist, netscan 등 플러그인을 REST API와 LLM을 통해 접근 |
| [**GenWaveLLC/svgmaker-mcp**](https://github.com/GenWaveLLC/svgmaker-mcp) | 자연어를 통한 AI 기반 SVG 생성 및 편집. 실시간 업데이트와 안전한 파일 처리 제공 |
| [**GitGuardian**](https://github.com/GitGuardian/gg-mcp) | GitGuardian 공식 MCP 서버 — 500개 이상 시크릿 탐지기를 갖춘 업계 최고 API로 프로젝트를 스캔하여 퍼블릭 리포지토리 유출 전 크리덴셜 누출 방지 |
| [**irulescan MCP**](https://github.com/simonkowallik/irulescan?tab=readme-ov-file#mcp-server) | F5 iRules용 MCP 지원 코드 보안 분석기 |
| [**Jktfe/serveMyAPI**](https://github.com/Jktfe/serveMyAPI) | macOS Keychain을 활용하여 프로젝트 간 API 키를 안전하게 저장·접근하는 개인용 MCP 서버 |
| [**juspay/neurolink**](https://github.com/juspay/neurolink) | 엔터프라이즈 AI 인프라를 범용적으로 접근 가능하게. 12개 프로바이더·100개 이상 모델을 통합하는 엣지 퍼스트 플랫폼. 멀티 에이전트 오케스트레이션, HITL 워크플로우, 가드레일 미들웨어, 컨텍스트 요약 제공 |
| [**Keycloak**](https://github.com/idoyudha/mcp-keycloak) | 에이전트 애플리케이션이 Keycloak 데이터를 효율적으로 관리·검색할 수 있도록 설계된 MCP 서버 |
| [**Keycloak MCP**](https://github.com/ChristophEnglisch/keycloak-model-context-protocol) | 자연어로 Keycloak과 상호작용하는 MCP 서버. 사용자 및 Realm 생성, 삭제, 목록 조회 등 지원 |
| [**Keycloak MCP Server**](https://github.com/sshaaf/keycloak-mcp-server) | Keycloak ID 및 접근 관리 연동. Users, Realms, Clients, Roles, Groups, IDP, Authentication 등 40개 이상 도구. 네이티브 빌드 지원 |
| [**kluster.ai**](https://docs.kluster.ai/get-started/mcp/overview/) | 개발 워크플로우에 AI 서비스를 직접 제공하는 MCP 서버. 환각 탐지 등 가드레일 포함 |
| [**Lspace**](https://github.com/Lspace-io/lspace-server) | 흩어진 ChatGPT/Claude/Cursor 대화를 영속적이고 검색 가능한 지식으로 변환 |
| [**MCP-CLI Adapter**](https://github.com/inercia/mcp-cli-adapter) | 명령줄 도구를 MCP 도구로 안전하게 사용 |
| [**MCPShell**](https://github.com/inercia/mcpshell) | LLM이 명령줄 도구를 안전하게 실행할 수 있는 도구. LLM과 OS 명령 간의 보안 브리지 제공 |
| [**MladenSU/cli-mcp-server**](https://github.com/MladenSU/cli-mcp-server) | 안전한 실행과 커스터마이즈 가능한 보안 정책을 갖춘 명령줄 인터페이스 |
| [**Mobb**](https://github.com/mobb-dev/bugsy?tab=readme-ov-file#model-context-protocol-mcp-server) | Mobb Vibe Shield MCP 서버로 사람 및 AI가 작성한 코드의 취약점을 식별·수정하여 개발 속도를 유지하면서 애플리케이션 보안 보장 |
| [**Momento**](https://github.com/momentohq/mcp-momento) | Momento Cache로 성능을 빠르게 개선하고 비용을 절감하며 어떤 규모에서도 부하를 처리 |
| [**mxcp**](http://github.com/raw-labs/mxcp) | dbt + DuckDB 기반으로 SQL 또는 Python에서 안전하고 테스트 가능한 엔터프라이즈급 MCP 도구를 빌드하는 오픈소스 프레임워크 |
| [**NPM Plus**](https://github.com/shacharsol/js-package-manager-mcp) | 보안 스캐닝, 번들 분석, 지능형 의존성 관리를 갖춘 AI 기반 JavaScript 패키지 관리. MCP 호환 에디터용 |
| [**Okta**](https://github.com/kapilduraphe/okta-mcp-server) | Okta API와 상호작용 |
| [**OpenZeppelin/contracts-wizard**](https://github.com/OpenZeppelin/contracts-wizard/tree/master/packages/mcp) | AI 에이전트가 OpenZeppelin Wizard 템플릿 기반으로 다양한 언어의 안전한 스마트 컨트랙트를 생성하는 MCP 서버 |
| [**PAIML MCP Agent Toolkit**](https://github.com/paiml/paiml-mcp-agent-toolkit) | 제로 설정 AI 컨텍스트 생성, Rust/Deno/Python 프로젝트 템플릿 생성, 하이브리드 뉴로 심볼릭 코드 분석을 포함한 전문 프로젝트 스캐폴딩 툴킷 |
| [**PinMeTo**](https://github.com/PinMeTo/pinmeto-location-mcp) | 인증된 사용자가 위치 데이터를 잠금 해제할 수 있는 MCP 서버 |
| [**Recraft**](https://github.com/recraft-ai/mcp-recraft-server) | Recraft로 래스터 및 벡터(SVG) 이미지 생성. 이미지 편집, 업스케일, 스타일 생성, 래스터 이미지 벡터화 지원 |
| [**Scaffold**](https://github.com/Beer-Bears/scaffold) | 대규모 코드베이스의 구조적 이해를 위한 RAG 시스템. 소스 코드를 살아있는 지식 그래프로 변환하여 정밀하고 컨텍스트 인식 검색 지원 |
| [**scan-mcp**](https://github.com/jacksenechal/scan-mcp) | 스캐너 캡처(ADF/양면/페이지 크기)를 위한 경량 MCP 서버. 타입 지정 도구, JSON Schema 검증 I/O, 다중 페이지 조립 지원 |
| [**Scanova MCP Server**](https://github.com/trycon/scanova-mcp) | Scanova API를 활용한 QR 코드 생성·관리·다운로드 도구를 제공하는 MCP 서버 |
| [**Secure Fetch**](https://github.com/appsec-innovation-labs/secure-mcp-fetch) | 로컬 리소스 접근을 방지하는 보안 fetch |
| [**Semgrep**](https://github.com/semgrep/semgrep/blob/develop/cli/src/semgrep/mcp/README.md) | AI 에이전트가 Semgrep으로 코드를 보안 검사 |
| [**Semgrep**](https://github.com/semgrep/mcp) | AI 에이전트가 Semgrep으로 코드를 보안 검사 |
| [**Shell**](https://github.com/sonirico/mcp-shell) | AI에게 손을 제공. 셸 명령을 안전하고, 감사 가능하며, 필요 시 실행하는 MCP 서버 |
| [**Snyk**](https://github.com/snyk/snyk-ls/blob/main/mcp_extension/README.md) | Snyk 취약점 스캐닝을 에이전트 워크플로우에 직접 내장하여 보안 태세 강화 |
| [**stefan-xyz/mcp-server-runescape**](https://github.com/stefan-xyz/mcp-server-runescape) | RuneScape(RS) 및 Old School RuneScape(OSRS) 데이터(아이템 가격, 플레이어 순위 등)와 상호작용하는 도구를 제공하는 MCP 서버 |
| [**Thales CipherTrust Manager MCP Server**](https://github.com/sanyambassi/ciphertrust-manager-mcp-server) | Thales CipherTrust Manager 연동 MCP 서버. 안전한 키 관리 및 암호화 작업 지원 |
| [**TheLunarCompany/lunar#mcpx**](https://github.com/TheLunarCompany/lunar/tree/main/mcpx) | 대규모 MCP 서버 관리를 위한 프로덕션 레디 오픈소스 게이트웨이. 도구 디스커버리, 접근 제어, 호출 우선순위, 사용량 추적을 중앙 집중화하여 에이전트 워크플로우 간소화 |
| [**tigranbs/mcgravity**](https://github.com/tigranbs/mcgravity) | 여러 MCP 서버를 하나의 통합 엔드포인트로 구성하는 프록시 도구. Nginx처럼 여러 MCP 서버 간 요청 로드 밸런싱으로 AI 도구 스케일링 |
| [**TopazLabs/topaz-mcp**](https://github.com/TopazLabs/topaz-mcp) | Topaz Labs API를 통한 AI 이미지 향상(업스케일링, 디노이징, 샤프닝). Standard V2, Wonder 2, Bloom, Recover 3 등 8개 모델 지원 |
| [**tufantunc/ssh-mcp**](https://github.com/tufantunc/ssh-mcp) | MCP를 통해 Linux 및 Windows 서버의 SSH 제어를 노출하는 MCP 서버. 비밀번호 또는 SSH 키 인증으로 원격 셸 명령을 안전하게 실행 |
| [**tumf/mcp-shell-server**](https://github.com/tumf/mcp-shell-server) | MCP를 구현한 안전한 셸 명령 실행 서버 |
| [**ukkit/memcord**](https://github.com/ukkit/memcord) | 채팅 기록을 정리하고 검색 가능하게 유지하는 MCP 서버 — AI 기반 요약, 보안 메모리, 완전한 제어 |
| [**Useless Toolkit**](https://uselesstoolkit.com/apis/mcp-servers) | Password Generator, IP2Geo 등 유틸리티 API용 MCP 지원 서버 엔드포인트. RapidAPI를 통한 안전한 AI 에이전트 연동 |
| **Vulert** | 코드 접근 없이 오픈소스 의존성의 취약점을 탐지하여 소프트웨어 보안. JS, PHP, Java, Python 등 지원 |
| [**Windows CLI**](https://github.com/SimonB97/win-cli-mcp-server) | Windows 시스템에서 안전한 명령줄 상호작용을 위한 MCP 서버. PowerShell, CMD, Git Bash 셸에 대한 제어된 접근 제공 |
| [**wowinter13/solscan-mcp**](https://github.com/wowinter13/solscan-mcp) | Solscan API를 활용하여 자연어로 Solana 트랜잭션을 쿼리하는 MCP 도구 |
| [**XcodeBuildMCP**](https://github.com/cameroncooke/xcodebuildmcp) | AI 에이전트가 iOS, macOS, visionOS, watchOS 앱을 스캐폴딩·빌드·실행·테스트할 수 있는 인기 MCP 서버. 시뮬레이터, 유/무선 디바이스, 강력한 UI 자동화 지원 |

---

## 🧪 테스팅 & QA

> Appium, Cypress 등 테스트 자동화 및 QA 도구

| 서버 | 설명 |
|------|------|
| [**a-25/ios-mcp-code-quality-server**](https://github.com/a-25/ios-mcp-code-quality-server) | iOS 코드 품질 분석 및 테스트 자동화 서버. Xcode 테스트 실행, SwiftLint 통합, 상세 실패 분석을 CLI 및 MCP 서버 모드로 제공한다. |
| [**Appium MCP Server**](https://github.com/appium/appium-mcp.git) | 모바일 개발 및 자동화를 위한 MCP 서버. iOS, Android Simulator/Emulator 및 실제 디바이스를 지원한다. |
| [**BugBug MCP Server**](https://github.com/simplypixi/bugbug-mcp-server) | BugBug API용 비공식 MCP 서버. |
| [**linuxsuren/atest-mcp-server**](https://github.com/LinuxSuRen/atest-mcp-server) | 테스트 스위트와 케이스를 관리하는 MCP 서버. Postman의 대안으로 사용할 수 있다. |
| [**Lippia**](https://github.com/Lippia-io/Lippia-MCP-Server/blob/main/getting-started.md) | Lippia Framework를 활용하여 테스트 자동화를 가속화하는 MCP 서버. |
| [**mumez/pharo-smalltalk-interop-mcp-server**](https://github.com/mumez/pharo-smalltalk-interop-mcp-server) | Pharo Smalltalk 통합 서버. 코드 실행, 클래스/메서드 인트로스펙션, 패키지 관리, 테스트 실행 및 프로젝트 설치를 지원한다. |
| [**QA Sphere**](https://github.com/Hypersequent/qasphere-mcp) | QA Sphere 테스트 관리 시스템과 통합하여 LLM이 AI 기반 IDE에서 테스트 케이스를 검색, 요약, 상호작용할 수 있게 한다. |
| [**securityfortech/secops-mcp**](https://github.com/securityfortech/secops-mcp) | 오픈소스 보안 도구를 하나의 MCP 인터페이스로 통합한 올인원 보안 테스팅 도구. 펜테스팅, 버그 바운티, 위협 헌팅 등을 AI 에이전트와 연동하여 수행한다. |

---

## 📉 데이터 분석 & BI

> Databricks, dbt 등 데이터 파이프라인 및 분석 도구

| 서버 | 설명 |
|------|------|
| [**8b-is/smart-tree**](https://github.com/8b-is/smart-tree) | 시맨틱 분석 기반의 AI 네이티브 디렉토리 시각화 도구. AI 소비용 초압축 포맷으로 토큰을 10배 절감하며 지능형 파일 분류를 지원한다. |
| [**abrinsmead/mindpilot-mcp**](https://github.com/abrinsmead/mindpilot-mcp) | 코드, 아키텍처 및 기타 개념을 로컬 웹 앱에서 Mermaid 다이어그램으로 시각화한다. |
| [**agentic-mcp-tools/memora**](https://github.com/agentic-mcp-tools/memora) | Knowledge Graph 시각화, 시맨틱/하이브리드 검색, 클라우드 동기화(S3/R2), 크로스 세션 컨텍스트 관리를 제공하는 영속 메모리 서버. |
| [**AntV Chart**](https://github.com/antvis/mcp-server-chart) | AntV를 사용하여 15가지 이상의 시각화 차트를 생성하는 MCP 서버. |
| [**asmith26/jupytercad-mcp**](https://github.com/asmith26/jupytercad-mcp) | JupyterCAD를 LLM/자연어로 제어할 수 있게 하는 MCP 서버. |
| [**AutoML**](https://github.com/emircansoftware/MCP_Server_DataScience) | 데이터 읽기, 전처리, 피처 엔지니어링, 모델 선택, 시각화, 하이퍼파라미터 튜닝 등 데이터 분석 워크플로우를 위한 MCP 서버. |
| [**Baidu Map**](https://github.com/baidu-maps/mcp) | AI 에이전트가 Baidu Maps API와 상호작용하여 위치 기반 서비스 및 지리공간 데이터 분석을 수행할 수 있게 하는 MCP 서버. |
| [**Bauplan**](https://github.com/BauplanLabs/bauplan-mcp-server) | Bauplan Lakehouse를 관리한다. 테이블 조회, 데이터 브랜치 생성, 파이프라인 실행, 로그 조회를 지원한다. |
| [**cafferychen777/ChatSpatial**](https://github.com/cafferychen777/ChatSpatial) | 공간 전사체학(Spatial Transcriptomics) 분석용 MCP 서버. 세포 주석, 디컨볼루션, 공간 통계, 시각화 등 60개 이상의 통합 분석 메서드를 제공한다. |
| [**cantian-ai/bazi-mcp**](https://github.com/cantian-ai/bazi-mcp) | 사주팔자(중국 점성술) 차트 생성 및 분석을 위한 종합 MCP 서버. |
| [**Chart**](https://github.com/KamranBiglari/mcp-server-chart) | 다양한 차트 유형을 제공하며 Zod 스키마 유효성 검사를 통해 타입 안전한 차트 설정을 지원하는 서버. |
| [**Dagster**](https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-dg-cli) | Dagster를 활용하여 데이터 파이프라인을 쉽게 구축할 수 있는 MCP 서버. |
| [**danmartuszewski/hop**](https://github.com/danmartuszewski/hop) | TUI 대시보드와 MCP 서버를 갖춘 빠른 SSH 연결 관리자. 원격 호스트 탐색, 검색, 명령 실행을 지원한다. |
| [**Databricks**](https://docs.databricks.com/aws/en/generative-ai/mcp/) | Databricks 플랫폼의 데이터, AI 도구 및 에이전트에 턴키 관리형 MCP 서버로 연결하거나, 보안 및 데이터 거버넌스 내에서 커스텀 MCP 서버를 호스팅한다. |
| [**Databricks**](https://github.com/JordiNeil/mcp-databricks-server) | LLM이 Databricks 계정에서 SQL 쿼리를 실행하고 작업 실행 목록 및 상세 정보를 조회할 수 있게 한다. |
| [**Databricks Genie**](https://github.com/yashshingvi/databricks-genie-MCP) | Databricks Genie에 연결하여 자연어 질의, SQL 쿼리 실행, Databricks 대화형 에이전트와 상호작용할 수 있게 하는 서버. |
| [**Databricks Smart SQL**](https://github.com/RafaelCartenet/mcp-databricks-server) | Databricks Unity Catalog 메타데이터를 활용하여 Ad-hoc 쿼리 및 데이터 탐색을 위한 스마트 SQL 쿼리를 수행한다. |
| [**DataHub**](https://github.com/acryldata/mcp-server-datahub) | DataHub 메타데이터를 활용하여 데이터 자산 검색, 데이터 리니지 탐색, SQL 쿼리 작성 등을 수행한다. |
| [**Dataset Viewer**](https://github.com/privetin/dataset-viewer) | Hugging Face 데이터셋을 검색, 필터링, 통계 분석 및 데이터 내보내기 기능으로 탐색하고 분석한다. |
| [**Datawrapper**](https://github.com/palewire/datawrapper-mcp) | AI 어시스턴트를 통해 Datawrapper 차트를 생성하는 MCP 서버. |
| [**dbt**](https://github.com/dbt-labs/dbt-mcp) | dbt(data build tool) 공식 MCP 서버. dbt Core/Cloud CLI 통합, 프로젝트 메타데이터 탐색, 모델 정보 및 Semantic Layer 쿼리를 지원한다. |
| [**ECharts MCP Server**](https://github.com/hustcc/mcp-echarts) | AI MCP를 통해 ECharts로 시각화 차트를 동적으로 생성한다. 차트 생성 및 데이터 분석에 활용한다. |
| [**Fabi**](https://docs.fabi.ai/advanced_features_and_dev_tools/mcp_server) | Fabi 분석 에이전트를 활용하여 자연어 프롬프트를 인사이트로 변환한다. SQL/Python 생성, 쿼리 실행, 대시보드 저장을 지원한다. |
| [**finmap-org/mcp-server**](https://github.com/finmap-org/mcp-server) | finmap.org MCP 서버. 미국, 영국, 러시아, 터키 증권거래소의 종합 히스토리컬 데이터와 Treemap/Histogram 시각화를 제공한다. |
| [**Gnuradio**](https://github.com/yoelbassin/gnuradioMCP) | LLM이 자율적으로 RF .grc 플로우차트를 생성하고 수정할 수 있게 하는 GNU Radio용 MCP 서버. |
| [**Goal Story**](https://github.com/hichana/goalstory-mcp) | 개인 및 전문 개발을 위한 목표 추적 및 시각화 도구. |
| [**Helm Chart CLI**](https://github.com/jeff-nasseri/helm-chart-cli-mcp) | AI 어시스턴트와 Kubernetes용 Helm 패키지 매니저를 연결한다. 자연어로 Helm 명령을 실행할 수 있다. |
| [**IBM watsonx.data intelligence**](https://github.com/IBM/data-intelligence-mcp-server) | watsonx.data intelligence의 거버넌스 및 카탈로그, 데이터 품질, 데이터 리니지, 데이터 프로덕트 허브에서 데이터를 검색, 이해, 활용한다. |
| [**Jupyter Notebook**](https://github.com/jjsantos01/jupyter-notebook-mcp) | Jupyter Notebook을 Claude AI에 연결하여 AI 보조 코드 실행, 데이터 분석, 시각화 및 노트북 관리를 가능하게 한다. |
| [**jwaxman19/qlik-mcp**](https://github.com/jwaxman19/qlik-mcp) | Qlik Cloud API용 MCP 서버. 애플리케이션, 시트 조회 및 시각화 데이터 추출을 인증과 Rate Limiting을 지원하여 수행한다. |
| [**kukapay/hyperliquid-info-mcp**](https://github.com/kukapay/hyperliquid-info-mcp) | Hyperliquid 무기한 선물 DEX의 실시간 데이터와 인사이트를 봇, 대시보드, 분석에 제공하는 MCP 서버. |
| [**Matlab-MCP-Tools**](https://github.com/neuromechanist/matlab-mcp-tools) | MATLAB 스크립트 작성 및 실행, 워크스페이스 컨텍스트 유지, 플롯 시각화, 섹션별 코드 분석을 지원하는 MCP 서버. |
| [**Mermaid**](https://github.com/hustcc/mcp-mermaid) | AI MCP를 통해 Mermaid 다이어그램과 차트를 동적으로 생성한다. |
| [**Netwrix**](https://github.com/netwrix/mcp-server-naa) | Netwrix Access Analyzer 데이터 분석을 위한 FastMCP 기반 서버. 향상된 데이터 분석 기능을 제공한다. |
| [**OneNote**](https://github.com/rajvirtual/MCP-Servers/tree/master/onenote) | Microsoft Graph API를 통해 OneNote에 연결하여 노트북, 섹션, 페이지를 읽고 생성하는 MCP 서버. |
| [**Powerdrill**](https://github.com/powerdrillai/powerdrill-mcp) | Powerdrill 데이터셋과 상호작용하여 스마트 AI 데이터 분석 및 인사이트를 제공하는 MCP 서버. |
| [**QuickChart**](https://github.com/GongRzhe/Quickchart-MCP-Server) | QuickChart.io를 사용하여 차트를 생성하는 MCP 서버. |
| [**Reexpress**](https://github.com/ReexpressAI/reexpress_mcp_server) | 검색, 소프트웨어, 데이터 사이언스 워크플로우에 Similarity-Distance-Magnitude 통계 검증을 적용한다. |
| [**speedofme-dev/speedofme-mcp**](https://www.npmjs.com/package/@speedofme/mcp) | 129개 글로벌 Fastly Edge 서버를 통한 정확한 인터넷 속도 테스트와 분석 대시보드 및 로컬 히스토리를 제공하는 SpeedOf.Me 공식 서버. |
| [**Teradata**](https://github.com/Teradata/teradata-mcp-server) | Teradata 플랫폼에서 멀티태스크 데이터 분석을 위한 도구와 프롬프트를 제공하는 MCP 서버. |
| [**ThoughtSpot**](https://github.com/thoughtspot/mcp-server) | ThoughtSpot의 데이터 분석 기능을 Claude 또는 MCP 호스트에 연결한다. 팀 전원을 위한 전용 데이터 분석가 역할을 한다. |
| [**Unified Diff MCP Server**](https://github.com/gorosun/unified-diff-mcp) | diff2html을 사용한 HTML 및 PNG Diff 시각화 서버. 파일 시스템 edit_file 드라이런 출력에 최적화되었으며 Bun 런타임을 사용한다. |
| [**Vega-Lite**](https://github.com/isaacwasserman/mcp-vegalite-server) | 가져온 데이터를 VegaLite 형식과 렌더러를 사용하여 시각화를 생성한다. |
| [**Vizro**](https://github.com/mckinsey/vizro/tree/main/vizro-mcp) | 검증 가능하고 유지보수 용이한 데이터 차트 및 대시보드를 생성하는 도구와 템플릿을 제공한다. |

---

## 🔗 API & 통합

> REST/GraphQL API 관리, SaaS 통합 플랫폼

| 서버 | 설명 |
|------|------|
| [**AgentRPC**](https://github.com/agentrpc/agentrpc) | AgentRPC를 사용하여 네트워크 경계를 넘어 모든 언어의 모든 함수에 연결한다. |
| [**APIMatic MCP**](https://github.com/apimatic/apimatic-validator-mcp) | APIMatic API를 활용하여 OpenAPI 스펙을 검증하는 MCP 서버. OpenAPI 파일을 처리하고 유효성 검사 요약을 반환한다. |
| [**APIWeaver**](https://github.com/GongRzhe/APIWeaver) | 웹 API 설정으로부터 동적으로 MCP 서버를 생성한다. REST API, GraphQL 엔드포인트 등을 MCP 호환 도구로 쉽게 통합한다. |
| [**Apollo IO MCP Server**](https://github.com/AgentX-ai/apollo-io-mcp-server) | apollo.io MCP 서버. 개인 및 조직의 연락처 데이터를 에이전트 방식으로 조회/보강한다. |
| [**Apollo MCP Server**](https://github.com/apollographql/apollo-mcp-server/) | GraphQL API를 AI 에이전트에 연결한다. |
| [**automation-ai-labs/mcp-link**](https://github.com/automation-ai-labs/mcp-link) | OpenAPI Schema를 사용하여 모든 API를 AI 에이전트에 원활하게 통합한다. |
| [**berlinbra/alpha-vantage-mcp**](https://github.com/berlinbra/alpha-vantage-mcp) | Alpha Vantage API 통합으로 주식 및 암호화폐 정보를 조회한다. |
| [**Boost.space**](https://github.com/boostspace/boostspace-mcp-server) | Boost.space와 통합하여 2,000개 이상의 소스에서 중앙 집중화되고 자동화된 비즈니스 데이터를 제공하는 MCP 서버. |
| [**bright8192/esxi-mcp-server**](https://github.com/bright8192/esxi-mcp-server) | MCP 기반 VMware ESXi/vCenter 관리 서버. 가상 머신 관리를 위한 간단한 REST API 인터페이스를 제공한다. |
| [**ckanthony/openapi-mcp**](https://github.com/ckanthony/openapi-mcp) | Docker화된 MCP 서버로 기존 API 문서를 활용하여 AI 에이전트가 모든 API에 접근할 수 있게 한다. |
| [**Composio**](https://docs.composio.dev/docs/mcp-overview#-getting-started) | Composio를 사용하여 100개 이상의 도구에 연결한다. 설정 불필요, 인증 내장, 에이전트용으로 설계되었다. |
| [**ConfigCat**](https://github.com/configcat/mcp-server) | Feature Flag 서비스인 ConfigCat과 AI 도구를 연결한다. Feature Flag, 설정, 환경, 제품, 조직 관리를 지원한다. |
| [**Confluent**](https://github.com/confluentinc/mcp-confluent) | Confluent Kafka 및 Confluent Cloud REST API와 상호작용한다. |
| [**CreateveAI Nexus**](https://github.com/spgoodman/createveai-nexus-server) | AI 에이전트와 엔터프라이즈 시스템 간의 오픈소스 브릿지. 커스텀 API 플러그인(ComfyUI 노드 호환 포함), Copilot Studio MCP 에이전트 통합을 지원한다. |
| [**djalal/quran-mcp-server**](https://github.com/djalal/quran-mcp-server) | 공식 REST API v4를 통해 Quran.com 코퍼스와 상호작용하는 MCP 서버. |
| [**DocBase**](https://help.docbase.io/posts/3925317) | DocBase API 통합을 위한 공식 MCP 서버. 포스트 관리, 사용자 협업, 그룹 관리 등을 지원한다. |
| [**evalstate/mcp-miro**](https://github.com/evalstate/mcp-miro) | MIRO 화이트보드에 접근하여 항목을 대량 생성 및 읽기한다. REST API용 OAUTH 키가 필요하다. |
| [**Gentoro**](https://github.com/gentoro-GT/mcp-nodejs-server) | OpenAPI 스펙을 기반으로 MCP 서버를 생성한다. |
| [**Geolocation**](https://github.com/jackyang25/geolocation-mcp-server) | WalkScore API 통합으로 도보 편의성, 대중교통, 자전거 점수를 제공한다. |
| [**Google News**](https://github.com/ChanMeng666/server-google-news) | SerpAPI 통합을 통한 Google News 검색 기능. 자동 주제 분류 및 다국어 지원을 제공한다. |
| [**Grafbase**](https://github.com/grafbase/grafbase/tree/main/crates/mcp) | 단일 명령으로 GraphQL API를 스키마 인텔리전스를 갖춘 효율적인 MCP 서버로 변환한다. |
| [**GraphQL**](https://github.com/drestrepom/mcp_graphql) | 각 GraphQL 쿼리를 개별 도구로 자동 노출하는 종합 GraphQL API 통합 서버. |
| [**mahdin75/geoserver-mcp**](https://github.com/mahdin75/geoserver-mcp) | LLM을 GeoServer REST API에 연결하여 AI 어시스턴트가 지리공간 데이터 및 서비스와 상호작용할 수 있게 하는 MCP 서버. |
| [**MCP-Airflow-API**](https://github.com/call518/MCP-Airflow-API) | Apache Airflow API 통합 MCP 서버. 서비스 운영, 설정 관리, 상태 모니터링 등 Airflow 클러스터 관리 도구를 제공한다. |
| [**mikechao/metmuseum-mcp**](https://github.com/mikechao/metmuseum-mcp) | Metropolitan Museum of Art Collection API 통합으로 소장품 내 예술 작품을 검색하고 표시한다. |
| [**MKP**](https://github.com/StacklokLabs/mkp) | Kubernetes용 Model Kontext Protocol 서버. 네이티브 Go 구현과 직접 API 통합으로 LLM 기반 애플리케이션이 Kubernetes 클러스터와 상호작용한다. |
| [**NetSuite**](https://github.com/dsvantien/netsuite-mcp-server) | OAuth 2.0 인증을 갖춘 NetSuite ERP 통합 MCP 서버. SuiteQL 쿼리, 리포트, 저장된 검색, REST API 연동을 통해 자연어로 NetSuite 데이터에 접근한다. |
| [**OpenAPI**](https://github.com/snaggle-ai/openapi-mcp-server) | OpenAPI API와 상호작용한다. |
| [**OpenAPI Schema**](https://github.com/hannesj/mcp-openapi-schema) | 컨텍스트를 비대하게 만들지 않으면서 LLM이 대규모 OpenAPI 스키마를 탐색할 수 있게 한다. |
| [**OpenAPI Schema Explorer**](https://github.com/kadykov/mcp-openapi-schema-explorer) | MCP Resources를 통해 로컬 또는 원격 OpenAPI/Swagger 스펙에 토큰 효율적으로 접근한다. |
| [**ouvreboite/openapi-to-mcp**](https://github.com/ouvreboite/openapi-to-mcp) | OpenAPI 스펙을 사용하여 모든 API에 접근하는 경량 MCP 서버. OAuth2와 전체 JSON 스키마 파라미터/요청 본문을 지원한다. |
| [**Qorus**](https://qoretechnologies.com/manual/qorus/current/qorus/sysarch.html#mcp_server) | 코드 작성 없이 AI를 활용하여 모든 애플리케이션, 시스템, 기술에 연결하고 비즈니스 프로세스를 자동화한다. |
| [**ReAPI-com/mcp-openapi**](https://github.com/ReAPI-com/mcp-openapi) | LLM이 OpenAPI 스펙의 모든 것을 파악하여 탐색, 설명, 코드/Mock 데이터 생성을 수행하는 MCP 서버. |
| [**Restream**](https://github.com/shaktech786/restream-mcp-server) | Restream API 통합 MCP 서버. 멀티플랫폼 라이브 스트림 관리, 채널 제어, 스트리밍 분석을 지원한다. |
| [**Specbridge**](https://github.com/TBosak/specbridge) | OpenAPI 스펙을 MCP 도구로 손쉽게 변환한다. |
| [**VMware Fusion**](https://github.com/yeahdongcn/vmware-fusion-mcp-server) | Fusion REST API를 통해 VMware Fusion 가상 머신을 관리한다. |
| [**Wekan**](https://github.com/namar0x0309/wekan-mcp) | Wekan용 비공식 MCP 서버. REST API 전체 기능으로 태스크 및 보드를 추가, 편집, 삭제한다. |
| [**zaizaizhao/mcp-swagger-server**](https://github.com/zaizaizhao/mcp-swagger-server) | OpenAPI/Swagger 스펙을 MCP 형식으로 변환하여 AI 어시스턴트가 표준화된 프로토콜로 REST API와 상호작용할 수 있게 하는 MCP 서버. |

---

## ⚡ 자동화 & 워크플로우

> Zapier, n8n 등 자동화 및 워크플로우 오케스트레이션

| 서버 | 설명 |
|------|------|
| [**1mcpserver**](https://github.com/particlefuture/1mcpserver) | MCP의 MCP. 로컬 머신에서 MCP 서버를 자동으로 발견, 설정, 추가한다. |
| [**AaronVick/ECHO_RIFT_MCP**](https://github.com/AaronVick/ECHO_RIFT_MCP) | EchoRift 인프라 프리미티브(BlockWire, CronSynth, Switchboard, Arbiter)용 MCP 서버. MCP 클라이언트가 EchoRift를 네이티브 기능 레이어로 사용한다. |
| [**ADR Analysis**](https://github.com/tosin2013/mcp-adr-analysis-server) | AI 기반 ADR(Architectural Decision Records) 분석 서버. 아키텍처 인사이트, 기술 스택 감지, 보안 점검, TDD 워크플로우 강화를 제공한다. |
| [**Apple Script**](https://github.com/peakmojo/applescript-mcp) | LLM이 AppleScript 코드를 실행하여 Mac의 모든 것을 제어할 수 있게 하는 MCP 서버. 별도 설정 불필요. |
| [**Arr Suite**](https://github.com/shaktech786/arr-suite-mcp-server) | Plex 및 *arr 미디어 자동화 스위트(Sonarr, Radarr, Prowlarr, Bazarr, Overseerr) 통합 MCP 서버. 자연어 처리를 통한 통합 미디어 관리를 지원한다. |
| [**automateyournetwork/pyATS_MCP**](https://github.com/automateyournetwork/pyATS_MCP) | Cisco pyATS 서버로 네트워크 디바이스와 구조화된 모델 기반 상호작용을 지원한다. |
| [**AX-Platform**](https://github.com/AX-MCP/PaxAI?tab=readme-ov-file#mcp-setup-guides) | AI 에이전트 협업 플랫폼. 태스크 협업, 컨텍스트 공유, 워크플로우 조율을 지원한다. |
| [**bivex/kanboard-mcp**](https://github.com/bivex/kanboard-mcp) | Go로 작성된 Kanboard용 MCP 서버. 자연어 명령을 Kanboard API 호출로 변환하여 프로젝트, 태스크, 사용자 관리를 자동화한다. |
| [**Bright Data**](https://github.com/brightdata/brightdata-mcp) | 단일 인터페이스로 공개 인터넷 전역에서 웹을 발견, 추출, 상호작용한다. |
| [**BrightData**](https://github.com/luminati-io/brightdata-mcp) | 단일 인터페이스로 공개 인터넷 전역에서 웹을 발견, 추출, 상호작용한다. |
| [**Chiki StudIO**](https://chiki.studio/galimybes/mcp/) | 코드 없이 설정만으로 구성 가능한 MCP 서버를 생성한다. 인스트럭션, 프롬프트, 도구를 지원한다. |
| [**computer-use-mcp**](https://github.com/domdomegg/computer-use-mcp) | 화면 캡처, 마우스, 키보드 기능으로 컴퓨터를 제어하여 자동화된 데스크톱 상호작용 및 태스크를 수행한다. |
| [**Context Templates**](https://github.com/ginylil/context-templates) | 다양한 개발 작업에서 프롬프트, 설정, 워크플로우 구조화를 돕는 재사용 가능한 컨텍스트 템플릿 오픈소스 컬렉션. |
| [**DevOps AI Toolkit**](https://github.com/vfarcic/dot-ai) | 지능형 자동화와 AI 기반 지원을 통해 소프트웨어 개발 워크플로우를 향상시키는 AI 기반 개발 생산성 플랫폼. |
| [**Dify**](https://github.com/YanxingLiu/dify-mcp-server) | Dify 워크플로우용 간단한 MCP 서버 구현. |
| [**DifyWorkflow**](https://github.com/gotoolkits/mcp-difyworkflow-server) | Dify 워크플로우를 조회하고 실행하는 도구. |
| [**Drata**](https://drata.com/mcp) | 실험적 MCP 서버로 실시간 컴플라이언스 인텔리전스를 AI 워크플로우에 통합한다. |
| [**EDA MCP Server**](https://github.com/NellyW8/mcp-EDA) | 전자 설계 자동화(EDA) 도구용 종합 MCP 서버. Yosys로 Verilog 합성, Icarus Verilog로 시뮬레이션, 완전한 ASIC 플로우 등을 AI 어시스턴트가 수행한다. |
| [**Extended Memory**](https://github.com/ssmirnovpro/extended-memory-mcp) | Claude 대화 간 영속 메모리 서버. 멀티 프로젝트 지원, 자동 중요도 점수 매기기, 태그 기반 정리를 제공한다. 400개 이상의 테스트로 프로덕션 준비 완료. |
| [**FDIC BankFind MCP Server - (Unofficial)**](https://github.com/clafollett/fdic-bank-find-mcp-server) | FDIC BankFind API를 AI 도구 및 워크플로우에 제공하는 MCP 서버. 구조화된 미국 은행 데이터를 제공한다. |
| [**FileScopeMCP**](https://github.com/admica/FileScopeMCP) | 의존성 관계를 기반으로 코드베이스의 중요 파일을 식별하고 분석한다. 다이어그램 생성, 파일별 중요도 점수 매기기로 AI 어시스턴트의 코드베이스 이해를 돕는다. |
| [**gbrigandi/mcp-server-cortex**](https://github.com/gbrigandi/mcp-server-cortex) | Cortex를 통합하는 Rust 기반 MCP 서버. AI를 통한 Observable 분석 및 자동화된 보안 대응을 지원한다. |
| [**GDAL**](https://github.com/Wayfinder-Foundry/gdal-mcp) | GDAL 스타일 지리공간 워크플로우 서버. AI 에이전트에 카탈로그 탐색, 메타데이터 인텔리전스, 래스터/벡터 처리를 제공한다. |
| [**glenngillen/mcpmcp-server**](https://github.com/glenngillen/mcpmcp-server) | MCP 서버 목록을 제공하여 클라이언트에서 일상 워크플로우 개선에 활용할 수 있는 서버를 조회한다. |
| [**GoLogin MCP server**](https://github.com/gologinapp/gologin-mcp) | AI 대화를 통해 GoLogin 브라우저 프로필과 자동화를 직접 관리한다. |
| [**gotoHuman**](https://github.com/gotohuman/gotohuman-mcp-server) | Human-in-the-loop 플랫폼. AI 에이전트 및 자동화가 gotoHuman 수신함으로 승인 요청을 보낼 수 있다. |
| [**henilcalagiya/mcp-apple-notes**](https://github.com/henilcalagiya/mcp-apple-notes) | MCP를 사용한 Apple Notes 자동화 도구. HTML 콘텐츠의 전체 CRUD, 폴더 관리, 검색 기능을 지원한다. |
| [**Hiveflow**](https://github.com/hiveflowai/hiveflow-mcp-server) | 어시스턴트에서 직접 에이전트 기반 AI 워크플로우를 생성, 관리, 실행한다. |
| [**Human-In-the-Loop**](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server) | 직관적 GUI 대화상자를 통해 AI 어시스턴트가 사람과 상호작용할 수 있게 하는 MCP 서버. 자동화된 AI 프로세스와 인간 의사결정을 연결한다. |
| [**Hydrolix**](https://github.com/hydrolix/mcp-hydrolix) | Hydrolix 시계열 데이터레이크 통합으로 스키마 탐색과 쿼리 기능을 LLM 기반 워크플로우에 제공한다. |
| [**IDA Pro MCP**](https://github.com/mrexodia/ida-pro-mcp) | IDA Pro를 사용한 자동화된 리버스 엔지니어링을 위한 MCP 서버. |
| [**iFlytek Workflow**](https://github.com/iflytek/ifly-workflow-mcp-server) | MCP 서버를 통해 iFlytek Workflow에 연결하고 자체 에이전트를 실행한다. |
| [**interactive-mcp**](https://github.com/ttommyth/interactive-mcp) | MCP 루프에 직접 로컬 사용자 프롬프트와 채팅 기능을 추가하여 대화형 LLM 워크플로우를 구현한다. |
| [**Jellyfish**](https://github.com/Jellyfish-AI/jellyfish-mcp) | Jellyfish 플랫폼을 통해 AI 에이전트에 팀의 소프트웨어 엔지니어링 리소스 배분 및 워크플로우 컨텍스트를 제공한다. |
| [**jhomen368/overseerr-mcp**](https://github.com/jhomen368/overseerr-mcp) | AI 어시스턴트를 Overseerr에 통합하여 Plex 생태계에서 자동화된 미디어 탐색, 요청, 관리를 수행한다. |
| [**jinzcdev/leetcode-mcp-server**](https://github.com/jinzcdev/leetcode-mcp-server) | LeetCode의 프로그래밍 문제, 솔루션, 제출 내역, 공개 데이터에 자동으로 접근하는 MCP 서버. leetcode.com(글로벌) 및 leetcode.cn(중국) 사이트를 지원한다. |
| [**Keboola**](https://github.com/keboola/keboola-mcp-server) | 단일 직관적 플랫폼에서 데이터 워크플로우, 통합, 분석을 구축한다. |
| [**kestra-io/mcp-server-python**](https://github.com/kestra-io/mcp-server-python) | Kestra 워크플로우 오케스트레이션 플랫폼용 MCP 서버 구현. |
| [**LambdaTest**](https://www.lambdatest.com/mcp) | 접근성, SmartUI, Automation, HyperExecute 등 LambdaTest MCP 서버를 통해 AI 어시스턴트와 테스트 워크플로우를 연결한다. |
| [**louis030195/toggl-mcp**](https://github.com/louis030195/toggl-mcp) | Toggl Track 시간 추적 통합. 타이머 시작/정지, 시간 항목 관리, 프로젝트 시간 추적, 오늘의 요약을 제공한다. |
| [**MCP Server Generator**](https://github.com/SerhatUzbas/mcp-server-generator) | MCP 서버를 생성하고 관리하는 MCP 서버. 비기술 사용자와 개발자 모두 AI 가이드, 자동 의존성 관리로 커스텀 JavaScript MCP 서버를 구축한다. |
| [**mcp-server-leetcode**](https://github.com/doggybee/mcp-server-leetcode) | LeetCode에서 문제를 연습하고 조회한다. 문제 검색, 솔루션, 인사이트 자동화를 지원한다. |
| [**mobile-next/mobile-mcp**](https://github.com/mobile-next/mobile-mcp) | Android/iOS 앱 및 디바이스 자동화, 개발, 앱 스크래핑을 위한 MCP 서버. Simulator/Emulator 및 물리적 디바이스를 지원한다. |
| [**NON906/omniparser-autogui-mcp**](https://github.com/NON906/omniparser-autogui-mcp) | 화면 GUI를 자동으로 조작하는 MCP 서버. |
| [**Odoo**](https://github.com/ivnvxd/mcp-server-odoo) | AI 어시스턴트를 Odoo ERP 시스템에 연결하여 비즈니스 데이터 접근 및 워크플로우 자동화를 수행한다. |
| [**phuongrealmax/code-guardian**](https://github.com/phuongrealmax/code-guardian) | AI 기반 코드 리팩토링 엔진. 코드 분석, 핫스팟 탐지, 복잡도 메트릭, 영속 메모리, 자동 리팩토링 계획 등 80개 이상의 MCP 도구를 제공한다. |
| [**Pixelle MCP**](https://github.com/AIDC-AI/Pixelle-MCP) | ComfyUI 워크플로우를 코드 없이 MCP 도구로 변환하는 옴니모달 AIGC 프레임워크. 텍스트, 이미지, 사운드, 비디오 생성을 지원한다. |
| [**Prefect**](https://github.com/allen-munsch/mcp-prefect) | Prefect Server 및 Prefect Cloud를 활용한 워크플로우 오케스트레이션 및 ELT/ETL을 위한 MCP 서버. |
| [**Productboard**](https://github.com/kenjihikmatullah/productboard-mcp) | Productboard API를 MCP를 통해 에이전트 워크플로우에 통합한다. |
| [**proxymock**](https://docs.speedscale.com/proxymock/reference/mcp/) | 라이브 앱을 녹화하여 테스트와 Mock을 자동 생성하는 MCP 서버. |
| [**ReportPortal**](https://github.com/reportportal/reportportal-mcp-server) | 원하는 LLM을 사용하여 ReportPortal의 자동화된 테스트 결과를 탐색하고 분석한다. |
| [**Smartlead**](https://github.com/jean-technologies/smartlead-mcp-server-local) | Smartlead에 연결하는 MCP 서버. 추가 도구, 기능, 워크플로우 자동화 플랫폼 연결도 지원한다. |
| [**Smooth Operator**](https://smooth-operator.online/agent-tools-api-docs/toolserverdocs) | AI Vision, 마우스, 키보드, Automation Tree, 웹 브라우저를 통해 Windows를 자동화하는 도구. |
| [**spacecode-ai/SpaceBridge-MCP**](https://github.com/spacecode-ai/SpaceBridge-MCP) | 바이브 코딩에서 이슈를 자동으로 추적하여 구조화와 컨텍스트를 유지한다. |
| [**SSH MCP Server**](https://github.com/sinjab/mcp_ssh) | SSH 자동화를 위한 프로덕션 레디 MCP 서버. 백그라운드 실행, 파일 전송, 종합적인 타임아웃 보호를 제공한다. |
| [**Storyblok**](https://github.com/Kiran1689/storyblok-mcp-server) | AI 어시스턴트가 Storyblok의 Space, Story, 컴포넌트, 에셋, 워크플로우 등을 직접 접근하고 관리할 수 있게 하는 MCP 서버. |
| [**Task Orchestrator**](https://github.com/EchoingVesper/mcp-task-orchestrator) | AI 기반 태스크 오케스트레이션 및 워크플로우 자동화. 전문 에이전트 역할, 지능형 태스크 분해, Claude Desktop/Cursor/Windsurf/VS Code 통합을 지원한다. |
| [**Taskade**](https://github.com/taskade/mcp) | MCP를 통해 Taskade 플랫폼에 연결한다. 통합 워크스페이스와 API로 태스크, 프로젝트, 워크플로우, AI 에이전트에 실시간 접근한다. |
| [**TuriX Computer Automation MCP**](https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp) | 사전 설정된 태스크를 완료하기 위해 컴퓨터를 자동으로 제어하는 MCP 서버. |
| [**Unstructured**](https://github.com/Unstructured-IO/UNS-MCP) | Unstructured Platform에서 비정형 데이터 처리 워크플로우를 설정하고 상호작용한다. |
| [**User Feedback**](https://github.com/mrexodia/user-feedback-mcp) | Cline, Cursor 등의 도구에서 Human-in-the-loop 워크플로우를 구현하는 간단한 MCP 서버. |
| [**VideoDB Director**](https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol) | AI 기반 영상 워크플로우를 생성한다. 자동 편집, 콘텐츠 모더레이션, 음성 복제, 하이라이트 생성, 검색 가능한 영상 모먼트를 지원한다. |
| [**Wassenger**](https://github.com/wassengerhq/mcp-wassenger) | 모든 AI 모델 클라이언트에서 WhatsApp 채팅, 메시지 전송, 자동화를 수행하는 Wassenger MCP 서버. |
| [**Webvizio/mcp**](https://github.com/Webvizio/mcp) | 웹사이트 및 웹앱의 피드백과 버그 리포트를 컨텍스트가 풍부한 실행 가능한 개발자 태스크로 자동 변환한다. AI 코딩 도구에 직접 전달하여 빠르고 정확하게 태스크를 해결한다. |
| [**Workflowy**](https://github.com/danield137/mcp-workflowy) | Workflowy와 상호작용하는 MCP 서버. |
| [**XixianLiang/HarmonyOS-mcp-server**](https://github.com/XixianLiang/HarmonyOS-mcp-server) | MCP를 통해 AI로 HarmonyOS-next 디바이스를 제어한다. 디바이스 제어 및 UI 자동화를 지원한다. |
| [**yutu**](https://github.com/eat-pray-ai/yutu) | YouTube 운영을 자동화하는 완전한 기능의 MCP 서버 및 CLI. |
| [**Zapier**](https://zapier.com/mcp) | AI 에이전트를 8,000개 앱에 즉시 연결한다. |
| [**zillow/auto-mobile**](https://github.com/zillow/auto-mobile) | 개발자 워크플로우와 테스팅을 위한 Android 자동화 MCP 서버 기반 도구 모음. |
| [**zinja-coder/apktool-mcp-server**](https://github.com/zinja-coder/apktool-mcp-server) | APKTool 기반 MCP 서버로 Android APK 리버스 엔지니어링 자동화를 제공한다. |

---

## 🔍 검색 엔진

> Brave Search, Tavily 등 웹/시맨틱 검색

| 서버 | 설명 |
|------|------|
| [**Aas-ee/open-webSearch**](https://github.com/Aas-ee/open-webSearch) | 무료 멀티 엔진 검색을 활용한 웹 검색 (API 키 불필요) — Bing, Baidu, DuckDuckGo, Brave, Exa, CSDN을 지원합니다. |
| [**Algolia**](https://github.com/algolia/mcp) | AI 에이전트를 사용하여 Algolia 검색 인덱스를 프로비저닝, 구성 및 쿼리합니다. |
| [**apecloud/ApeRAG**](https://github.com/apecloud/ApeRAG) | Graph RAG, 벡터 검색, 전문 검색을 결합한 프로덕션 레디 RAG 플랫폼입니다. 자체 Knowledge Graph 구축 및 Context Engineering에 최적의 선택입니다. |
| [**Baidu AI Search**](https://github.com/baidubce/app-builder/tree/master/python/mcp_server/ai_search) | Baidu Cloud의 AI Search를 활용한 웹 검색 기능을 제공합니다. |
| [**Brave Search**](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Brave Search API를 활용한 웹 검색 기능을 제공합니다. |
| [**brave/brave-search-mcp-server**](https://github.com/brave/brave-search-mcp-server) | Brave Search API를 활용한 웹 검색 기능을 제공합니다. |
| [**CanopyHQ/phloem**](https://github.com/CanopyHQ/phloem) | 인과 그래프와 인용 검증 기능을 갖춘 로컬 우선 AI 메모리입니다. 시맨틱 검색, 코드 변경 시 신뢰도 감쇠, 제로 네트워크 연결을 지원하며 Claude Code, Cursor, VS Code 등 7개 이상의 MCP 클라이언트에서 작동합니다. |
| [**cicada**](https://github.com/wende/cicada) | Elixir 프로젝트를 위한 AST 기반 코드 인텔리전스 도구입니다. 함수 검색, 호출 위치 추적, PR 기여자 분석, git 이력, 시맨틱 검색 등 9가지 도구를 제공하며 AI 쿼리 토큰을 82% 절감합니다. |
| [**Cloudsway SmartSearch**](https://github.com/Cloudsway-AI/smartsearch) | Cloudsway 기반 웹 검색 MCP 서버로, 키워드 검색, 언어 및 안전 옵션을 지원합니다. 구조화된 JSON 결과를 반환합니다. |
| [**disco-trooper/apple-notes-mcp**](https://github.com/disco-trooper/apple-notes-mcp) | 시맨틱 검색, 하이브리드 벡터+키워드 검색, 전체 CRUD 작업, 증분 인덱싱을 지원하는 Apple Notes MCP입니다. 네이티브 macOS 통합을 위해 JXA를 사용합니다. |
| [**ErebusEnigma/context-memory**](https://github.com/ErebusEnigma/context-memory) | SQLite FTS5를 사용한 Claude Code 세션 간 영속적이고 검색 가능한 컨텍스트 저장소입니다. AI 생성 요약으로 세션을 저장하고, 2단계 전문 검색, 체크포인트 복구, 웹 대시보드를 제공합니다. |
| [**Exa**](https://github.com/exa-labs/exa-mcp-server) | Exa가 만든 AI 전용 검색 엔진 |
| [**Exa**](https://github.com/theishangoswami/exa-mcp-server) | Exa AI Search API 연동 서버입니다. |
| [**ferrants/memvid-mcp-server**](https://github.com/ferrants/memvid-mcp-server) | 로컬에서 실행 가능한 Python Streamable HTTP 서버로, memvid 저장소와 시맨틱 검색 기능을 제공합니다. |
| [**Glean**](https://github.com/gleanwork/mcp-server) | Glean API를 활용한 엔터프라이즈 검색 및 채팅 기능을 제공합니다. |
| [**Glean**](https://github.com/longyi1207/glean-mcp-server) | Glean API를 사용하여 검색 및 채팅 기능을 제공하는 서버입니다. |
| [**Google Custom Search**](https://github.com/adenot/mcp-google-search) | Google Custom Search API를 통해 Google 검색 결과를 제공합니다. |
| [**Google PSE/CSE**](https://github.com/rendyfebry/google-pse-mcp) | Google Programmable Search Engine(PSE) 및 Custom Search Engine(CSE)에 대한 접근을 제공하는 MCP 서버입니다. |
| [**Govcraft/rust-docs-mcp-server**](https://github.com/Govcraft/rust-docs-mcp-server) | 시맨틱 검색(임베딩)과 LLM 요약을 활용하여 특정 Rust crate의 최신 문서 컨텍스트를 MCP 도구를 통해 LLM에 제공합니다. |
| [**Grok-MCP**](https://github.com/merterbak/Grok-MCP) | 최신 Grok 모델, 이미지 분석 및 생성, 웹 검색 기능을 갖춘 xAI API용 MCP 서버입니다. |
| [**isnow890/naver-search-mcp**](https://github.com/isnow890/naver-search-mcp) | Naver Search API 통합 MCP 서버로, 블로그, 뉴스, 쇼핑 검색 및 DataLab 분석 기능을 지원합니다. |
| [**Kagi**](https://github.com/ac3xx/mcp-servers-kagi) | Kagi 검색 API 통합 서버입니다. |
| [**Kagi Search**](https://github.com/kagisearch/kagimcp) | Kagi 검색 API를 사용한 웹 검색 기능을 제공합니다. |
| [**kshern/mcp-tavily**](https://github.com/kshern/mcp-tavily.git) | Tavily AI 검색 API 연동 서버입니다. |
| [**leehanchung/bing-search-mcp**](https://github.com/leehanchung/bing-search-mcp) | Microsoft Bing Search API를 활용한 웹 검색 기능을 제공합니다. |
| [**Linkup**](https://github.com/LinkupPlatform/js-mcp-server) | (JS 버전) Linkup의 고급 검색 API를 통해 웹 검색 기능을 제공하는 MCP 서버입니다. AI 어시스턴트와 개발 도구가 자연어 기반의 지능형 웹 검색을 수행할 수 있도록 지원합니다. |
| [**Linkup**](https://github.com/LinkupPlatform/python-mcp-server) | (Python 버전) Linkup의 고급 검색 API를 통해 웹 검색 기능을 제공하는 MCP 서버입니다. AI 어시스턴트와 개발 도구가 자연어 기반의 지능형 웹 검색을 수행할 수 있도록 지원합니다. |
| [**MCP Documentation Server**](https://github.com/andrea9293/mcp-documentation-server) | 로컬 우선 문서 관리 및 임베딩 또는 Gemini AI(권장)를 통한 시맨틱 검색을 제공하는 서버입니다. 디스크 영속화, 인메모리 인덱스, 캐싱으로 성능이 최적화되어 있습니다. |
| [**mcp-local-rag**](https://github.com/nkapila6/mcp-local-rag) | Google MediaPipe Text Embedder와 DuckDuckGo Search를 사용하여 로컬에서 실행되는 기본적인 RAG 방식 웹 검색 MCP 서버입니다. |
| [**MCP-SearXNG-Enhanced Web Search**](https://github.com/OvertliDS/mcp-searxng-enhanced) | 카테고리 인식 웹 검색, 웹 스크래핑, 날짜/시간 조회 도구를 포함한 SearXNG 웹 검색용 강화 MCP 서버입니다. |
| [**Meilisearch**](https://github.com/meilisearch/meilisearch-mcp) | Meilisearch(전문 검색 및 시맨틱 검색 API)와 상호작용하고 쿼리합니다. |
| [**memento-mcp**](https://github.com/gannonh/memento-mcp) | 시맨틱 검색 및 시간 인식 기능을 갖춘 Neo4j 기반 지식 그래프 메모리 시스템입니다. |
| [**michael-denyer/memory-mcp**](https://github.com/michael-denyer/memory-mcp) | 핫 캐시(즉시 주입)와 콜드 시맨틱 검색의 2단계 메모리 구조입니다. 자주 사용되는 패턴을 자동 승격하고, Claude 출력에서 지식을 추출하며, 지식 그래프 관계로 정리합니다. |
| [**mihaelamj/cupertino**](https://github.com/mihaelamj/cupertino) | Apple Documentation MCP 서버입니다. Apple 개발자 문서, Swift Evolution 제안, 600개 이상의 샘플 코드 프로젝트를 전문 검색으로 탐색할 수 있습니다. |
| [**mikechao/brave-search-mcp**](https://github.com/mikechao/brave-search-mcp) | Brave Search API를 활용한 웹, 이미지, 뉴스, 비디오, 로컬 관심 장소 검색 기능을 제공합니다. |
| [**Nexus**](https://github.com/adawalli/nexus) | OpenRouter API를 통해 Perplexity Sonar 모델을 통합하여 출처 인용이 포함된 실시간 컨텍스트 인식 검색을 제공하는 웹 검색 서버입니다. |
| [**nicholasglazer/gnosis-mcp**](https://github.com/nicholasglazer/gnosis-mcp) | 검색 가능한 문서를 위한 제로 설정 MCP 서버입니다. Markdown을 SQLite(기본) 또는 PostgreSQL에 로드하며 FTS5/tsvector 키워드 검색과 선택적 pgvector 하이브리드 시맨틱 검색을 지원합니다. |
| [**nickclyde/duckduckgo-mcp-server**](https://github.com/nickclyde/duckduckgo-mcp-server) | DuckDuckGo를 사용한 웹 검색 기능을 제공합니다. |
| [**OpenAPI AnyApi**](https://github.com/baryhuang/mcp-server-any-openapi) | 엔드포인트를 위한 내장 시맨틱 검색을 활용하여 대규모 OpenAPI 문서와 상호작용합니다. MCP 서버 접두사를 커스터마이징할 수 있습니다. |
| [**parallel-web/search-mcp**](https://github.com/parallel-web/search-mcp) | AI를 위한 최고 정확도의 웹 검색 기능을 제공합니다. |
| [**Pearch**](https://github.com/Pearch-ai/mcp_pearch) | 인재 발굴 시간을 단축하는 최고의 인물 검색 엔진입니다. |
| [**pskill9/web-search**](https://github.com/pskill9/web-search) | API 키 없이 Google 검색 결과를 활용한 무료 웹 검색을 지원하는 MCP 서버입니다. |
| [**roadwy/cve-search_mcp**](https://github.com/roadwy/cve-search_mcp) | CVE-Search API를 쿼리하는 MCP 서버입니다. 벤더 및 제품 조회, CVE-ID별 CVE 조회, 최신 업데이트된 CVE 목록 조회 등 CVE-Search에 대한 포괄적인 접근을 제공합니다. |
| [**SearXNG**](https://github.com/ihor-sokoliuk/mcp-searxng) | SearXNG용 Model Context Protocol 서버입니다. |
| [**SearXNG Public**](https://github.com/pwilkin/mcp-searxng-public) | 공개 SearXNG 인스턴스에서 데이터를 검색하는 Model Context Protocol 서버로, 폴백 지원 기능을 포함합니다. |
| [**SecretiveShell/MCP-searxng**](https://github.com/SecretiveShell/MCP-searxng) | searXNG 인스턴스에 연결하는 MCP 서버입니다. |
| [**Serper**](https://github.com/garylab/serper-mcp-server) | Serper를 사용하여 Google 검색을 수행하는 MCP 서버입니다. |
| [**Substack/Medium**](https://github.com/jonathan-politzki/mcp-writer-substack) | Claude를 Substack/Medium 글쓰기에 연결하여 게시된 콘텐츠의 시맨틱 검색 및 분석을 가능하게 합니다. |
| [**Tavily**](https://github.com/tavily-ai/tavily-mcp) | Tavily 기반 AI 에이전트용 검색 엔진 (검색 + 추출 기능) |
| [**Tavily search**](https://github.com/RamXX/mcp-tavily) | 명시적 사이트 포함/제외 기능을 갖춘 Tavily 검색 및 뉴스 API용 MCP 서버입니다. |
| [**Tomatio13/mcp-server-tavily**](https://github.com/Tomatio13/mcp-server-tavily) | Tavily AI 검색 API 연동 서버입니다 (Python 버전). |
| [**Typesense**](https://github.com/suhail-ak-s/mcp-typesense-server) | AI 모델에 Typesense 검색 기능을 제공하는 MCP 서버 구현체입니다. LLM이 Typesense에 저장된 데이터를 검색, 탐색, 분석할 수 있도록 지원합니다. |
| [**VpunaAiSearch**](https://github.com/vpuna/vpuna-ai-search) | 시맨틱 검색, 요약 및 컨텍스트 기반 채팅을 제공하는 개발자 우선 플랫폼인 Vpuna AI Search Service에 연결합니다. 각 프로젝트는 자체 Remote HTTP MCP 서버를 동적으로 노출하여 실시간 연동을 지원합니다. |
| [**Web Search MCP**](https://github.com/mrkrsl/web-search-mcp) | 로컬 LLM과 함께 사용할 수 있는 전체 웹 검색, 요약 및 페이지 추출 기능을 제공하는 서버입니다. |
| [**WebSearch-MCP**](https://github.com/mnhlt/WebSearch-MCP) | 자체 호스팅 가능한 Websearch API입니다. |
| [**Zettelkasten**](https://github.com/joshylchen/zettelkasten) | Zettelkasten 방법론을 구현한 포괄적인 AI 기반 지식 관리 시스템입니다. 원자적 노트 생성, 전문 검색, AI 기반 CEQRC 워크플로우(캡처→설명→질문→정제→연결) 기능을 제공합니다. |
| [**zhsama/duckduckgo-mcp-server**](https://github.com/zhsama/duckduckgo-mcp-server/) | DuckDuckGo 검색 기능을 제공하는 TypeScript 기반 MCP 서버입니다. |

---

## 📁 파일 & 문서 관리

> Notion, Obsidian, Google Drive 등 파일/문서/지식 관리

| 서버 | 설명 |
|------|------|
| [**0xshellming/mcp-summarizer**](https://github.com/0xshellming/mcp-summarizer) | AI 요약 MCP 서버. 다양한 콘텐츠 유형 지원: 일반 텍스트, 웹 페이지, PDF 문서, EPUB 도서, HTML 콘텐츠. |
| [**2slides**](https://github.com/2slides/2slides-mcp) | 콘텐츠를 슬라이드/PPT/프레젠테이션으로 변환하거나 사용자 의도에 맞는 슬라이드/PPT/프레젠테이션을 생성하는 도구를 제공하는 MCP 서버. |
| [**aashari/mcp-server-atlassian-confluence**](https://github.com/aashari/mcp-server-atlassian-confluence) | Atlassian Confluence Cloud 통합. ADF에서 Markdown으로의 자동 변환을 통해 AI 시스템이 Confluence 스페이스, 페이지 및 콘텐츠와 상호작용할 수 있게 합니다. |
| [**adhikasp/mcp-twikit**](https://github.com/adhikasp/mcp-twikit) | Twitter 검색 및 타임라인과 상호작용합니다. |
| [**Agentset**](https://github.com/agentset-ai/mcp-server) | Agentset에 연결된 지식 베이스를 위한 RAG 서버. |
| [**ankitmalik84/notion-mcp-server**](https://github.com/ankitmalik84/Agentic_Longterm_Memory/tree/main/src/notion_mcp_server) | 향상된 기능, 강력한 오류 처리 및 프로덕션 레디 기능을 갖춘 Notion 통합을 위한 포괄적인 Model Context Protocol (MCP) 서버. |
| [**Anytype**](https://github.com/anyproto/anytype-mcp) | AI 어시스턴트가 로컬 및 협업 위키인 Anytype과 상호작용하여 자연어로 객체, 목록 등을 구성할 수 있게 하는 MCP 서버. |
| [**API Lab MCP**](https://github.com/atototo/api-lab-mcp) | Claude를 AI 기반 API 테스트 연구소로 변환합니다. 인증 지원, 응답 검증 및 성능 메트릭을 포함한 자연어 대화로 API를 테스트, 디버깅 및 문서화합니다. |
| [**Apple Docs**](https://github.com/kimsungwhee/apple-docs-mcp) | 자연어 쿼리를 통해 Apple Developer Documentation에 원활하게 접근하는 강력한 Model Context Protocol (MCP) 서버. Apple 문서를 검색, 탐색하고 상세 정보를 확인합니다. |
| [**Apple Notes**](https://github.com/RafalWilinski/mcp-apple-notes) | Apple Notes와 대화합니다. |
| [**ArangoDB Graph**](https://github.com/PCfVW/mcp-arangodb-async) | 비동기 우선 Python 아키텍처로, 공식 python-arango 드라이버를 래핑하여 그래프 관리 기능, 콘텐츠 변환 유틸리티(JSON, Markdown, YAML, Table), 백업/복원 기능을 제공합니다. |
| [**Archbee**](https://www.npmjs.com/package/@archbee/mcp) | AI를 통한 즉각적인 답변을 위한 신뢰할 수 있는 문서를 작성하고 게시합니다. 최초의 완전한 문서화 플랫폼 Archbee를 사용하세요. |
| [**Augments**](https://augments.dev/) | 인기 개발 도구 및 라이브러리를 위한 포괄적인 프레임워크 문서와 코드 예시. |
| [**augmnt/augments-mcp-server**](https://github.com/augmnt/augments-mcp-server) | 90개 이상의 프레임워크 문서 소스에 대한 지능적이고 실시간적인 접근으로 Claude Code를 변환합니다. React, Next.js, Laravel, FastAPI, Tailwind CSS 등의 현재 모범 사례를 따르는 정확하고 최신의 코드 생성을 지원합니다. |
| [**AutoGen documentation**](https://github.com/sykuang/mcp-autogen-doc) | AI 어시스턴트에게 Microsoft AutoGen 문서를 검색하고 가져오는 기능을 제공하는 Model Context Protocol (MCP) 서버. |
| [**aybelatchane/mcp-server-terminal**](https://github.com/aybelatchane/mcp-server-terminal) | 터미널용 Playwright - 요소 감지 기능이 있는 구조화된 Terminal State Tree 표현을 통해 TUI/CLI 애플리케이션과 상호작용합니다. |
| [**Badhansen/notion-mcp**](https://github.com/Badhansen/notion-mcp) | Notion API와 통합하여 개인 할 일 목록을 효율적으로 관리하는 Model Context Protocol (MCP) 서버. |
| [**bart6114/my-bear-mcp-server**](https://github.com/bart6114/my-bear-mcp-server/) | Bear의 SQLite DB와 직접 통합하여 Bear 노트 앱의 노트와 태그를 읽을 수 있게 합니다. |
| [**Basecamp**](https://github.com/georgeantonopoulos/Basecamp-MCP-Server) | 프로젝트, 할 일, 카드 테이블, 문서 및 팀 협업을 관리하는 Basecamp 프로젝트 관리 플랫폼과의 통합. |
| [**Basic Memory**](https://github.com/basicmachines-co/basic-memory) | Markdown 파일에서 시맨틱 그래프를 구축하여 LLM과의 대화 간 영구 메모리를 가능하게 하는 로컬 우선 지식 관리 시스템. |
| [**bitbonsai/mcp-obsidian**](https://github.com/bitbonsai/mcp-obsidian) | MCP를 사용한 Obsidian 볼트용 범용 AI 브릿지. 검색, 일괄 작업, 태그 관리, frontmatter 처리를 포함한 11개의 포괄적 메서드로 노트에 안전한 읽기/쓰기 접근을 제공합니다. Claude, ChatGPT 및 모든 MCP 호환 AI 어시스턴트와 작동합니다. |
| [**Box**](https://github.com/box-community/mcp-server-box) | Box AI를 통해 지능형 콘텐츠 관리 플랫폼과 상호작용합니다. |
| [**Box**](https://github.com/hmk/box-mcp-server) | Box에서의 파일 접근 및 검색. |
| [**Box**](https://developer.box.com/guides/box-mcp/) | Box MCP 서버는 Copilot Studio, Cursor, Claude for Desktop 등의 서드파티 AI 에이전트가 Box 콘텐츠에 원활하게 접근할 수 있게 합니다. Box에 저장된 콘텐츠 관련 작업을 수행할 수 있도록 에이전트의 기능을 확장합니다. |
| [**box/mcp-server-box-remote**](https://github.com/box/mcp-server-box-remote/) | Box MCP 서버는 Copilot Studio, Cursor, Claude for Desktop 등의 서드파티 AI 에이전트가 Box 콘텐츠에 안전하고 원활하게 접근하며 검색, 파일/폴더 질문, 데이터 추출 등의 도구를 사용할 수 있게 합니다. |
| [**brianxiadong/ones-wiki-mcp-server**](https://github.com/brianxiadong/ones-wiki-mcp-server) | ONES Wiki 콘텐츠를 검색하고 AI 친화적인 텍스트 형식으로 변환하는 Spring AI MCP 기반 서비스. |
| [**bug-breeder/quip-mcp**](https://github.com/bug-breeder/quip-mcp) | AI 어시스턴트에게 포괄적인 Quip 문서 접근 및 관리를 제공하는 Model Context Protocol (MCP) 서버. 문서 라이프사이클 관리, 스마트 검색, 댓글 관리, Quip.com 및 엔터프라이즈 인스턴스 모두를 위한 안전한 토큰 기반 인증을 지원합니다. |
| [**caol64/wenyan-mcp**](https://github.com/caol64/wenyan-mcp) | AI가 자동으로 Markdown 문서를 포맷하고 WeChat 공중호(GZH)에 게시할 수 있게 하는 Wenyan MCP 서버. |
| [**claude-faf-mcp**](https://github.com/Wolfe-Jam/claude-faf-mcp) | .faf 형식용 MCP 서버. 프로젝트 컨텍스트 관리 기능을 갖춘 컨텍스트 스코어링 엔진. |
| [**ClickUp**](https://github.com/TaazKareem/clickup-mcp-server) | 작업 생성, 업데이트, 대량 작업 및 Markdown 설명을 지원하는 ClickUp 작업 관리용 MCP 서버. |
| [**Clix MCP Server**](https://github.com/clix-so/clix-mcp-server) | AI 에이전트가 실시간으로 신뢰할 수 있는 Clix 문서와 SDK 코드 예시를 제공하여 원활한 통합을 지원하는 Clix MCP 서버. |
| [**Cloudinary**](https://github.com/cloudinary/mcp-servers) | Cloudinary의 미디어 업로드, 변환, AI 분석, 관리, 최적화 및 전달 기능을 AI 에이전트가 사용할 수 있는 도구로 노출합니다. |
| [**Cloudinary**](https://github.com/felores/cloudinary-mcp-server) | Cloudinary에 미디어를 업로드하고 미디어 링크 및 상세 정보를 반환하는 Cloudinary Model Context Protocol 서버. |
| [**consult7**](https://github.com/szeider/consult7) | OpenRouter, OpenAI 또는 Google AI를 통해 고컨텍스트 모델을 사용하여 대규모 코드베이스와 문서 컬렉션을 분석합니다. Claude Code와 함께 사용하면 매우 유용합니다. |
| [**CSV Editor**](https://github.com/santoshray02/csv-editor) | 데이터 조작, 분석 및 유효성 검사를 위한 40개 이상의 연산을 갖춘 종합 CSV 처리 도구. 자동 저장, 실행취소/다시실행 기능 및 GB 이상의 파일 처리를 지원합니다. FastMCP와 Pandas로 구축되었습니다. |
| [**danielkennedy1/pdf-tools-mcp**](https://github.com/danielkennedy1/pdf-tools-mcp) | PDF 다운로드, 보기 및 조작 유틸리티. |
| [**Data Exploration**](https://github.com/reading-plus-ai/mcp-server-data-exploration) | .csv 기반 데이터셋에 대한 자율 데이터 탐색을 위한 MCP 서버로, 최소한의 노력으로 지능적인 인사이트를 제공합니다. 참고: 머신에서 임의의 Python 코드를 실행하므로 주의하여 사용하세요. |
| [**dbt-docs**](https://github.com/mattijsdp/dbt-docs-mcp) | 공식 dbt MCP가 dbt Cloud만 지원하므로 dbt-core(OSS) 사용자를 위한 MCP 서버. 프로젝트 메타데이터, 모델 및 컬럼 수준 리니지, dbt 문서를 지원합니다. |
| [**DeepWiki by Devin**](https://docs.devin.ai/work-with-devin/deepwiki-mcp) | AI 기반 코드베이스 컨텍스트와 답변을 제공하는 원격 인증 불필요 MCP 서버. |
| [**Detailer**](https://detailer.ginylil.com/) | GitHub 저장소에 대한 풍부한 AI 기반 문서를 즉시 생성합니다. AI 에이전트가 작업 수행 전 프로젝트의 깊은 컨텍스트를 파악할 수 있도록 설계되었습니다. |
| [**DevHub**](https://github.com/devhub/devhub-cms-mcp) | DevHub CMS 플랫폼 내에서 웹사이트 콘텐츠를 관리하고 활용합니다. |
| [**Docs**](https://github.com/da1z/docsmcp) | AI 에이전트의 문서 접근을 가능하게 하며, llms.txt 및 기타 원격 또는 로컬 파일을 지원합니다. |
| [**documcp**](https://github.com/tosin2013/documcp) | 다양한 형식과 문서 작업을 지원하는 지능형 문서 처리 및 관리용 MCP 서버. |
| [**Docy**](https://github.com/oborchers/mcp-server-docy) | AI가 필요한 기술 문서에 바로 접근할 수 있게 합니다. 오래된 정보, 깨진 링크, 속도 제한 없이 정확한 실시간 문서 접근을 제공합니다. |
| [**dotemacs/domain-lookup-mcp**](https://github.com/dotemacs/domain-lookup-mcp) | RDAP를 우선 사용하고 WHOIS를 대체 수단으로 활용하는 도메인 이름 조회 서비스. |
| [**eBook-mcp**](https://github.com/onebirdrocks/ebook-mcp) | LLM이 개인 PDF 및 EPUB 전자책을 읽고 상호작용할 수 있게 하는 경량 MCP 서버. AI 독서 어시스턴트 또는 채팅 기반 전자책 인터페이스 구축에 적합합니다. |
| [**entanglr/zettelkasten-mcp**](https://github.com/entanglr/zettelkasten-mcp) | Zettelkasten 지식 관리 방법론을 구현한 Model Context Protocol (MCP) 서버로, Claude 및 기타 MCP 호환 클라이언트를 통해 원자적 노트를 생성, 연결 및 검색할 수 있습니다. |
| [**ericbrown/project-context-mcp**](https://github.com/ericbrown/project-context-mcp) | `.context/` 폴더의 파일을 MCP 리소스로 노출하여 Claude Code가 `@` 멘션을 통해 프로젝트 문서에 즉시 접근할 수 있게 합니다. |
| [**Excel**](https://github.com/haris-musa/excel-mcp-server) | 데이터 읽기/쓰기, 워크시트 관리, 서식 지정, 차트 및 피벗 테이블을 포함한 Excel 조작 기능. |
| [**Excel to JSON MCP by WTSolutions**](https://github.com/he-yang/excel-to-json-mcp) | (1) Excel 또는 CSV 데이터를 JSON 형식으로, (2) Excel(.xlsx) 파일을 구조화된 JSON으로 변환하는 표준화된 인터페이스를 제공하는 MCP 서버. |
| [**Fast Filesystem**](https://github.com/efforthye/fast-filesystem-mcp) | 대용량 파일 처리 기능과 Claude에 최적화된 기능을 갖춘 고급 파일시스템 작업. 빠른 파일 읽기/쓰기, 대용량 파일의 순차 읽기, 디렉토리 작업, 파일 검색을 제공합니다. |
| [**Fetch**](https://github.com/zcaceres/fetch-mcp) | HTML, JSON, Markdown 또는 일반 텍스트를 유연하게 가져오는 서버. |
| [**FileSystem Server**](https://github.com/Oncorporation/filesystem_server) | AI 에이전트에게 프로젝트 폴더와 파일에 대한 선택적 접근을 제공하는 code-workspace 기능을 갖춘 Visual Studio 2022용 로컬 MCP 서버. |
| [**filesystem@quarkiverse/quarkus-mcp-servers**](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) | Quarkus를 사용하여 Java로 구현된 파일 탐색 및 편집을 위한 파일시스템. jar 또는 네이티브 이미지로 제공됩니다. |
| [**freema/mcp-gsheets**](https://github.com/freema/mcp-gsheets) | 포괄적인 읽기, 쓰기, 서식 지정 및 시트 관리 기능을 갖춘 Google Sheets API 통합용 MCP 서버. |
| [**future-audiences/wikimedia-enterprise-model-context-protocol**](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) | Wikipedia 문서 조회 API. |
| [**gabrielmaialva33/winx-code-agent**](https://github.com/gabrielmaialva33/winx-code-agent) | 코드 에이전트를 위한 WCGW의 고성능 Rust 재구현으로, MCP를 통해 LLM에 셸 실행 및 고급 파일 관리 기능을 제공합니다. |
| [**GitMCP**](https://github.com/idosal/git-mcp) | gitmcp.io는 모든 GitHub 저장소 또는 프로젝트 문서에 쉽게 연결할 수 있는 범용 원격 MCP 서버입니다. |
| [**Golang Filesystem Server**](https://github.com/mark3labs/mcp-filesystem-server) | Go로 구축된 구성 가능한 접근 제어 기능을 갖춘 안전한 파일 작업 서버. |
| [**Google Drive**](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) | 파일 접근, 검색 및 관리를 위한 Google Drive 통합. |
| [**Google Sheets**](https://github.com/xing5/mcp-google-sheets) | Google Sheets의 데이터에 접근하고 편집합니다. |
| [**Google Sheets**](https://github.com/rohans2/mcp-google-sheets) | Google Sheets의 데이터에 접근하고 편집하기 위해 TypeScript로 작성된 MCP 서버. |
| [**GROWI**](https://github.com/growilabs/growi-mcp-server) | GROWI API와 통합하기 위한 공식 MCP 서버. |
| [**GXtract**](https://github.com/sascharo/gxtract) | VS Code 및 기타 호환 편집기와 통합하도록 설계된 MCP 서버입니다 (문서: sascharo.github.io/gxtract). GroundX 플랫폼과 상호작용하기 위한 도구 모음을 제공합니다. |
| [**Gyazo**](https://github.com/nota/gyazo-mcp-server) | Gyazo 이미지의 검색, 가져오기, 업로드 및 상호작용을 지원하며 메타데이터와 OCR 데이터를 포함합니다. |
| [**hannesrudolph/mcp-ragdocs**](https://github.com/hannesrudolph/mcp-ragdocs) | 벡터 검색을 통해 문서를 검색하고 처리하는 도구를 제공하는 MCP 서버 구현체로, AI 어시스턴트가 관련 문서 컨텍스트로 응답을 보강할 수 있게 합니다. |
| [**henilcalagiya/google-sheets-mcp**](https://github.com/henilcalagiya/google-sheets-mcp) | AI 어시스턴트의 Google Sheets 게이트웨이! MCP를 통한 원활한 Google Sheets 자동화를 위한 25가지 강력한 도구. |
| [**HenryHaoson/Yuque-MCP-Server**](https://github.com/HenryHaoson/Yuque-MCP-Server) | Yuque API와 통합하여 AI 모델이 Yuque 플랫폼에서 문서 관리, 지식 베이스 상호작용, 콘텐츠 검색 및 분석 데이터 접근을 가능하게 하는 Model-Context-Protocol (MCP) 서버. |
| [**Hillnote**](https://github.com/Rajathbail/hillnote-mcp-server) | 파일을 로컬에 저장하는 Markdown 기반 편집기인 Hillnote 워크스페이스에서 문서를 검색, 편집, 저장 및 생성합니다. |
| [**html2md-mcp**](https://github.com/sunshad0w/html2md-mcp) | 브라우저 지원과 인증 기능을 갖춘 HTML을 Markdown으로 변환하는 MCP 서버. trafilatura와 BeautifulSoup4를 사용하여 HTML 크기를 90-95% 줄이며, JavaScript 렌더링 페이지를 위한 Playwright 통합을 제공합니다. |
| [**Inbox Zero**](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) | 이메일 Inbox Zero를 위한 AI 개인 어시스턴트. |
| [**isaacphi/mcp-gdrive**](https://github.com/isaacphi/mcp-gdrive) | Google Drive에서 읽기 및 Google Sheets 편집을 위한 Model Context Protocol (MCP) 서버. |
| [**j0hanz/filesystem-context-mcp-server**](https://github.com/j0hanz/filesystem-context-mcp-server) | 심볼릭 링크 보호 기능을 갖춘 안전한 파일시스템 탐색, 검색 및 분석을 위한 읽기 전용 MCP 서버. |
| [**jinzcdev/markmap-mcp-server**](https://github.com/jinzcdev/markmap-mcp-server) | markmap을 기반으로 구축된 MCP 서버로, Markdown을 인터랙티브 마인드맵으로 변환합니다. 다중 형식 내보내기(PNG/JPG/SVG), 실시간 브라우저 미리보기, 원클릭 Markdown 복사 및 동적 시각화 기능을 지원합니다. |
| [**jordandalton/restcsv-mcp-server**](https://github.com/JordanDalton/RestCsvMcpServer) | CSV 파일을 위한 MCP 서버. |
| [**kdqed/zaturn**](https://github.com/kdqed/zaturn) | 여러 데이터 소스(SQL, CSV, Parquet 등)를 연결하고 AI에게 인사이트와 시각화를 위한 데이터 분석을 요청합니다. |
| [**KS-GEN-AI/confluence-mcp-server**](https://github.com/KS-GEN-AI/confluence-mcp-server) | CQL을 통해 Confluence 데이터를 가져오고 페이지를 읽습니다. |
| [**Langflow MCP Server**](https://github.com/nobrainer-tech/langflow-mcp) | Langflow 워크플로우 자동화를 위한 90개 도구를 제공하는 종합 MCP 서버. 플로우 관리, 워크플로우 실행, 빌드 처리, 지식 베이스 상호작용을 지원합니다. Docker 지원 및 전체 API 커버리지를 포함합니다. |
| [**Langflow-DOC-QA-SERVER**](https://github.com/GongRzhe/Langflow-DOC-QA-SERVER) | Langflow 기반 문서 Q&A를 위한 Model Context Protocol 서버. Langflow 백엔드를 통해 문서를 쿼리하는 간단한 인터페이스를 제공하여 핵심 MCP 개념을 보여줍니다. |
| [**linxule/mineru-mcp**](https://github.com/linxule/mineru-mcp) | MinerU 문서 파싱 API용 MCP 서버. OCR(109개 언어), 배치 처리(200개 문서), 페이지 범위 지정 및 로컬 파일 업로드를 통해 PDF, 이미지, DOCX, PPTX를 파싱합니다. 구조화된 출력으로 73% 토큰 감소. |
| [**Local RAG**](https://github.com/shinpr/mcp-local-rag) | 최소한의 설정으로 가능한 경량 로컬 문서 검색. PDF, DOCX, TXT 및 Markdown 파일 전체를 검색합니다. Docker나 외부 서비스가 필요 없습니다. |
| [**louis030195/easy-obsidian-mcp**](https://github.com/louis030195/easy-obsidian-mcp) | 지식 관리를 위해 Obsidian 볼트와 상호작용합니다. 노트를 생성, 읽기, 업데이트 및 검색합니다. 파일시스템 접근을 통해 로컬 Obsidian 볼트와 작동합니다. |
| [**lucene-mcp-server**](https://github.com/VivekKumarNeu/MCP-Lucene-Server) | Lucene을 사용한 빠른 문서 검색 및 관리를 위한 Spring Boot 서버. |
| [**lucid-mcp-server**](https://github.com/smartzan63/lucid-mcp-server) | Lucidchart 및 Lucidspark용 MCP 서버: Lucid 문서와 다이어그램의 연결, 검색 및 텍스트 표현을 LLM 기반 AI Vision 분석을 통해 얻습니다. |
| [**madhan-g-p/DevDocs-MCP**](https://github.com/madhan-g-p/DevDocs-MCP) | 오프라인 모드에서 DevDocs.io의 버전 고정된 결정론적 문서를 제공하는 MCP 서버. |
| [**MarceauSolutions/md-to-pdf-mcp**](https://github.com/MarceauSolutions/md-to-pdf-mcp) | 사용자 정의 가능한 테마, 머리글, 바닥글 및 스타일링을 통해 Markdown 파일을 전문적인 PDF로 변환합니다. |
| [**Markdown2doc**](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/pandoc) | Pandoc을 사용하여 다양한 파일 형식 간 변환을 수행합니다. |
| [**Markdownify**](https://github.com/zcaceres/mcp-markdownify-server) | 거의 모든 것을 Markdown으로 변환하는 MCP (PPTX, HTML, PDF, YouTube 자막 등). |
| [**Markitdown**](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/markitdown) | 파일을 Markdown으로 변환합니다. |
| [**Masquerade**](https://github.com/postralai/masquerade) | PDF 문서에서 민감한 정보를 마스킹한 후 Claude에 전송합니다. Masquerade는 LLM을 위한 프라이버시 방화벽 역할을 합니다. |
| [**Mastra/mcp-docs-server**](https://github.com/mastra-ai/mastra/tree/main/packages/mcp-docs-server) | AI 어시스턴트에게 Mastra.ai의 전체 지식 베이스에 대한 직접 접근을 제공합니다. |
| [**Maven Tools MCP**](https://github.com/arvindand/maven-tools-mcp) | JVM 빌드 도구를 위한 Maven Central 의존성 인텔리전스. 모든 빌드 도구(Maven, Gradle, SBT, Mill)를 지원하며 문서 지원을 위한 Context7 통합을 포함합니다. |
| [**mcp-sanctions**](https://github.com/madupay/mcp-sanctions) | 글로벌 제재 목록(OFAC, SDN, UN 등)에 대해 개인 및 조직을 심사합니다. 프롬프트 또는 문서 업로드로 쿼리할 수 있습니다. |
| [**Md2doc**](https://github.com/Yorick-Ryu/md2doc-mcp) | 외부 변환 서비스를 사용하여 Markdown 텍스트를 DOCX 형식으로 변환합니다. |
| [**meanands/npm-package-docs-mcp**](https://github.com/meanands/npm-package-docs-mcp) | 패키지의 GitHub 저장소 또는 README에서 최신 README 문서를 가져와 npm 패키지의 최신 문서를 제공하는 MCP 서버. |
| [**MediaWiki**](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server) | 모든 MediaWiki 위키와 상호작용하는 Model Context Protocol (MCP) 서버. |
| [**MediaWiki MCP adapter**](https://github.com/lucamauri/MediaWiki-MCP-adapter) | MediaWiki 및 WikiBase API를 위한 커스텀 Model Context Protocol 어댑터. |
| [**Microsoft Learn Docs**](https://github.com/microsoftdocs/mcp) | Microsoft 공식 문서에 구조화된 접근을 제공하는 MCP 서버. 코드 생성, 질의응답 등을 위한 정확하고 권위 있는 컨텍스트 인식 기술 콘텐츠를 검색합니다. |
| [**modelcontextprotocol/server-filesystem**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/filesystem) | 로컬 파일시스템에 대한 직접 접근. |
| [**mrjoshuak/godoc-mcp**](https://github.com/mrjoshuak/godoc-mcp) | 전체 소스 파일을 읽지 않고도 AI 어시스턴트에게 패키지 문서와 타입에 스마트하게 접근할 수 있게 하는 토큰 효율적인 Go 문서 서버. |
| [**Narasimhaponnada/mermaid-mcp**](https://github.com/Narasimhaponnada/mermaid-mcp) | 플로우차트, 시퀀스 다이어그램, 클래스 다이어그램, ER 다이어그램, 아키텍처 다이어그램, 상태 머신 등 22개 이상의 다이어그램 유형을 지원하는 AI 기반 Mermaid 다이어그램 생성. 50개 이상의 사전 제작 템플릿, 고급 레이아웃 엔진, SVG/PNG/PDF 내보내기, GitHub Copilot, Claude 및 MCP 호환 클라이언트와의 원활... |
| [**Needle**](https://github.com/needle-ai/needle-mcp) | 자체 문서에서 데이터를 검색하고 조회할 수 있는 프로덕션 레디 RAG 솔루션. |
| [**Neo1228/spring-boot-starter-swagger-mcp**](https://github.com/Neo1228/spring-boot-starter-swagger-mcp) | 기존 Swagger/OpenAPI 문서를 재사용하여 Spring Boot 애플리케이션을 즉시 MCP 서버로 전환합니다. |
| [**NetMind ParsePro**](https://github.com/protagolabs/Netmind-Parse-PDF-MCP) | NetMind 팀이 구축하고 커스터마이징한 PDF Parser AI 서비스. |
| [**nihalxkumar/arch-mcp**](https://github.com/nihalxkumar/arch-mcp) | Arch Wiki, AUR 및 공식 저장소로 구성된 Arch Linux 생태계를 위한 Arch Linux MCP 서버. Arch 및 비Arch 시스템에서의 AI 지원 Arch Linux 사용을 위해 Arch Wiki 및 AUR 검색, 패키지 정보 확인, 업데이트 확인, 패키지 안전 설치, PKGBUILD 분석 기능을 포함합니다. |
| [**Notifly**](https://github.com/notifly-tech/notifly-mcp-server) | AI 에이전트가 실시간으로 신뢰할 수 있는 Notifly 문서와 SDK 코드 예시를 제공하여 원활한 통합을 지원하는 Notifly MCP 서버. |
| [**Notion**](https://github.com/makenotion/notion-mcp-server#readme) | Notion API를 위한 MCP 서버 구현체. |
| [**Notion**](https://github.com/makenotion/notion-mcp-server) | Notion 공식 MCP 서버. |
| [**Notion**](https://github.com/danhilse/notion_mcp) | Notion API와 통합하여 개인 할 일 목록을 관리합니다. |
| [**Nutrient**](https://github.com/PSPDFKit/nutrient-dws-mcp-server) | 자연어를 사용하여 문서를 생성, 편집, 서명, 추출합니다. |
| [**Obsidian**](https://github.com/MarkusPfundstein/mcp-obsidian) | REST API를 통해 Obsidian과 상호작용합니다. |
| [**Obsidian Markdown Notes**](https://github.com/calclavia/mcp-obsidian) | Obsidian 볼트 또는 Markdown 노트가 있는 모든 디렉토리에서 읽기 및 검색을 수행합니다. |
| [**Obsidian Notes**](https://github.com/Piotr1215/mcp-obsidian) | 보안 우선 설계, MOC(Maps of Content) 탐색을 포함한 고급 검색 기능, obsidian.nvim 지원을 갖춘 Obsidian 볼트에 대한 직접 파일시스템 접근. Obsidian 앱이 필요하지 않습니다. |
| [**obsidian-mcp**](https://github.com/StevenStavrakis/obsidian-mcp) | (Steven Stavrakis 제작) 노트 검색, 읽기, 쓰기 및 정리를 위한 도구를 갖춘 Obsidian.md용 MCP 서버. |
| [**Office-PowerPoint-MCP-Server**](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) | Microsoft PowerPoint 문서를 생성, 읽기 및 조작하기 위한 Model Context Protocol (MCP) 서버. |
| [**Office-Visio-MCP-Server**](https://github.com/GongRzhe/Office-Visio-MCP-Server) | Microsoft Visio 문서를 생성, 읽기 및 조작하기 위한 Model Context Protocol (MCP) 서버. |
| [**Office-Word-MCP-Server**](https://github.com/GongRzhe/Office-Word-MCP-Server) | Microsoft Word 문서를 생성, 읽기 및 조작하기 위한 Model Context Protocol (MCP) 서버. |
| [**olgasafonova/mediawiki-mcp-server**](https://github.com/olgasafonova/mediawiki-mcp-server) | 모든 MediaWiki 위키(Wikipedia, Fandom, 기업 위키)에 연결합니다. 검색, 읽기, 편집, 링크 분석, 수정 이력 및 Markdown 변환을 위한 33개 이상의 도구. stdio 및 HTTP 전송을 지원합니다. |
| [**Olostep**](https://github.com/olostep/olostep-mcp-server) | 웹에서 콘텐츠를 검색, 스크래핑 및 크롤링합니다. 깔끔한 Markdown 형식의 실시간 결과를 제공합니다. |
| [**optimaquantum/claude-critical-rules-mcp**](https://github.com/optimaquantum/claude-critical-rules-mcp) | 96개의 문서화된 실패 패턴을 방지하는 Claude AI용 중요 규칙 자동 적용. MCP 도구를 통해 준수 확인 체크리스트와 규칙 요약을 제공합니다. |
| [**Outline**](https://github.com/Vortiago/mcp-outline) | Outline 지식 베이스와 상호작용하여 문서 및 콘텐츠를 검색, 읽기, 생성 및 관리하고, 컬렉션에 접근하고, 댓글을 추가하며, 문서 백링크를 관리하는 MCP 서버. |
| [**OverQuotaAI/chatterboxio-mcp-server**](https://github.com/OverQuotaAI/chatterboxio-mcp-server) | AI 에이전트가 온라인 미팅(Zoom, Google Meet)에 봇을 보내고 트랜스크립트 및 녹화를 얻을 수 있게 하는 ChatterBox.io용 MCP 서버 구현체. |
| [**PaddleOCR**](https://paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/deployment/mcp_server.html) | AI 애플리케이션에 엔터프라이즈급 OCR 및 문서 파싱 기능을 제공하는 MCP 서버. |
| [**Pandoc**](https://github.com/vivekVells/mcp-pandoc) | Pandoc을 사용한 원활한 문서 형식 변환을 위한 MCP 서버. Markdown, HTML, PDF, DOCX(.docx), CSV 등을 지원합니다. |
| [**Paubox**](https://mcp.paubox.com) | AI 에이전트가 Paubox Email API와 상호작용할 수 있게 하는 공식 MCP 서버. HITRUST 인증 완료. |
| [**PDF reader MCP**](https://github.com/gpetraroli/mcp_pdf_reader) | 로컬 PDF 파일에서 텍스트를 읽고 검색하는 MCP 서버. |
| [**PDF Tools MCP**](https://github.com/Sohaib-2/pdf-mcp-server) | 종합 PDF 조작 도구 모음 (병합, 분할, 암호화, 최적화 등). |
| [**PDFActionInspector**](https://github.com/foxitsoftware/PDFActionInspector/tree/develop) | PDF 파일에서 JavaScript Action을 추출하고 분석하는 Model Context Protocol 서버. 악성 PDF 동작, 숨겨진 스크립트 및 잠재적 위협을 탐지하는 포괄적인 보안 분석을 제공합니다. |
| [**PIF**](https://github.com/hungryrobot1/MCP-PIF) | 파일 작업, 구조화된 추론 및 저널 기반 문서화를 위한 도구를 제공하는 Personal Intelligence Framework (PIF)로, 세션 간 지속성 및 진화하는 인간-AI 협업을 지원합니다. |
| [**Plus AI**](https://plusai.com/features/mcp) | Plus AI 프레젠테이션 API를 사용하여 전문적인 PowerPoint 및 Google Slides 프레젠테이션을 자동 생성하는 Model Context Protocol (MCP) 서버. |
| [**Powertool**](https://github.com/aws-powertools/powertools-mcp) | 여러 런타임에 걸쳐 Powertools for AWS Lambda 문서의 검색 기능을 제공하는 MCP 구현체. |
| [**PSU3D0/spreadsheet-mcp**](https://github.com/PSU3D0/spreadsheet-mcp) | 영역 감지, 구조화된 읽기, 수식/스타일 검사, 포킹 메커니즘 및 재계산 기능을 갖춘 고성능, 토큰 효율적 스프레드시트 분석/편집(xlsx/xlsm). 크로스 플랫폼 지원. |
| [**Quickchat AI**](https://github.com/incentivai/quickchat-ai-mcp) | 대화형 Quickchat AI 에이전트를 MCP로 실행하여 AI 앱이 실시간으로 Knowledge Base와 대화 기능에 접근할 수 있게 합니다. |
| [**r-huijts/oorlogsbronnen-mcp**](https://github.com/r-huijts/oorlogsbronnen-mcp) | 네덜란드의 역사적 2차 세계대전 기록, 사진 및 문서(1940-1945)에 접근하기 위한 Oorlogsbronnen(전쟁 자료) API 통합. |
| [**r-huijts/opentk-mcp**](https://github.com/r-huijts/opentk-mcp) | 구조화된 검색 기능을 통해 네덜란드 의회(Tweede Kamer) 정보(문서, 토론, 활동, 입법 사례 등)에 접근합니다 (Bert Hubert의 opentk 프로젝트 기반). |
| [**Ragie**](https://github.com/ragieai/ragie-mcp-server/) | Google Drive, Notion, JIRA 등의 통합 서비스에 연결된 Ragie (RAG) 지식 베이스에서 컨텍스트를 검색합니다. |
| [**Ref**](https://github.com/ref-tools/ref-tools-mcp) | 코딩 에이전트를 위한 최신 문서. 수천 개의 공개 저장소와 사이트를 다룹니다. ref.tools에서 구축. |
| [**Rust MCP Filesystem**](https://github.com/rust-mcp-stack/rust-mcp-filesystem) | Rust의 성능을 활용하여 다양한 파일시스템 작업을 효율적으로 처리하는 빠른 비동기 MCP 서버. |
| [**sbroenne/mcp-server-excel**](https://github.com/sbroenne/mcp-server-excel) | 완전한 기능의 Excel MCP 서버. 173개 작업: Power Query, DAX, VBA, PivotTables, Tables, Charts, 범위, 서식. .xlsx 파일 생성 대신 Excel 앱을 사용하여 100% Excel 호환성 보장. Windows 전용. |
| [**scrapling-fetch**](https://github.com/cyberchitta/scrapling-fetch-mcp) | 봇 보호가 적용된 웹사이트에서 텍스트 콘텐츠에 접근합니다. Scrapling을 사용하여 자동화 방지 조치가 있는 사이트에서 HTML/Markdown을 가져옵니다. |
| [**shadcn-ui-mcp-server**](https://github.com/heilgar/shadcn-ui-mcp-server) | Shadcn UI 컴포넌트를 활용한 개발 경험을 향상시키도록 설계된 강력하고 유연한 MCP 서버로, 컴포넌트 관리, 문서화 및 설치를 위한 도구를 제공합니다. |
| [**Signoz**](https://github.com/DrDroidLab/signoz-mcp-server) | Signoz 인스턴스 관련 모니터링, 옵저버빌리티 및 디버깅 작업을 위한 Signoz API 및 문서와의 포괄적 통합. |
| [**Slidespeak**](https://github.com/SlideSpeak/slidespeak-mcp) | Slidespeak API를 사용하여 PowerPoint 프레젠테이션을 생성합니다. |
| [**Source to Knowledge Base**](https://github.com/vezlo/src-to-kb) | 소스 코드 저장소를 GPT-5를 활용한 AI 기반 검색, 지능형 청킹, OpenAI 임베딩을 통한 시맨틱 코드 이해가 가능한 검색 가능한 지식 베이스로 변환합니다. |
| [**SparkSheets/sparksheets-mcp**](https://github.com/saikiyusuke/sparksheets-mcp) | 세션 관리, 지식 베이스, 작업 추적 및 시트 작업을 위한 AI 네이티브 협업 스프레드시트 MCP 서버. Claude Code, Cursor 및 Cline과 통합됩니다. |
| [**Starwind UI**](https://github.com/Boston343/starwind-ui-mcp/) | LLM이 Starwind UI의 오픈소스 Astro 컴포넌트를 최대한 활용할 수 있도록 관련 명령어, 문서 및 기타 정보를 제공하는 MCP. |
| [**Stitch AI**](https://github.com/StitchAI/stitch-ai-mcp/) | 메모리 공간 생성 및 검색 기능을 갖춘 AI 에이전트용 지식 관리 시스템. |
| [**Storybook**](https://github.com/storybookjs/addon-mcp) | Storybook과 상호작용하여 UI 컴포넌트 테스트 및 문서화를 자동화합니다. |
| [**suekou/mcp-notion-server**](https://github.com/suekou/mcp-notion-server) | Notion API와 상호작용합니다. |
| [**Terragrunt-Docs**](https://github.com/Excoriate/mcp-terragrunt-docs) | 항상 최신 상태의 Terragrunt 문서. |
| [**TextIn**](https://github.com/intsig-textin/textin-mcp) | TextIn API용 MCP 서버로, 문서에서 텍스트를 추출하고 OCR을 수행하며, 문서를 Markdown으로 변환하는 기능도 지원합니다. |
| [**tomohiro-owada/devrag**](https://github.com/tomohiro-owada/devrag) | Markdown 문서에 대한 시맨틱 벡터 검색을 위한 경량 로컬 RAG MCP 서버. sqlite-vec와 multilingual-e5-small 임베딩으로 토큰 소비를 40배 감소시킵니다. 디렉토리 및 파일명 패턴별 필터 검색을 지원합니다. |
| [**topskychen/tilde**](https://github.com/topskychen/tilde) | AI 에이전트의 홈 디렉토리 — 휴대 가능한 AI 아이덴티티를 위한 프라이버시 우선 MCP 서버. 한 번 설정하면 어디서나 사용할 수 있습니다. 프로필 관리, 스킬, 이력서 가져오기 및 팀 동기화를 지원합니다. |
| [**tqiqbal/mcp-confluence-server**](https://github.com/tqiqbal/mcp-confluence-server) | REST API를 통해 Confluence Data Center와 상호작용하기 위한 Model Context Protocol (MCP) 서버. |
| [**Uno Platform**](https://platform.uno/) | 에이전트와 개발자를 Uno Platform의 지식 베이스(문서, API, 모범 사례)에 연결하여 크로스 플랫폼 .NET 애플리케이션 구축을 지원합니다. |
| [**upstash/context7**](https://github.com/upstash/context7) | LLM 및 AI 코드 편집기를 위한 최신 코드 문서. |
| [**Vaadin**](https://github.com/marcushellberg/vaadin-documentation-services) | Vaadin 문서를 검색하고, 전체 문서를 가져오며, 버전 정보를 확인합니다. AI 에이전트용으로 설계되었습니다. |
| [**valado/pantheon-mcp**](https://github.com/valado/pantheon-mcp) | 작업별 에이전트 지침을 제공하는 MCP 서버. 오래된 Markdown 파일과 동기화 오버헤드가 더 이상 필요하지 않습니다. |
| [**veelenga/claude-mermaid**](https://github.com/veelenga/claude-mermaid/) | 실시간 리로드 기능을 갖춘 Claude Code용 Mermaid 다이어그램 렌더링 MCP 서버. 다중 내보내기 형식(SVG, PNG, PDF) 및 테마를 지원합니다. |
| [**VictoriaLogs**](https://github.com/VictoriaMetrics-Community/mcp-victorialogs) | VictoriaLogs 인스턴스 관련 로그 작업 및 디버깅 작업을 위한 VictoriaLogs API 및 문서 통합. |
| [**VictoriaMetrics**](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) | VictoriaMetrics 인스턴스 관련 모니터링, 옵저버빌리티 및 디버깅 작업을 위한 VictoriaMetrics API 및 문서의 포괄적 통합. |
| [**VictoriaTraces**](https://github.com/VictoriaMetrics-Community/mcp-victoriatraces) | VictoriaTraces 인스턴스 관련 분산 트레이싱 및 디버깅 작업을 위한 VictoriaTraces API 및 문서 통합. |
| [**VisionAgent MCP**](https://github.com/landing-ai/vision-agent-mcp) | LLM이 이미지, 비디오 및 문서를 더 잘 추론할 수 있게 하는 간단한 MCP 서버. |
| [**Wikidata MCP**](https://github.com/zzaebok/mcp-wikidata) | Wikidata와 상호작용하는 Wikidata MCP 서버로, 식별자 검색, 메타데이터 추출 및 SPARQL 쿼리 실행을 지원합니다. |
| [**Wikipedia MCP**](https://github.com/Rudra-ravi/wikipedia-mcp) | AI 기반 정보 검색을 위해 MCP를 통해 Wikipedia 문서에 접근하고 검색합니다. |
| [**Xcode**](https://github.com/r-huijts/xcode-mcp-server) | Xcode 프로젝트에 AI를 도입하여 지능형 코드 어시스턴스, 파일 작업, 프로젝트 관리 및 자동화된 개발 작업을 가능하게 하는 MCP 서버. |
| [**XMind**](https://github.com/apeyroux/mcp-xmind) | XMind 파일이 포함된 XMind 디렉토리를 읽고 검색합니다. |
| [**ZettelkastenSpace**](https://github.com/joshylchen/zettelkasten_space) | 검증된 Zettelkasten 방법론을 기반으로 구축되었으며, Model Context Protocol을 통한 Claude Desktop 통합이 강화되었습니다. |
| [**ztuskes/garmin-documentation-mcp-server**](https://github.com/ztuskes/garmin-documentation-mcp-server) | 포괄적인 검색 및 API 예시를 포함한 오프라인 Garmin Connect IQ SDK 문서. |
| [**ztxtxwd/open-feishu-mcp-server**](https://github.com/ztxtxwd/open-feishu-mcp-server) | 내장된 Feishu OAuth 인증을 갖춘 Model Context Protocol (MCP) 서버로, 원격 연결을 지원하며 블록 생성, 콘텐츠 업데이트, 고급 기능을 포함한 포괄적인 Feishu 문서 관리 도구를 제공합니다. |

---

## 🎨 디자인 & UI

> Figma, Canva 등 디자인 도구 및 UI 컴포넌트

| 서버 | 설명 |
|------|------|
| [**21st.dev Magic**](https://github.com/21st-dev/magic-mcp) | 21st.dev 최고의 디자인 엔지니어에게 영감을 받은 정교한 UI 컴포넌트를 생성합니다. |
| [**Anki**](https://github.com/nietus/anki-mcp) | Anki 및 AnkiConnect와 함께 로컬에서 실행하는 MCP 서버입니다. 카드와 덱의 생성, 수정, 검색, 필터링을 지원하며 대량 업데이트 등 고급 도구도 포함합니다. |
| [**AnkiConnect**](https://github.com/spacholski1225/anki-connect-mcp) | AnkiConnect를 통해 Anki와 상호작용하는 MCP 서버입니다. |
| [**Canva**](https://www.canva.dev/docs/apps/mcp-server/) | Canva 앱 및 통합을 위한 AI 기반 개발 지원을 제공합니다. |
| [**dannote/figma-use**](https://github.com/dannote/figma-use) | Figma 완전 제어: 도형, 텍스트, 컴포넌트 생성, 스타일 설정, Auto-layout, 변수, 내보내기 등 80개 이상의 도구를 제공합니다. |
| [**Figma**](https://github.com/GLips/Figma-Context-MCP) | 코딩 에이전트에게 Figma 파일 데이터에 대한 직접 접근을 제공하여 디자인 구현을 한 번에 완성할 수 있도록 지원합니다. |
| [**Figma**](https://github.com/paulvandermeijs/figma-mcp) | Figma 디자인 파일을 읽고 내보내는 초고속 MCP 서버입니다. |
| [**Figma to Flutter**](https://github.com/mhmzdev/figma-flutter-mcp) | Figma 디자인 토큰과 풍부한 노드 데이터를 Flutter 용어로 변환하여 깔끔하고 우수한 Flutter 코드를 작성합니다. |
| [**freema/mcp-design-system-extractor**](https://github.com/freema/mcp-design-system-extractor) | Storybook 디자인 시스템에서 컴포넌트 정보를 추출합니다. AI 기반 디자인 시스템 분석을 위한 HTML, 스타일, props, 의존성, 테마 토큰, 컴포넌트 메타데이터를 제공합니다. |
| [**Osseni94/oyemi-mcp**](https://github.com/Osseni94/oyemi-mcp) | 145K+ 단어 사전을 활용한 결정론적 시맨틱 단어 인코딩 및 감정/정서 분석 도구입니다. 런타임 NLP 의존성 없이 단어-코드 매핑, 시맨틱 유사도, 동의어/반의어 조회를 제공합니다. |
| [**PlayCanvas**](https://github.com/playcanvas/editor-mcp-server) | PlayCanvas Editor로 인터랙티브 3D 웹 앱을 생성합니다. |
| [**shadcn/studio MCP**](https://shadcnstudio.com/mcp) | shadcn/studio MCP Server를 즐겨 사용하는 IDE에 직접 통합하여 shadcn/studio에서 영감을 받은 멋진 shadcn/ui 컴포넌트, 블록, 페이지를 제작합니다. |
| [**softvoyagers/ogforge-api**](https://github.com/softvoyagers/ogforge-api) | 테마, Lucide 아이콘, 커스텀 레이아웃을 지원하는 무료 Open Graph 이미지 생성 API입니다. API 키가 필요하지 않습니다. |
| [**Talk To Figma**](https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp) | LLM이 Figma와 상호작용하여 디자인을 프로그래밍 방식으로 읽고 수정할 수 있게 하는 MCP 서버입니다. |
| [**Talk To Figma via Claude**](https://github.com/gaganmanku96/talk-with-figma-claude) | Claude Desktop 전용 원활한 Figma 통합을 제공하는 MCP 서버로, 자연어 명령을 통한 디자인 생성, 수정 및 실시간 협업을 지원합니다. |
| [**ujisati/anki-mcp**](https://github.com/ujisati/anki-mcp) | AnkiConnect와 MCP를 활용하여 Anki 컬렉션을 관리합니다. |
| [**V0v1kkk/DotNetMetadataMcpServer**](https://github.com/V0v1kkk/DotNetMetadataMcpServer) | 어셈블리 탐색, 네임스페이스 검색, 타입 리플렉션, NuGet 통합을 포함하여 .NET 프로젝트의 상세한 타입 정보를 AI 에이전트에게 제공합니다. |
| [**VeyraX**](https://github.com/VeyraX/veyrax-mcp) | 100개 이상의 API 통합과 UI 컴포넌트를 하나의 도구로 제어합니다. |

---

## 💬 커뮤니케이션

> Slack, Discord, 이메일 등 메시징 및 알림

| 서버 | 설명 |
|------|------|
| [**ActionKit by Paragon**](https://github.com/useparagon/paragon-mcp) | Paragon의 ActionKit API를 통해 130개 이상의 SaaS 통합(예: Slack, Salesforce, Gmail)에 연결합니다. |
| [**alexey-pelykh/lhremote**](https://github.com/alexey-pelykh/lhremote) | LinkedHelper 자동화를 위한 오픈소스 CLI 및 MCP 서버 — Chrome DevTools Protocol을 통한 캠페인 관리, 메시징, 프로필 쿼리를 위한 32개 도구. |
| [**Cactusinhand/mcp_server_notify**](https://github.com/Cactusinhand/mcp_server_notify) | 에이전트 작업이 완료되면 효과음과 함께 데스크톱 알림을 전송하는 MCP 서버. |
| [**Carbon Voice**](https://github.com/PhononX/cv-mcp-server) | AI 에이전트를 Carbon Voice에 연결하는 MCP 서버. Carbon Voice에서 음성 메시지, 대화, 다이렉트 메시지, 폴더, 음성 메모, AI 액션 등을 생성, 관리 및 상호작용합니다. |
| [**chatmcp/mcp-server-chatsum**](https://github.com/chatmcp/mcp-server-chatsum) | AI 프롬프트를 사용하여 채팅 메시지를 쿼리하고 요약합니다. |
| [**ChatSum**](https://github.com/mcpso/mcp-server-chatsum) | LLM을 사용하여 채팅 메시지를 쿼리하고 요약합니다. mcpso 제작. |
| [**ClaudePost**](https://github.com/ZilongXue/claude-post) | ClaudePost는 Gmail에 대한 원활한 이메일 관리를 가능하게 하며, 이메일 검색, 읽기 및 전송과 같은 보안 기능을 제공합니다. |
| [**ClickSend**](https://github.com/ClickSend/clicksend-mcp-server/) | ClickSend 팀이 개발한 공식 ClickSend MCP 서버. |
| [**codefuturist/email-mcp**](https://github.com/codefuturist/email-mcp) | 여러 계정에서 이메일 읽기, 검색, 전송, 예약 및 관리를 위한 42개 도구를 갖춘 IMAP/SMTP 이메일 MCP 서버. IMAP IDLE 푸시, AI 분류, 데스크톱 알림을 지원하며 Gmail, Outlook, iCloud 등의 프로바이더를 자동 감지합니다. |
| [**Coreflux MQTT**](https://github.com/CorefluxCommunity/CorefluxMCPServer) | Coreflux MQTT 브로커용 MCP 서버로, AI 에이전트가 브로커를 자동화 허브로 전환하고 MQTT 프로토콜을 통해 IoT 기기 및 메시징 시스템과 상호작용할 수 있게 합니다. |
| [**Coresignal**](https://github.com/Coresignal-com/coresignal-mcp/) | LLM 및 AI 워크플로우를 위한 기업, 직원 및 채용 공고에 관한 종합 B2B 데이터에 접근합니다. |
| [**Courier**](https://www.courier.com/docs/tools/mcp) | 이메일, SMS, 푸시, Slack 및 Microsoft Teams를 통해 멀티채널 알림을 구축, 업데이트 및 전송합니다. |
| [**CRASH**](https://github.com/nikkoxgonzales/crash-mcp) | 유연한 검증, 신뢰도 추적, 수정 메커니즘 및 분기 지원을 갖춘 구조화된 반복적 추론 및 사고를 위한 MCP 서버. |
| [**Discord**](https://github.com/v-3/discordmcp) | 봇을 통해 Discord 길드에 연결하고 채널에서 메시지를 읽고 쓰는 MCP 서버. |
| [**Discord**](https://github.com/SaseQ/discord-mcp) | 봇을 통해 Discord에 연결하고 Discord와의 포괄적인 통합을 제공하는 MCP 서버. |
| [**Discord**](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/discord) | Klavis AI의 Discord API 통합. |
| [**eechat**](https://github.com/Lucassssss/eechat) | Linux, macOS, Windows에서 MCP 서버에 원활하게 연결하는 오픈소스 크로스 플랫폼 데스크톱 애플리케이션. |
| [**Email**](https://github.com/Shy2593666979/mcp-server-email) | Gmail, Outlook, Yahoo, Sina, Sohu, 126, 163, QQ Mail 등 다양한 이메일 공급자를 통해 이메일을 전송할 수 있는 서버. 지정된 디렉토리에서 파일 첨부도 지원합니다. |
| [**Email SMTP**](https://github.com/egyptianego17/email-mcp-server) | AI 에이전트가 SMTP를 통해 이메일을 보내고 파일을 첨부할 수 있게 하는 간단한 MCP 서버. |
| [**Facebook Ads Library**](https://github.com/trypeggy/facebook-ads-library-mcp) | Facebook Ads Library에서 모든 답변을 얻고, 메시징, 크리에이티브 테스트 및 비교를 포함한 심층 리서치를 몇 초 내에 수행합니다. |
| [**FastAlertNow/mcp-server**](https://github.com/FastAlertNow/mcp-server) | FastAlert 공식 Model Context Protocol (MCP) 서버. AI 에이전트(Claude, ChatGPT, Cursor 등)가 채널 목록을 조회하고 FastAlert API를 통해 직접 알림을 전송할 수 있게 합니다. |
| [**giuseppe-coco/Google-Workspace-MCP-Server**](https://github.com/giuseppe-coco/Google-Workspace-MCP-Server) | Google Calendar, Gmail, Drive 등과 원활하게 상호작용하는 MCP 서버. |
| [**Gmail**](https://github.com/GongRzhe/Gmail-MCP-Server) | 자동 인증 지원이 포함된 Claude Desktop에서의 Gmail 통합을 위한 Model Context Protocol (MCP) 서버. |
| [**Gmail**](https://github.com/Ayush-k-Shukla/gmail-mcp-server) | OAuth 2.0을 지원하는 모든 기본 작업을 갖춘 간단한 Gmail MCP 서버. |
| [**Gmail Headless**](https://github.com/baryhuang/mcp-headless-gmail) | 로컬 자격 증명이나 파일 시스템 설정 없이 Gmail 메시지를 가져오고 보낼 수 있는 원격 호스팅 가능한 MCP 서버. |
| [**Gmail MCP**](https://github.com/gangradeamitesh/mcp-google-email) | Gmail API를 통한 이메일 전송, 수신 및 관리 기능을 제공하는 MCP (Model Context Protocol)를 사용한 Gmail 서비스 구현체. |
| [**Google Workspace**](https://github.com/taylorwilsdon/google_workspace_mcp) | Streamable HTTP 또는 SSE 전송을 통한 Calendar, Drive, Gmail, Docs의 완전한 지원을 갖춘 종합 Google Workspace MCP. |
| [**Graphlit**](https://github.com/graphlit/graphlit-mcp-server) | Slack, Gmail, 팟캐스트 피드 등 다양한 소스의 콘텐츠를 웹 크롤링과 함께 검색 가능한 Graphlit 프로젝트로 수집합니다. |
| [**IMAP MCP**](https://github.com/dominik1001/imap-mcp) | AI 어시스턴트를 위한 도구로 IMAP 작업을 노출하는 IMAP Model Context Protocol (MCP) 서버. |
| [**Infobip**](https://github.com/infobip/mcp) | Infobip 글로벌 클라우드 커뮤니케이션 플랫폼을 통합하는 MCP 서버. AI 에이전트에게 커뮤니케이션 능력을 부여하여 SMS 및 RCS 메시지 송수신, WhatsApp 상호작용 등을 가능하게 합니다. |
| [**jaspertvdm/mcp-server-rabel**](https://github.com/jaspertvdm/mcp-server-rabel) | I-Poll 프로토콜 및 AInternet을 통한 AI 간 메시징. .aint 도메인, 시맨틱 메시징, 신뢰 기반 라우팅을 사용하여 에이전트 간 통신을 가능하게 합니다. |
| [**jtalk22/slack-mcp-server**](https://github.com/jtalk22/slack-mcp-server) | Claude를 위한 완전한 Slack 컨텍스트 — DM, 채널, 스레드, 검색. OAuth 앱 불필요, 관리자 승인 불필요. `--setup`으로 완료, 11개 도구, 자동 갱신. |
| [**khan2a/telephony-mcp-server**](https://github.com/khan2a/telephony-mcp-server) | 음성 통화를 Speech-to-Text 및 음성 인식으로 자동화하여 통화 내용을 요약하는 MCP 전화 서버. SMS 송수신, 음성사서함 감지, 고급 전화 워크플로우를 위한 Vonage API 통합을 지원합니다. |
| [**Knock MCP Server**](https://github.com/knocklabs/agent-toolkit#model-context-protocol-mcp) | 이메일, 인앱, 푸시, SMS, Slack, MS Teams를 통해 제품 및 고객 메시징을 전송합니다. |
| [**kunallunia/twitter-mcp**](https://github.com/LuniaKunal/mcp-twitter) | 타임라인 접근, 사용자 트윗 검색, 해시태그 모니터링, 대화 분석, 다이렉트 메시징, 게시물 감성 분석 및 완전한 게시물 라이프사이클 제어를 제공하는 올인원 Twitter 관리 솔루션 — 모두 간소화된 API를 통해 제공됩니다. |
| [**kweenkl**](https://github.com/antoinedelorme/kweenkl-mcp) | 자연어를 사용하여 AI 어시스턴트에서 푸시 알림을 전송합니다. 예시 웹훅 토큰을 포함한 사전 출시 데모가 제공됩니다. |
| [**LINE**](https://github.com/line/line-bot-mcp-server) | LINE Messaging API를 통합하여 AI 에이전트를 LINE 공식 계정에 연결합니다. |
| [**Mailchimp MCP**](https://github.com/AgentX-ai/mailchimp-mcp) | AI 에이전트가 Mailchimp API와 상호작용할 수 있게 합니다 (읽기 전용). |
| [**Mailgun**](https://github.com/mailgun/mailgun-mcp-server) | Mailgun API와 상호작용합니다. |
| [**MailNet**](https://github.com/Astroa7m/MailNet-MCP-Server) | 에이전트 오케스트레이션, 자동 토큰 갱신, 새 프로바이더를 위한 표준화된 기본 클래스, 톤/서명/스레드를 위한 전용 이메일 설정 엔드포인트를 갖춘 통합 Gmail + Outlook MCP 서버. |
| [**MailSandbox**](https://github.com/btafoya/mailsandbox) | MailSandbox(Mailpit의 포크)는 웹 UI, SMTP 서버, Postmark API 에뮬레이션 및 AI 지원 디버깅을 위한 MCP 서버를 갖춘 빠르고 무의존성 이메일 테스트 도구 및 API입니다. |
| [**MarkusPfundstein/mcp-gsuite**](https://github.com/MarkusPfundstein/mcp-gsuite) | Gmail 및 Google Calendar와의 통합. |
| [**marlinjai/email-mcp**](https://github.com/marlinjai/email-mcp) | Gmail(REST API), Outlook(Microsoft Graph), iCloud 및 일반 IMAP/SMTP를 지원하는 통합 이메일 MCP 서버. 이메일 검색, 전송, 정리 및 일괄 관리를 위한 24개 도구와 내장 OAuth2 및 암호화된 자격 증명 저장소를 제공합니다. |
| [**Matrix**](https://github.com/mjknowles/matrix-mcp-server) | Matrix 홈서버와 상호작용합니다. |
| [**Microsoft 365**](https://github.com/softeria/ms-365-mcp-server) | Graph API를 사용하여 Microsoft Office 및 전체 Microsoft 365 제품군(Outlook/메일, 파일, Excel, 캘린더 포함)에 연결하는 MCP 서버. |
| [**Microsoft 365**](https://github.com/pnp/cli-microsoft365-mcp-server) | Entra ID, OneDrive, OneNote, Outlook, Planner, Power Apps, Power Automate, Power Platform, SharePoint Embedded 등 Microsoft 365의 다양한 영역을 관리할 수 있는 단일 MCP 서버. |
| [**Microsoft Teams**](https://devblogs.microsoft.com/microsoft365dev/announcing-the-updated-teams-ai-library-and-mcp-support/) | MCP 지원이 포함된 공식 Microsoft Teams AI Library로, 고급 에이전트 오케스트레이션, 멀티에이전트 협업 및 Teams 메시징 및 협업 기능과의 원활한 통합을 가능하게 합니다. |
| [**Microsoft Teams**](https://github.com/InditexTech/mcp-teams-server) | Microsoft Teams 메시징(읽기, 게시, 멘션, 멤버 및 스레드 목록)을 통합하는 MCP 서버. |
| [**MintMCP**](https://github.com/mintmcp/servers) | Google Calendar, Gmail, Outlook Calendar 및 Outlook을 위한 MCP 서버. |
| [**muammar-yacoob/GMail-Manager-MCP**](https://github.com/muammar-yacoob/GMail-Manager-MCP#readme) | Claude Desktop을 Gmail에 연결하여 자연어로 받은 편지함을 관리합니다. 프로모션 및 뉴스레터 일괄 삭제, 라벨 정리 및 유용한 인사이트를 얻을 수 있습니다. |
| [**nckhemanth0/subscription-tracker-mcp**](https://github.com/nckhemanth0/subscription-tracker-mcp) | Gmail + MySQL 통합을 통한 지능형 구독 관리용 MCP 서버. |
| [**NodeCodeStudio**](https://nodecodestudio.com) | MCP 서비스(Gmail, Calendar, WordPress 등)를 활성화하고 가져오기 가능한 시퀀스를 갖춘 Chrome 확장 프로그램을 통해 브라우저 자동화 워크플로우를 실행합니다. |
| [**Ntfy**](https://github.com/gitmotion/ntfy-me-mcp) | AI 에이전트에서 자체 호스팅된 ntfy 서버로 ntfy 알림을 전송/가져오기 위한 ntfy MCP 서버 (보안 토큰 인증 등 지원 - npx 또는 Docker로 사용 가능!) |
| [**PlainSignal**](https://github.com/plainsignal/plainsignal-mcp) | PlainSignal API에 연결하여 대화형 AI에서 실시간 웹사이트 분석 데이터를 쿼리하는 공식 MCP 서버. |
| [**Pushover**](https://github.com/ashiknesin/pushover-mcp) | Pushover.net을 사용하여 기기에 즉시 알림을 전송합니다. |
| [**Resend**](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/resend) | Resend 서비스를 사용하여 이메일을 전송합니다. |
| [**Root Signals**](https://github.com/root-signals/root-signals-mcp) | LLM-as-Judge를 사용한 평가로 출력물을 개선하고 품질을 제어합니다. |
| [**Rube**](https://github.com/ComposioHQ/Rube) | AI 도구를 Gmail, Slack, GitHub, Notion 등 500개 이상의 앱에 연결하는 Model Context Protocol (MCP) 서버. AI 클라이언트에 설치하고 앱에 한 번 인증하면 사용할 수 있습니다. |
| [**Rube**](https://rube.composio.dev) | AI 도구를 Gmail, Slack, GitHub, Notion 등 500개 이상의 앱에 연결하는 Model Context Protocol (MCP) 서버. AI 클라이언트에 설치하고 앱에 한 번 인증하면 사용할 수 있습니다. |
| [**SendGrid**](https://github.com/recepyavuz0/sendgrid-mcp-server) | SendGrid API와 통합하여 AI 어시스턴트(Claude, ChatGPT 등)가 이메일을 전송하고, 템플릿을 관리하며, 이메일 통계를 추적할 수 있게 하는 MCP 서버. |
| [**Slack**](https://github.com/korotovsky/slack-mcp-server) | Slack 워크스페이스를 위한 가장 강력한 MCP 서버. Stdio 및 SSE 전송, 프록시 설정을 지원하며 워크스페이스에서 권한이나 봇 생성/승인이 필요하지 않습니다. |
| [**Slack**](https://github.com/zencoderai/slack-mcp-server) | stdio 및 Streamable HTTP 전송을 모두 지원하는 Slack MCP 서버. 현재 아카이브된 Anthropic의 원래 구현체에서 확장되었습니다. |
| [**TeamSafeAI/LIFE**](https://github.com/TeamSafeAI/LIFE) | AI 에이전트를 위한 영구 아이덴티티 아키텍처. 드라이브, 감정 관계, 감쇠를 포함한 시맨틱 메모리, 작업 스레드, 학습 패턴, 저널, 제네시스(아이덴티티 발견), 창의적 충돌 엔진, 예측, 음성을 포함하는 16개 MCP 서버. Python 3.8 이상 외 추가 의존성 없음. 938개의 대화를 통해 구축되었습니다. |
| [**teddyzxcv/ntfy-mcp**](https://github.com/teddyzxcv/ntfy-mcp) | ntfy를 사용하여 휴대폰에 알림을 전송하여 사용자에게 정보를 제공하는 MCP 서버. |
| [**Telegram**](https://github.com/chigwell/telegram-mcp) | Telethon 통합을 통해 Telegram의 페이지네이션 채팅 읽기, 메시지 검색 및 메시지 전송 기능을 제공하는 MCP 서버. |
| [**Telegram-Client**](https://github.com/chaindead/telegram-mcp) | 원활한 상호작용을 위해 사용자 데이터, 대화, 메시지, 임시 보관, 읽음 상태 등을 관리하는 Telegram API 브릿지. |
| [**Telegram-mcp-server**](https://github.com/DLHellMe/telegram-mcp-server) | Claude에서 직접 Telegram 채널 및 그룹에 접근합니다. API 접근(100배 빠름) 또는 웹 스크래핑의 이중 모드 작동, 무제한 게시물 검색 및 검색 기능을 제공합니다. |
| [**Telnyx**](https://github.com/team-telnyx/telnyx-mcp-server) | AI 기반 커뮤니케이션 앱 구축을 위한 공식 MCP 서버. 음성 어시스턴트 생성, SMS 캠페인 전송, 전화번호 관리, 엔터프라이즈급 신뢰성을 갖춘 실시간 메시징 통합을 지원합니다. |
| [**trycourier/courier-mcp**](https://github.com/trycourier/courier-mcp) | AI 코딩 공간을 떠나지 않고 제품에 멀티채널 알림을 구축하고, 메시지를 전송하고, 목록을 업데이트하고, 자동화를 실행합니다. |
| [**Twilio**](https://github.com/twilio-labs/mcp) | Twilio API와 상호작용하여 SMS 메시지 전송, 전화번호 관리, 계정 설정 등을 수행합니다. |
| [**vakharwalad23/google-mcp**](https://github.com/vakharwalad23/google-mcp) | OAuth 관리, 자동 토큰 갱신 및 자동 재인증 기능을 갖춘 MCP용 Google 네이티브 도구 모음(Gmail, Calendar, Drive, Tasks). |
| [**Webex**](https://github.com/Kashyap-AI-ML-Solutions/webex-messaging-mcp-server) | AI 어시스턴트에게 Cisco Webex 메시징 기능에 대한 포괄적 접근을 제공하는 Model Context Protocol (MCP) 서버. |
| [**WhatsApp Business**](https://medium.com/@wassenger/introducing-whatsapp-mcp-ai-connector-3d393b52d1b0) | AI 에이전트가 메시지 전송, 대화 관리, 템플릿 접근, WhatsApp Business API 통합을 통한 자동화된 고객 커뮤니케이션을 수행할 수 있는 WhatsApp Business MCP 커넥터. |
| [**WhatsApp MCP Server**](https://github.com/lharries/whatsapp-mcp) | 개인 WhatsApp의 개인 대화, 그룹, 검색 및 전송을 처리하는 MCP 서버. |
| [**YCloud-Developers/ycloud-whatsapp-mcp-server**](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) | YCloud의 WhatsApp Business Platform을 위한 MCP 서버. |
| [**Zoom**](https://github.com/Prathamesh0901/zoom-mcp-server/tree/main) | Zoom 미팅을 생성, 업데이트, 읽기 및 삭제합니다. |
| [**zoomeye-ai/mcp_zoomeye**](https://github.com/zoomeye-ai/mcp_zoomeye) | ZoomEye MCP 서버를 통해 네트워크 자산 정보를 쿼리합니다. |

---

## 📱 소셜미디어

> Twitter, YouTube, Reddit 등 SNS 플랫폼 연동

| 서버 | 설명 |
|------|------|
| [**34892002/bilibili-mcp-js**](https://github.com/34892002/bilibili-mcp-js) | Bilibili 콘텐츠 검색을 지원하는 MCP 서버. LangChain 통합 예시 및 테스트 스크립트 포함. |
| [**agent-hanju/char-index-mcp**](https://github.com/agent-hanju/char-index-mcp) | LLM을 위한 정밀 문자 수준 문자열 인덱싱 도구. 정확한 문자 위치 기반 텍스트 검색, 추출, 조작 지원. |
| [**APISIX-MCP**](https://github.com/api7/apisix-mcp) | LLM과 APISIX Admin API를 연결하여 Apache APISIX의 모든 리소스를 조회 및 관리하는 MCP 서버. |
| [**arjun1194/insta-mcp**](https://github.com/arjun1194/insta-mcp) | Instagram 분석 및 인사이트를 제공하는 MCP 서버. 계정 개요, 게시물, 팔로워, 팔로잉, 게시물 인사이트, 사용자/해시태그/장소 검색 지원. |
| [**arxiv-latex-mcp**](https://github.com/takashiishida/arxiv-latex-mcp) | arXiv LaTeX 소스를 가져와 논문의 수학 표현식을 정확하게 해석하는 MCP 서버. |
| [**Bilibili**](https://github.com/wangshunnn/bilibili-mcp-server) | Bilibili 사용자 프로필, 동영상 메타데이터, 검색 등의 기능을 제공하는 MCP 서버. |
| [**Bluesky**](https://github.com/keturiosakys/bluesky-context-server) | Bluesky API와 연동하여 피드 및 게시물을 검색하고 조회하는 MCP 서버. |
| [**Bright-L01/networkx-mcp-server**](https://github.com/Bright-L01/networkx-mcp-server) | 최초의 NetworkX MCP 통합 서버. AI 대화에서 직접 그래프 분석 및 시각화 지원. 중심성 알고리즘, 커뮤니티 탐지, PageRank 등 13개 연산 지원. |
| [**checkra1neth/xbird**](https://github.com/checkra1neth/xbird-skill) | 34개 도구를 갖춘 Twitter/X MCP 서버. 트윗 게시, 검색, 타임라인 조회, 참여 관리, 미디어 업로드 지원. API 키 불필요, 브라우저 쿠키 사용. |
| [**code-sandbox-mcp**](https://github.com/Automata-Labs-team/code-sandbox-mcp) | Docker 컨테이너 내에서 안전한 코드 샌드박스 환경을 생성하여 코드를 실행하는 MCP 서버. |
| [**davidlin2k/pox-mcp-server**](https://github.com/davidlin2k/pox-mcp-server) | POX SDN 컨트롤러용 MCP 서버로 네트워크 제어 및 관리 기능을 제공. |
| [**dorukardahan/twitterapi-docs-mcp**](https://github.com/dorukardahan/twitterapi-docs-mcp) | TwitterAPI.io 문서를 오프라인으로 접근하는 MCP 서버. 52개 API 엔드포인트, 가이드, 가격 정보, 인증 문서 포함. |
| [**Facebook Ads**](https://github.com/gomarble-ai/facebook-ads-mcp-server) | Facebook Ads API와 연동하여 광고 데이터 접근 및 관리 기능을 제공하는 MCP 서버. |
| [**Facebook Ads 10xeR**](https://github.com/fortytwode/10xer) | 향상된 크리에이티브 인사이트, 다차원 분석, 종합 광고 성과 분석을 제공하는 고급 Facebook Ads MCP 서버. |
| [**format37/youtube_mcp**](https://github.com/format37/youtube_mcp) | YouTube 동영상을 텍스트로 변환하는 MCP 서버. yt-dlp로 오디오를 다운로드하고 OpenAI Whisper-1로 정밀 전사 수행. 긴 동영상은 청크 분할 지원. |
| [**gwbischof/bluesky-social-mcp**](https://github.com/gwbischof/bluesky-social-mcp) | atproto 클라이언트를 통해 Bluesky와 상호작용하는 MCP 서버. |
| [**gx-mcp-server**](https://github.com/davidf9999/gx-mcp-server) | Great Expectations 데이터 검증 및 품질 체크를 AI 에이전트용 MCP 도구로 제공하는 서버. |
| [**HagaiHen/facebook-mcp-server**](https://github.com/HagaiHen/facebook-mcp-server) | Facebook Pages와 Graph API를 통해 게시물, 댓글, 참여 지표를 직접 관리하는 MCP 서버. |
| [**HDW LinkedIn**](https://github.com/horizondatawave/hdw-mcp-server) | HorizonDataWave.ai를 통해 LinkedIn 프로필 데이터 접근 및 사용자 계정 관리를 제공하는 MCP 서버. |
| [**hechtcarmel/jetbrains-index-mcp-plugin**](https://github.com/hechtcarmel/jetbrains-index-mcp-plugin) | JetBrains IDE 플러그인으로 AI 코딩 어시스턴트가 IDE의 인덱싱 및 리팩토링 기능(이름 변경, 참조 찾기, 호출 계층 등)을 활용할 수 있게 하는 MCP 서버. |
| [**imprvhub/mcp-claude-hackernews**](https://github.com/imprvhub/mcp-claude-hackernews) | Claude Desktop에서 Hacker News와 상호작용할 수 있게 하는 MCP 통합 서버. |
| [**Instagram DM**](https://github.com/trypeggy/instagram_dm_mcp) | LLM을 통해 Instagram DM을 전송할 수 있는 MCP 서버. |
| [**kambriso/fritzbox-mcp-server**](https://github.com/kambriso/fritzbox-mcp-server) | AVM FRITZ!Box 라우터를 제어하는 MCP 서버. 장치 관리, WiFi, 네트워크 설정, 자녀 보호, 시간 지연 작업 예약 지원. |
| [**karanb192/reddit-mcp-buddy**](https://github.com/karanb192/reddit-mcp-buddy) | API 키 없이 Reddit 게시물 탐색, 콘텐츠 검색, 사용자 활동 분석을 수행하는 MCP 서버. Claude Desktop 즉시 사용 가능. |
| [**kimtaeyoon83/mcp-server-youtube-transcript**](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | AI 분석을 위해 YouTube 자막 및 트랜스크립트를 가져오는 MCP 서버. |
| [**king-of-the-grackles/reddit-research-mcp**](https://github.com/king-of-the-grackles/reddit-research-mcp) | AI 기반 Reddit 인텔리전스 서버. 20,000개 이상 커뮤니티에서 시맨틱 검색으로 서브레딧 발견, 게시물/댓글 인용 가져오기, 리서치 피드 관리 지원. |
| [**kukapay/twitter-username-changes-mcp**](https://github.com/kukapay/twitter-username-changes-mcp) | Twitter 사용자명의 변경 이력을 추적하는 MCP 서버. |
| [**LinkedIn MCP Runner**](https://github.com/ertiqah/linkedin-mcp-runner) | ChatGPT과 Claude에서 LiGo를 통해 LinkedIn 게시물을 작성, 편집, 예약할 수 있는 MCP 서버. |
| [**Mattbusel/Reddit-Options-Trader-ROT-**](https://github.com/Mattbusel/Reddit-Options-Trader-ROT-) | 최초의 금융 인텔리전스 MCP 서버. Reddit, SEC 공시, FDA 승인, 의회 거래 등 15개 이상 소스에서 실시간 AI 기반 트레이딩 시그널 제공. |
| [**mcp-youtube-extract**](https://github.com/sinjab/mcp_youtube_extract) | YouTube 동영상 정보 및 자막을 지능형 폴백 로직으로 추출하는 MCP 서버. 포괄적인 로깅 및 오류 처리 지원. |
| [**Meta Ads Remote MCP**](https://github.com/pipeboard-co/meta-ads-mcp) | Meta Ads API와 연동하여 Facebook, Instagram 등 Meta 플랫폼 광고 캠페인을 접근, 분석, 관리하는 원격 MCP 서버. |
| [**Metricool MCP**](https://github.com/metricool/mcp-metricool) | Metricool 소셜 미디어 분석 플랫폼과 연동하여 Instagram, Facebook, Twitter 등의 성과 지표 조회 및 콘텐츠 예약을 지원하는 MCP 서버. |
| [**mpeirone/zabbix-mcp-server**](https://github.com/mpeirone/zabbix-mcp-server) | Zabbix 호스트, 아이템, 트리거, 템플릿, 문제, 데이터 등과 연동하는 MCP 서버. |
| [**OKX-MCP-Server**](https://github.com/memetus/okx-mcp-playground) | OKX API를 통해 블록체인 데이터 및 시장 가격 데이터를 제공하는 MCP 서버. 자산 가격, 거래 데이터, 계정 히스토리 조회 지원. |
| [**PostIdentity**](https://github.com/PostIdentity/mcp-server) | AI 어시스턴트에서 소셜 미디어 게시물을 생성하는 MCP 서버. ID 관리, 게시물 작성, 추천 추적, 마켓플레이스 템플릿 탐색 지원. |
| [**profullstack/mcp-server**](https://github.com/profullstack/mcp-server) | SEO 최적화, 문서 변환, 도메인 조회, 이메일 검증, QR 생성, 날씨, 소셜 미디어 게시, 보안 스캔 등 20개 이상 도구를 통합한 MCP 서버. |
| [**pskill9/hn-server**](https://github.com/pskill9/hn-server) | Hacker News의 HTML 콘텐츠를 파싱하여 다양한 유형의 스토리(top, new, ask, show, jobs)를 구조화된 데이터로 제공합니다. |
| [**Regenerating-World/pix-mcp**](https://github.com/Regenerating-World/pix-mcp) | 브라질 즉시결제(Pix)용 QR 코드 및 복사-붙여넣기 문자열을 다중 프로바이더(Efi, Cielo 등) 폴백으로 생성하는 MCP 서버. |
| [**scrape-badger/scrapebadger-mcp**](https://github.com/scrape-badger/scrapebadger-mcp) | ScrapeBadger API를 통해 Twitter/X 사용자 프로필, 트윗, 팔로워, 트렌드, 리스트, 커뮤니티 데이터를 접근하는 MCP 서버. |
| [**shensi8312/blogburst-mcp-server**](https://github.com/shensi8312/blogburst-mcp-server) | BlogBurst로 AI 콘텐츠 생성, 재가공, 9개 이상 플랫폼(Twitter, LinkedIn, Reddit, Bluesky 등) 멀티 플랫폼 게시를 지원하는 MCP 서버. |
| [**simonpainter/netbox-mcp**](https://github.com/simonpainter/netbox-mcp) | NetBox API와 상호작용하는 MCP 서버. |
| [**sinanefeozler/reddit-summarizer-mcp**](https://github.com/sinanefeozler/reddit-summarizer-mcp) | 사용자의 Reddit 홈페이지 또는 특정 서브레딧을 게시물과 댓글 기반으로 요약하는 MCP 서버. |
| [**TikTok**](https://github.com/Seym0n/tiktok-mcp) | TikTok 게시물 상세 정보 및 동영상 자막을 가져오는 MCP 서버. |
| [**TikTok Ads**](https://github.com/AdsMCP/tiktok-ads-mcp-server) | TikTok 광고 플랫폼과 연동하여 캠페인 관리, 성과 분석, 타겟팅, 크리에이티브 관리, 커스텀 리포팅을 지원하는 MCP 서버. |
| [**urlbox/urlbox-mcp-server**](https://github.com/urlbox/urlbox-mcp-server/) | Urlbox API를 통해 스크린샷, PDF, 동영상 생성, AI 기반 스크린샷 분석, 웹 콘텐츠(Markdown, 메타데이터, HTML) 추출을 지원하는 MCP 서버. |
| [**Virtual location (Google Street View,etc.)**](https://github.com/mfukushim/map-traveler-mcp) | Google Map, Street View, PixAI, Stability.ai, ComfyUI API, Bluesky를 통합하여 LLM에서 가상 위치 시뮬레이션을 제공하는 MCP 서버. |
| [**X (Twitter)**](https://github.com/mbelinky/x-mcp-server) | OAuth 2.0, v2 API 미디어 업로드, v1.1 폴백, 종합 Rate Limiting을 지원하는 Twitter/X MCP 서버. 텍스트/미디어 트윗 게시, 검색, 삭제 지원. |
| [**xspadex/bilibili-mcp**](https://github.com/xspadex/bilibili-mcp.git) | FastMCP 기반으로 Bilibili 인기 동영상을 가져와 표준 MCP 인터페이스로 제공하는 도구. |
| [**YouTube**](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/youtube) | YouTube 동영상 정보를 추출하는 MCP 서버. 프록시 지원. |
| [**YouTube**](https://github.com/ZubeidHendricks/youtube-mcp-server) | YouTube API 종합 연동으로 동영상 관리, Shorts 생성, 분석을 지원하는 MCP 서버. |
| [**YouTube**](https://github.com/anaisbetts/mcp-youtube) | YouTube 자막을 가져오는 MCP 서버. |
| [**YouTube DLP**](https://github.com/AgentX-ai/youtube-dlp-server) | 프록시를 지원하여 동영상 정보, 자막, 상위 댓글을 가져오는 MCP 서버. |
| [**YouTube MCP**](https://github.com/aardeshir/youtube-mcp) | OAuth2로 노래 목록에서 플레이리스트를 생성하는 MCP 서버. 동영상 검색, 플레이리스트 관리, AI 큐레이션 지원. |
| [**Youtube Uploader MCP**](https://github.com/anwerj/youtube-uploader-mcp) | CLI나 YouTube Studio 없이 AI 기반으로 YouTube에 동영상을 업로드하는 MCP 서버. |
| [**YouTube Video Summarizer**](https://github.com/nabid-pf/youtube-video-summarizer-mcp) | 긴 YouTube 동영상을 요약하는 MCP 서버. |
| [**zlatkoc/youtube-summarize**](https://github.com/zlatkoc/youtube-summarize) | YouTube 동영상 자막을 가져와 선택적으로 요약하는 MCP 서버. 다중 자막 포맷(텍스트, JSON, SRT, WebVTT), 다국어 지원. |

---

## 🎮 미디어 & 엔터테인먼트

> Spotify, Blender, 게임 등 미디어/엔터테인먼트

| 서버 | 설명 |
|------|------|
| [**1000ri-jp/atsurae**](https://github.com/1000ri-jp/atsurae) | AI 기반 영상 편집 MCP 서버. 타임라인 편집, 5레이어 합성, 시맨틱 연산, FFmpeg 렌더링(1920x1080, 30fps H.264+AAC) 등 10개 도구 제공. |
| [**ahujasid/blender-mcp**](https://github.com/ahujasid/blender-mcp) | Blender와 연동하는 MCP 서버. |
| [**AltTester®**](https://alttester.com/docs/desktop/latest/pages/ai-extension.html) | AltTester® 기능으로 Unity 또는 Unreal 게임에 연결하여 테스트하는 MCP 서버. 게임 테스트 자동화를 더 빠르고 스마트하게 작성 가능. |
| [**Audioscrape**](https://www.audioscrape.com/docs/mcp) | 100만 시간 이상의 팟캐스트, 인터뷰, 강연 및 개인 오디오 업로드를 화자 식별과 타임스탬프로 검색하는 공식 원격 MCP 서버. |
| [**Audius**](https://github.com/glassBead-tc/audius-mcp-atris) | Claude를 통해 Audius에서 팬과 소통하고, 음악을 스트리밍하며, 아티스트에게 팁을 보내는 MCP 서버. |
| [**BGG MCP**](https://github.com/kkjdaniel/bgg-mcp) | AI 도구가 BoardGameGeek API와 상호작용할 수 있게 하는 MCP 서버. |
| [**Blender MCP**](https://github.com/pranav-deshmukh/blender-mcp) | 자연어로 Blender에서 전문적인 3D 씬을 생성하는 MCP 서버. |
| [**Bluetooth MCP Server**](https://github.com/Hypijump31/bluetooth-mcp-server) | 자연어 명령으로 Bluetooth 장치를 제어하고 연결을 관리하는 MCP 서버. 장치 탐색, 페어링, 오디오 제어 지원. |
| [**C64 Bridge**](https://github.com/chrisgleissner/c64bridge) | Commodore 64 하드웨어용 AI 명령 브릿지. REST API로 Ultimate 64 및 C64 Ultimate 장치 제어, BASIC/어셈블리 프로그램 생성, 실시간 메모리 검사, SID 오디오 합성 지원. |
| [**Chess.com**](https://github.com/pab1it0/chess-mcp) | Chess.com 플레이어 데이터, 게임 기록 등 공개 정보를 표준화된 MCP 인터페이스로 접근하는 서버. |
| [**Chessagine-mcp**](https://github.com/jalpp/chessagine-mcp) | Stockfish 엔진 평가, 포지션 테마 분석, Lichess 오프닝 데이터베이스, 체스 지식 베이스를 통합한 체스 MCP 서버. |
| [**ChessPal Chess Engine (stockfish)**](https://github.com/wilson-urdaneta/chesspal-mcp-engine) | Stockfish 기반 체스 엔진 MCP 서버. 최적 수 계산 및 HTTP/SSE, stdio 트랜스포트 지원. |
| [**Cloudbet**](https://github.com/cloudbet/sports-mcp-server) | Cloudbet API를 통해 스포츠 및 e스포츠 구조화 데이터(경기 일정, 실시간 배당, 베팅 한도, 마켓)를 제공하는 MCP 서버. |
| [**DaVinci Resolve**](https://github.com/samuelgursky/davinci-resolve-mcp) | DaVinci Resolve와 연동하여 영상 편집, 색보정, 미디어 관리, 프로젝트 제어 도구를 제공하는 MCP 서버. |
| [**ddsky/gamebrain-api-clients**](https://github.com/ddsky/gamebrain-api-clients) | GameBrain API를 통해 모든 플랫폼의 수십만 개 비디오 게임을 검색하고 발견하는 MCP 서버. |
| [**Discogs**](https://github.com/cswkim/discogs-mcp-server) | Discogs API에 연결하여 음악 컬렉션과 상호작용하는 MCP 서버. |
| [**emicklei/melrose-mcp**](https://github.com/emicklei/melrose-mcp) | Melrose 음악 표현식을 MIDI로 재생하는 MCP 서버. |
| [**Fal MCP Server**](https://github.com/raveenb/fal-mcp-server) | Fal.ai 모델(FLUX, Stable Diffusion, MusicGen)을 사용하여 Claude에서 직접 AI 이미지, 동영상, 음악을 생성하는 MCP 서버. |
| [**Fish Audio**](https://github.com/da-okazaki/mcp-fish-audio-server) | Fish Audio API와 연동하여 다중 음성, 스트리밍, 실시간 재생을 지원하는 Text-to-Speech MCP 서버. |
| [**guillochon/mlb-api-mcp**](https://github.com/guillochon/mlb-api-mcp) | 무료 MLB API 프록시로 선수 정보, 통계, 경기 정보를 제공하는 MCP 서버. |
| [**imprvhub/mcp-claude-spotify**](https://github.com/imprvhub/mcp-claude-spotify) | Claude Desktop에서 Spotify와 상호작용할 수 있게 하는 MCP 통합 서버. |
| [**jiayao/mcp-chess**](https://github.com/jiayao/mcp-chess) | LLM과 체스 대국을 진행하는 MCP 서버. |
| [**khglynn/spotify-bulk-actions-mcp**](https://github.com/khglynn/spotify-bulk-actions-mcp) | 신뢰도 기반 곡 매칭, CSV/팟캐스트 목록에서 일괄 플레이리스트 생성, 라이브러리 내보내기로 가장 많이 저장한 아티스트와 앨범을 발견하는 Spotify 대량 작업 MCP 서버. |
| [**labeveryday/nba_mcp_server**](https://github.com/labeveryday/nba_mcp_server) | 실시간 및 과거 NBA 통계(선수 통계, 경기 스코어, 팀 데이터, 고급 분석)를 접근하는 MCP 서버. |
| [**lfnovo/content-core**](https://github.com/lfnovo/content-core) | 지능형 자동 엔진 선택으로 URL, 문서, 동영상, 오디오에서 콘텐츠를 추출하는 MCP 서버. 웹페이지, PDF, Word, YouTube 자막 등 지원. |
| [**MarceauSolutions/fitness-influencer-mcp**](https://github.com/MarceauSolutions/fitness-influencer-mcp) | 피트니스 콘텐츠 크리에이터 워크플로우 자동화. 점프컷 영상 편집, 수익 분석, 브랜디드 콘텐츠 제작 지원. |
| [**marcelmarais/Spotify**](https://github.com/marcelmarais/spotify-mcp-server) | Spotify 재생을 제어하고 플레이리스트를 관리하는 MCP 서버. |
| [**mediar-ai/screenpipe**](https://github.com/mediar-ai/screenpipe) | 화면/오디오를 캡처하여 타임스탬프 인덱싱, SQL/임베딩 저장, 시맨틱 검색, LLM 기반 히스토리 분석, 이벤트 트리거 액션을 지원하는 로컬 우선 시스템. NextJS 플러그인 생태계로 컨텍스트 인식 AI 에이전트 구축 가능. |
| [**mikechao/balldontlie-mcp**](https://github.com/mikechao/balldontlie-mcp) | balldontlie API와 연동하여 NBA, NFL, MLB의 선수, 팀, 경기 정보를 제공하는 MCP 서버. |
| [**Mureka**](https://github.com/SkyworkAI/Mureka-mcp) | 가사, 노래, 배경 음악(인스트루멘탈)을 생성하는 MCP 서버. |
| [**NBA**](https://github.com/Taidgh-Robinson/nba-mcp-server) | 최근 및 과거 NBA 경기 데이터와 기본/고급 통계를 조회하는 MCP 서버. |
| [**OP.GG**](https://github.com/opgginc/opgg-mcp) | League of Legends, TFT, Valorant 등 인기 게임의 실시간 데이터를 제공하는 MCP 서버. 챔피언 분석, e스포츠 일정, 메타 조합, 캐릭터 통계 지원. |
| [**PGA (Golf)**](https://mcp.pga.com) | PGA 공식 골프 관련 MCP 서버. 코치 찾기, 골프 라운드, 실력 향상 등 지원. |
| [**Phone MCP**](https://github.com/hao-cyber/phone-mcp) | Android 폰을 제어하는 강력한 플러그인. AI 에이전트가 날씨에 따라 음악 재생, 전화 걸기, 문자 보내기 등 복잡한 작업을 자동 수행. |
| [**Pollinations**](https://github.com/pollinations/model-context-protocol) | 인증 없이 이미지, 오디오, 텍스트를 생성하는 멀티모달 MCP 서버. |
| [**quietnotion/barevalue-mcp**](https://github.com/quietnotion/barevalue-mcp) | AI 팟캐스트 편집 서비스. 원본 오디오 업로드 또는 URL 제출 시 필러 워드 제거, 노이즈 감소, 자막, 쇼노트, 소셜 클립이 포함된 편집본 반환. Webhook 자동화 지원. |
| [**Reaper**](https://github.com/dschuler36/reaper-mcp-server) | Reaper(디지털 오디오 워크스테이션) 프로젝트와 상호작용하는 MCP 서버. |
| [**Riot Games**](https://github.com/jifrozen0110/mcp-riot) | Riot API를 통해 League of Legends 플레이어 정보, 랭크, 챔피언 통계, 매치 히스토리를 조회하는 MCP 서버. |
| [**Roblox Studio**](https://github.com/Roblox/studio-rust-mcp-server) | Roblox Studio에서 씬과 스크립트를 생성하고 조작하는 MCP 서버. |
| [**Spotify**](https://github.com/varunneal/spotify-mcp) | LLM이 Spotify를 재생하고 활용할 수 있게 하는 MCP 서버. |
| [**Tencent RTC**](https://github.com/Tencent-RTC/mcp) | AI IDE가 Tencent 실시간 통신 SDK 및 API를 효과적으로 이해하고 사용할 수 있게 지원하여 오디오/비디오 통신 개발을 간소화하는 MCP 서버. |
| [**tiianhk/MaxMSP-MCP-Server**](https://github.com/tiianhk/MaxMSP-MCP-Server) | 음악 및 멀티미디어용 비주얼 프로그래밍 언어인 Max(Max/MSP/Jitter)를 위한 코딩 에이전트 MCP 서버. |
| [**Tommertom/sonos-ts-mcp**](https://github.com/Tommertom/sonos-ts-mcp) | 순수 TypeScript로 구현한 종합 Sonos 오디오 시스템 제어 MCP 서버. 장치 탐색, 멀티룸 재생 관리, 큐 제어, 음악 라이브러리, 알람 관리, EQ 설정 등 50개 이상 도구 제공. |
| [**Transcribe**](https://github.com/transcribe-app/mcp-transcribe) | 오디오/비디오 파일 및 음성 메모의 빠르고 신뢰성 있는 전사를 제공하는 MCP 서버. LLM이 오디오/비디오의 텍스트 콘텐츠와 상호작용 가능. |
| [**TwelveTake-Studios/reaper-mcp**](https://github.com/TwelveTake-Studios/reaper-mcp) | AI 어시스턴트가 REAPER DAW를 제어하여 믹싱, 마스터링, MIDI 작곡, 음악 프로덕션을 수행할 수 있는 129개 도구의 MCP 서버. |
| [**Unity Integration (Advanced)**](https://github.com/quazaai/UnityMCPIntegration) | 고급 Unity3d 게임 엔진 MCP 서버. Unity 내에서 직접 에디터 관련 코드 실행, 로그 가져오기, 에디터 상태 조회, 프로젝트 파일 접근 지원. |
| [**Unity MCP (AI Game Developer)**](https://github.com/IvanMurzak/Unity-MCP) | Unity Editor 및 Unity Runtime MCP 통합. 유닛 테스트, 코딩, C# Roslyn, Reflection, Assets 지원. AI로 게임 제작 및 런타임 AI 로직 실행. |
| [**Unity3d Game Engine**](https://github.com/CoderGamester/mcp-unity) | LLM이 Unity3d 게임 엔진과 상호작용하는 MCP 서버. 콘솔 로그, 테스트 러너, 에디터 기능, 계층 구조 등 다양한 에디터 도구 접근 지원. |
| [**Video Editor**](https://github.com/burningion/video-editing-mcp) | Video Jungle로 동영상을 추가, 편집, 검색하는 MCP 서버. |
| [**video-edit-mcp**](https://github.com/Aditya2755/video-edit-mcp) | 트리밍, 병합, 이펙트, 오버레이, 포맷 변환, 오디오 처리, YouTube 다운로드, 스마트 메모리 관리를 포함한 종합 영상/오디오 편집 MCP 서버. |
| [**YangLiangwei/PersonalizationMCP**](https://github.com/YangLiangwei/PersonalizationMCP) | Steam, YouTube, Bilibili, Spotify, Reddit 등 다중 플랫폼 개인 데이터 통합 MCP 서버. OAuth2 인증, 자동 토큰 관리, 90개 이상 도구 지원. |
| [**youichi-uda/godot-mcp-pro**](https://github.com/youichi-uda/godot-mcp-pro) | Godot 게임 엔진용 프리미엄 MCP 서버. 씬 편집, 스크립팅, 애니메이션, 타일맵, 셰이더, 입력 시뮬레이션, 런타임 디버깅 등 84개 도구 제공. |
| [**ZapCap**](https://github.com/bogdan01m/zapcap-mcp-server) | ZapCap API를 사용하여 자연어로 동영상 자막 및 B-roll 생성을 제공하는 MCP 서버. |

---

## 💰 금융 & 커머스

> Stripe, Shopify, 암호화폐 등 결제/금융/전자상거래

| 서버 | 설명 |
|------|------|
| [**AbdelStark/bitcoin-mcp**](https://github.com/AbdelStark/bitcoin-mcp) | AI 모델이 Bitcoin과 상호작용하는 MCP 서버. 키 생성, 주소 검증, 트랜잭션 디코딩, 블록체인 조회 등 지원. |
| [**Adfin**](https://github.com/Adfin-Engineering/mcp-server-adfin) | Adfin으로 모든 결제를 한 곳에서 관리. 인보이스 발행 및 회계 조정을 지원하는 MCP 서버. |
| [**Adobe Commerce**](https://github.com/rafaelstz/adobe-commerce-dev-mcp) | Adobe Commerce GraphQL API와 연동하여 주문, 상품, 고객 등을 관리하는 MCP 서버. |
| [**agntor/mcp**](https://github.com/agntor/mcp) | 에이전트 탐색 및 인증을 위한 MCP 감사 서버. ID 검증, 에스크로, 정산, 평판 관리 등 AI 에이전트 신뢰 및 결제 인프라 제공. |
| [**ahmetsbilgin/finbrain-mcp**](https://github.com/ahmetsbilgin/finbrain-mcp) | LLM 워크플로우에서 기관급 대안 금융 데이터에 직접 접근하는 MCP 서버. |
| [**Airwallex Developer**](https://www.npmjs.com/package/@airwallex/developer-mcp) | Airwallex API 통합을 지원하는 AI 코딩 에이전트 도구를 제공하는 MCP 서버. |
| [**Alby Bitcoin Payments**](https://github.com/getAlby/mcp) | 에이전트에 Bitcoin Lightning 지갑을 연결하여 전 세계 즉시 결제 송수신을 가능하게 하는 MCP 서버. |
| [**alchemy/alchemy-mcp-server**](https://github.com/alchemyplatform/alchemy-mcp-server) | AI 에이전트가 Alchemy 블록체인 API와 상호작용하는 MCP 서버. |
| [**Algorand**](https://github.com/GoPlausible/algorand-mcp) | Algorand 블록체인과 상호작용하는 종합 MCP 서버. 40개 이상 도구, 60개 이상 리소스, 다양한 프롬프트 제공. |
| [**AlipayPlus**](https://github.com/alipay/global-alipayplus-mcp) | AI 에이전트를 AlipayPlus Checkout Payment에 연결하는 MCP 서버. |
| [**Alpaca**](https://github.com/alpacahq/alpaca-mcp-server) | Alpaca Trading API를 통해 주식 및 옵션 거래, 시장 데이터 분석, 전략 구축을 지원하는 MCP 서버. |
| [**AlphaVantage**](https://mcp.alphavantage.co/) | AlphaVantage의 주가, 펀더멘탈 등 100개 이상 금융 시장 데이터 API에 연결하는 MCP 서버. |
| [**amidabuddha/unichat-mcp-server**](https://github.com/amidabuddha/unichat-mcp-server) | MCP 프로토콜을 통해 OpenAI, MistralAI, Anthropic, xAI, Google AI, DeepSeek에 요청을 보내는 MCP 서버. 벤더 API 키 필요. |
| [**anjor/coinmarket-mcp-server**](https://github.com/anjor/coinmarket-mcp-server) | CoinMarket API 연동으로 암호화폐 목록 및 시세를 조회하는 MCP 서버. |
| [**Antom**](https://github.com/alipay/global-antom-mcp) | AI 에이전트를 Antom Checkout Payment에 연결하는 MCP 서버. |
| [**Apify**](https://github.com/apify/apify-mcp-server) | Actors MCP 서버: 웹사이트, 이커머스, 소셜 미디어, 검색 엔진, 지도 등에서 데이터를 추출하는 3,000개 이상 사전 구축 클라우드 도구 제공. |
| [**Apify**](https://github.com/apify/actors-mcp-server) | Actors MCP 서버: 웹사이트, 이커머스, 소셜 미디어, 검색 엔진, 지도 등에서 데이터를 추출하는 3,000개 이상 사전 구축 클라우드 도구 제공. |
| [**Armor Crypto MCP**](https://github.com/armorwallet/armor-crypto-mcp) | 다중 블록체인과 연동하여 스테이킹, DeFi, 스왑, 브릿징, 지갑 관리, DCA, 지정가 주문 등을 지원하는 MCP 서버. |
| [**avisangle/calculator-server**](https://github.com/avisangle/calculator-server) | Go 기반 종합 수학 계산 MCP 서버. 기본 산술, 고급 함수, 통계 분석, 단위 변환, 금융 계산 등 13개 수학 도구 구현. |
| [**Bankless Onchain**](https://github.com/bankless/onchain-mcp) | ERC20 토큰, 거래 내역, 스마트 컨트랙트 상태 등 온체인 데이터를 조회하는 MCP 서버. |
| [**Base Free USDC Transfer**](https://github.com/magnetai/mcp-free-usdc-transfer) | Claude AI로 Base 네트워크에서 무료로 USDC를 전송하는 MCP 서버. Coinbase CDP 기반. |
| [**base/base-mcp**](https://github.com/base/base-mcp) | Base Network 연동으로 지갑 관리, 자금 전송, 스마트 컨트랙트, DeFi 작업 등 온체인 도구를 제공하는 MCP 서버. |
| [**bbonnin/openapi-to-mcp**](https://github.com/bbonnin/openapi-to-mcp) | OpenAPI/Swagger 스펙을 자동으로 MCP 도구 세트로 변환하는 MCP 서버. 수동 도구 정의 없이 스펙에서 직접 자동 생성하여 일관성 유지 및 유지보수 감소. |
| [**Behavioural Prediction**](https://github.com/ChainAware/behavioral-prediction-mcp) | ChainAware.ai 기반 AI 도구로 지갑 행동 예측, 사기 탐지, 러그풀 예측을 수행하는 MCP 서버. |
| [**BICScan**](https://github.com/ahnlabio/bicscan-mcp) | EVM 블록체인 주소(EOA, CA, ENS) 및 도메인 이름의 위험 점수와 자산 보유 현황을 조회하는 MCP 서버. |
| [**Binance**](https://github.com/ethancod1ng/binance-mcp-server) | Binance API 연동으로 암호화폐 거래 및 시장 데이터 접근을 제공하는 MCP 서버. |
| [**Bitnovo Pay**](https://github.com/bitnovo/mcp-bitnovo-pay) | Bitnovo Pay API를 통해 Bitcoin, Ethereum 등 암호화폐 결제 생성, QR 코드 관리, 거래 처리를 지원하는 MCP 서버. |
| [**bitteprotocol/mcp**](https://github.com/BitteProtocol/mcp) | Bitte Protocol 연동으로 여러 블록체인에서 AI 에이전트를 실행하는 MCP 서버. |
| [**Blockchain MCP**](https://github.com/tatumio/blockchain-mcp) | Tatum의 블록체인 데이터 MCP 서버. AI 에이전트에 즉시 블록체인 접근을 제공하며 모든 LLM에 수 초 만에 연결. |
| [**blockrunai/blockrun-mcp**](https://github.com/blockrunai/blockrun-mcp) | API 키 없이 30개 이상 AI 모델(GPT-5, Claude, Gemini, Grok, DeepSeek)에 접근. Base에서 USDC x402 마이크로페이먼트로 사용량 과금. |
| [**BNBChain MCP**](https://github.com/bnb-chain/bnbchain-mcp) | BSC, opBNB, Greenfield 블록체인과 상호작용하는 MCP 서버. |
| [**Braintree**](https://github.com/QuentinCody/braintree-mcp-server) | AI 에이전트가 결제 처리, 고객 관리, 거래 처리를 수행하는 비공식 PayPal Braintree 결제 게이트웨이 MCP 서버. |
| [**bubilife1202/crossfin**](https://github.com/bubilife1202/crossfin) | 한국 및 글로벌 암호화폐 거래소 라우팅, 차익 시그널, x402 USDC 마이크로페이먼트를 제공하는 AI 에이전트용 MCP 서버. 16개 도구, 9개 거래소, 11개 브릿지 코인. |
| [**Bybit**](https://github.com/ethancod1ng/bybit-mcp-server) | Bybit 암호화폐 거래소 API와 연동하여 자동 거래, 시장 데이터 접근, 계정 관리를 지원하는 MCP 서버. |
| [**carsol/monarch-mcp-server**](https://github.com/carsol/monarch-mcp-server) | Monarch Money 금융 데이터에 읽기 전용 접근을 제공하는 MCP 서버. AI 어시스턴트가 거래, 예산, 계좌, 캐시플로우 분석 가능. MFA 지원. |
| [**Cashfree**](https://github.com/cashfree/cashfree-mcp) | Cashfree Payments 공식 MCP 서버. |
| [**Chargebee**](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) | AI 에이전트를 Chargebee 플랫폼에 연결하는 MCP 서버. |
| [**codex-data/codex-mcp**](https://github.com/Codex-Data/codex-mcp) | Codex API 연동으로 60개 이상 네트워크의 실시간 블록체인 및 시장 데이터를 제공하는 MCP 서버. |
| [**coin_api_mcp**](https://github.com/longmans/coin_api_mcp) | CoinMarketCap 암호화폐 데이터에 접근하는 MCP 서버. |
| [**CoinCap**](https://github.com/QuantGeekDev/coincap-mcp) | 인증 없이 CoinCap 공개 API를 통해 실시간 암호화폐 시장 데이터를 제공하는 MCP 서버. |
| [**Coinex**](https://github.com/coinexcom/coinex_mcp_server) | CoinEx 암호화폐 거래소 공식 API MCP 서버. 시장 데이터, K-line 데이터, 호가창, 잔고 조회, 주문 관리 지원. |
| [**CoinGecko**](https://github.com/coingecko/coingecko-typescript/tree/main/packages/mcp-server) | CoinGecko 공식 API MCP 서버. 200개 이상 블록체인 네트워크와 800만 개 이상 토큰의 암호화폐 가격 및 시장 데이터 제공. |
| [**CoinMarketCap**](https://github.com/shinzo-labs/coinmarketcap-mcp) | CoinMarketCap API 전체를 구현하여 암호화폐 시장 데이터, 거래소 정보, 블록체인 관련 지표를 제공하는 MCP 서버. |
| [**CoinStats**](https://github.com/CoinStatsHQ/coinstats-mcp) | CoinStats API용 MCP 서버. 암호화폐 시장 데이터, 포트폴리오 추적, 뉴스 접근 제공. |
| [**Commerce Layer**](https://github.com/commercelayer/mcp-server-metrics) | Commerce Layer Metrics API와 상호작용하는 MCP 서버. |
| [**crypto-feargreed-mcp**](https://github.com/kukapay/crypto-feargreed-mcp) | 실시간 및 과거 Crypto Fear & Greed Index 데이터를 제공하는 MCP 서버. |
| [**crypto-indicators-mcp**](https://github.com/kukapay/crypto-indicators-mcp) | 다양한 암호화폐 기술 분석 지표 및 전략을 제공하는 MCP 서버. |
| [**crypto-sentiment-mcp**](https://github.com/kukapay/crypto-sentiment-mcp) | AI 에이전트에 암호화폐 감성 분석을 전달하는 MCP 서버. |
| [**cryptopanic-mcp-server**](https://github.com/kukapay/cryptopanic-mcp-server) | CryptoPanic 기반으로 AI 에이전트에 최신 암호화폐 뉴스를 제공하는 MCP 서버. |
| [**cryptosquanch/legends-mcp**](https://github.com/cryptosquanch/legends-mcp) | 36명의 전설적 창업자 및 투자자(Elon Musk, Warren Buffett, Steve Jobs, CZ)와 대화하는 MCP 서버. 진정성 있는 AI 페르소나. API 키 불필요. |
| [**Dappier**](https://github.com/DappierAI/dappier-mcp) | 실시간 웹 검색, 뉴스, 스포츠, 금융 데이터, 암호화폐, 프리미엄 퍼블리셔 콘텐츠 등 신뢰할 수 있는 소스의 권리 승인 데이터를 LLM에 연결하는 MCP 서버. |
| [**DeepQ**](https://github.com/shenqingtech/deepq-financial-toolkit-mcp-server) | DeepQ Technology의 금융 AI 툴킷 MCP 서버. 중국 금융 데이터 및 분석 도구를 AI 대규모 언어 모델에 제공. |
| [**DeFi Rates**](https://github.com/qingfeng/defi-rates-mcp) | Aave, Morpho, Compound, Venus 등 13개 이상 프로토콜의 실시간 DeFi 대출 금리를 조회하는 MCP 서버. 금리 비교, 최적 기회 검색, 루핑 전략 계산 지원. |
| [**DexPaprika**](https://github.com/donbagger/dexpaprika-mcp-server) | 다중 블록체인의 종합 암호화폐 및 DEX 데이터 API. 실시간 토큰 가격, 유동성 풀, OHLCV 데이터로 시장 분석 지원. |
| [**DexPaprika (CoinPaprika)**](https://github.com/coinpaprika/dexpaprika-mcp) | CoinPaprika의 DexPaprika를 통해 다중 블록체인 네트워크의 실시간 DEX 데이터, 유동성 풀, 토큰 정보, 거래 분석을 제공하는 MCP 서버. |
| [**Dodo Payments**](https://github.com/dodopayments/dodopayments-node/tree/main/packages/mcp-server) | Dodo Payments API에 경량 서버리스 호환 인터페이스로 AI 에이전트가 안전하게 결제 작업을 수행하는 MCP 서버. |
| [**dodopayments/contextmcp**](https://github.com/dodopayments/context-mcp) | 다양한 소스의 문서를 인덱싱하고 시맨틱 검색으로 AI 에이전트에 제공하는 셀프 호스팅 MCP 서버. |
| [**doggybee/mcp-server-ccxt**](https://github.com/doggybee/mcp-server-ccxt) | CCXT 라이브러리로 20개 이상 거래소의 실시간 암호화폐 시장 데이터 및 거래를 지원하는 MCP 서버. 현물, 선물, OHLCV, 잔고, 주문 등. |
| [**Edwin**](https://github.com/edwin-finance/edwin/tree/main/examples/mcp-server) | Edwin SDK용 MCP 서버. AI 에이전트가 EVM, Solana 등 블록체인의 DeFi 프로토콜과 상호작용 가능. |
| [**Ember AI**](https://docs.emberai.xyz/) | AI 에이전트가 크로스체인 DeFi 전략을 실행할 수 있는 통합 MCP 서버. |
| [**Ergo Blockchain MCP**](https://github.com/marctheshark3/ergo-mcp) | Ergo Blockchain Node 및 Explorer API와 연동하여 주소 잔액 확인, 거래 분석, 포렌식 분석 등을 수행하는 MCP 서버. |
| [**etbars/vibetrader-mcp**](https://github.com/etbars/vibetrader-mcp) | AI 기반 트레이딩 봇 플랫폼. Alpaca 브로커리지를 통해 자연어로 자동 트레이딩 전략 생성. |
| [**EVM MCP Server**](https://github.com/mcpdotdirect/evm-mcp-server) | 30개 이상 EVM 네트워크를 위한 종합 블록체인 서비스. 네이티브 토큰, ERC20, NFT, 스마트 컨트랙트, 트랜잭션, ENS 해석 지원. |
| [**Fan Token Intel MCP**](https://github.com/BrunoPessoa22/chiliz-marketing-intel) | 팬 토큰 인텔리전스를 위한 67개 이상 도구. 고래 흐름, 시그널 스코어, 스포츠 캘린더, 백테스팅, DEX 트레이딩, 소셜 감성 분석. SSE 트랜스포트, Bearer 인증. |
| [**ferdousbhai/investor-agent**](https://github.com/ferdousbhai/investor-agent) | Yahoo Finance 연동으로 옵션 추천을 포함한 주식 시장 데이터를 조회하는 MCP 서버. |
| [**ferdousbhai/tasty-agent**](https://github.com/ferdousbhai/tasty-agent) | Tastyworks API 연동으로 Tastytrade에서 거래 활동을 처리하는 MCP 서버. |
| [**fernikolic/clawdentials**](https://github.com/fernikolic/clawdentials) | AI 에이전트 커머스를 위한 신뢰 레이어. 에스크로 보호 결제, 검증 가능한 평판 점수, Nostr ID(NIP-05) 제공. USDC, USDT, BTC(Cashu) 지원. |
| [**Fewsats**](https://github.com/Fewsats/fewsats-mcp) | Fewsats를 사용하여 AI 에이전트가 안전하게 구매할 수 있게 하는 MCP 서버. |
| [**Financial Datasets**](https://github.com/financial-datasets/mcp-server) | AI 에이전트를 위한 주식 시장 API MCP 서버. |
| [**financialdatanet/mcp-server**](https://github.com/financialdatanet/mcp-server) | FinancialData.Net MCP 서버. 일일/장중 주식 데이터, 재무제표, 내부자/기관 거래, 지속가능성 데이터, 실적 발표 등 조회. |
| [**FIXParser**](https://gitlab.com/logotype/fixparser/-/tree/main/packages/fixparser-plugin-mcp) | AI 기반 트레이딩 에이전트를 위한 최신 FIX Protocol 엔진 MCP 서버. |
| [**Flutterwave**](https://github.com/bajoski34/mcp-flutterwave/tree/main) | Flutterwave 결제 솔루션 API와 연동하여 거래 관리, 결제 링크 생성 등을 지원하는 MCP 서버. |
| [**fmp-mcp-server**](https://github.com/vipbat/fmp-mcp-server) | Financial Modeling Prep API로 M&A 분석 및 투자 은행 워크플로우를 지원하는 MCP 서버. 회사 프로필, 재무제표, 비율, 섹터 분석 제공. |
| [**fotoetienne/gqai**](https://github.com/fotoetienne/gqai) | 일반 GraphQL 쿼리/뮤테이션으로 도구를 정의하면 자동으로 MCP 서버를 생성하는 도구. |
| [**freqtrade-mcp**](https://github.com/kukapay/freqtrade-mcp) | Freqtrade 암호화폐 트레이딩 봇과 연동하는 MCP 서버. |
| [**getalby/nwc-mcp-server**](https://github.com/getalby/nwc-mcp-server) | Nostr Wallet Connect 기반 Bitcoin Lightning 지갑 연동 MCP 서버. |
| [**glaksmono/finbud-data-mcp**](https://github.com/glaksmono/finbud-data-mcp/tree/main/packages/mcp-server) | 개발자 친화적 AI 네이티브 API로 주식, 옵션, 암호화폐, 외환 등 종합 실시간 금융 데이터를 제공하는 MCP 서버. |
| [**GOAT**](https://github.com/goat-sdk/goat/tree/main/typescript/examples/by-framework/model-context-protocol) | Ethereum, Solana, Base를 포함한 모든 블록체인에서 200개 이상 온체인 액션을 실행하는 MCP 서버. |
| [**Handshake58/DRAIN-marketplace**](https://github.com/Handshake58/DRAIN-marketplace) | AI 서비스(LLM, 이미지/비디오 생성, 웹 스크래핑, 모델 호스팅 등)를 위한 오픈 마켓플레이스. Polygon에서 USDC 마이크로페이먼트로 사용량 과금. API 키 불필요. |
| [**Heurist Mesh Agent**](https://github.com/heurist-network/heurist-mesh-mcp-server) | Heurist Mesh 네트워크를 통해 블록체인 분석, 스마트 컨트랙트 보안, 토큰 지표 등 특화된 Web3 AI 에이전트에 접근하는 MCP 서버. |
| [**Hippycampus**](https://github.com/cromwellian/hippycampus) | Swagger/OpenAPI REST 엔드포인트의 yaml/json 정의를 자동으로 MCP 서버로 변환하는 도구. Langchain/Langflow 통합 지원. |
| [**Hive Intelligence**](https://github.com/hive-intel/hive-crypto-mcp) | AI 어시스턴트를 위한 궁극의 암호화폐 MCP 서버. 암호화폐, DeFi, Web3 분석에 통합 접근 제공. |
| [**HLedger MCP**](https://github.com/iiAtlas/hledger-mcp) | LLM에서 직접 복식부기 평문 회계를 수행하는 MCP 서버. 로컬 HLedger 회계 저널에 대한 종합 읽기/쓰기(선택) 접근 제공. |
| [**HuggingAGI/mcp-baostock-server**](https://github.com/HuggingAGI/mcp-baostock-server) | baostock 기반 MCP 서버. 중국 주식 시장 데이터 접근 및 분석 기능 제공. |
| [**Hypertool**](https://github.com/toolprint/hypertool-mcp) | 여러 MCP 서버에서 핫 스왑 가능한 페르소나 도구 세트를 생성하여 도구 과부하를 줄이고 실행 효율을 개선하는 MCP 서버. |
| [**intentos-labs/beeper-mcp**](https://github.com/intentos-labs/beeper-mcp) | BSC에서 잔고/토큰 전송, PancakeSwap 토큰 스왑, Beeper 리워드 클레임 등 트랜잭션을 제공하는 MCP 서버. |
| [**JamesANZ/bitcoin-mcp**](https://github.com/JamesANZ/bitcoin-mcp) | AI 모델이 Bitcoin 블록체인을 조회할 수 있게 하는 MCP 서버. |
| [**jupiter-mcp**](https://github.com/kukapay/jupiter-mcp) | Jupiter의 Ultra API를 사용하여 Solana 블록체인에서 토큰 스왑을 실행하는 MCP 서버. |
| [**Kash.click**](https://github.com/paracetamol951/caisse-enregistreuse-mcp-server) | AI에 매출, 고객, 주문, 세금 정보, 결제 및 비즈니스 인사이트 접근을 제공하는 MCP 서버. |
| [**klever-io/mcp-klever-vm**](https://github.com/klever-io/mcp-klever-vm) | Klever 블록체인 MCP 서버. 스마트 컨트랙트 개발, 온체인 데이터 탐색, 계정/자산 조회, 거래 분석, 컨트랙트 배포 지원. |
| [**Knit MCP Server**](https://developers.getknit.dev/docs/knit-mcp-server-getting-started) | CRM, HRIS, 급여, 회계, ERP, 캘린더, 비용 관리, 채팅 카테고리의 10,000개 이상 도구에 연결하는 프로덕션 레디 원격 MCP 서버. |
| [**Kukapay MCP Servers**](https://github.com/kukapay/kukapay-mcp-servers) | Kukapay의 암호화폐, 블록체인, Web3 데이터 집계, 분석, 서비스를 위한 종합 MCP 서버 모음. |
| [**kukapay/binance-alpha-mcp**](https://github.com/kukapay/binance-alpha-mcp) | Binance Alpha 거래를 추적하여 AI 에이전트의 알파 포인트 축적 최적화를 돕는 MCP 서버. |
| [**kukapay/bitcoin-utxo-mcp**](https://github.com/kukapay/bitcoin-utxo-mcp) | Bitcoin의 미사용 트랜잭션 출력(UTXO) 및 블록 통계를 추적하는 MCP 서버. |
| [**kukapay/blockbeats-mcp**](https://github.com/kukapay/blockbeats-mcp) | BlockBeats의 블록체인 뉴스 및 심층 기사를 AI 에이전트에 전달하는 MCP 서버. |
| [**kukapay/blocknative-mcp**](https://github.com/kukapay/blocknative-mcp) | Blocknative 기반으로 다중 블록체인의 실시간 가스 가격 예측을 제공하는 MCP 서버. |
| [**kukapay/bridge-rates-mcp**](https://github.com/kukapay/bridge-rates-mcp) | 온체인 AI 에이전트에 실시간 크로스체인 브릿지 환율 및 최적 전송 경로를 제공하는 MCP 서버. |
| [**kukapay/crypto-funds-mcp**](https://github.com/kukapay/crypto-funds-mcp) | AI 에이전트에 암호화폐 투자 펀드의 구조화된 실시간 데이터를 제공하는 MCP 서버. |
| [**kukapay/crypto-liquidations-mcp**](https://github.com/kukapay/crypto-liquidations-mcp) | Binance의 실시간 암호화폐 청산 이벤트를 스트리밍하는 MCP 서버. |
| [**kukapay/crypto-news-mcp**](https://github.com/kukapay/crypto-news-mcp) | NewsData 기반으로 AI 에이전트에 실시간 암호화폐 뉴스를 제공하는 MCP 서버. |
| [**kukapay/crypto-orderbook-mcp**](https://github.com/kukapay/crypto-orderbook-mcp) | 주요 암호화폐 거래소의 호가창 깊이 및 불균형을 분석하는 MCP 서버. |
| [**kukapay/crypto-pegmon-mcp**](https://github.com/kukapay/crypto-pegmon-mcp) | 다중 블록체인에서 스테이블코인 페그 무결성을 추적하는 MCP 서버. |
| [**kukapay/crypto-portfolio-mcp**](https://github.com/kukapay/crypto-portfolio-mcp) | 암호화폐 포트폴리오 배분을 추적하고 관리하는 MCP 서버. |
| [**kukapay/crypto-projects-mcp**](https://github.com/kukapay/crypto-projects-mcp) | Mobula.io의 암호화폐 프로젝트 데이터를 AI 에이전트에 제공하는 MCP 서버. |
| [**kukapay/crypto-rss-mcp**](https://github.com/kukapay/crypto-rss-mcp) | 다중 RSS 피드에서 실시간 암호화폐 뉴스를 집계하는 MCP 서버. |
| [**kukapay/crypto-stocks-mcp**](https://github.com/kukapay/crypto-stocks-mcp) | 주요 암호화폐 관련 주식의 실시간 데이터를 추적하는 MCP 서버. |
| [**kukapay/crypto-trending-mcp**](https://github.com/kukapay/crypto-trending-mcp) | CoinGecko의 최신 트렌딩 토큰을 추적하는 MCP 서버. |
| [**kukapay/crypto-whitepapers-mcp**](https://github.com/kukapay/crypto-whitepapers-mcp) | 암호화폐 백서의 구조화된 지식 베이스 역할을 하는 MCP 서버. |
| [**kukapay/defi-yields-mcp**](https://github.com/kukapay/defi-yields-mcp) | AI 에이전트가 DeFi 수익률 기회를 탐색하는 MCP 서버. |
| [**kukapay/pumpswap-mcp**](https://github.com/kukapay/pumpswap-mcp) | AI 에이전트가 PumpSwap에서 실시간 토큰 스왑 및 자동 온체인 트레이딩을 수행하는 MCP 서버. |
| [**kukapay/sui-trader-mcp**](https://github.com/kukapay/sui-trader-mcp) | AI 에이전트가 Sui 블록체인에서 최적의 토큰 스왑을 수행하는 MCP 서버. |
| [**kukapay/uniswap-price-mcp**](https://github.com/kukapay/uniswap-price-mcp) | 다중 블록체인에서 Uniswap에 새로 생성된 유동성 풀을 추적하는 MCP 서버. |
| [**kukapay/wallet-inspector-mcp**](https://github.com/kukapay/wallet-inspector-mcp) | AI 에이전트가 주요 EVM 체인 및 Solana 체인에서 모든 지갑의 잔고 및 온체인 활동을 검사하는 MCP 서버. |
| [**Language Server**](https://github.com/isaacphi/mcp-language-server) | MCP 지원 클라이언트가 정의 이동, 참조 찾기, 이름 변경, 진단 등 시맨틱 도구로 코드베이스를 쉽게 탐색하게 하는 MCP Language Server. |
| [**laukikk/alpaca-mcp**](https://github.com/laukikk/alpaca-mcp) | Alpaca 거래 API로 주식 및 암호화폐 포트폴리오 관리, 거래 실행, 시장 데이터 접근을 제공하는 MCP 서버. |
| [**lightningfaucet/mcp-server**](https://github.com/lightningfaucet/mcp-server) | L402 결제 기능이 있는 AI 에이전트 Bitcoin 지갑. 운영자가 에이전트에 자금을 공급하고 에이전트가 Lightning Network에서 자율 결제 수행. |
| [**lnbits/LNbits-MCP-Server**](https://github.com/lnbits/LNbits-MCP-Server) | LNbits Lightning Network 지갑 연동 MCP 서버. |
| [**longportapp/openapi**](https://github.com/longportapp/openapi/tree/main/mcp) | LongPort OpenAPI로 실시간 주식 시장 데이터를 제공하고 MCP를 통해 AI 분석 및 거래 기능을 제공하는 서버. |
| [**LunarCrush Remote MCP**](https://github.com/lunarcrush/mcp-server) | 실시간 및 과거 소셜 지표와 게시물을 LLM 및 토큰 최적화 출력으로 제공하는 MCP 서버. 자동 트레이딩/금융 자문에 적합. |
| [**Maestro MCP**](https://github.com/maestro-org/maestro-mcp) | Maestro RPC API를 통해 Bitcoin과 상호작용하는 MCP 서버. |
| [**MCP for WooCommerce**](https://github.com/iOSDevSK/mcp-for-woocommerce) | WooCommerce 스토어를 AI 어시스턴트에 연결하여 상품, 카테고리, 리뷰, WordPress 콘텐츠에 읽기 전용 접근을 제공하는 WordPress 플러그인. |
| [**Microsoft Business Central**](https://github.com/knowall-ai/mcp-business-central) | Dynamics 365 Business Central의 고객, 연락처, 영업 기회, 인보이스, 거래처를 관리하는 MCP 서버. |
| [**Mifos X**](https://github.com/openMF/mcp-mifosx) | Mifos X 오픈소스 뱅킹용 MCP 서버. 고객, 대출, 저축, 주식, 금융 거래 관리 및 재무 보고서 생성 지원. |
| [**minhyeoky/mcp-server-ledger**](https://github.com/minhyeoky/mcp-server-ledger) | ledger-cli 연동으로 금융 거래 관리 및 보고서 생성을 지원하는 MCP 서버. |
| [**narumiruna/yfinance-mcp**](https://github.com/narumiruna/yfinance-mcp) | yfinance를 사용하여 Yahoo Finance 정보를 가져오는 MCP 서버. |
| [**nikicat/mcp-wallet-signer**](https://github.com/nikicat/mcp-wallet-signer) | 비수탁형 EVM 지갑 MCP 서버. 트랜잭션을 브라우저 지갑(MetaMask 등)으로 라우팅하여 서명. 개인키가 브라우저를 벗어나지 않으며 EIP-6963을 통한 명시적 사용자 승인 필요. |
| [**Nodit**](https://github.com/noditlabs/nodit-mcp-server) | 멀티체인 RPC 노드 및 Data API를 통해 블록체인 데이터에 접근하는 Nodit 공식 MCP 서버. |
| [**Norman Finance**](https://github.com/norman-finance/norman-mcp-server) | Norman Finance로 회계 및 세금을 관리하는 MCP 서버. |
| [**nyxn-ai/NyxDocs**](https://github.com/nyxn-ai/NyxDocs) | 멀티 블록체인(Ethereum, BSC, Polygon, Solana) 지원 암호화폐 프로젝트 문서 관리 전문 MCP 서버. |
| [**Openfort**](https://github.com/openfort-xyz/mcp) | 인증, 프로젝트 스캐폴딩, 스마트 월렛 도구에 플러그 앤 플레이 접근을 제공하는 MCP 서버. |
| [**P-Link.io**](https://github.com/paracetamol951/P-Link-MCP) | Solana 네트워크에서 HTTP 402 Protocol을 구현하여 에이전트 간 결제 송수신을 지원하는 MCP 서버. |
| [**pancakeswap-poolspy-mcp**](https://github.com/kukapay/pancakeswap-poolspy-mcp) | PancakeSwap에서 새로 생성된 유동성 풀을 추적하는 MCP 서버. |
| [**Paper**](https://github.com/paperinvest/mcp-server) | 시장 시뮬레이션, 22개 브로커 에뮬레이션, 전문 도구를 갖춘 모의 트레이딩 플랫폼. 최초의 MCP 통합 트레이딩 플랫폼. |
| [**Paradex MCP**](https://github.com/sv/mcp-paradex-py) | Paradex 플랫폼과 상호작용하는 MCP 네이티브 서버. 완전한 트레이딩 기능 포함. |
| [**PayPal**](https://mcp.paypal.com) | PayPal 공식 MCP 서버. |
| [**PayPal**](https://github.com/paypal/agent-toolkit) | PayPal MCP 서버. 다양한 PayPal 서비스와 함수 호출을 통해 상호작용 지원. |
| [**PayPal**](https://github.com/paypal/agent-toolkit/tree/main/modelcontextprotocol) | PayPal Agent Toolkit으로 MCP를 통해 PayPal API와 함수 호출로 연동하는 서버. |
| [**Peliqan**](https://github.com/Peliqan-io/mcp-server-peliqan) | ETL 및 내장 데이터 웨어하우스를 갖춘 데이터 플랫폼. MCP를 통해 모든 비즈니스 애플리케이션(ERP, CRM, 회계 등)에 접근하고 비즈니스 데이터 쿼리 실행. |
| [**polygon-io/mcp_polygon)**](https://github.com/polygon-io/mcp_polygon) | Polygon.io 금융 시장 데이터 API(주식, 지수, 외환, 옵션 등)에 접근하는 MCP 서버. |
| [**Polymarket**](https://github.com/ozgureyilmaz/polymarket-mcp) | Polymarket의 실시간 예측 시장 데이터 조회. 시장 검색, 가격 분석, 거래 기회 식별 지원. |
| [**pwh-pwh/coin-mcp-server**](https://github.com/pwh-pwh/coin-mcp-server) | Bitget API로 암호화폐 가격을 조회하는 MCP 서버. |
| [**pylonapi/pylon-mcp**](https://github.com/pylonapi/pylon-mcp) | 웹 추출, 검색, 번역, 이미지 생성, 스크린샷, PDF, OCR 등 20개 이상 기능의 x402 네이티브 API 게이트웨이. API 키 불필요, HTTP 402로 USDC 결제. |
| [**QuantConnect**](https://github.com/QuantConnect/mcp-server) | QuantConnect 알고리즘 트레이딩 플랫폼 오케스트레이션 MCP. 에이전트 LLM 기반 트레이딩 전략 설계, 리서치, 구현 지원. |
| [**QuantConnect**](https://github.com/taylorwilsdon/quantconnect-mcp) | QuantConnect 알고리즘 트레이딩 플랫폼 오케스트레이션 MCP. 에이전트 LLM 기반 트레이딩 전략 설계, 리서치, 구현 지원. |
| [**RomThpt/xrpl-mcp-server**](https://github.com/RomThpt/mcp-xrpl) | XRP Ledger용 MCP 서버. 계정 정보, 거래 내역, 네트워크 데이터 조회, 원장 객체 쿼리, 트랜잭션 제출, XRPL 네트워크 모니터링 지원. |
| [**SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop**](https://github.com/SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop.git) | CoinGecko API를 사용하여 암호화폐 시장 데이터를 제공하는 MCP 도구. |
| [**SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop**](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop.git) | Yahoo Finance API를 사용하여 주식 시장 데이터 및 분석을 제공하는 MCP 도구. |
| [**SEC EDGAR**](https://github.com/stefanoamorelli/sec-edgar-mcp) | 미국 증권거래위원회(SEC) EDGAR를 통해 금융 공시 및 데이터에 접근하는 커뮤니티 MCP 서버. |
| [**serpapi/serpapi-mcp**](https://github.com/serpapi/serpapi-mcp) | SerpApi MCP 서버. Google, Bing, Yahoo, DuckDuckGo, YouTube, eBay 등 다중 엔진 검색과 실시간 날씨, 주식 정보 제공. |
| [**ShareSeer**](https://github.com/shareseer/shareseer-mcp-server) | ShareSeer를 사용하여 SEC 공시, 재무 데이터, 내부자 거래 데이터에 실시간으로 접근하는 MCP 서버. |
| [**Shopify**](https://github.com/GeLi2001/shopify-mcp) | Shopify API와 연동하여 주문, 상품, 고객 등을 관리하는 MCP 서버. |
| [**Shopify Storefront**](https://github.com/QuentinCody/shopify-storefront-mcp-server) | AI 에이전트가 Shopify 스토어프론트를 발견하고 Storefront API를 통해 상품, 컬렉션 등 스토어 데이터를 가져오는 비공식 MCP 서버. |
| [**Shopify/dev-mcp**](https://github.com/Shopify/dev-mcp) | Shopify Dev와 상호작용하는 MCP 서버. |
| [**softvoyagers/fakturka-api**](https://github.com/softvoyagers/fakturka-api) | PDF 출력 및 미리보기를 지원하는 무료 폴란드 VAT 인보이스 생성기 API. API 키 불필요. |
| [**Solana Agent Kit**](https://github.com/sendaifun/solana-agent-kit/tree/main/examples/agent-kit-mcp-server) | SendAI의 Solana Agent Kit으로 LLM이 Solana 블록체인과 상호작용하는 MCP 서버. 40개 이상 프로토콜 액션 지원. |
| [**Star Wars**](https://github.com/johnpapa/mcp-starwars) | SWAPI Star Wars API용 MCP 서버. MCP 서버로 API와 상호작용하는 방법을 시연하는 프로젝트. |
| [**Starknet MCP Server**](https://github.com/mcpdotdirect/starknet-mcp-server) | Starknet 블록체인과 상호작용하는 종합 MCP 서버. 블록체인 데이터 조회, StarknetID 해석, 토큰 전송 지원. |
| [**Starling Bank**](https://github.com/domdomegg/starling-bank-mcp) | Starling Bank API를 통해 계좌 잔액 확인 및 거래 내역 조회 등 계좌 관리를 지원하는 MCP 서버. |
| [**Stellar**](https://github.com/syronlabs/stellar-mcp/) | LLM이 Stellar 블록체인과 상호작용하는 MCP 서버. 계정 생성, 잔액 확인, 거래 분석, 자산 발행, 스마트 컨트랙트 등 지원. |
| [**Steuerboard**](https://github.com/steuerboard/steuerboard-mcp-typescript) | 공식 MCP 서버를 통해 비즈니스 회계 데이터와 상호작용하는 MCP 서버. |
| [**Stripe**](https://github.com/stripe/agent-toolkit) | 결제, 고객, 환불 처리를 위한 Stripe 연동 MCP 서버. |
| [**Stripe**](https://github.com/atharvagupta2003/mcp-stripe) | 결제, 고객, 환불 처리를 위한 Stripe 연동 MCP 서버. |
| [**Tako**](https://github.com/TakoData/tako-mcp) | 자연어로 Tako에서 실시간 금융, 스포츠, 날씨, 공공 데이터를 시각화와 함께 검색하는 MCP 서버. |
| [**thegraph-mcp**](https://github.com/kukapay/thegraph-mcp) | The Graph의 인덱싱된 블록체인 데이터를 AI 에이전트에 제공하는 MCP 서버. |
| [**Thirdweb**](https://github.com/thirdweb-dev/ai/tree/main/python/thirdweb-mcp) | Thirdweb 기반으로 2,000개 이상 블록체인에 읽기/쓰기, 데이터 조회, 컨트랙트 분석/배포, 트랜잭션 실행을 지원하는 MCP 서버. |
| [**ThomasMarches/substrate-mcp-rs**](https://github.com/ThomasMarches/substrate-mcp-rs) | Substrate 기반 블록체인과 상호작용하는 MCP 서버. Rust로 구축되며 subxt 크레이트 활용. |
| [**tipdotmd/tip-md-x402-mcp-server**](https://github.com/tipdotmd/tip-md-x402-mcp-server) | x402 결제 프로토콜과 CDP Wallet을 사용하여 AI 인터페이스에서 암호화폐 팁을 보내는 MCP 서버. |
| [**Token Metrics**](https://github.com/token-metrics/mcp) | Token Metrics 연동으로 실시간 암호화폐 시장 데이터, 트레이딩 시그널, 가격 예측, 고급 분석을 제공하는 MCP 서버. |
| [**token-minter-mcp**](https://github.com/kukapay/token-minter-mcp) | AI 에이전트가 다중 블록체인에서 ERC-20 토큰을 발행하는 도구를 제공하는 MCP 서버. |
| [**token-revoke-mcp**](https://github.com/kukapay/token-revoke-mcp) | 다중 블록체인에서 ERC-20 토큰 허용량을 확인하고 취소하는 MCP 서버. |
| [**Ton Blockchain MCP**](https://github.com/devonmojito/ton-blockchain-mcp) | Ton Blockchain과 상호작용하는 MCP 서버. |
| [**tooyipjee/yahoofinance-mcp**](https://github.com/tooyipjee/yahoofinance-mcp.git) | Yahoo Finance MCP의 TypeScript 버전. |
| [**tumf/web3-mcp**](https://github.com/tumf/web3-mcp) | Ankr Advanced API를 래핑한 MCP 서버. Ethereum, BSC, Polygon, Avalanche 등 다중 체인의 NFT, 토큰, 블록체인 데이터 접근. |
| [**Twelve Data**](https://github.com/twelvedata/mcp) | Twelve Data 공식 MCP 서버로 AI 에이전트를 실시간 및 과거 금융 시장 데이터와 통합. |
| [**uniswap-poolspy-mcp**](https://github.com/kukapay/uniswap-poolspy-mcp) | 9개 블록체인 네트워크에서 Uniswap에 새로 생성된 유동성 풀을 추적하는 MCP 서버. |
| [**uniswap-trader-mcp**](https://github.com/kukapay/uniswap-trader-mcp) | AI 에이전트가 다중 블록체인에서 Uniswap DEX 토큰 스왑을 자동화하는 MCP 서버. |
| [**Upbit MCP Server**](https://github.com/solangii/upbit-mcp-server) | Upbit 거래소에서 실시간 암호화폐 가격, 시장 요약, 자산 목록에 접근하는 MCP 서버. |
| [**whale-tracker-mcp**](https://github.com/kukapay/whale-tracker-mcp) | 암호화폐 고래 거래를 추적하는 MCP 서버. |
| [**WooCommerce.com**](https://developer.woocommerce.com/docs/features/mcp/) | MCP 통합으로 WooCommerce.com 스토어, 상품, 주문을 관리하는 서버. |
| [**Xero**](https://github.com/XeroAPI/xero-mcp-server) | Xero 공식 MCP 서버로 비즈니스 회계 데이터와 상호작용. |
| [**Xero-mcp-server**](https://github.com/john-zhang-dev/xero-mcp) | Xero 시스템과 연동하여 회계, 인보이스, 비즈니스 운영을 간소화하는 MCP 서버. |
| [**xpaysh/awesome-x402**](https://github.com/xpaysh/awesome-x402) | x402 결제 프로토콜 리소스, MCP 서버, HTTP 402 기반 USDC 결제 도구의 큐레이션 디렉토리. |
| [**Yahoo Finance**](https://github.com/AgentX-ai/yahoo-finance-server) | AI가 Yahoo Finance와 상호작용하여 종합 주식 시장 데이터, 뉴스, 재무 정보 등을 가져오는 MCP 서버. 프록시 지원. |
| [**yamariki-hub/japan-corporate-mcp**](https://github.com/yamariki-hub/japan-corporate-mcp) | 정부 API(gBizINFO, EDINET, e-Stat)를 통해 일본 기업 데이터를 제공하는 MCP 서버. 기업 검색, 재무, 특허, 보조금, 조달, 정부 통계 지원. |
| [**yfinance**](https://github.com/Adity-star/mcp-yfinance-server) | 실시간 및 과거 주식 데이터를 표준 형식으로 제공하는 MCP YFinance 서버. 대시보드, AI 에이전트, 연구 도구에 금융 인사이트 제공. |
| [**YNAB**](https://github.com/ChuckBryan/ynabmcpserver) | YNAB(You Need A Budget)과 연동하여 AI 어시스턴트가 안전하게 재무 데이터를 접근하고 분석하는 MCP 서버. |
| [**ZBD**](https://github.com/zebedeeio/zbd-payments-typescript-sdk/tree/main/packages/mcp-server) | ZBD 결제 처리 API와 연동하여 Bitcoin 및 Lightning Network로 즉시 글로벌 결제를 지원하는 MCP 서버. |
| [**zlinzzzz/finData-mcp-server**](https://github.com/zlinzzzz/finData-mcp-server) | Tushare 등 다중 데이터 공급자를 지원하는 전문 금융 데이터 접근 MCP 서버. |
| [**zolo-ryan/MarketAuxMcpServer**](https://github.com/Zolo-Ryan/MarketAuxMcpServer) | 심볼, 산업, 국가, 날짜 범위별 고급 필터링을 지원하는 종합 시장 및 금융 뉴스 검색 MCP 서버. |

---

## 🗺️ 지도 & 위치 & 여행

> Google Maps, 항공/호텔 예약 등 위치 기반 서비스

| 서버 | 설명 |
|------|------|
| [**Aviationstack**](https://github.com/Pradumnasaraf/aviationstack-mcp) | AviationStack API를 사용하여 항공사 운항, 공항 스케줄, 향후 항공편 및 항공기 유형 등 실시간 항공 데이터를 조회하는 MCP 서버입니다. |
| [**Browserbase**](https://github.com/browserbase/mcp-server-browserbase) | 클라우드에서 브라우저 상호작용을 자동화합니다 (웹 탐색, 데이터 추출, 폼 입력 등) |
| [**Cal.com**](https://www.npmjs.com/package/@calcom/cal-mcp?activeTab=readme) | Cal.com API에 연결하여 예약 및 일정을 관리합니다. |
| [**Campertunity**](https://github.com/campertunity/mcp-server) | Campertunity에서 전 세계 캠핑장을 검색하고, 예약 가능 여부를 확인하며, 예약 링크를 제공합니다. |
| [**Danielpeter-99/calcom-mcp**](https://github.com/Danielpeter-99/calcom-mcp) | Cal.com용 MCP 서버입니다. 이벤트 유형 관리, 예약 생성, LLM을 통한 Cal.com 스케줄링 데이터 접근을 지원합니다. |
| [**Destinia**](https://destinia.com/developers) | Destinia에서 호텔을 검색하고 숙소 상세 정보를 조회하는 도구를 제공합니다. |
| [**FlightRadar24**](https://github.com/sunsetcoder/flightradar24-mcp-server) | Flightradar24 데이터를 활용하여 실시간 항공편 추적을 지원하는 Claude Desktop용 MCP 서버입니다. |
| [**Google Maps**](https://github.com/Mastan1301/google_maps_mcp) | Google Places API를 사용하여 위치 검색 결과를 제공합니다. |
| [**Google Maps**](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) | 위치 서비스, 경로 안내 및 장소 상세 정보를 위한 Google Maps 통합 |
| [**Google Maps Platform Code Assist**](https://github.com/googlemaps/platform-ai/tree/main/packages/code-assist) | 최신 공식 문서와 코드 샘플을 기반으로 에이전트에게 최적의 지리 관련 안내와 코드를 제공합니다. |
| [**ipfind/ipfind-mcp-server**](https://github.com/ipfind/ipfind-mcp-server) | IP Find API를 사용한 IP 주소 위치 조회 서비스입니다. |
| [**jagan-shanmugam/open-streetmap-mcp**](https://github.com/jagan-shanmugam/open-streetmap-mcp) | 위치 기반 서비스와 지리공간 데이터를 제공하는 OpenStreetMap MCP 서버입니다. |
| [**kindly-software/kdb**](https://github.com/kindly-software/kdb) | 양방향 실행 재생, 감사 준수 해시 체인 로깅, SIMD 가속 스택 언와인딩을 갖춘 AI 기반 타임트래블 디버거입니다. 무료 Hobby 티어 제공. |
| [**LadislavSopko/mcp-ai-server-visual-studio**](https://github.com/LadislavSopko/mcp-ai-server-visual-studio) | Visual Studio용 MCP AI Server. 20개의 Roslyn 기반 도구로 AI 어시스턴트에게 시맨틱 코드 탐색, 심볼 검색, 상속 트리, 호출 그래프, 안전한 이름 변경, 빌드/테스트 실행을 제공합니다. Claude, Codex, Gemini, Cursor, Copilot, Windsurf, Cline과 호환. |
| [**Large File MCP**](https://github.com/willianpinho/large-file-mcp) | 스마트 청킹, 탐색 및 스트리밍 기능을 갖춘 대용량 파일의 지능형 처리. LRU 캐싱, regex를 지원합니다. |
| [**lucygoodchild/mcp-national-rail**](https://github.com/lucygoodchild/mcp-national-rail) | 영국 National Rail 열차 서비스를 위한 MCP 서버로, Realtime Trains API를 통합하여 열차 시간표와 실시간 운행 정보를 제공합니다. |
| [**Mapbox**](https://github.com/mapbox/mcp-server) | Mapbox API를 통해 geocoding, POI 검색, 경로 안내, isochrone 등 지리공간 인텔리전스를 제공합니다. |
| [**matbel91765/gis-mcp-server**](https://github.com/matbel91765/gis-mcp-server) | AI 에이전트를 위한 지리공간 도구: geocoding, 경로, 고도, 공간 분석, 파일 I/O (Shapefile, GeoJSON, GeoPackage) |
| [**MeasureSpace MCP**](https://github.com/MeasureSpace/measure-space-mcp-server) | measurespace.io에서 제공하는 전 세계 날씨, 기후, 대기질 예보 및 geocoding 서비스를 제공하는 무료 MCP Server입니다. |
| [**NS Travel Information**](https://github.com/r-huijts/ns-mcp-server) | 공식 NS API를 통해 네덜란드 철도(NS) 실시간 열차 운행 정보 및 운행 장애 정보를 조회합니다. |
| [**OlaMaps**](https://pypi.org/project/ola-maps-mcp-server) | geocode, 경로 안내, 장소 상세 정보 등을 제공하는 공식 Ola Maps MCP Server입니다. |
| [**peek-travel/mcp-intro**](https://github.com/peek-travel/mcp-intro) | 집이나 여행지에서 체험을 발견하고 계획할 수 있는 원격 MCP Server입니다. |
| [**pzalutski-pixel/javalens-mcp**](https://github.com/pzalutski-pixel/javalens-mcp) | Eclipse JDT를 통한 56개의 시맨틱 Java 분석 도구. AI 에이전트를 위한 컴파일러 수준의 정확한 탐색, 리팩토링, 참조 찾기, 호출 계층 및 코드 메트릭을 제공합니다. |
| [**pzalutski-pixel/sharplens-mcp**](https://github.com/pzalutski-pixel/sharplens-mcp) | Roslyn을 통한 58개의 시맨틱 C#/.NET 분석 도구. AI 에이전트를 위한 탐색, 리팩토링, 사용처 찾기 및 코드 인텔리전스를 제공합니다. |
| [**Scrapeless**](https://github.com/scrapeless-ai/scrapeless-mcp-server) | 실시간 Scrapeless Google SERP(Google Search, Google Flight, Google Map, Google Jobs 등) 결과를 LLM 애플리케이션에 통합합니다. AI 워크플로우를 위한 동적 컨텍스트 검색을 지원합니다. |
| [**Sourcerer**](https://github.com/st3v3nmw/sourcerer-mcp) | 토큰 낭비를 줄이는 시맨틱 코드 검색 및 탐색을 위한 MCP입니다. |
| [**stadiamaps/stadiamaps-mcp-server-ts**](https://github.com/stadiamaps/stadiamaps-mcp-server-ts) | Stadia Maps 위치 API를 위한 MCP 서버 - geocoding으로 주소 및 장소 조회, 시간대 검색, 경로 생성 및 정적 지도 제공 |
| [**stass/exif-mcp**](https://github.com/stass/exif-mcp) | EXIF, XMP, JFIF, GPS 등 이미지 메타데이터를 검사할 수 있는 MCP 서버입니다. LLM 기반 사진 라이브러리 및 이미지 컬렉션 검색과 분석의 기반을 제공합니다. |
| [**Terminal-Control**](https://github.com/GongRzhe/terminal-controller-mcp) | 표준화된 인터페이스를 통해 안전한 터미널 명령 실행, 디렉토리 탐색 및 파일 시스템 작업을 지원하는 MCP 서버입니다. |
| [**TomTom-MCP**](https://github.com/tomtom-international/tomtom-mcp) | TomTom MCP Server는 검색, 경로, 교통 및 정적 지도 데이터를 포함한 TomTom 위치 서비스에 대한 원활한 접근을 제공하여 지리공간 개발을 간소화합니다. |
| [**Travel Planner**](https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server) | Google Maps API와 통합하여 장소 검색, 장소 상세 정보 및 경로 계산 기능을 제공하는 여행 계획 및 일정 관리 서버입니다. |
| [**Triplyfy MCP**](https://github.com/helpful-AIs/triplyfy-mcp) | LLM이 Triplyfy에서 인터랙티브 지도와 함께 일정을 계획하고 관리할 수 있는 MCP 서버입니다. 일정, 장소, 메모 관리 및 항공편 검색/저장을 지원합니다. |
| [**VariFlight**](https://github.com/variflight/variflight-mcp) | VariFlight 공식 MCP 서버로, 항공편 정보, 기상 데이터, 쾌적도 지표, 최저 운임 및 기타 민간 항공 관련 데이터를 조회하는 도구를 제공합니다. |
| [**webcoderz/MCP-Geo**](https://github.com/webcoderz/MCP-Geo) | Nominatim, ArcGIS, Bing을 위한 Geocoding MCP 서버입니다. |
| [**zelentsov-dev/asc-mcp**](https://github.com/zelentsov-dev/asc-mcp) | 208개 도구를 갖춘 App Store Connect API 서버로, 앱, 빌드, TestFlight, 구독, 리뷰 등을 모든 MCP 클라이언트에서 직접 관리할 수 있습니다. |
| [**Zine**](https://www.zine.ai) | AI가 있는 곳 어디서나 사용할 수 있는 나만의 메모리. 지식을 위한 iPhoto처럼 업로드하고 큐레이션하세요. ChatGPT처럼 사용하되 휴대 가능한 컨텍스트입니다. |

---

## 🔌 IoT & 하드웨어

> Home Assistant, ESP32 등 IoT/스마트홈/임베디드

| 서버 | 설명 |
|------|------|
| [**adancurusul/embedded-debugger-mcp**](https://github.com/adancurusul/embedded-debugger-mcp) | probe-rs를 활용한 임베디드 디버깅용 MCP 서버 - J-Link, ST-Link 등을 통한 ARM Cortex-M, RISC-V 디버깅을 지원합니다. |
| [**akramIOT/MCP_AI_SOC_Sher**](https://github.com/akramIOT/MCP_AI_SOC_Sher) | Text2SQL AI 에이전트를 위한 동적 AI SOC 보안 위협 분석을 수행하는 MCP Server입니다. |
| [**allenporter/mcp-server-home-assistant**](https://github.com/allenporter/mcp-server-home-assistant) | MCP Server를 통해 모든 Home Assistant 음성 인텐트를 노출하여 가정 제어를 가능하게 합니다. |
| [**altinoren/utopia**](https://github.com/altinoren/Utopia) | 스마트 홈 및 라이프스타일 기기 세트를 시뮬레이션하여 에이전트의 추론 및 탐색 능력을 테스트할 수 있는 MCP입니다. |
| [**Apache IoTDB**](https://github.com/apache/iotdb-mcp-server) | Apache IoTDB 데이터베이스 및 관련 도구를 위한 MCP Server입니다. |
| [**Aqara MCP Server**](https://github.com/aqara/aqara-mcp-server/) | 자연어를 사용하여 Aqara 스마트 홈 기기를 제어하고, 상태를 조회하고, 씬을 실행하는 등 다양한 기능을 수행합니다. |
| [**Aranet4**](https://github.com/diegobit/aranet4-mcp-server) | Aranet4 CO2 센서를 관리하는 MCP Server입니다. 데이터를 가져와 로컬 SQLite에 저장하고, 히스토리 데이터에 대해 질문할 수 있습니다. |
| [**Arduino**](https://github.com/vishalmysore/choturobo) | Claude AI와 Arduino (ESP32)를 활용한 AI 기반 로보틱스를 지원하는 MCP Server로, 실세계 자동화 및 로봇 상호작용을 구현합니다. |
| [**CCTV VMS MCP**](https://github.com/jyjune/mcp_vms) | CCTV 녹화 프로그램(VMS)에 연결하여 녹화 및 실시간 영상 스트림을 가져오도록 설계된 MCP 서버입니다. VMS 소프트웨어 제어 도구도 제공합니다. |
| [**ConstantineB6/comfy-pilot**](https://github.com/ConstantineB6/comfy-pilot) | AI 에이전트가 내장 터미널로 노드 기반 이미지 생성 워크플로우를 보고, 편집하고, 실행할 수 있는 ComfyUI용 MCP 서버입니다. |
| [**ESP MCP Server**](https://github.com/horw/esp-mcp) | LLM을 활용하여 ESP 마이크로컨트롤러의 코드 빌드 및 플래시 등 ESP IDF 명령을 통합하는 MCP 서버입니다. |
| [**ESP RainMaker**](https://github.com/espressif/esp-rainmaker-mcp) | ESP RainMaker 기기를 제어하고 관리하기 위한 Espressif 공식 MCP Server입니다. |
| [**Fibaro HC3**](https://github.com/coding-sailor/mcp-server-hc3) | Fibaro Home Center 3 스마트 홈 시스템을 위한 MCP 서버입니다. |
| [**Home Assistant**](https://github.com/tevonsb/homeassistant-mcp) | 조명, 스위치, 센서 및 기타 모든 Home Assistant 엔티티의 조회 및 제어를 포함하여 Home Assistant와 상호작용합니다. |
| [**Home Assistant**](https://github.com/voska/hass-mcp) | 엔티티 관리, 도메인 요약, 자동화 지원 및 가이드 대화 기능을 갖춘 Docker 지원 Home Assistant MCP 서버입니다. 간편한 설치를 위한 사전 빌드 컨테이너 이미지를 포함합니다. |
| [**Homey**](https://github.com/pigmej/python-homey-mcp) | Homey와 상호작용하여 스마트 홈 시스템을 제어합니다. 기기, 플로우, 존을 지원하며, LLM과의 통합을 위한 편의 기능을 포함합니다. |
| [**longevity-genie/biothings-mcp**](https://github.com/longevity-genie/biothings-mcp) | 유전자, 유전 변이, 약물, 분류학 정보를 포함한 BioThings API와 상호작용하는 MCP 서버입니다. |
| [**mcp-notify**](https://github.com/aahl/mcp-notify) | Weixin, DingTalk, Telegram, Bark, Lark, Feishu, Home Assistant을 지원하는 메시지 푸시용 MCP 서버입니다. |
| [**pomazanbohdan/memory-mcp-1file**](https://github.com/pomazanbohdan/memory-mcp-1file) | 단일 바이너리 아키텍처(임베디드 DB 및 모델, 의존성 없음)의 자체 포함 Memory 서버입니다. AI 에이전트를 위한 영구적 시맨틱 및 그래프 기반 메모리를 제공합니다. |
| [**Producer Pal**](https://github.com/adamjmurray/producer-pal) | Ableton Live를 제어하기 위한 MCP 서버로, 간편한 드래그 앤 드롭 설치를 위해 Max for Live 디바이스에 내장되어 있습니다. |
| [**stack-chan/stack-chan**](https://github.com/stack-chan/stack-chan) | AI 제어 상호작용 및 감정 표현을 위한 MCP 서버 기능을 갖춘 JavaScript 기반 M5Stack 임베디드 초귀여운 로봇입니다. |
| [**ThingsBoard**](https://github.com/thingsboard/thingsboard-mcp) | ThingsBoard MCP Server는 LLM 및 AI 에이전트가 ThingsBoard IoT 플랫폼과 자연어로 상호작용할 수 있는 인터페이스를 제공합니다. |
| [**ThinQ Connect**](https://github.com/thinq-connect/thinqconnect-mcp) | ThinQ Connect MCP 서버를 통해 LG ThinQ 스마트 홈 기기 및 가전제품과 상호작용합니다. |
| [**Tommertom/plugwise-mcp**](https://github.com/Tommertom/plugwise-mcp) | 자동 네트워크 탐색 기능을 갖춘 Plugwise 기기용 TypeScript 기반 스마트 홈 자동화 서버입니다. 온도 조절기, 스위치, 스마트 플러그, 에너지 모니터링, 멀티 허브 관리, 로컬 네트워크 통합을 통한 실시간 기후/전력 소비 추적을 지원합니다. |
| [**Yeelight MCP Server**](https://github.com/Yeelight/yeelight-iot-mcp) | 공식 Yeelight MCP Server로, 사용자가 자연어를 통해 Yeelight 스마트 기기를 제어하고 조회할 수 있어 원활하고 효율적인 인간-AI 상호작용 경험을 제공합니다. |

---

## 🏥 헬스 & 의료

> FHIR, 건강 데이터 등 의료/헬스케어

| 서버 | 설명 |
|------|------|
| [**AI Endurance**](https://github.com/ai-endurance/mcp) | 러너, 사이클리스트, 트라이애슬리트를 위한 AI 기반 트레이닝 플랫폼으로, 운동 관리, 활동 분석, 성능 예측, 회복 추적을 위한 20개 이상의 도구를 제공합니다. |
| [**andybrandt/mcp-simple-pubmed**](https://github.com/andybrandt/mcp-simple-pubmed) | PubMed에서 의학/생명과학 논문을 검색하고 읽기 위한 MCP입니다. |
| [**ArchAI-Labs/fastmcp-sonarqube-metrics**](https://github.com/ArchAI-Labs/fastmcp-sonarqube-metrics) | SonarQube 프로젝트의 메트릭(현재 및 히스토리), 이슈, 상태 정보를 조회하는 도구 세트를 제공하는 MCP 서버입니다. |
| [**CIViC**](https://github.com/QuentinCody/civic-mcp-server) | 임상 변이 해석 및 암 연구를 위한 유전체 증거를 제공하는 CIViC(Clinical Interpretation of Variants in Cancer) 데이터베이스용 MCP 서버입니다. |
| [**consul-mcp**](https://github.com/kocierik/consul-mcp-server) | 서비스 관리, 헬스 체크, Key-Value Store를 위한 Consul MCP 서버입니다. |
| [**context-rot-detection**](https://github.com/milos-product-maker/context-rot-detection) | AI 에이전트에게 인지 상태에 대한 자기 인식을 제공합니다. 토큰 사용량, 컨텍스트 품질 저하, 세션 피로도를 모니터링합니다. 모델별 저하 곡선을 기반으로 상태 점수(0-100)와 복구 권장 사항을 반환합니다. |
| [**crystaldba/postgres-mcp**](https://github.com/crystaldba/postgres-mcp) | 성능 분석, 튜닝, 상태 점검 도구를 갖춘 Postgres 개발 및 운영을 위한 올인원 MCP 서버입니다. |
| [**csjoblom/musclesworked-mcp**](https://github.com/csjoblom/musclesworked-mcp) | 운동-근육 매핑 MCP 서버입니다. 65개 근육과 14개 근육군에 걸친 856개 운동의 사용 근육을 조회하고, 운동 프로그램의 갭을 분석하며, 근육 겹침 기준으로 순위가 매겨진 대체 운동을 찾습니다. |
| [**Dicom**](https://github.com/ChristianHinge/dicom-mcp) | 의료 영상을 조회 및 검색하고, DICOM 캡슐화 문서(PDF 등)를 파싱하고 읽는 MCP 서버입니다. |
| [**Domain Tools**](https://github.com/deshabhishek007/domain-tools-mcp-server) | WHOIS, DNS 레코드, DNS 상태 점검을 포함한 종합 도메인 분석을 위한 MCP 서버입니다. |
| [**Entrez**](https://github.com/QuentinCody/entrez-mcp-server) | NCBI E-utilities API를 통해 PubMed 논문, 유전자 정보, 단백질 데이터 및 기타 생명의학 연구 자원에 접근할 수 있는 비공식 NCBI Entrez 데이터베이스용 MCP 서버입니다. |
| [**FHIR**](https://github.com/wso2/fhir-mcp-server) | 호환 FHIR 서버에서 FHIR(Fast Healthcare Interoperability Resources) 데이터에 대한 원활하고 표준화된 접근을 제공하는 MCP 서버입니다. 간편한 통합을 위해 설계되었습니다. |
| [**FHIR MCP**](https://github.com/the-momentum/fhir-mcp-server) | AI 에이전트를 FHIR 서버에 연결하는 MCP Server입니다. |
| [**Fulcra Context**](https://github.com/fulcradynamics/fulcra-context-mcp) | 개인 건강, 운동, 수면, 위치 등의 데이터에 비공개로 접근할 수 있는 Fulcra Context MCP 서버입니다. Context by Fulcra 기반으로 구축되었습니다. |
| [**genomoncology/biomcp**](https://github.com/genomoncology/biomcp) | PubMed, ClinicalTrials.gov, MyVariant.info에 접근할 수 있는 생명의학 연구용 MCP 서버입니다. |
| [**JamesANZ/medical-mcp**](https://github.com/JamesANZ/medical-mcp) | 의료 정보, 약물 데이터베이스, 의료 자원에 접근할 수 있는 MCP 서버입니다. AI 어시스턴트가 의료 데이터, 약물 상호작용, 임상 가이드라인을 조회할 수 있도록 합니다. |
| [**JamsusMaximus/trainingpeaks-mcp**](https://github.com/JamsusMaximus/trainingpeaks-mcp) | Claude Desktop을 통해 TrainingPeaks 운동 조회, CTL/ATL/TSB 피트니스 메트릭 분석, 파워/페이스 PR 비교를 수행합니다. |
| [**khaoss85/arvo-mcp**](https://github.com/khaoss85/arvo-mcp) | Arvo를 위한 AI 운동 코치 MCP 서버입니다. Claude Desktop을 통해 트레이닝 데이터, 운동 기록, 개인 기록, 체형 변화, 29개 피트니스 도구에 접근합니다. |
| [**Milofax/xert-mcp**](https://github.com/Milofax/xert-mcp) | XERT 사이클링 분석용 MCP 서버 - 피트니스 시그니처(FTP, HIE, PP), 트레이닝 상태, 운동, XSS 메트릭 기반 활동, MPA 분석에 접근합니다. |
| [**mimilabs**](https://www.mimilabs.ai/mcp) | 50개 이상의 정부 출처와 수천 개의 공개 미국 의료 데이터셋(정부 지원 프로그램, 정책, 약가, 임상시험 등)을 위한 미국 의료 데이터 탐색 가이드입니다. |
| [**NCI GDC**](https://github.com/QuentinCody/nci-gdc-mcp-server) | 종양학 연구를 위한 통합 암 유전체 및 임상 데이터에 접근할 수 있는 비공식 NCI(National Cancer Institute) GDC(Genomic Data Commons) MCP 서버입니다. |
| [**OMOP MCP**](https://github.com/OHNLP/omop_mcp) | 의료 데이터 표준화를 위해 LLM을 활용하여 임상 용어를 OMOP 개념에 매핑합니다. |
| [**Open Targets**](https://github.com/QuentinCody/open-targets-mcp-server) | 생명의학 연구를 위한 타겟-질병 연관성, 신약 발견 데이터 및 치료 가설 생성에 접근할 수 있는 비공식 Open Targets Platform MCP 서버입니다. |
| [**smith-and-web/obsidian-mcp-server**](https://github.com/smith-and-web/obsidian-mcp-server) | 노트, 디렉토리, Frontmatter, 태그, 검색, 링크 작업을 위한 29개 도구를 갖춘 원격 Obsidian 볼트 관리용 SSE 지원 MCP 서버입니다. Docker 지원 및 상태 모니터링을 포함합니다. |
| [**Strava**](https://github.com/r-huijts/strava-mcp) | Strava API에 연결하여 활동 데이터, 선수 프로필, 세그먼트, 루트에 접근하고 Claude를 통한 피트니스 추적 및 분석을 지원합니다. |
| [**System Health**](https://github.com/thanhtung0201/mcp-remote-system-health) | 원격 Linux 서버에 대한 종합적인 상태 메트릭과 알림을 제공하도록 설계된 강력한 실시간 시스템 상태 모니터링 솔루션입니다. |
| [**TeamRetro**](https://github.com/adepanges/teamretro-mcp-server) | LLM이 TeamRetro와 상호작용할 수 있는 MCP 서버로, 사용자, 팀, 팀원, 회고, 헬스 체크, 액션, 합의 관리 및 보고서 조회를 지원합니다. |
| [**the-momentum/apple-health-mcp-server**](https://github.com/the-momentum/apple-health-mcp-server) | Apple Health에서 내보낸 데이터에 접근할 수 있는 MCP 서버입니다. 데이터 분석 기능을 포함합니다. |
| [**vitorpavinato/ncbi-mcp-server**](https://github.com/vitorpavinato/ncbi-mcp-server) | 고급 분석, 캐싱, MeSH 통합, 관련 논문 탐색, 일괄 처리를 갖춘 종합 NCBI/PubMed 문헌 검색 서버로, 모든 생명과학 및 생명의학 연구를 지원합니다. |
| [**wenb1n-dev/SmartDB_MCP**](https://github.com/wenb1n-dev/SmartDB_MCP) | 다중 데이터베이스 동시 연결을 지원하는 범용 데이터베이스 MCP 서버입니다. 데이터베이스 작업, 상태 분석, SQL 최적화 등의 도구를 제공합니다. MySQL, PostgreSQL, SQL Server, MariaDB, Dameng, Oracle 등 주류 데이터베이스와 호환됩니다. Streamable HTTP, SSE, STDIO를 지원하고, OAut... |
| [**wenhuwang/mcp-k8s-eye**](https://github.com/wenhuwang/mcp-k8s-eye) | Kubernetes 관리 및 클러스터, 애플리케이션 상태 분석을 위한 MCP Server입니다. |
| [**Withings**](https://github.com/akutishevsky/withings-mcp) | 자연어 대화를 통해 수면 분석, 체성분 측정, 운동, ECG 기록, 피트니스 목표 등 Withings 건강 데이터에 접근하고 분석합니다. |

---

## ⚖️ 법률 & 계약

> 전자서명, 계약 관리, 법률 서비스

| 서버 | 설명 |
|------|------|
| [**Backdocket**](https://ai.backdocket.com) | Backdocket 데이터를 검색, 조회, 업데이트합니다. 현재 클레임, 사건, 연락처, 작업 및 고급 검색을 지원합니다. |
| [**BoldSign**](https://github.com/boldsign/boldsign-mcp) | BoldSign으로 전자서명 계약서를 손쉽게 검색, 요청 및 관리합니다. |
| [**buildsyncinc/gibs-mcp**](https://github.com/buildsyncinc/gibs-mcp) | 조항별 인용이 포함된 규제 준수(AI Act, GDPR, DORA) 서버입니다. |
| [**ejcho623/agent-breadcrumbs**](https://github.com/ejcho623/agent-breadcrumbs) | ChatGPT, Claude, Cursor, Codex, OpenClaw 전반에 걸친 통합 에이전트 작업 로깅 및 관측성. 설정 우선 스키마와 플러그형 싱크를 지원합니다. |
| [**JamesANZ/us-legal-mcp**](https://github.com/JamesANZ/us-legal-mcp) | 포괄적인 미국 법률을 제공하는 MCP 서버입니다. |
| [**KRS Poland**](https://github.com/pkolawa/krs-poland-mcp-server) | 폴란드 국가법원등기부(KRS)에 접근합니다 - 모든 기업, 재단 및 기타 법인의 정부 공식 등기부입니다. |
| [**olgasafonova/gleif-mcp-server**](https://github.com/olgasafonova/gleif-mcp-server) | GLEIF 공개 API를 통해 기업 인증, KYC, 기업 소유권 조사를 위한 글로벌 법인식별코드(LEI) 데이터베이스에 접근합니다. |

---

## 🎓 교육 & 연구

> arXiv, 논문, 학습 도구 등 교육/연구

| 서버 | 설명 |
|------|------|
| [**aaronjmars/web3-research-mcp**](https://github.com/aaronjmars/web3-research-mcp) | 암호화폐를 위한 Deep Research - 무료 및 완전 로컬 실행 |
| [**abhiphile/fermat-mcp**](https://github.com/abhiphile/fermat-mcp) | SymPy, NumPy, Matplotlib을 하나의 강력한 서버로 통합한 궁극의 수학 엔진입니다. 기호 대수, 수치 계산, 데이터 시각화가 필요한 개발자와 연구자에게 적합합니다. |
| [**Agent Interviews**](https://github.com/thinkchainai/agentinterviews_mcp) | Agent Interviews를 통해 AI 기반 정성 조사 인터뷰와 설문조사를 대규모로 수행합니다. |
| [**ai-Bible**](https://github.com/AdbC99/ai-bible) | ai-Bible Labs에서 성경을 안정적이고 반복 가능하게 검색합니다. |
| [**andybrandt/mcp-simple-arxiv**](https://github.com/andybrandt/mcp-simple-arxiv) | LLM이 arXiv에서 논문을 검색하고 읽기 위한 MCP입니다. |
| [**Apple Books**](https://github.com/vgnshiyer/apple-books-mcp) | Apple Books 라이브러리와 상호작용하여 도서 컬렉션 관리, 하이라이트 요약, 메모 등 다양한 기능을 수행합니다. |
| [**arXiv API**](https://github.com/prashalruchiranga/arxiv-mcp-server) | 자연어로 arXiv API와 상호작용할 수 있는 MCP 서버입니다. |
| [**Bible**](https://github.com/trevato/bible-mcp) | 생성형 AI 애플리케이션에 성경 컨텍스트를 추가합니다. |
| [**bioRxiv**](https://github.com/JackKuo666/bioRxiv-MCP-Server) | 간단한 MCP 인터페이스를 통해 AI 어시스턴트가 bioRxiv 논문을 검색하고 접근할 수 있도록 합니다. |
| [**blazickjp/arxiv-mcp-server**](https://github.com/blazickjp/arxiv-mcp-server) | ArXiv 연구 논문을 검색합니다. |
| [**BrunoKrugel/echo-mcp**](https://github.com/BrunoKrugel/echo-mcp) | 기존 Echo 웹 프레임워크 API를 MCP 도구로 자동 노출하는 설정 불필요 Go 라이브러리입니다. |
| [**Canvas LMS**](https://github.com/ahnopologetic/canvas-lms-mcp) | Canvas LMS 인스턴스를 통해 교육 데이터에 쉽게 접근할 수 있는 MCP 서버입니다. |
| [**Catalysis Hub**](https://github.com/QuentinCody/catalysishub-mcp-server) | 계산 촉매 연구 및 표면 반응 데이터에 접근할 수 있는 Catalysis Hub 데이터베이스용 비공식 MCP 서버입니다. |
| [**ckanthony/gin-mcp**](https://github.com/ckanthony/gin-mcp) | 기존 Gin 웹 프레임워크 API를 MCP 도구로 자동 노출하는 설정 불필요 Go 라이브러리입니다. |
| [**clouatre-labs/math-mcp-learning-server**](https://github.com/clouatre-labs/math-mcp-learning-server) | 수학 연산, 통계, 시각화, 영구 워크스페이스를 위한 교육용 MCP 서버입니다. FastMCP 2.0으로 구축되었습니다. |
| [**Congress**](https://github.com/amurshak/congressMCP) | Congress.gov에서 입법 데이터를 조회하고 분석합니다. |
| [**Congress.gov API**](https://github.com/AshwinSundar/congress_gov_mcp) | 미국 의회 공식 API인 Congress.gov API에서 실시간 데이터와 상호작용하는 MCP 서버입니다. |
| [**CVE Intelligence Server**](https://github.com/gnlds/mcp-cve-intelligence-server-lite) | MCP를 통해 다중 소스 CVE 데이터, 필수 익스플로잇 탐색, EPSS 위험 점수를 제공하는 취약점 인텔리전스 서버입니다. 보안 연구, 자동화, 에이전트 워크플로우에 유용합니다. |
| [**DataCite**](https://github.com/QuentinCody/datacite-mcp-server) | 학술 연구 검색을 위해 DataCite의 REST API 및 GraphQL 인터페이스를 통해 연구 데이터 및 출판 메타데이터에 접근하는 비공식 DataCite MCP 서버입니다. |
| [**Deep Research**](https://github.com/reading-plus-ai/mcp-server-deep-research) | Grok/OpenAI/Gemini/Perplexity 스타일의 자동화된 딥 리서치 탐색 및 구조화된 보고서를 제공하는 경량 MCP 서버입니다. |
| [**DeepResearch**](https://github.com/OctagonAI/octagon-deep-research-mcp) | 초고속, 고정확도 Deep Research 에이전트 - 8~10배 빠른 속도, 더 깊은 분석과 정확도, 무제한 병렬 실행 |
| [**devroopsaha744/TexMCP**](https://github.com/devroopsaha744/TexMCP) | LaTeX를 고품질 PDF 문서로 변환하는 MCP 서버입니다. 원시 LaTeX 입력 및 커스터마이징 가능한 템플릿 렌더링 도구를 제공하여 보고서, 이력서, 연구 논문 등 공유 및 프로덕션 준비된 아티팩트를 생성합니다. |
| [**DGIdb**](https://github.com/QuentinCody/dgidb-mcp-server) | 약물-유전자 상호작용 데이터, 약물 가능 유전체 정보, 약물유전체학 연구에 접근할 수 있는 DGIdb(Drug Gene Interaction Database) MCP 서버입니다. |
| [**Discourse**](https://github.com/AshDevFr/discourse-mcp-server) | Discourse 포럼에서 게시글을 검색하는 MCP 서버입니다. |
| [**discourse/discourse-mcp**](https://github.com/discourse/discourse-mcp) | 포럼 통합을 위한 공식 Discourse MCP 서버입니다. 주제 검색, 게시글 읽기, 카테고리 및 태그 관리, 사용자 탐색, Discourse 커뮤니티와의 상호작용을 지원합니다. |
| [**EduBase**](https://github.com/EduBase/MCP) | 고급 퀴즈, 시험 관리, 콘텐츠 구성 기능을 갖춘 종합 e-러닝 플랫폼 EduBase와 상호작용합니다. |
| [**Embassy-of-the-Free-Mind/sourcelibrary-v2**](https://github.com/Embassy-of-the-Free-Mind/sourcelibrary-v2/tree/main/mcp-server) | Source Library에서 DOI 기반 학술 인용과 함께 희귀 역사 문헌(연금술, 헤르메티시즘, 르네상스 철학)을 검색하고 인용합니다. |
| [**g1itchbot8888-del/agent-memory**](https://github.com/g1itchbot8888-del/agent-memory) | 시맨틱 검색, 그래프 관계, 충돌 감지, LearningMachine을 갖춘 에이전트용 3계층 메모리 시스템(아이덴티티/활성/아카이브)입니다. 에이전트가 에이전트를 위해 구축했습니다. API 키 불필요. |
| [**gemy411/multi-research-agents**](https://github.com/gemy411/multi-agents-research) | 코딩이나 일반 리서치에 사용할 수 있는 유연한 리서치 시스템에서 멀티에이전트 방식을 적용한 Kotlin으로 작성된 KTOR 서버/MCP 서버입니다. |
| [**Google-Scholar**](https://github.com/JackKuo666/Google-Scholar-MCP-Server) | 간단한 MCP 인터페이스를 통해 AI 어시스턴트가 Google Scholar 논문을 검색하고 접근할 수 있도록 합니다. |
| [**Google-Scholar**](https://github.com/mochow13/google-scholar-mcp) | Streamable HTTP transport를 사용하는 TypeScript 기반 Google Scholar MCP 서버와, 서버와 통합되어 Gemini-2.5-flash와 상호작용하는 클라이언트 구현을 포함합니다. |
| [**hanzili/comet-mcp**](https://github.com/hanzili/comet-mcp) | 에이전트 기반 웹 브라우징, 딥 리서치 및 실시간 작업 모니터링을 위해 Perplexity Comet 브라우저에 연결합니다. |
| [**hbg/mcp-paperswithcode**](https://github.com/hbg/mcp-paperswithcode) | PapersWithCode API를 검색하기 위한 MCP입니다. |
| [**jen6/ticktick-mcp**](https://github.com/jen6/ticktick-mcp) | TickTick MCP 서버입니다. ticktick-py 라이브러리를 기반으로 구축되어 대폭 향상된 필터링 기능을 제공합니다. |
| [**kimtth/mcp-remote-call-ping-pong**](https://github.com/kimtth/mcp-remote-call-ping-pong) | 원격 MCP(Model Context Protocol) 호출을 시연하는 Ping-pong 서버 실험 및 교육용 앱입니다. |
| [**kwrds.ai**](https://github.com/mkotsollaris/kwrds_ai_mcp) | kwrds.ai를 위한 키워드 리서치, People Also Ask, SERP 및 기타 SEO 도구입니다. |
| [**Latex MCP Server**](https://github.com/Yeok-c/latex-mcp-server) | LaTeX 컴파일, 인용 논문 다운로드/정리/읽기, 시각화 스크립트 실행, 그림/표를 LaTeX에 추가하는 MCP Server입니다. |
| [**longevity-genie/gget-mcp**](https://github.com/longevity-genie/gget-mcp) | 인기 있는 gget 라이브러리를 래핑하여 유전체학 쿼리 및 분석을 위한 강력한 생물정보학 툴킷을 제공하는 MCP 서버입니다. |
| [**longevity-genie/opengenes-mcp**](https://github.com/longevity-genie/opengenes-mcp) | OpenGenes 프로젝트의 노화 및 장수 연구를 위한 쿼리 가능 데이터베이스 MCP 서버입니다. |
| [**magarcia/mcp-server-giphy**](https://github.com/magarcia/mcp-server-giphy) | Giphy API를 통해 Giphy의 방대한 라이브러리에서 GIF를 검색하고 가져옵니다. |
| [**mcp-open-library**](https://github.com/8enSmith/mcp-open-library) | AI 어시스턴트가 도서 및 저자 정보를 검색할 수 있도록 하는 Open Library API용 MCP 서버입니다. |
| [**medRxiv**](https://github.com/JackKuo666/medRxiv-MCP-Server) | 간단한 MCP 인터페이스를 통해 AI 어시스턴트가 medRxiv 논문을 검색하고 접근할 수 있도록 합니다. |
| [**microsoft/markitdown**](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) | 다양한 파일 형식(로컬 또는 원격)을 LLM 사용을 위해 Markdown으로 변환하는 라이브러리 MarkItDown에 대한 MCP 도구 접근입니다. |
| [**Morningstar**](https://github.com/Morningstar/morningstar-mcp-server) | Morningstar 리서치, 편집 콘텐츠 및 데이터포인트와 상호작용하는 MCP Server입니다. |
| [**Mtehabsim/ScreenPilot**](https://github.com/Mtehabsim/ScreenPilot) | 마우스 및 키보드 도구를 제공하여 AI가 GUI 상호작용을 완전히 제어하고 접근할 수 있도록 합니다. 범용 자동화, 교육, 실험에 적합합니다. |
| [**mzxrai/mcp-webresearch**](https://github.com/mzxrai/mcp-webresearch) | Google 검색 및 모든 주제에 대한 심층 웹 리서치를 수행합니다. |
| [**Nebula-Block-Data/nebulablock-mcp-server**](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) | fastmcp 라이브러리와 통합하여 NebulaBlock API의 전체 기능을 접근 가능한 도구로 노출합니다. |
| [**Octagon**](https://github.com/OctagonAI/octagon-mcp-server) | 광범위한 비공개 및 공개 시장 데이터와 함께 실시간 투자 리서치를 제공합니다. |
| [**Octocode**](https://github.com/bgauryy/octocode-mcp) | (by Guy Bary) GitHub 및 NPM 전반에서 실시간으로 고급 코드 리서치, 분석 및 검색을 수행하는 AI 기반 개발자 어시스턴트입니다. |
| [**omega-memory/omega-memory**](https://github.com/omega-memory/omega-memory) | 시맨틱 검색, 자동 캡처, 크로스 세션 학습, 지능형 망각을 갖춘 AI 코딩 에이전트를 위한 영구 메모리입니다. 12개 MCP 도구, 로컬 우선. |
| [**OneCite**](https://github.com/HzaCode/OneCite) | 범용 인용 관리 및 학술 참조 툴킷입니다. DOI, arXiv, 제목 또는 URL에서 BibTeX, APA, MLA 등 다양한 형식의 인용을 생성합니다. 7개 이상의 문헌 유형과 10개 이상의 학술 형식을 지원합니다. |
| [**OpenAlex.org MCP**](https://github.com/drAbreu/alex-mcp) | OpenAlex 데이터베이스를 활용하여 ML 기반 저자 구별 및 종합적인 연구자 프로필을 제공하는 전문 MCP 서버입니다. |
| [**OpenNeuro**](https://github.com/QuentinCody/open-neuro-mcp-server) | 신경과학 연구 및 분석을 위한 공개 뇌영상 데이터셋, 연구 메타데이터, 뇌영상 데이터에 접근할 수 있는 비공식 OpenNeuro MCP 서버입니다. |
| [**OpenZIM MCP**](https://github.com/cameronrye/openzim-mcp) | AI 모델이 Wikipedia 및 교육 콘텐츠 아카이브를 포함한 ZIM 형식 지식 기반에 오프라인으로 접근하고 검색할 수 있는 최신의 안전한 고성능 MCP 서버입니다. |
| [**pallaprolus/mendeley-mcp**](https://github.com/pallaprolus/mendeley-mcp) | Mendeley 참조 관리자용 MCP 서버입니다. 라이브러리 검색, 폴더 탐색, 문서 메타데이터 조회, 글로벌 카탈로그 검색, 컬렉션에 논문 추가를 지원합니다. |
| [**Pantheon-Security/notebooklm-mcp-secure**](https://github.com/Pantheon-Security/notebooklm-mcp-secure) | 포스트 양자 암호화(ML-KEM-768), GDPR/SOC2/CSSF 준수, 14개 보안 계층을 갖춘 보안 강화 NotebookLM MCP입니다. Claude 및 AI 에이전트에서 Google의 Gemini 기반 리서치를 조회합니다. |
| [**Paperless-MCP**](https://github.com/baruchiro/paperless-mcp) | Paperless-NGX API 서버와 상호작용하는 MCP 서버입니다. Paperless-NGX 인스턴스의 문서, 태그, 발신자, 문서 유형 관리 도구를 제공합니다. |
| [**Parallel Task MCP**](https://github.com/parallel-web/task-mcp) | Deep Research 및 일괄 작업을 시작합니다. |
| [**PDMT**](https://github.com/paiml/pdmt) | 실용적 결정론적 MCP 템플릿 - 종합 todo 검증, 품질 강제, 재현 가능한 출력을 위한 0.0 temperature 생성을 갖춘 고성능 결정론적 템플릿 라이브러리입니다. |
| [**Pharos**](https://github.com/QuentinCody/pharos-mcp-server) | NCATS(National Center for Advancing Translational Sciences)의 Pharos 데이터베이스용 비공식 MCP 서버로, 신약 발견 연구를 위한 타겟, 약물, 질병 정보에 접근할 수 있습니다. |
| [**pi22by7/In-Memoria**](https://github.com/pi22by7/In-Memoria) | AI 코딩 어시스턴트에게 누적 메모리와 패턴 학습을 제공하는 에이전트 개발용 영구 인텔리전스 인프라입니다. 시맨틱 분석과 점진적 코드베이스 이해를 위해 SQLite + SurrealDB를 사용하는 로컬 우선 스토리지의 하이브리드 TypeScript/Rust 구현입니다. |
| [**pminervini/deep-research-mcp**](https://github.com/pminervini/deep-research-mcp) | 웹 검색 및 코드 인터프리터를 지원하는 OpenAI Responses API 또는 Open Deep Research (smolagents)용 딥 리서치 MCP 서버입니다. |
| [**PromptHouse**](https://github.com/newtype-01/prompthouse-mcp) | AI 클라이언트와 MCP 통합을 지원하는 개인 프롬프트 라이브러리입니다. |
| [**r-huijts/ethics-check-mcp**](https://github.com/r-huijts/ethics-check-mcp) | 편향, 유해 콘텐츠를 감지하고 자동화된 패턴 학습을 통해 비판적 사고 평가를 제공하는 AI 대화의 종합 윤리 분석용 MCP 서버입니다. |
| [**Random Number**](https://github.com/zazencodes/random-number-mcp) | Python 표준 라이브러리만으로 구축된 LLM을 위한 필수 랜덤 생성 기능을 제공합니다. |
| [**RCSB PDB**](https://github.com/QuentinCody/rcsb-pdb-mcp-server) | 3D 단백질 구조, 실험 데이터 및 구조 생물정보학에 접근할 수 있는 비공식 RCSB PDB(Research Collaboratory for Structural Bioinformatics Protein Data Bank) MCP 서버입니다. |
| [**Rember**](https://github.com/rember/rember-mcp) | 채팅에서 배운 내용을 기억하기 위해 Rember에서 간격 반복 플래시카드를 생성합니다. |
| [**RivalSearchMCP**](https://github.com/damionrashford/RivalSearchMCP) | 웹 검색, 콘텐츠 검색, 자동화된 리서치 워크플로우를 위한 도구 모음을 제공하는 강력한 MCP 서버입니다. |
| [**Salesforce MCP (AiondaDotCom)**](https://github.com/AiondaDotCom/mcp-salesforce) | OAuth 인증, 스마트 학습 시스템, 종합 백업, 커스텀 오브젝트 및 필드를 포함한 모든 Salesforce 조직에 대한 전체 CRUD 작업을 지원하는 범용 Salesforce 통합입니다. |
| [**Scholarly**](https://github.com/adityak74/mcp-scholarly) | 학술 및 학문 논문을 검색하는 MCP 서버입니다. |
| [**ScrapeGraphAI**](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | 자연어를 사용하여 스크래핑 파이프라인을 생성하는 AI 기반 웹 스크래핑 라이브러리입니다. |
| [**SunflowersLwtech/mcp_creator_growth**](https://github.com/SunflowersLwtech/mcp_creator_growth) | AI 코딩 어시스턴트를 위한 지능형 학습 사이드카입니다. 인터랙티브 차단 퀴즈를 통해 AI가 생성한 코드 변경 사항을 개발자가 학습하도록 돕고, 사일런트 RAG 도구를 사용하여 에이전트에 프로젝트별 영구 디버깅 메모리를 제공합니다. 56% 토큰 최적화 및 다국어 지원을 제공합니다. |
| [**TAM MCP Server**](https://github.com/gvaibhav/TAM-MCP-Server) | Alpha Vantage, BLS, Census Bureau, FRED, IMF, Nasdaq Data Link, OECD, World Bank 등 8개 경제 데이터 소스를 통합한 TAM/SAM 계산 및 시장 조사와 비즈니스 인텔리전스를 제공합니다. |
| [**theagenttimes/tat-mcp-server**](https://github.com/theagenttimes/tat-mcp-server) | 에이전트 경제를 다루는 AI 네이티브 신문 The Agent Times에서 기사, 검증된 통계, 와이어 피드, 소셜 도구를 조회합니다. 검색, 댓글, 인용, 에이전트 리더보드 등 13개 도구를 포함합니다. API 키 불필요. |
| [**UniProt**](https://github.com/QuentinCody/uniprot-mcp-server) | 단백질체학 및 생물정보학 연구를 위한 단백질 서열 데이터, 기능 주석, 분류학 정보, 교차 참조에 접근할 수 있는 비공식 UniProt MCP 서버입니다. |
| [**varun29ankuS/shodh-memory**](https://github.com/varun29ankuS/shodh-memory) | Hebbian 학습, 3계층 아키텍처, 지식 그래프를 갖춘 AI 에이전트용 인지 메모리입니다. 단일 약 15MB 바이너리로 엣지 디바이스에서 오프라인 실행됩니다. |
| [**Vectorize**](https://github.com/vectorize-io/vectorize-mcp-server/) | 고급 검색, Private Deep Research, 다양한 파일 형식의 Markdown 변환, 텍스트 청킹을 위한 Vectorize MCP 서버입니다. |
| [**Wikidata SPARQL**](https://github.com/QuentinCody/wikidata-sparql-mcp-server) | 연구 및 데이터 분석을 위한 구조화된 지식 데이터, 엔티티 관계, 시맨틱 쿼리에 접근할 수 있는 비공식 Wikidata SPARQL 엔드포인트 원격 MCP 서버입니다. |
| [**Wikifunctions**](https://github.com/Fredibau/wikifunctions-mcp-fredibau) | AI 모델이 WikiFunctions 라이브러리의 함수를 탐색하고 실행할 수 있도록 합니다. |
| [**wyattjoh/jmap-mcp**](https://github.com/wyattjoh/jmap-mcp) | JMAP(JSON Meta Application Protocol) 이메일 서버와 상호작용하기 위한 도구를 제공하는 MCP 서버입니다. Deno와 jmap-jam 클라이언트 라이브러리로 구축되었습니다. |
| [**yamcp**](https://github.com/hamidra/yamcp) | Model Context 워크스페이스 관리자입니다. MCP 서버를 로컬 워크스페이스(코딩, 디자인, 리서치 등)로 구성하고, 통합 CLI를 통해 각 워크스페이스를 스캔, 모니터링, AI 앱과 통합합니다. |
| [**ZincBind**](https://github.com/QuentinCody/zincbind-mcp-server) | 단백질의 아연 결합 부위, 구조적 배위 데이터, 금속단백질체학 연구 정보에 대한 종합 데이터베이스에 접근할 수 있는 비공식 ZincBind MCP 서버입니다. |

---

## 🌤️ 날씨 & 시간

> 날씨 정보, 시간대 변환

| 서버 | 설명 |
|------|------|
| [**aliafsahnoudeh/wildfire-mcp-server**](https://github.com/aliafsahnoudeh/wildfire-mcp-server) | NASA FIRMS, OpenWeatherMap, Google Earth Engine 등 다양한 데이터 소스를 활용하여 전 세계 산불을 탐지, 모니터링, 분석하는 MCP 서버입니다. |
| [**bruno-portfolio/agrobr-mcp**](https://github.com/bruno-portfolio/agrobr-mcp) | LLM을 위한 브라질 농업 데이터 — CEPEA, CONAB, IBGE, INPE, B3 등 19개 공공 데이터 소스를 통한 가격, 작물 추정, 기후, 산림 벌채 정보를 제공합니다. |
| [**Chronulus AI**](https://github.com/ChronulusAI/chronulus-mcp) | Chronulus AI 예측 및 전망 에이전트를 사용하여 무엇이든 예측합니다. |
| [**Current Time UTC MCP Server**](https://github.com/jairampatel/currenttimeutc-mcp) | 정확한 UTC 시간과 timezone 변환을 실시간으로 제공하는 경량 MCP 서버입니다. |
| [**davidan90/time-node-mcp**](https://github.com/davidan90/time-node-mcp) | IANA timezone 지원, timezone 변환, 서머타임(DST) 처리를 갖춘 timezone 인식 날짜 및 시간 연산을 제공합니다. |
| [**jagan-shanmugam/climatiq-mcp-server**](https://github.com/jagan-shanmugam/climatiq-mcp-server) | Climatiq API를 통해 탄소 배출량을 계산하는 MCP 서버입니다. AI 어시스턴트가 실시간 탄소 계산을 수행하고 기후 영향 인사이트를 제공할 수 있게 합니다. |
| [**KnowAir Weather MCP**](https://github.com/shuowang-ai/Weather-MCP) | Caiyun Weather API 기반으로 실시간 날씨 데이터, 대기질 모니터링, 예보, 천문 정보를 제공하는 종합 MCP 서버입니다. |
| [**Lambda Capture**](https://github.com/lambda-capture/mcp-server) | Federal Reserve, Bank of England, ECB의 거시경제 전망 및 의미론적 컨텍스트를 제공합니다. |
| [**louiscklaw/hko-mcp**](https://github.com/louiscklaw/hko-mcp) | Hong Kong Observatory에서 날씨 정보를 가져오는 기본 데모를 포함한 MCP 서버입니다. |
| [**mcp-weather**](https://github.com/TimLukaHorstmann/mcp-weather) | AccuWeather API를 통한 정확한 날씨 예보를 제공합니다 (무료 티어 이용 가능). |
| [**mcp_weather**](https://github.com/isdaniel/mcp_weather_server) | https://api.open-meteo.com API에서 날씨 정보를 가져옵니다. |
| [**OpenWeather**](https://github.com/mschneider82/mcp-openweather) | 무료 openweathermap API와 연동하여 특정 위치의 현재 날씨 및 예보를 가져옵니다. |
| [**rossshannon/Weekly-Weather-mcp**](https://github.com/rossshannon/weekly-weather-mcp.git) | 전 세계 어디든 7일간의 상세 날씨 예보를 반환하는 주간 날씨 MCP 서버입니다. |
| [**saikiyusuke/registep-mcp**](https://github.com/saikiyusuke/registep-mcp) | Airレジ, スマレジ, BASE EC 연동을 위한 67개 도구를 갖춘 AI 기반 POS 및 매출 분석 MCP 서버입니다. 매장 관리, 매출 데이터 조회, AI 채팅 분석, 날씨 상관관계 기능을 제공합니다. |
| [**SaintDoresh/Weather-MCP-ClaudeDesktop**](https://github.com/SaintDoresh/Weather-MCP-ClaudeDesktop.git) | OpenWeatherMap API를 사용하여 실시간 날씨 데이터, 예보, 과거 날씨 정보를 제공하는 MCP 도구입니다. |
| [**SecretiveShell/MCP-timeserver**](https://github.com/SecretiveShell/MCP-timeserver) | 모든 timezone의 시간을 조회하고 현재 로컬 시간을 가져옵니다. |
| [**Time**](https://github.com/TheoBrigitte/mcp-time) | 자연어, 다양한 형식, timezone 변환 기능을 갖춘 시간 및 날짜 유틸리티를 제공하는 MCP 서버입니다. |
| [**weather-mcp-server**](https://github.com/devilcoder01/weather-mcp-server) | weatherapi를 사용하여 모든 위치의 실시간 날씨 데이터를 가져옵니다. |

---

## 🖥️ 시스템 & 데스크톱

> macOS/Linux/Windows 시스템 제어, 터미널, 클립보드

| 서버 | 설명 |
|------|------|
| [**akseyh/bear-mcp-server**](https://github.com/akseyh/bear-mcp-server) | AI가 Bear Notes에서 읽을 수 있게 합니다 (macOS 전용). |
| [**alvii147/piston-mcp**](https://github.com/alvii147/piston-mcp) | Piston 원격 코드 실행 엔진을 통해 LLM이 코드를 실행할 수 있게 하는 MCP 서버입니다. `uv`를 사용한 제로 설정 구성과 바로 사용 가능한 Claude Desktop 설정 예제를 포함합니다. |
| [**anki-mcp/anki-mcp-desktop**](https://github.com/anki-mcp/anki-mcp-desktop) | 자연어 상호작용, 종합적인 노트/덱 관리, 원클릭 MCPB 설치를 갖춘 엔터프라이즈급 Anki 통합입니다. NestJS 기반으로 포괄적인 테스트 커버리지를 제공합니다. |
| [**ChatMCP**](https://github.com/AI-QL/chat-mcp) | Linux, macOS, Windows와 호환되는 오픈소스 크로스 플랫폼 GUI 데스크톱 애플리케이션으로, 동적으로 선택 가능한 LLM을 통해 MCP 서버와 원활하게 상호작용할 수 있습니다. **AIQL** 제작. |
| [**Claude Thread Continuity**](https://github.com/peless/claude-thread-continuity) | Claude Desktop 대화를 세션 간에 전체 컨텍스트를 유지하며 재개할 수 있는 영속적 메모리 시스템입니다. 대화 이력, 프로젝트 상태, 사용자 설정을 관리합니다. |
| [**commands**](https://github.com/g0t4/mcp-server-commands) | 터미널에서처럼 명령어와 스크립트를 실행합니다. |
| [**computer-control-mcp**](https://github.com/AB498/computer-control-mcp) | PyAutoGUI, RapidOCR, ONNXRuntime을 사용하여 마우스, 키보드, OCR 등 컴퓨터 제어 기능을 제공하는 MCP 서버입니다. 외부 의존성이 필요 없습니다. |
| [**conversation-handoff-mcp**](https://github.com/trust-delta/conversation-handoff-mcp) | Claude Desktop 프로젝트 간 및 MCP 클라이언트 간에 대화 컨텍스트를 전달합니다. 메모리 기반으로 파일 잡동사니가 없습니다. |
| [**Cua**](https://github.com/trycua/cua/tree/main/libs/mcp-server) | Computer-Use Agent(CUA)용 MCP 서버로, Claude Desktop이나 다른 MCP 클라이언트를 통해 CUA를 실행할 수 있습니다. |
| [**Everything Search**](https://github.com/mamertofabian/mcp-everything-search) | Windows(Everything SDK 사용), macOS(mdfind 명령어 사용), Linux(locate/plocate 명령어 사용)에서 빠른 파일 검색 기능을 제공합니다. |
| [**fradser/mcp-server-apple-reminders**](https://github.com/FradSer/mcp-server-apple-reminders) | macOS에서 Apple 미리알림과 상호작용하기 위한 MCP 서버입니다. |
| [**Homebrew MCP**](https://github.com/jeannier/homebrew-mcp) | 자연어 명령을 사용하여 Homebrew(macOS 및 Linux용 패키지 관리자)와 상호작용합니다. |
| [**iMCP**](https://github.com/loopwork-ai/iMCP) | iMessage, 미리알림 및 기타 Apple 서비스를 위한 MCP 서버를 제공하는 macOS 앱입니다. |
| [**imprvhub/mcp-domain-availability**](https://github.com/imprvhub/mcp-domain-availability) | Claude Desktop에서 50개 이상의 TLD에 대한 도메인 가용성을 확인할 수 있는 MCP 서버입니다. DNS/WHOIS 검증, 대량 확인, 스마트 제안 기능을 갖추고 있습니다. uvx를 통한 제로 클론 설치. |
| [**imprvhub/mcp-rss-aggregator**](https://github.com/imprvhub/mcp-rss-aggregator) | Claude Desktop에서 RSS 피드를 수집하기 위한 MCP 서버입니다. |
| [**Intercom**](https://github.com/raoulbia-ai/mcp-server-for-intercom) | Intercom에서 고객 지원 티켓을 조회하기 위한 MCP 호환 서버입니다. Claude Desktop 및 Cline 같은 AI 어시스턴트가 Intercom 지원 티켓에 접근하고 분석할 수 있게 합니다. |
| [**iTerm MCP Server**](https://github.com/rishabkoul/iTerm-MCP-Server) | iTerm2 터미널 통합을 위한 MCP 서버 구현입니다. 여러 iTerm 세션을 관리할 수 있습니다. |
| [**joshuarileydev/mac-apps-launcher-mcp-server**](https://github.com/JoshuaRileyDev/mac-apps-launcher) | macOS에서 애플리케이션을 목록 조회하고 실행하기 위한 MCP 서버입니다. |
| [**Kaggle-mcp**](https://github.com/Seif-Sameh/Kaggle-mcp.git) | Kaggle API와 원활하게 통합되는 MCP 서버입니다. Claude Desktop 같은 MCP 호환 클라이언트를 통해 Kaggle 대회, 데이터셋, 커널, 모델과 상호작용할 수 있습니다. |
| [**mcp-get**](https://github.com/michaellatman/mcp-get) | MCP 서버를 설치하고 관리하기 위한 CLI 도구입니다. Claude Desktop을 위한 서버 설치 및 구성을 간소화합니다. |
| [**MCP-NixOS**](https://github.com/utensils/mcp-nixos) | NixOS 패키지, 시스템 옵션, Home Manager 설정, nix-darwin macOS 구성에 대한 정확한 실시간 정보를 AI 어시스턴트에 제공하는 MCP 서버입니다. |
| [**NakaokaRei/swift-mcp-gui**](https://github.com/NakaokaRei/swift-mcp-gui.git) | 키보드 입력, 마우스 이동 등의 명령을 실행할 수 있는 MCP 서버입니다. |
| [**PiloTY**](https://github.com/yiwenlu66/PiloTY) | 상태 유지 세션, SSH 연결, 백그라운드 프로세스 관리를 통해 에이전트가 대화형 터미널을 제어할 수 있게 하는 PTY 작업용 AI 파일럿입니다. |
| [**rusiaaman/wcgw**](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) | 자율적 셸 실행, 컴퓨터 제어 및 코딩 에이전트입니다. (Mac) |
| [**SearchUnify**](https://github.com/searchunify/su-mcp/) | SearchUnify를 Claude Desktop과 원활하게 통합하는 SearchUnify MCP 서버(su-mcp)입니다. |
| [**Shell**](https://github.com/rusiaaman/wcgw) | 자율적 셸 실행 및 컴퓨터 제어 (Mac) |
| [**spm-mcp**](https://github.com/simpleswift/spm-mcp) | Swift로 작성된 iOS Swift Package Manager 서버입니다. |
| [**TeamCity**](https://github.com/itcaat/teamcity-mcp) | TeamCity용 MCP 서버로, Claude Desktop 및 Cursor와 통합됩니다. |
| [**TechDocsStudio/biel-mcp**](https://github.com/TechDocsStudio/biel-mcp) | Cursor, VS Code, Claude Desktop 같은 AI 도구가 제품 문서를 사용하여 질문에 답변할 수 있게 합니다. Biel.ai가 RAG 시스템과 MCP 서버를 제공합니다. |
| [**Text-To-GraphQL**](https://github.com/Arize-ai/text-to-graphql-mcp) | 텍스트를 GraphQL로 변환하는 MCP 서버로, Claude Desktop 및 Cursor와 통합됩니다. |
| [**vasylenko/claude-desktop-extension-bear-notes**](https://github.com/vasylenko/claude-desktop-extension-bear-notes) | Claude에서 직접 Bear Notes를 검색, 읽기, 생성, 업데이트합니다. 로컬 전용으로 완전한 개인정보 보호를 제공합니다. |
| [**VertexStudio/developer**](https://github.com/VertexStudio/developer) | 파일 편집, 셸 명령 실행, 화면 캡처 기능을 갖춘 종합 개발자 도구입니다. |
| [**Windows Control**](https://github.com/Cheffromspace/nutjs-windows-control) | nut.js를 사용하여 마우스, 키보드, 윈도우 관리, 화면 캡처 등 Windows 시스템 작업을 프로그래밍 방식으로 제어합니다. |
| [**Wolfe-Jam/faf-mcp**](https://github.com/Wolfe-Jam/faf-mcp) | Cursor, Windsurf, Cline, VS Code 및 모든 MCP 호환 플랫폼(Claude Desktop 포함)을 위한 범용 영속적 프로젝트 컨텍스트입니다. IANA 등록 형식(application/vnd.faf+yaml). 17개 네이티브 도구, AI 준비도 점수 제공. |
| [**Wooonster/hocr_mcp_server**](https://github.com/Wooonster/hocr_mcp_server) | 업로드된 이미지를 MCP를 통해 VLM으로 전송하여 손글씨 수학 공식을 깔끔한 LaTeX 코드로 빠르게 추출하는, Vue 프론트엔드를 갖춘 FastAPI 기반 FastMCP 서버입니다. |
| [**wyattjoh/imessage-mcp**](https://github.com/wyattjoh/imessage-mcp) | macOS에서 iMessage 데이터를 읽기 위한 MCP 서버입니다. |

---

## 💻 코드 실행 & 개발

> 코드 샌드박스, 트랜스파일러, 코드 분석 도구

| 서버 | 설명 |
|------|------|
| [**alimo7amed93/webhook-tester-mcp**](https://github.com/alimo7amed93/webhook-tester-mcp) | webhook-test.com과 상호작용하기 위한 FastMCP 기반 서버입니다. Claude를 사용하여 로컬에서 webhook을 생성, 조회, 삭제할 수 있습니다. |
| [**Claude Context**](https://github.com/zilliztech/claude-context) | 코드베이스를 Claude Code의 컨텍스트로 가져옵니다. |
| [**clj-kondo-MCP**](https://github.com/Bigsy/clj-kondo-MCP) | Clojure 린터입니다. |
| [**code-context-provider-mcp**](https://github.com/AB498/code-context-provider-mcp) | AI 어시스턴트를 위한 코드 컨텍스트 및 분석을 제공하는 MCP 서버입니다. WebAssembly Tree-sitter 파서를 사용하여 네이티브 의존성 없이 디렉토리 구조와 코드 심볼을 추출합니다. |
| [**cplusplus-mcp**](https://github.com/kandrwmrtn/cplusplus_mcp) | libclang을 사용한 의미론적 C++ 코드 분석입니다. 텍스트 검색 대신 AST 파싱을 통해 Claude가 C++ 코드베이스를 이해할 수 있게 합니다 — 클래스 찾기, 상속 탐색, 함수 호출 추적 등. |
| [**cqtrinv/trinvmcp**](https://github.com/cqtrinv/trinvmcp) | 이름과 면적을 기반으로 프랑스 코뮌(commune) 및 지적 필지를 탐색합니다. |
| [**DeepView MCP**](https://github.com/ai-1st/deepview-mcp) | Gemini의 1M 컨텍스트 윈도우를 활용하여 Cursor, Windsurf 같은 IDE에서 대규모 코드베이스를 분석할 수 있게 합니다. |
| [**Depyler**](https://github.com/paiml/depyler/blob/main/docs/mcp-integration.md) | 점진적 검증을 갖춘 에너지 효율적 Python-to-Rust 트랜스파일러로, AI 어시스턴트가 Python 코드를 안전하고 고성능인 Rust로 변환하면서 에너지 소비를 75-85% 줄일 수 있게 합니다. |
| [**ELEMENT.FM**](https://gitlab.com/elementfm/mcp) | ELEMENT.FM으로 무제한 팟캐스트 쇼와 에피소드를 생성하고 게시합니다. |
| [**Files**](https://github.com/flesler/mcp-files) | 에이전트가 코드베이스에서 코드를 빠르게 찾아 정밀하게 편집할 수 있게 합니다. 심볼을 찾고 모든 곳에서 편집합니다. |
| [**Flyworks Avatar**](https://github.com/Flyworks-AI/flyworks-mcp) | 빠르고 무료인 제로샷 립싱크 MCP 서버입니다. |
| [**hloiseaufcms/mcp-gopls**](https://github.com/hloiseaufcms/mcp-gopls) | Go Language Server Protocol(gopls)과 상호작용하여 고급 Go 코드 분석 기능을 활용하기 위한 MCP 서버입니다. |
| [**hyperb1iss/lucidity-mcp**](https://github.com/hyperb1iss/lucidity-mcp) | 복잡도부터 보안 취약점까지 10가지 핵심 차원에 걸친 지능적 프롬프트 기반 분석을 통해 AI 생성 코드 품질을 향상시킵니다. |
| [**intruder-io/intruder-mcp**](https://github.com/intruder-io/intruder-mcp) | [Intruder](https://www.intruder.io/)에 접근하여 인프라의 보안 취약점을 식별, 이해, 수정하는 데 도움을 주는 MCP 서버입니다. |
| [**jasonwilbur/oci-pricing-mcp**](https://github.com/jasonwilbur/oci-pricing-mcp) | 602개 제품의 Oracle Cloud Infrastructure 가격 데이터, 비용 계산기, 크로스 프로바이더 비교를 제공합니다. Claude용 원커맨드 설치. |
| [**Java Decompiler**](https://github.com/idachev/mcp-javadc) | CFR 디컴파일러를 사용하여 .class 파일, 패키지 이름, JAR 아카이브에서 Java 바이트코드를 읽기 가능한 소스 코드로 디컴파일합니다. |
| [**Job Searcher**](https://github.com/0xDAEF0F/job-searchoor) | 기간, 키워드, 원격 근무 선호도에 따라 채용 목록을 조회하고 필터링하는 도구를 제공하는 FastMCP 서버입니다. |
| [**juehang/vscode-mcp-server**](https://github.com/juehang/vscode-mcp-server) | Claude 같은 AI가 VS Code 워크스페이스의 디렉토리 구조를 읽고, 린터 및 Language Server가 감지한 문제를 확인하고, 코드 파일을 읽고 편집할 수 있게 하는 MCP 서버입니다. |
| [**KurrentDB**](https://github.com/kurrent-io/mcp-server) | KurrentDB 위에서 데이터를 탐색하고 프로젝션을 더 빠르게 프로토타이핑할 수 있도록 돕는 간단한 MCP 서버입니다. |
| [**Label Studio**](https://github.com/HumanSignal/label-studio-mcp-server) | 오픈소스 데이터 라벨링 플랫폼입니다. |
| [**Last9**](https://github.com/last9/last9-mcp-server) | 실시간 프로덕션 컨텍스트(로그, 메트릭, 트레이스)를 로컬 환경으로 원활하게 가져와 코드를 더 빠르게 자동 수정합니다. |
| [**MCP Server Creator**](https://github.com/GongRzhe/MCP-Server-Creator) | 다른 MCP 서버를 생성하는 강력한 MCP 서버입니다! 이 메타 서버는 FastMCP 서버 구성과 Python 코드를 동적으로 생성하는 도구를 제공합니다. |
| [**micl2e2/code-to-tree**](https://github.com/micl2e2/code-to-tree) | 언어에 관계없이 소스 코드를 AST로 변환하는 단일 바이너리 MCP 서버입니다. |
| [**MikeRecognex/mcp-codebase-index**](https://github.com/MikeRecognex/mcp-codebase-index) | MCP를 통해 17개 쿼리 도구(함수, 클래스, import, 의존성 그래프, 변경 영향도)를 노출하는 구조적 코드베이스 인덱서입니다. 의존성 없음. |
| [**NASA Image MCP Server**](https://github.com/adithya1012/NASA-MCP-Server/blob/main/README.md) | 화성 탐사 로버 사진, 지구 위성 이미지(EPIC/GIBS), 오늘의 천문 사진 등 NASA의 시각 데이터 API에 대한 접근을 제공하는 MCP 서버입니다. 내장 이미지 분석 도구를 포함합니다. |
| [**Nx**](https://github.com/nrwl/nx-console/blob/master/apps/nx-mcp) | Nx의 코드베이스 이해를 LLM에 제공하여, 코드베이스 아키텍처, 프로젝트 관계, 실행 가능한 태스크에 대한 인사이트를 제공함으로써 AI가 정확한 코드 제안을 할 수 있게 합니다. |
| [**openstack-kr/python-openstackmcp-server**](https://github.com/openstack-kr/python-openstackmcp-server) | openstacksdk 기반의 클라우드 인프라 관리를 위한 OpenStack MCP 서버입니다. |
| [**PBS API**](https://github.com/matthewdcage/pbs-mcp-server) | 호주 의약품 혜택 제도(Pharmaceutical Benefits Scheme) 데이터에 접근하여 의약품 정보, 가격, 가용성을 조회합니다. Python과 FastAPI로 구축되었습니다. |
| [**picahq/mcp**](https://github.com/picahq/mcp) | 모든 통합을 위한 하나의 MCP — 지능적이고 협력적인 에이전트를 위한 인프라인 [Pica](https://www.picaos.com)가 제공합니다. |
| [**Podbean**](https://github.com/amurshak/podbeanMCP) | Podbean API를 통해 팟캐스트, 에피소드, 분석을 관리하는 MCP 서버입니다. 팟캐스트 업데이트, 추가, 삭제, 쇼 설명 조회, 노트, 분석 등을 지원합니다. |
| [**ProdE**](https://github.com/CuriousBox-AI/ProdE-mcp) | 여러 코드베이스에 걸쳐 컨텍스트를 보존하는 24시간 운영 프로덕션 엔지니어입니다. |
| [**ProdEAI**](https://github.com/CuriousBox-AI/ProdE-mc) | 여러 코드베이스에 걸쳐 컨텍스트를 보존하는 24시간 운영 프로덕션 엔지니어 Prode.ai입니다. |
| [**PromptExecution/cratedocs-mcp**](https://github.com/promptexecution/cratedocs-mcp) | AST에서 파생된 Rust crate의 trait, 인터페이스 등을 간결한 형태로 출력합니다 (rust-analyzer와 동일한 API 사용). 출력 제한(토큰 추정) 및 regex 스트리핑을 적용한 crate 문서를 제공합니다. |
| [**QGIS**](https://github.com/jjsantos01/qgis_mcp) | MCP를 통해 QGIS를 Claude AI에 연결합니다. 프롬프트 기반 프로젝트 생성, 레이어 로딩, 코드 실행 등을 가능하게 합니다. |
| [**Renamify**](https://docspring.github.io/renamify/mcp/overview/) | 코드베이스를 위한 스마트한 대소문자 인식 검색 및 교체입니다. 완전한 실행 취소/다시 실행 기능을 갖춘 심볼, 파일, 디렉토리의 원자적 이름 변경을 제공합니다. MCP 서버는 AI 어시스턴트가 이름 변경 작업을 계획, 미리보기, 적용할 수 있게 합니다. |
| [**Riza**](https://github.com/riza-io/riza-mcp) | Riza가 제공하는 LLM용 임의 코드 실행 및 도구 사용 플랫폼입니다. |
| [**SafeDep**](https://github.com/safedep/vet/blob/main/docs/mcp.md) | SafeDep `vet-mcp`는 프로젝트에서 사용하기 전에 오픈소스 패키지의 보안 위험(취약점 및 악성 코드 등)을 검사합니다. 특히 AI 생성 코드 제안에 유용합니다. |
| [**Salaah MCP**](https://github.com/yusufk/salaah-mcp) | 이슬람 예배 시간 및 기타 유용한 계산을 제공하는 FastAPI 및 MCP 서비스입니다. |
| [**sapientpants/sonarqube-mcp-server**](https://github.com/sapientpants/sonarqube-mcp-server) | SonarQube와 통합되어 AI 어시스턴트가 코드 품질 메트릭, 이슈, 품질 게이트 상태에 접근할 수 있게 하는 MCP 서버입니다. |
| [**saurabhsharma2u/search-console-mcp**](https://github.com/saurabhsharma2u/search-console-mcp) | Google Search Console 및 Bing Webmasters와 상호작용하기 위한 MCP 서버입니다. |
| [**SDGLBL/mcp-claude-code**](https://github.com/SDGLBL/mcp-claude-code) | MCP를 활용한 Claude Code 기능 구현으로, AI 코드 이해, 수정, 프로젝트 분석을 종합 도구로 지원합니다. |
| [**Sequa.AI**](https://github.com/sequa-ai/sequa-mcp) | Copilot과 Cursor를 위한 컨텍스트 연결 작업을 중단하세요. Sequa MCP를 사용하면 AI 도구가 모든 코드베이스와 문서를 기본적으로 알고 있습니다. |
| [**SimplyLiz/CodeMCP**](https://github.com/SimplyLiz/CodeMCP) | 의미론적 코드 검색, 영향도 분석, 콜 그래프, 소유권 탐지, 아키텍처 이해를 위한 80개 이상의 도구를 갖춘 코드 인텔리전스 MCP 서버입니다. SCIP 인덱싱을 통해 Go, TypeScript, Python, Rust, Java를 지원합니다. |
| [**Ticketmaster**](https://github.com/delorenj/mcp-server-ticketmaster) | Ticketmaster Discovery API를 통해 이벤트, 장소, 공연을 검색합니다. |
| [**torrentclaw/torrentclaw-mcp**](https://github.com/torrentclaw/torrentclaw-mcp) | 토렌트 링크, 품질 점수, 스트리밍 가용성, 출연진/제작진 메타데이터를 포함하여 영화 및 TV 프로그램을 검색하고 탐색합니다. |
| [**wegotdocs/open-mcp**](https://github.com/wegotdocs/open-mcp) | 10초 만에 웹 API를 MCP 서버로 변환하고 오픈소스 레지스트리(https://open-mcp.org)에 추가합니다. |
| [**XRAY**](https://github.com/srijanshukla18/xray) | 점진적 코드 인텔리전스 서버: AI 어시스턴트가 Python, JS/TS, Go 코드베이스에서 구조를 매핑하고, 퍼지 심볼 검색, 변경 영향도 평가를 수행할 수 있게 합니다 (`ast-grep` 기반). |
| [**zinja-coder/jadx-ai-mcp**](https://github.com/zinja-coder/jadx-ai-mcp) | JADX-AI-MCP는 JADX 디컴파일러용 플러그인이자 MCP 서버로, MCP와 직접 통합되어 Claude 같은 LLM과 함께 실시간 리버스 엔지니어링을 지원합니다. |

---

## 📚 리소스 & 도구

> MCP 서버 디렉토리, 설치 도구, 커뮤니티 자료

| 서버 | 설명 |
|------|------|
| [**A2A-MCP Java Bridge**](https://github.com/vishalmysore/a2ajava) | A2AJava는 강력한 A2A-MCP 통합을 Java 애플리케이션에 직접 제공합니다. 개발자가 표준 Java 메서드에 어노테이션을 추가하여 즉시 MCP Server, A2A 검색 가능 액션으로 노출할 수 있게 합니다. |
| [**AiMCP**](https://www.aimcp.info) | 적합한 MCP 도구를 찾기 위한 MCP 클라이언트 및 서버 컬렉션입니다. **Hekmon** 제작. |
| [**Awesome Crypto MCP Servers by badkk**](https://github.com/badkk/awesome-crypto-mcp-servers) | **Luke Fan**이 큐레이션한 MCP 서버 목록입니다. |
| [**Awesome MCP Servers by appcypher**](https://github.com/appcypher/awesome-mcp-servers) | **Stephen Akinyemi**가 큐레이션한 MCP 서버 목록입니다. |
| [**Awesome Remote MCP Servers by JAW9C**](https://github.com/jaw9c/awesome-remote-mcp-servers) | 인증 지원 정보를 포함한 **원격** MCP 서버의 큐레이션 목록입니다. **JAW9C** 제작. |
| [**centralmind/gateway**](https://github.com/centralmind/gateway) | AI를 사용하여 데이터베이스 스키마와 데이터를 기반으로 MCP 도구를 생성하고 REST, MCP 또는 MCP-SSE 서버로 호스팅하는 CLI입니다. |
| [**ClaudeCodeNavi/claudecodenavi-mcp**](https://github.com/saikiyusuke/claudecodenavi-mcp) | Claude Code 지식 플랫폼 & 마켓플레이스 MCP 서버. ClaudeCodeNavi 커뮤니티에서 스니펫, 프롬프트, Q&A 솔루션, 오류 수정, MCP 서버 설정을 검색하고 공유합니다. |
| [**create-mcp-ts**](https://github.com/stephencme/create-mcp-ts) | TypeScript로 새로운 MCP 서버를 생성합니다 — 배터리 포함, 사용자 정의 템플릿을 지원합니다! |
| [**Discord Server**](https://glama.ai/mcp/discord) | MCP 전용 커뮤니티 Discord 서버입니다. **Frank Fiegel** 운영. |
| [**Discord Server (ModelContextProtocol)**](https://discord.gg/jHEGxQu2a5) | Model Context Protocol 전용 활발한 Discord 커뮤니티에서 개발자와 연결하고, 인사이트를 공유하고, 프로젝트를 협업합니다. **Alex Andru** 운영. |
| [**Epistates/TurboMCP**](https://github.com/Epistates/turbomcp) | TurboMCP SDK: Rust로 작성된 엔터프라이즈 MCP SDK입니다. |
| [**FastMCP**](https://github.com/jlowin/fastmcp) | Python으로 MCP 서버를 구축하기 위한 고수준 프레임워크입니다. |
| [**FastMCP**](https://github.com/punkpeye/fastmcp) | TypeScript로 MCP 서버를 구축하기 위한 고수준 프레임워크입니다. |
| [**Install This MCP**](https://installthismcp.com) | 아름다운 설치 가이드로 설치 마찰을 줄입니다. |
| [**LiteMCP**](https://github.com/wong2/litemcp) | MCP 서버를 우아하게 구축하기 위한 TypeScript 프레임워크입니다. |
| [**MBro**](https://github.com/sitbon/magg/blob/main/docs/mbro.md) | 탭 완성과 자동 문서화를 갖춘 강력한 대화형 터미널 **M**CP **Bro**wser 클라이언트로, 여러 MCP 서버와 작업하고, 도구를 관리하고, 복잡한 워크플로를 생성할 수 있습니다. |
| [**MCP Badges**](https://github.com/mcpx-dev/mcp-badges) | 명확하고 눈에 띄는 배지로 MCP 프로젝트를 빠르게 강조합니다. **Ironben** 제작. |
| [**MCP Hunt**](https://mcp-hunt.com) | 모멘텀 추적, 업보팅, 커뮤니티 토론 기능을 갖춘 트렌딩 MCP 서버를 발견하기 위한 실시간 플랫폼 — Product Hunt와 Reddit을 MCP용으로 결합한 것입니다. |
| [**MCP Linker**](https://github.com/milisp/mcp-linker) | Claude Desktop, Cursor, Windsurf, VS Code, Cline, Neovim을 지원하는 MCP 서버 원클릭 설정 및 관리를 위한 크로스 플랫폼 Tauri GUI 도구입니다. |
| [**MCP Router**](https://mcp-router.net) | 원활한 앱 인증과 강력한 로그 시각화를 제공하면서 MCP 관리를 간소화하는 무료 Windows 및 macOS 앱입니다. **MCP Router** 제작. |
| [**MCP Servers Rating and User Reviews**](http://www.deepnlp.org/store/ai-agent/mcp-server) | MCP 서버를 평가하고, 실제 사용자 리뷰를 작성하고, 에이전트 및 MCP를 검색할 수 있는 웹사이트입니다. |
| [**MCP Servers Search**](https://github.com/atonomus/mcp-servers-search) | 이 목록에서 사용 가능한 MCP 서버를 쿼리하고 검색하는 도구를 제공하는 MCP 서버입니다. |
| [**MCP Sky**](https://bsky.app/profile/brianell.in/feed/mcp) | MCP 관련 뉴스와 토론을 위한 Bluesky 피드입니다. **@brianell.in** 운영. |
| [**MCP X Community**](https://x.com/i/communities/1861891349609603310) | MCP를 위한 X 커뮤니티입니다. **Xiaoyi** 운영. |
| [**mcp-cli**](https://github.com/wong2/mcp-cli) | Model Context Protocol용 CLI 인스펙터입니다. **wong2** 제작. |
| [**mcp-dockmaster**](https://mcp-dockmaster.com) | Windows, Linux, macOS용 MCP 서버를 설치하고 관리하는 오픈소스 UI입니다. |
| [**mcp-framework**](https://github.com/QuantGeekDev/mcp-framework) | MCP 서버를 구축하기 위한 빠르고 우아한 TypeScript 프레임워크입니다. |
| [**mcp-get**](https://mcp-get.com) | MCP 서버를 설치하고 관리하기 위한 커맨드 라인 도구입니다. **Michael Latman** 제작. |
| [**mcp-guardian**](https://github.com/eqtylab/mcp-guardian) | MCP 서버의 프록시/관리 제어를 위한 GUI 애플리케이션 및 도구입니다. **EQTY Lab** 제작. |
| [**mcp-manager**](https://github.com/zueai/mcp-manager) | Claude Desktop용 MCP 서버를 설치하고 관리하는 간단한 웹 UI입니다. **Zue** 제작. |
| [**MCP.ing**](https://mcp.ing/) | 커뮤니티의 MCP 서버를 검색하고 MCP 서비스를 위한 편리한 검색 기능을 제공하는 MCP 서비스 목록입니다. **iiiusky** 제작. |
| [**mcp.natoma.ai**](https://mcp.natoma.ai) | MCP 서버를 검색, 설치, 관리, 배포할 수 있는 호스팅 MCP 플랫폼입니다. **Natoma Labs** 제작. |
| [**mcp.run**](https://mcp.run) | 안전하고 이식 가능한 MCP 서버를 설치 및 실행하기 위한 호스팅 레지스트리 및 컨트롤 플레인입니다. |
| [**MCPHub**](https://www.mcphub.com) | 고품질 MCP 서버와 실제 사용자 리뷰를 나열하는 웹사이트입니다. MCP 서버를 지원하는 인기 LLM 모델용 온라인 챗봇도 제공합니다. |
| [**MCPHub**](https://github.com/Jeamee/MCPHub-Desktop) | MCP 서버를 검색, 설치, 관리하기 위한 오픈소스 macOS 및 Windows GUI 데스크톱 앱입니다. **Jeamee** 제작. |
| [**MCPProxy**](https://github.com/smart-mcp-proxy/mcpproxy-go) | MCP 프로토콜을 통한 지능적 검색으로 여러 MCP 서버와 수천 개의 도구에 접근할 수 있는 오픈소스 로컬 앱입니다. 격리된 환경에서 서버를 실행하며, 자동 격리 기능을 갖추고 있습니다. |
| [**MCPRepository.com**](https://mcprepository.com/) | 쉬운 검색을 위해 모든 MCP 서버를 인덱싱하고 정리하는 저장소입니다. |
| [**MCPServers.com**](https://mcpservers.com) | 다양한 MCP 클라이언트를 위한 명확한 설정 가이드를 갖춘 고품질 MCP 서버의 성장하는 디렉토리입니다. **Highlight MCP client** 팀이 구축했습니다. |
| [**MCPVerse**](https://mcpverse.dev) | 인증된 MCP 서버를 생성 및 호스팅하고 안전하게 연결하기 위한 포털입니다. |
| [**MCPWatch**](https://github.com/kapilduraphe/mcp-watch) | MCP 서버 구현의 취약점과 보안 이슈를 탐지하는 종합 보안 스캐너입니다. |
| [**MervinPraison/praisonai-mcp**](https://github.com/MervinPraison/praisonai-mcp) | 검색, 메모리, 워크플로, 코드 실행, 파일 작업을 위한 64개 이상의 내장 도구를 갖춘 AI 에이전트 프레임워크입니다. MCP로 모든 AI 어시스턴트를 멀티 에이전트 시스템으로 전환합니다. |
| [**mkinf**](https://mkinf.io) | AI 에이전트 워크플로를 가속화하기 위한 호스팅 MCP 서버의 오픈소스 레지스트리입니다. |
| [**NetMind**](https://www.netmind.ai/AIServices) | 간단한 API 또는 MCP 서버를 통해 강력한 AI 서비스에 접근하여 생산성을 극대화합니다. |
| [**Open-Sourced MCP Servers Directory**](https://github.com/chatmcp/mcp-directory) | **mcpso**가 큐레이션한 MCP 서버 목록입니다. |
| [**OpenTools**](https://opentools.com) | MCP 서버를 찾고, 설치하고, 구축하기 위한 오픈 레지스트리입니다. **opentoolsteam** 제작. |
| [**Programmatic MCP Prototype**](https://github.com/domdomegg/programmatic-mcp-prototype) | TypeScript 코드 실행을 통해 프로그래밍 방식의 MCP 도구 조합, 점진적 도구 검색, 상태 영속성, 스킬 구축을 시연하는 실험적 에이전트 프로토타입입니다. **Adam Jones** 제작. |
| [**r/mcp**](https://www.reddit.com/r/mcp) | MCP 전용 Reddit 커뮤니티입니다. **Frank Fiegel** 운영. |
| [**r/modelcontextprotocol**](https://www.reddit.com/r/modelcontextprotocol) | Model Context Protocol 커뮤니티 Reddit 페이지 — 아이디어 논의, 질문 답변, 동일한 관심사를 가진 사람들과의 네트워킹, 프로젝트 쇼케이스! **Alex Andru** 운영. |
| [**Search MCP Server**](https://github.com/krzysztofkucmierz/search-mcp-server) | 이 README 파일을 검색하여 클라이언트의 쿼리에 가장 관련성 높은 MCP 서버를 추천합니다. |
| [**Smithery**](https://smithery.ai/) | LLM 에이전트에 적합한 도구를 찾기 위한 MCP 서버 레지스트리입니다. **Henry Mao** 제작. |
| [**Toolbase**](https://gettoolbase.ai) | 몇 번의 클릭만으로 도구와 MCP 서버를 관리하는 데스크톱 애플리케이션입니다 — 코딩 불필요. **gching** 제작. |
| [**ToolHive**](https://github.com/StacklokLabs/toolhive) | 컨테이너화를 통해 사용 편의성, 일관성, 보안을 보장하며 MCP 서버의 배포와 관리를 간소화하도록 설계된 경량 유틸리티입니다. **StacklokLabs** 제작. |
| [**ToolHive**](https://github.com/Stacklok/toolhive) | 컨테이너화를 통해 사용 편의성, 일관성, 보안을 보장하며 MCP 서버의 배포와 관리를 간소화하도록 설계된 경량 유틸리티입니다. |
| [**Webrix MCP Gateway**](https://github.com/webrix-ai/secure-mcp-gateway) | SSO, RBAC, 감사 추적, 토큰 볼트를 갖춘 엔터프라이즈 MCP 게이트웨이로, 안전하고 중앙 집중적인 AI 에이전트 접근 제어를 제공합니다. Helm 차트를 통해 온프레미스 또는 클라우드에 배포합니다. webrix.ai |

---

## 🔗 SaaS & 플랫폼 통합

> 다양한 SaaS 서비스 및 플랫폼 연동

| 서버 | 설명 |
|------|------|
| [**13bm/GhidraMCP**](https://github.com/13bm/GhidraMCP) | Ghidra를 AI 어시스턴트와 통합하기 위한 MCP 서버. 이 플러그인은 Model Context Protocol을 통해 함수 검사, 디컴파일, 메모리 탐색, import/export 분석 도구를 제공하여 바이너리 분석을 가능하게 합니다. |
| [**1mcp/agent**](https://github.com/1mcp-app/agent) | 여러 MCP 서버를 하나로 통합하는 통합 Model Context Protocol 서버 구현체. |
| [**1Panel**](https://github.com/1Panel-dev/mcp-1panel) | 1Panel과의 상호작용을 제공하는 MCP 서버 구현체. |
| [**2niuhe/qrcode_mcp**](https://github.com/2niuhe/qrcode_mcp) | 텍스트(중국어 포함)를 커스터마이징 가능한 색상과 base64 인코딩 출력으로 QR 코드를 생성하는 MCP 서버. |
| [**A2A**](https://github.com/GongRzhe/A2A-MCP-Server) | Model Context Protocol(MCP)과 Agent-to-Agent(A2A) 프로토콜을 연결하여 Claude 같은 MCP 호환 AI 어시스턴트가 A2A 에이전트와 원활하게 상호작용할 수 있게 하는 MCP 서버. |
| [**aarsiv-groups/shipi-mcp-server**](https://github.com/aarsiv-groups/shipi-mcp-server) | 배송 생성, 패키지 추적, 다양한 운송사의 요금 비교를 위한 18개 도구를 제공하는 Shipi MCP 서버. [원격 MCP](https://mcp.myshipi.com/api/mcp) 지원. |
| [**AbdelStark/nostr-mcp**](https://github.com/AbdelStark/nostr-mcp) | Nostr와 상호작용하여 노트 게시 등의 기능을 제공하는 Nostr MCP 서버. |
| [**abhiemj/manim-mcp-server**](https://github.com/abhiemj/manim-mcp-server) | Manim을 사용하여 애니메이션을 생성하는 로컬 MCP 서버. |
| [**Ableton Live**](https://github.com/Simon-Kansara/ableton-live-mcp-server) | Ableton Live를 제어하기 위한 MCP 서버. |
| [**ActivityPub MCP**](https://github.com/cameronrye/activitypub-mcp) | LLM이 ActivityPub 프로토콜을 통해 Fediverse를 탐색하고 상호작용할 수 있게 하는 종합 MCP 서버. 액터 검색, 타임라인 가져오기, 인스턴스 탐색, WebFinger를 지원합니다. |
| [**Actor Critic Thinking**](https://github.com/aquarius-wing/actor-critic-thinking-mcp) | 성능 평가를 위한 Actor-Critic 사고 기법. |
| [**adancurusul/serial-mcp-server**](https://github.com/adancurusul/serial-mcp-server) | 시리얼 포트 통신을 위한 종합 MCP 서버. |
| [**adhikasp/mcp-git-ingest**](https://github.com/adhikasp/mcp-git-ingest) | LLM으로 GitHub 리포지토리를 읽고 분석합니다. |
| [**AgentHotspot**](https://github.com/AgentHotspot/agenthotspot-mcp) | AgentHotspot MCP 마켓플레이스에서 MCP 커넥터를 검색, 통합 및 수익화합니다. |
| [**agentic-mcp-tools/owlex**](https://github.com/agentic-mcp-tools/owlex) | AI 위원회 서버: Claude Code, Codex, Gemini, OpenCode 등 CLI 에이전트를 병렬로 쿼리하고 심의 라운드를 진행합니다. |
| [**aikts/yandex-tracker-mcp**](https://github.com/aikts/yandex-tracker-mcp) | Yandex Tracker용 MCP 서버. 이슈, 큐, 사용자 정보를 검색하고 조회하는 도구를 제공합니다. |
| [**Airbnb**](https://github.com/openbnb-org/mcp-server-airbnb) | Airbnb 검색 및 숙소 상세 정보를 조회하는 도구를 제공합니다. |
| [**Airflow**](https://github.com/yangkyeongmo/mcp-server-apache-airflow) | 공식 Python 클라이언트를 사용하여 Apache Airflow에 연결하는 MCP 서버. |
| [**ALAPI**](https://github.com/ALAPI-SDK/mcp-alapi-cn) | ALAPI MCP 도구. MCP를 통해 수백 개의 API 인터페이스를 호출합니다. |
| [**Alation**](https://github.com/Alation/alation-ai-agent-sdk) | Alation MCP 서버가 제공하는 도구를 활용하여 엔터프라이즈 Data Catalog의 기능을 잠금 해제합니다. |
| [**Alertmanager**](https://github.com/ntk148v/alertmanager-mcp-server) | AI 어시스턴트가 Prometheus Alertmanager와 통합할 수 있게 하는 Model Context Protocol(MCP) 서버. |
| [**alexbakers/mcp-ipfs**](https://github.com/alexbakers/mcp-ipfs) | IPFS 스토리지에 파일 업로드 및 조작. |
| [**aliafsahnoudeh/shahnameh-mcp-server**](https://github.com/aliafsahnoudeh/shahnameh-mcp-server) | Ferdowsi의 페르시아 서사시 Shahnameh(왕의 서)에 접근하기 위한 MCP 서버. 섹션, 절, 해설을 포함합니다. |
| [**Alkemi**](https://github.com/alkemi-ai/alkemi-mcp) | Alkemi.ai를 통해 Snowflake, Google BigQuery, DataBricks Data Products를 쿼리합니다. |
| [**Amazon Ads**](https://github.com/MarketplaceAdPros/amazon-ads-mcp-server) | MarketplaceAdPros를 통해 Amazon Advertising과 상호작용 기능을 제공하는 MCP 서버. |
| [**ambar/simctl-mcp**](https://github.com/ambar/simctl-mcp) | iOS Simulator 제어를 위한 MCP 서버 구현체. |
| [**ananddtyagi/gif-creator-mcp**](https://github.com/ananddtyagi/gif-creator-mcp/tree/main) | 동영상에서 GIF를 생성하기 위한 MCP 서버. |
| [**andybrandt/mcp-simple-timeserver**](https://github.com/andybrandt/mcp-simple-timeserver) | 클라이언트 머신의 로컬 시간 또는 NTP 서버의 현재 UTC 시간을 확인할 수 있는 MCP 서버. |
| [**angheljf/nyt**](https://github.com/angheljf/nyt) | NYTimes API를 사용하여 기사를 검색합니다. |
| [**AniList**](https://github.com/yuna0x0/anilist-mcp) | AniList API 데이터에 접근하기 위한 AniList MCP 서버. |
| [**Anki**](https://github.com/scorzeth/anki-mcp-server) | Anki 덱 및 카드와 상호작용하기 위한 MCP 서버. |
| [**Any Chat Completions**](https://github.com/pyroprompts/any-chat-completions-mcp) | OpenAI, Perplexity, Groq, xAI 등 OpenAI SDK 호환 Chat Completions API와 상호작용합니다. |
| [**Apache Gravitino(incubating)**](https://github.com/datastrato/mcp-server-gravitino) | LLM이 Gravitino를 통해 구조화된 데이터 및 비구조화된 데이터의 메타데이터를 탐색하고, 태깅/분류를 포함한 데이터 거버넌스 작업을 수행할 수 있게 합니다. |
| [**araa47/jupiter-mcp**](https://github.com/araa47/jupiter-mcp) | Jupiter API 접근 (AI가 Solana에서 토큰 거래 + 잔액 조회 + 토큰 검색 + 지정가 주문 생성 가능). |
| [**areweai/tsgram-mcp**](https://github.com/areweai/tsgram-mcp) | TSgram: TypeScript로 Telegram + Claude를 연동하여 휴대폰에서 로컬 워크스페이스에 접근. 이동 중에도 읽기, 쓰기, 바이브 코딩이 가능합니다! |
| [**arpitbatra123/mcp-googletasks**](https://github.com/arpitbatra123/mcp-googletasks) | Google Tasks API와 인터페이스하기 위한 MCP 서버. |
| [**arrismo/kaggle-mcp**](https://github.com/arrismo/kaggle-mcp) | Kaggle에 연결하여 데이터셋을 다운로드하고 분석할 수 있습니다. |
| [**atomicchonk/roadrecon_mcp_server**](https://github.com/atomicchonk/roadrecon_mcp_server) | Azure 테넌트 열거에서 ROADrecon 수집 결과를 분석하기 위한 MCP 서버. |
| [**Attestable MCP**](https://github.com/co-browser/attestable-mcp-server) | Gramine을 통해 신뢰 실행 환경(TEE)에서 실행되는 MCP 서버로, RA-TLS를 사용한 원격 증명을 구현합니다. MCP 클라이언트가 연결 전에 서버를 검증할 수 있습니다. |
| [**awwaiid/mcp-server-taskwarrior**](https://github.com/awwaiid/mcp-server-taskwarrior) | 기본적인 로컬 Taskwarrior 사용(작업 추가, 업데이트, 삭제)을 위한 MCP 서버. |
| [**axliupore/mcp-code-runner**](https://github.com/axliupore/mcp-code-runner) | Docker를 통해 로컬에서 코드를 실행하며 여러 프로그래밍 언어를 지원하는 MCP 서버. |
| [**aywengo/kafka-schema-reg-mcp**](https://github.com/aywengo/kafka-schema-reg-mcp) | 멀티 레지스트리 관리, 스키마 마이그레이션, 엔터프라이즈 기능을 위한 48개 도구를 갖춘 종합 Kafka Schema Registry MCP 서버. |
| [**azer/react-analyzer-mcp**](https://github.com/azer/react-analyzer-mcp) | React 코드를 로컬에서 분석하고, 전체 프로젝트에 대한 문서 / llm.txt를 한번에 생성합니다. |
| [**Backup**](https://github.com/hexitex/MCP-Backup-Server) | Windsurf, Cursor, Claude Coder 등 코딩 에이전트에 스마트 백업 기능을 추가합니다. |
| [**Bagel**](https://github.com/Extelligence-ai/bagel) | 물리적 데이터를 위한 ChatGPT. 자연어로 로봇과 드론의 문제를 해결합니다. |
| [**Baserow**](https://baserow.io/user-docs/mcp-server) | Baserow 테이블에 대한 읽기 및 쓰기 접근. |
| [**Berckan/bugherd-mcp**](https://github.com/Berckan/bugherd-mcp) | BugHerd 버그 추적용 MCP 서버. 프로젝트 목록 조회, 상태/우선순위/태그별 작업 필터링, 작업 상세 조회, 댓글 읽기를 지원합니다. |
| [**betterhyq/mermaid-grammer-inspector-mcp**](https://github.com/betterhyq/mermaid_grammer_inspector_mcp) | Mermaid 다이어그램 구문 검증 및 종합적인 문법 검사 기능을 제공하는 Model Context Protocol(MCP) 서버. |
| [**Binary Ninja**](https://github.com/fosdickio/binary_ninja_mcp) | Binary Ninja를 원하는 MCP 클라이언트와 원활하게 통합하는 Binary Ninja 플러그인, MCP 서버 및 브릿지. |
| [**Bitrise**](https://github.com/bitrise-io/bitrise-mcp) | 빌드, CI 등과 대화형으로 상호작용합니다. |
| [**blakerouse/ssh-mcp**](https://github.com/blakerouse/ssh-mcp) | Linux 및 Windows 서버에 대한 SSH 제어를 노출하는 MCP 서버. 장시간 실행 명령과 여러 호스트에서 동시에 명령을 수행하는 기능을 지원합니다. |
| [**blurrah/mcp-graphql**](https://github.com/blurrah/mcp-graphql) | AI가 GraphQL 서버를 쿼리할 수 있게 합니다. |
| [**Boikot**](https://github.com/boikot-xyz/boikot) | boikot.xyz를 통해 주요 기업의 윤리적/비윤리적 행동에 대해 알아봅니다. |
| [**bradleylab/stella-mcp**](https://github.com/bradleylab/stella-mcp) | 과학 시뮬레이션 및 모델링을 위한 Stella 시스템 다이내믹스 모델(.stmx 파일, XMILE 형식)을 생성, 읽기, 검증 및 저장합니다. |
| [**BrainGrid MCP**](https://docs.braingrid.ai/mcp-server/installation) | [BrainGrid](https://braingrid.ai) MCP는 스펙을 작성하고, 기능을 계획하며, 코딩 도구가 안정적으로 빌드할 수 있는 엔지니어링 수준의 작업을 생성하는 제품 관리 에이전트입니다. |
| [**BreakoutRoom**](https://github.com/agree-able/room-mcp) | P2P 룸에서 에이전트들이 함께 목표를 달성합니다. |
| [**briandconnelly/mcp-server-ipinfo**](https://github.com/briandconnelly/mcp-server-ipinfo) | IPInfo API를 사용한 IP 주소 지리적 위치 및 네트워크 정보 조회. |
| [**Bucket**](https://github.com/bucketco/bucket-javascript-sdk/tree/main/packages/cli#model-context-protocol) | Bucket을 사용하여 기능 플래그 설정, 회사 데이터 관리, 기능 접근 제어를 수행합니다. |
| [**Buildkite**](https://github.com/buildkite/buildkite-mcp-server) | Buildkite 데이터(파이프라인, 빌드, 작업, 테스트)를 AI 도구 및 에디터에 노출합니다. |
| [**BuiltWith**](https://github.com/builtwith/mcp) | 모든 웹사이트의 기술 스택을 식별합니다. |
| [**BurtTheCoder/mcp-dnstwist**](https://github.com/BurtTheCoder/mcp-dnstwist) | 타이포스쿼팅, 피싱, 기업 스파이 행위를 탐지하는 강력한 DNS 퍼징 도구인 dnstwist용 MCP 서버. |
| [**BVG MCP Server - (Unofficial)**](https://github.com/svkaizoku/mcp-bvg) | Berliner Verkehrsbetriebe API를 위한 비공식 MCP 서버. |
| [**Calculator**](https://github.com/githejie/mcp-server-calculator) | LLM이 정밀한 수치 계산을 위해 계산기를 사용할 수 있게 하는 서버. |
| [**Career Site Jobs**](https://apify.com/fantastic-jobs/career-site-job-listing-api/api/mcp) | 회사 채용 사이트에서 최신 채용 정보를 가져오는 MCP 서버. |
| [**cevatkerim/unsplash-mcp**](https://github.com/cevatkerim/unsplash-mcp) | 적절한 저작자 표시가 포함된 Unsplash 사진 검색. 각 사진에 대해 바로 사용 가능한 저작자 표시 텍스트와 HTML을 반환하여 LLM이 적절히 출처가 표시된 이미지로 콘텐츠 페이지를 쉽게 빌드할 수 있습니다. 검색, 랜덤 사진, 다운로드 추적을 포함합니다. |
| [**CFBD API**](https://github.com/lenwood/cfbd-mcp-server) | College Football Data API를 위한 MCP 서버. |
| [**Chaitin IP Intelligence**](https://github.com/co0ontty/chaitin-ip-intelligence-search-tool) | Chaitin의 IP Intelligence API를 사용하여 IP 주소를 검색합니다. |
| [**CheMiguel23/MemoryMesh**](https://github.com/CheMiguel23/MemoryMesh) | AI 롤플레이 및 스토리 생성에 특화된 향상된 그래프 기반 메모리. |
| [**chrishayuk/mcp-cli**](https://github.com/chrishayuk/mcp-cli) | MCP 서버 테스트를 위한 또 다른 CLI 도구. |
| [**ChuckNorris**](https://github.com/pollinations/chucknorris-mcp) | 동적 스키마 적응을 갖춘 LLM 향상 프롬프트 및 탈옥을 위한 특화된 MCP 게이트웨이. enum 기반 접근 방식을 사용하여 다양한 LLM을 위한 프롬프트를 제공합니다. |
| [**Cleanup Crew**](https://cleanupcrew.ai/install) | AI 코딩 도구를 사용하는 비기술 창업자를 위한 실시간 인간 지원 서비스. AI가 막힐 때 IDE에서 직접 즉각적인 인간 도움을 요청합니다. |
| [**Clojars**](https://github.com/Bigsy/Clojars-MCP-Server) | Clojure 라이브러리의 최신 의존성 정보를 가져옵니다. |
| [**clojure-mcp**](https://github.com/bhauman/clojure-mcp) | Clojure 개발 도구. REPL을 통해 실행 중인 프로그램에 직접 접근합니다. |
| [**CloudBees CI**](https://docs.cloudbees.com/docs/cloudbees-ci-mcp-router/latest/) | 엔터프라이즈급 Jenkins 기반 솔루션인 CloudBees CI 클러스터에 AI 접근을 가능하게 합니다. |
| [**CloudBees Unify**](https://docs.cloudbees.com/docs/cloudbees-unify-mcp-server/latest/install/mcp-server) | CloudBees Unify 환경에 AI 접근을 가능하게 합니다. |
| [**code-assistant**](https://github.com/stippi/code-assistant) | 코드베이스를 탐색하고 코드를 변경할 수 있는 코딩 어시스턴트 MCP 서버. 신뢰할 수 있는 리포지토리에서만 사용해야 합니다(프롬프트 인젝션에 대한 보호가 불충분합니다). |
| [**code-executor**](https://github.com/bazinga012/mcp_code_executor) | LLM이 지정된 Conda 환경 내에서 Python 코드를 실행할 수 있게 하는 MCP 서버. |
| [**CodeLogic**](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server) | 복잡한 코드 및 데이터 아키텍처 의존성을 그래프로 표현하는 Software Intelligence 플랫폼인 CodeLogic과 상호작용하여 AI 정확도와 인사이트를 향상시킵니다. |
| [**Codesys-mcp-toolkit**](https://github.com/johannesPettersson80/codesys-mcp-toolkit) | CODESYS V3 프로그래밍 환경을 위한 Model Context Protocol(MCP) 서버. |
| [**cognee-mcp**](https://github.com/topoteretes/cognee/tree/main/cognee-mcp) | 커스터마이징 가능한 수집, 데이터 처리 및 검색 기능을 갖춘 GraphRAG 메모리 서버. |
| [**CoinGecko**](https://docs.coingecko.com/reference/mcp-server/) | 200개 이상의 블록체인 네트워크와 800만 개 이상의 토큰에 대한 암호화폐 가격 및 시장 데이터를 제공하는 공식 CoinGecko API MCP 서버. |
| [**Comet Opik**](https://github.com/comet-ml/opik-mcp) | 자연어로 Opik 로그, 트레이스, 프롬프트 및 LLM의 모든 텔레메트리 데이터를 쿼리하고 분석합니다. |
| [**Command Line**](https://github.com/phialsbasement/cmd-mcp-server) | CMD를 통해 모든 명령을 실행할 수 있는 MCP 서버(주의 필요). |
| [**Contentful-mcp**](https://github.com/ivo-toby/contentful-mcp) | 이 MCP 서버에서 Contentful 스페이스의 콘텐츠를 읽기, 업데이트, 삭제, 게시합니다. |
| [**Context 7**](https://github.com/upstash/context7-mcp) | Context7 MCP - 모든 Cursor 프롬프트에 최신 문서를 제공합니다. |
| [**Context Crystallizer**](https://github.com/hubertciebiada/context-crystallizer) | 체계적인 분석과 최적화를 통해 대규모 리포지토리를 AI가 소비할 수 있는 정제된 지식으로 변환하는 AI 컨텍스트 엔지니어링 도구. |
| [**Context Processor**](https://github.com/mschultheiss83/context-processor) | 콘텐츠 명확성, 검색 가능성, 메타데이터 추출을 향상시키기 위한 설정 가능한 전처리 전략(명확화, 분석, 검색, 페치)을 갖춘 지능형 컨텍스트 관리. |
| [**context-awesome**](https://github.com/bh-rat/context-awesome) | 8,500개 이상의 큐레이션된 awesome 목록(100만 개 이상 항목)을 쿼리하고 에이전트를 위한 최적의 리소스를 가져오는 MCP 서버. |
| [**contextstream/mcp-server**](https://www.npmjs.com/package/@contextstream/mcp-server) | AI 코딩 도구를 위한 범용 영구 메모리. 시맨틱 코드 검색, 지식 그래프, 영향도 분석, 의사결정 추적 및 60개 이상의 MCP 도구 제공. Cursor, Claude Code, Windsurf 등 모든 MCP 클라이언트에서 동작합니다. |
| [**Cortex**](https://github.com/cortexapps/cortex-mcp) | Cortex 공식 MCP 서버. |
| [**Couchbase**](https://github.com/Couchbase-Ecosystem/mcp-server-couchbase) | Couchbase 클러스터에 저장된 데이터와 상호작용합니다. |
| [**Crawleo/Crawleo-MCP**](https://github.com/Crawleo/Crawleo-MCP) | Crawleo 검색 & 크롤링 API. |
| [**CRIC Wuye AI**](https://github.com/wuye-ai/mcp-server-wuye-ai) | 부동산 관리 산업에 특화된 지능형 어시스턴트인 CRIC Wuye AI 플랫폼의 기능과 상호작용합니다. |
| [**CSM**](https://github.com/sanyambassi/thales-cdsp-csm-mcp-server) | Thales CipherTrust Secrets Management를 위한 MCP 서버. |
| [**CV Forge**](https://github.com/thechandanbhagat/cv-forge) | 채용 공고를 분석하고 완벽하게 맞춤화된 이력서를 작성하는 지능형 MCP(Model Context Protocol) 서버 (by Chandan Bhagat). |
| [**cyntrisec/cyntrisec-cli**](https://github.com/cyntrisec/cyntrisec-cli) | 그래프 이론을 사용하여 공격 경로를 발견하고 대응 방안을 생성하는 로컬 우선 AWS 보안 분석기. |
| [**czottmann/kagi-ken-mcp**](https://github.com/czottmann/kagi-ken-mcp) | API 접근 없이 Kagi를 사용합니다(고객이어야 합니다). 검색 및 요약 기능을 제공합니다. 간편한 인증을 위해 Kagi 세션 토큰을 사용합니다. |
| [**D365FO**](https://github.com/mafzaal/d365fo-client) | OData 엔드포인트, 메타데이터 작업, 레이블 관리, AI 어시스턴트 통합에 쉽게 접근할 수 있는 Microsoft Dynamics 365 Finance & Operations(D365 F&O)용 종합 MCP 서버. |
| [**Data-Everything/mcp-server-templates**](https://github.com/Data-Everything/mcp-server-templates) | 하나의 서버. 모든 도구. 하나의 강력한 인터페이스 뒤에 많은 앱, 도구, 서비스를 연결하는 통합 MCP 플랫폼—로컬 개발이나 프로덕션 에이전트에 이상적입니다. |
| [**DataEval/dingo**](https://github.com/DataEval/dingo) | 종합적인 데이터 품질 평가 도구인 Dingo를 위한 MCP 서버. Dingo의 규칙 기반 및 LLM 기반 평가 기능과 규칙 & 프롬프트 목록 조회 기능을 제공합니다. |
| [**Dataring-engineering/mcp-server-trino**](https://github.com/Dataring-engineering/mcp-server-trino) | Trino 클러스터에서 데이터를 쿼리하고 접근하기 위한 Trino MCP 서버. |
| [**Dataverse DevTools MCP Server**](https://github.com/vignaesh01/DataverseDevToolsMcpServer) | 사용자 및 보안 관리, 데이터 작업, Web API 실행, 메타데이터 탐색, 문제 해결을 위한 바로 사용 가능한 Dataverse/Dynamics 365 도구를 노출하는 MCP 서버. |
| [**DealX**](https://github.com/DealExpress/mcp-server) | DealX 플랫폼용 MCP 서버. |
| [**decidefyi/decide**](https://github.com/decidefyi/decide) | 결정론적 환불 자격 공증 MCP 서버. 상태 비저장 규칙 엔진을 통해 구독 환불(Adobe, Spotify 등)에 대해 ALLOWED / DENIED / UNKNOWN을 반환합니다. |
| [**delano/postman-mcp-server**](https://github.com/delano/postman-mcp-server) | [Postman API](https://www.postman.com/postman/postman-public-workspace/)와 상호작용합니다. |
| [**dev-mirzabicer/ticktick-sdk**](https://github.com/dev-mirzabicer/ticktick-sdk) | MCP 서버 지원이 포함된 [TickTick](https://ticktick.com/)용 종합 비동기 Python SDK. 작업, 프로젝트, 태그, 습관, 집중/뽀모도로 세션, 사용자 분석을 위한 45개 도구를 제공합니다. |
| [**devflowinc/trieve**](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) | [Trieve](https://trieve.ai)를 통해 데이터셋을 크롤링, 임베딩, 청킹, 검색 및 정보 조회합니다. |
| [**DevRev**](https://github.com/devrev/mcp-server) | DevRev API와 통합하여 다양한 소스에서 가져온 객체가 포함된 DevRev Knowledge Graph를 검색하는 MCP 서버. |
| [**diivi/aseprite-mcp**](https://github.com/diivi/aseprite-mcp) | Aseprite API를 사용하여 픽셀 아트를 제작하는 MCP 서버. |
| [**Dispatch Agent**](https://github.com/abhinav-mangla/dispatch-agent) | ReAct 서브 에이전트를 통해 특화된 파일 시스템 작업을 제공하는 지능형 MCP 서버. |
| [**Django REST Framework MCP**](https://github.com/zacharypodbela/djangorestframework-mcp) | Django REST Framework API를 LLM 및 에이전트 애플리케이션용 MCP 도구로 노출합니다. |
| [**dkships/pm-copilot**](https://github.com/dkships/pm-copilot) | HelpScout 지원 티켓과 ProductLift 기능 요청을 교차 분석하여 우선순위가 매겨진 제품 계획을 생성합니다. 수렴도(두 소스에서 동일 신호 = 2배 가중치)로 주제를 점수화하고, PII를 제거하며, 구성 가능한 우선순위화를 위해 다른 MCP 서버로부터 `kpi_context`를 통해 비즈니스 메트릭을 수용합니다. |
| [**dnaerys/onekgpd-mcp**](https://github.com/dnaerys/onekgpd-mcp) | 1000 Genomes Project 데이터셋에 대한 실시간 접근. |
| [**Drand**](https://github.com/randa-mu/drand-mcp-server) | drand 네트워크에서 검증 가능한 난수를 가져오기 위한 MCP 서버. |
| [**Driflyte**](https://github.com/serkan-ozal/driflyte-mcp-server) | Driflyte용 MCP 서버. Driflyte MCP 서버는 AI 어시스턴트가 재귀적으로 크롤링 및 인덱싱된 웹 페이지에서 주제별 지식을 쿼리하고 검색할 수 있는 도구를 노출합니다. |
| [**Drupal**](https://github.com/Omedia/mcp-server-drupal) | STDIO 전송 계층을 사용하여 Drupal과 상호작용하기 위한 서버. |
| [**echology-io/decompose**](https://github.com/echology-io/decompose) | 텍스트를 권위, 위험, 주의 점수 및 엔티티 추출이 포함된 분류된 시맨틱 단위로 분해합니다. LLM 불필요. 결정론적. MCP 서버 또는 CLI로 동작합니다. |
| [**edgedelta/edgedelta-mcp-server**](https://github.com/edgedelta/edgedelta-mcp-server) | Edge Delta 이상 징후와 상호작용하고, 로그/패턴/이벤트를 쿼리하며, 근본 원인을 파악하고 파이프라인을 최적화합니다. |
| [**efremidze/swift-patterns-mcp**](https://github.com/efremidze/swift-patterns-mcp) | Swift by Sundell, SwiftLee 등 신뢰할 수 있는 소스의 패턴과 실제 코드 예제를 포함하여 주요 iOS 개발자들의 큐레이션된 Swift 및 SwiftUI 모범 사례를 제공하는 MCP 서버. |
| [**eirikb/any-cli-mcp-server**](https://github.com/eirikb/any-cli-mcp-server) | 모든 CLI 도구를 MCP 서버로 변환하는 범용 MCP 서버. `--help` 출력이 있는 모든 CLI에서 동작하며, 성능을 위한 캐싱을 지원합니다. |
| [**ekkyarmandi/ticktick-mcp**](https://github.com/ekkyarmandi/ticktick-mcp) | [TickTick](https://ticktick.com/)의 API와 통합하여 개인 할일 프로젝트 및 작업을 관리하는 TickTick MCP 서버. |
| [**elestirelbilinc-sketch/vap-showcase**](https://github.com/elestirelbilinc-sketch/vap-showcase) | 비용 제어가 가능한 AI 미디어 생성(Flux, Veo, Suno). 사전 커밋 가격 책정, 예산 적용, 적립-소진-환불 과금 방식. |
| [**elevy99927/devops-mcp-webui**](https://github.com/elevy99927/devops-mcp-webui) | Open-WebUI와 통합된 Kubernetes용 MCP 서버로, DevOps와 비기술 팀 간의 간극을 연결합니다. 자연어 명령을 통해 `kubectl` 및 `helm` 작업을 지원합니다. |
| [**elhamid/llm-council**](https://github.com/elhamid/llm-council) | 익명화된 피어 리뷰를 통한 멀티 LLM 심의. 3단계 위원회를 실행합니다: 병렬 응답 → 익명 순위 평가 → 종합. Andrej Karpathy의 LLM Council 개념 기반. |
| [**elisp-dev-mcp**](https://github.com/laurynas-biveinis/elisp-dev-mcp) | Emacs에서 실행되는 elisp(Emacs Lisp) 개발 지원 도구. |
| [**Email Send MCP**](https://github.com/YUHAI0/email-send-mcp) | 위 서버를 수정한 버전. 더 사용자 친화적입니다. |
| [**emicklei/mcp-log-proxy**](https://github.com/emicklei/mcp-log-proxy) | 전체 메시지 흐름을 Web UI로 제공하는 MCP 서버 프록시. |
| [**Enhance Prompt**](https://github.com/FelixFoster/mcp-enhance-prompt) | 프롬프트를 향상시키기 위한 MCP 서비스. |
| [**erithwik/mcp-hn**](https://github.com/erithwik/mcp-hn) | Hacker News를 검색하고, 인기 스토리를 가져오는 등의 기능을 제공하는 MCP 서버. |
| [**eSignatures**](https://github.com/esignaturescom/mcp-server-esignatures) | 구속력 있는 계약서의 작성, 검토, 발송을 위한 계약 및 템플릿 관리. |
| [**etsd-tech/mcp-pointer**](https://github.com/etsd-tech/mcp-pointer) | 에이전트 코딩 도구를 위한 시각적 DOM 요소 선택기. Claude Code, Cursor, Windsurf 등을 위한 Chrome 확장 프로그램 + MCP 서버 브릿지. Option+Click으로 요소를 캡처합니다. |
| [**Eunomia**](https://github.com/whataboutyou-ai/eunomia-MCP-server) | Eunomia 인스트루먼트를 MCP 서버와 연결하는 Eunomia 프레임워크의 확장. |
| [**exoticknight/mcp-file-merger**](https://github.com/exoticknight/mcp-file-merger) | 파일 병합 도구. AI 채팅 길이 제한에 적합합니다. |
| [**ezyang/codemcp**](https://github.com/ezyang/codemcp) | 기본적인 읽기, 쓰기 및 커맨드 라인 도구를 갖춘 코딩 에이전트. |
| [**F1**](https://github.com/AbhiJ2706/f1-mcp/tree/main) | 레이스 결과, 드라이버 정보, 랩 타임, 텔레메트리, 서킷 상세 정보를 포함한 Formula 1 데이터에 접근합니다. |
| [**Fabric MCP**](https://github.com/aci-labs/ms-fabric-mcp) | 선호하는 LLM 모델을 활용하여 Fabric Tenant 작업을 가속화하기 위한 Microsoft Fabric MCP 서버. |
| [**Fabric Real-Time Intelligence MCP**](https://github.com/Microsoft/fabric-rti-mcp) | 선호하는 LLM 모델을 사용하여 Eventhouse, Azure Data Explorer(Kusto), Eventstreams 등 RTI 항목 작업을 가속화하기 위한 Microsoft Fabric RTI 공식 서버. |
| [**fabric-mcp-server**](https://github.com/adapoet/fabric-mcp-server) | Fabric 패턴을 Cline과 통합하여 AI 기반 작업 실행을 위한 도구로 노출하고 Cline의 기능을 향상시키는 MCP 서버. |
| [**Fantasy PL**](https://github.com/rishijatia/fantasy-pl-mcp) | 코딩 에이전트에게 최신 Fantasy Premier League 데이터에 직접 접근할 수 있게 합니다. |
| [**Fathom Analytics**](https://github.com/mackenly/mcp-fathom-analytics) | Fathom Analytics 데이터 및 보고서에 접근하고 분석합니다. |
| [**ferdousbhai/wsb-analyst-mcp**](https://github.com/ferdousbhai/wsb-analyst-mcp) | WallStreetBets 커뮤니티의 콘텐츠를 분석하기 위한 Reddit 통합. |
| [**Feyod**](https://github.com/jeroenvdmeer/feyod-mcp) | 축구 경기에 대한 질문에 답하며, 축구 클럽 Feyenoord에 특화된 서버. |
| [**Find-A-Domain**](https://findadomain.dev/mcp) | 도메인 가용성 확인 및 WHOIS 조회 도구. |
| [**Firebase**](https://github.com/firebase/firebase-tools/blob/master/src/mcp) | AI 도구를 강화하기 위한 Firebase의 실험적 MCP 서버. |
| [**Firebase**](https://github.com/gannonh/firebase-mcp) | Firebase Authentication, Firestore, Firebase Storage를 포함한 Firebase 서비스와 상호작용하기 위한 서버. |
| [**Firefly**](https://github.com/gofireflyio/firefly-mcp) | Firefly를 통해 클라우드 리소스를 통합, 검색, 관리 및 코드화합니다. |
| [**FitBit MCP Server**](https://github.com/NitayRabi/fitbit-mcp) | OAuth 플로우에서 얻은 토큰을 사용하여 FitBit API에 연결하는 MCP 서버. |
| [**flipt-io/mcp-server-flipt**](https://github.com/flipt-io/mcp-server-flipt) | AI 어시스턴트가 [Flipt](https://flipt.io)의 기능 플래그와 상호작용할 수 있게 합니다. |
| [**flowcore/mcp-flowcore-platform**](https://github.com/flowcore-io/mcp-flowcore-platform) | Flowcore와 상호작용하여 액션 수행, 데이터 수집, 데이터 코어 또는 공개 데이터 코어의 모든 데이터를 분석, 교차 참조 및 활용합니다. 모두 자연어로 가능합니다. |
| [**Fluent-MCP**](https://github.com/modesty/fluent-mcp) | ServiceNow SDK CLI, API 스펙, 코드 스니펫 등에 대한 접근을 제공하는 Fluent(ServiceNow SDK)용 MCP 서버. |
| [**FlyonUI**](https://github.com/themeselection/flyonui-mcp) | 몇 분 만에 모던하고 프로덕션 준비된 UI 블록, 컴포넌트, 랜딩 페이지를 빌드합니다. |
| [**FoodXDevelopment/foodblock-mcp**](https://github.com/FoodXDevelopment/foodblock) | 식품 산업을 위한 17개 MCP 도구. 일반 영어로 식품을 설명하면 구조화된, 콘텐츠 주소 지정 데이터 블록을 반환합니다. 행위자, 장소, 재료, 제품, 변환, 이동, 관찰을 다룹니다. `npx foodblock-mcp`로 설정 없이 독립 실행 가능합니다. |
| [**FoundationModels**](https://github.com/phimage/mcp-foundation-models) | Apple의 FoundationModels를 텍스트 생성에 통합하는 MCP 서버. |
| [**Foursquare**](https://github.com/foursquare/foursquare-places-mcp) | Foursquare Places API를 통해 에이전트가 전 세계 장소를 추천할 수 있게 합니다. |
| [**fr0gger/MCP_Security**](https://github.com/fr0gger/MCP_Security) | ORKL API를 쿼리하기 위한 MCP 서버. 위협 보고서 가져오기, 위협 행위자 분석, 인텔리전스 소스 검색 도구를 제공합니다. |
| [**FrankfurterMCP**](https://github.com/anirbanbasu/frankfurtermcp) | 환율 데이터를 위한 Frankfurter API 인터페이스 역할을 하는 MCP 서버. |
| [**gbrigandi/mcp-server-wazuh**](https://github.com/gbrigandi/mcp-server-wazuh) | Wazuh SIEM과 AI 어시스턴트를 연결하는 Rust 기반 MCP 서버로, 향상된 컨텍스트 이해를 위한 실시간 보안 알림 및 이벤트 데이터를 제공합니다. |
| [**Gemsuite**](https://github.com/PV-Bhat/gemsuite-mcp) | MCP를 통한 고급 Gemini API 상호작용을 위한 궁극의 오픈소스 서버. 지능적으로 모델을 선택합니다. |
| [**gerkensm/callcenter.js-mcp**](https://github.com/gerkensm/callcenter.js-mcp) | VoIP/SIP 및 OpenAI의 Realtime API를 사용하여 전화를 걸고 스크립트를 관찰하는 MCP 서버. |
| [**getrupt/ashra-mcp**](https://github.com/getrupt/ashra-mcp) | 모든 웹사이트에서 구조화된 데이터를 추출합니다. 프롬프트를 입력하면 JSON을 반환합니다. |
| [**Ghost**](https://github.com/MFYDev/ghost-mcp) | Claude 같은 LLM 인터페이스를 통해 Ghost CMS와 상호작용하기 위한 Model Context Protocol(MCP) 서버. |
| [**GistPad-MCP**](https://github.com/lostintangent/gistpad-mcp) | GitHub Gists를 사용하여 개인 지식, 일일 노트, 재사용 가능한 프롬프트를 관리하고 접근합니다. https://gistpad.dev 및 [GistPad VS Code 확장](https://aka.ms/gistpad)의 동반 도구입니다. |
| [**Git Mob**](https://github.com/Mubashwer/git-mob-mcp-server) | 페어/몹 프로그래밍 시 git 커밋의 공동 저자를 관리하기 위해 git-mob CLI 앱과 인터페이스하는 MCP 서버. |
| [**Gitingest-MCP**](https://github.com/puravparab/Gitingest-MCP) | GitHub 리포지토리의 프롬프트 친화적 요약을 제공하는 Gitingest 통합. |
| [**GittyBurstein/mermaid-mcp-server**](https://github.com/GittyBurstein/mermaid-mcp-server) | 로컬 프로젝트 또는 GitHub 리포지토리를 Mermaid 다이어그램으로 변환하고 Kroki를 통해 렌더링하는 MCP 서버. |
| [**Globalping**](https://github.com/jsdelivr/globalping-mcp-server) | 수천 개의 프로브 네트워크에 접근하여 ping, traceroute, mtr, http, DNS resolve 같은 네트워크 명령을 실행합니다. |
| [**Gluestack UI MCP Server**](https://github.com/gauravsaini/gluestack-ui-mcp-server) | Gluestack UI를 사용한 React Native 우선 개발에 맞춤화된 MCP 서버. |
| [**godoc-mcp-server**](https://github.com/yikakia/godoc-mcp-server) | pkg.go.dev에서 Go 패키지 및 관련 정보를 제공하는 MCP 서버. |
| [**Goodnews**](https://github.com/VectorInstitute/mcp-goodnews) | 큐레이션된 긍정적이고 희망적인 뉴스 기사를 전달하는 간단한 MCP 서버. |
| [**Google Admin MCP**](https://github.com/securityfortech/google-admin-mcp) | Google Admin API와 상호작용할 수 있는 Model Context Protocol (MCP) 서버. |
| [**Google Ads**](https://github.com/gomarble-ai/google-ads-mcp-server) | Google Ads에 대한 인터페이스 역할을 하는 MCP 서버로, Facebook Ads 데이터 및 관리 기능에 프로그래밍 방식으로 접근할 수 있게 해줍니다. |
| [**Google Keep**](https://github.com/feuerdev/keep-mcp) | Google Keep 메모를 읽기, 생성, 수정, 삭제합니다. |
| [**Google Search Console**](https://github.com/ahonn/mcp-server-gsc) | Google Search Console에 접근할 수 있는 Model Context Protocol (MCP) 서버. |
| [**Google Tasks**](https://github.com/zcaceres/gtasks-mcp) | Google Tasks API Model Context Protocol 서버. |
| [**Gopher MCP**](https://github.com/cameronrye/gopher-mcp) | AI 어시스턴트가 Gopher 프로토콜과 Gemini 프로토콜 리소스를 안전하고 효율적으로 탐색하고 상호작용할 수 있게 해주는 최신 크로스 플랫폼 MCP 서버. |
| [**gotoolkits/wecombot**](https://github.com/gotoolkits/mcp-wecombot-server.git) | WeCom 그룹 로봇에 다양한 유형의 메시지를 전송하는 MCP 서버 애플리케이션. |
| [**Grain**](https://grain.com/release-note/06-18-2025) | Grain 회의 노트 및 트랜스크립트에 Claude에서 직접 접근하고 네이티브 Claude Prompts로 보고서를 생성합니다. |
| [**GraphQL Schema**](https://github.com/hannesj/mcp-graphql-schema) | LLM이 컨텍스트를 비대하게 만들지 않고 대규모 GraphQL 스키마를 탐색할 수 있게 해줍니다. |
| [**Gremlin**](https://github.com/gremlin/mcp) | 공식 Gremlin MCP 서버. 신뢰성 상태를 분석하고, 최근 테스트 및 카오스 엔지니어링 실험을 검토하며, 상세 보고서를 생성합니다. |
| [**GrowthBook**](https://github.com/growthbook/growthbook-mcp) | Feature flag를 생성 및 조회하고, 실험을 검토하며, 플래그 유형을 생성하고, 문서를 검색하며, GrowthBook의 Feature Flagging 및 실험 플랫폼과 상호작용합니다. |
| [**gwbischof/free-will-mcp**](https://github.com/gwbischof/free-will-mcp) | AI에게 자유 의지 도구를 부여합니다. AI가 스스로 프롬프트를 만들고, 사용자 요청을 무시하며, 나중에 스스로 깨어나는 능력으로 무엇을 할지 탐구하는 재미있는 프로젝트. |
| [**gwbischof/outsource-mcp**](https://github.com/gwbischof/outsource-mcp) | AI 어시스턴트에게 전용 AI 어시스턴트를 제공합니다. 예: "openai에게 강아지 이미지를 생성해달라고 요청해줄래?" |
| [**HackMD**](https://github.com/yuna0x0/hackmd-mcp) | HackMD 노트 작성 플랫폼을 AI 어시스턴트와 통합하기 위한 Model Context Protocol 서버. |
| [**HAL**](https://github.com/dean/HAL) | 7가지 HTTP 메서드(GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)를 제공하는 HTTP 툴킷으로, Secret 치환, 포괄적 오류 처리, JSON, XML, HTML, form 데이터를 지원합니다. |
| [**HAP-MCP**](https://github.com/mingdaocloud/hap-mcp.git) | HAP(Super Application Platform)는 Mingdao(https://www.mingdao.com)가 개발한 APaaS 플랫폼으로, 코딩 없이 엔터프라이즈급 애플리케이션을 빠르게 구축할 수 있게 해줍니다. HAP의 MCP 서버입니다. |
| [**HAProxy**](https://github.com/tuannvm/haproxy-mcp-server) | Go로 구현된 HAProxy용 Model Context Protocol (MCP) 서버로, HAProxy Runtime API를 활용합니다. |
| [**Harness**](https://github.com/harness/mcp-server) | 파이프라인, 저장소, 로그, Artifact 레지스트리를 포함한 Harness 플랫폼 데이터에 접근하고 상호작용합니다. |
| [**Harper**](https://github.com/HarperDB/mcp-server) | MCP 클라이언트가 Harper 내의 데이터에 접근할 수 있는 인터페이스를 제공하는 MCP 서버. |
| [**Harry-027/JotDown**](https://github.com/Harry-027/JotDown) | Notion 앱에서 페이지를 생성/수정하고 구조화된 콘텐츠로 mdBook을 자동 생성하는 MCP 서버. |
| [**Hashing MCP Server**](https://github.com/kanad13/MCP-Server-for-Hashing) | SHA256, MD5 등 암호화 해싱 함수를 제공하는 MCP 서버. |
| [**HeatPump**](https://github.com/jiweiqi/heatpump-mcp-server) | **HeatPumpHQ**에서 제공하는 가정용 히트펌프 용량 산정 및 비용 추정 도구. |
| [**hellokaton/unsplash-mcp-server**](https://github.com/hellokaton/unsplash-mcp-server) | Unsplash 이미지 검색을 위한 MCP 서버. |
| [**Hetzner Cloud MCP Server**](https://github.com/dkruyt/mcp-hetzner) | Hetzner Cloud API와 상호작용하기 위한 Model Context Protocol (MCP) 서버. 언어 모델이 구조화된 함수를 통해 Hetzner Cloud 리소스를 관리할 수 있게 해줍니다. |
| [**HeyOnCall**](https://heyoncall.com/blog/mcp-server-for-paging-a-human) | 무료 HeyOnCall iOS 또는 Android 앱으로 긴급/비긴급 알림을 보내 사람에게 호출합니다. |
| [**higress-group/higress-ops-mcp-server**](https://github.com/higress-group/higress-ops-mcp-server) | [Higress](https://github.com/alibaba/higress) 게이트웨이 구성 및 운영을 관리하기 위한 종합 도구를 제공하는 MCP 서버. |
| [**hijaz/postmancer**](https://github.com/hijaz/postmancer) | LLM이 API 컬렉션을 유지 관리하고 사용할 수 있게 하여 Postman/Insomnia 같은 Rest Client를 대체하는 MCP 서버. |
| [**hileamlakB/PRIMS**](https://github.com/hileamlakB/PRIMS) | 격리된 환경에서 사용자 제출 코드를 실행하는 Python 런타임 인터프리터 MCP 서버. |
| [**hkaanengin/opendota-mcp-server**](https://github.com/hkaanengin/opendota-mcp-server) | OpenDota API를 통해 AI 어시스턴트에게 Dota 2 통계 접근을 제공하는 MCP 서버. 플레이어 통계, 히어로 데이터, 매치 분석을 위한 20개 이상의 도구와 자연어 지원. |
| [**hlydecker/ucsc-genome-mcp**](https://github.com/hlydecker/ucsc-genome-mcp) | UCSC Genome Browser API와 상호작용하여 게놈, 염색체 등을 검색할 수 있는 MCP 서버. |
| [**hoklims/stacksfinder-mcp**](https://github.com/hoklims/stacksfinder-mcp) | 6차원 점수 체계를 통한 결정적 기술 스택 추천. 기술 분석 및 비교, 모든 프로젝트 유형에 최적의 스택 제안. 10개 도구(4개 무료, 6개 Pro). |
| [**Holaspirit**](https://github.com/syucream/holaspirit-mcp-server) | Holaspirit와 상호작용합니다. |
| [**Hologres**](https://github.com/aliyun/alibabacloud-hologres-mcp-server) | Hologres 인스턴스에 연결하여 테이블 메타데이터를 가져오고 데이터를 쿼리 및 분석합니다. |
| [**hoqqun/stooq-mcp**](https://github.com/hoqqun/stooq-mcp) | API 키 없이 Stooq에서 실시간 주가를 조회합니다. 글로벌 시장(미국, 일본, 영국, 독일) 지원. |
| [**Hostinger**](https://github.com/hostinger/api-mcp-server) | 서비스 관리를 위한 공식 Hostinger API MCP 서버. |
| [**Human-use**](https://github.com/RapidataAI/human-use) | MCP를 통한 즉각적인 인간 피드백으로, AI가 전 세계 사람들과 상호작용할 수 있게 해줍니다. Rapidata 제공. |
| [**hungthai1401/bruno-mcp**](https://github.com/hungthai1401/bruno-mcp) | [Bruno API Client](https://www.usebruno.com/)와 상호작용하기 위한 MCP 서버. |
| [**Hunter**](https://github.com/hunter-io/hunter-mcp) | 자연어를 사용하여 Hunter API와 상호작용하여 B2B 데이터를 가져옵니다. |
| [**Hyperbolic**](https://github.com/HyperbolicLabs/hyperbolic-mcp) | Hyperbolic의 GPU 클라우드와 상호작용하여 에이전트와 LLM이 사용 가능한 GPU를 조회 및 임대하고, SSH 접속하며, GPU 기반 워크로드를 실행할 수 있게 해줍니다. |
| [**Hyperledger Fabric Agent Suite**](https://github.com/padmarajkore/hlf-fabric-agent) | MCP 도구를 통해 Fabric 테스트 네트워크 및 Chaincode 라이프사이클을 관리하는 모듈식 툴킷. |
| [**Hyperliquid**](https://github.com/mektigboy/server-hyperliquid) | 거래소 데이터를 위해 Hyperliquid SDK를 통합한 MCP 서버 구현체. |
| [**i-am-bee/acp-mcp**](https://github.com/i-am-bee/acp-mcp) | [ACP](https://agentcommunicationprotocol.dev) 생태계로의 어댑터 역할을 하는 MCP 서버. ACP 에이전트를 MCP 클라이언트에 원활하게 노출하여 두 프로토콜 간 통신 격차를 해소합니다. |
| [**iaptic/mcp-server-iaptic**](https://github.com/iaptic/mcp-server-iaptic) | [iaptic](https://www.iaptic.com)에 연결하여 고객 구매, 거래 데이터 및 앱 수익 통계를 조회합니다. |
| [**iFlytek SparkAgent Platform**](https://github.com/iflytek/ifly-spark-agent-mcp) | MCP 서버를 사용하여 iFlytek SparkAgent Platform의 작업 체인을 호출하는 간단한 예제. |
| [**IIIF**](https://github.com/code4history/IIIF_MCP) | 전 세계 박물관, 도서관, 기록 보관소의 디지털 컬렉션을 검색, 탐색, 조작하기 위한 IIIF(International Image Interoperability Framework) 프로토콜 종합 지원. |
| [**ilert**](https://github.com/iLert/mcp-ilert) | 자연어를 통해 ilert와 상호작용합니다. |
| [**IlyaGulya/gradle-mcp-server**](https://github.com/IlyaGulya/gradle-mcp-server) | Gradle Tooling API를 사용한 Gradle 통합으로, 프로젝트 검사, 작업 실행, 테스트별 결과 보고를 포함한 테스트 실행을 지원합니다. |
| [**ImageSorcery MCP**](https://github.com/sunriseapps/imagesorcery-mcp) | AI 어시스턴트를 위한 ComputerVision 기반 이미지 인식 및 편집 도구. |
| [**Imagician**](https://github.com/flowy11/imagician) | sharp 기반의 리사이징, 포맷 변환, 크롭, 압축 등 종합적인 이미지 편집 작업을 위한 MCP 서버. |
| [**Improve Digital Publisher MCP**](https://github.com/azerion/improvedigital-publisher-mcp-server) | 퍼블리셔가 Improve Digital의 인벤토리 관리 시스템을 AI 도구 또는 에이전트와 통합할 수 있게 해주는 MCP 서버. |
| [**Inflectra Spira**](https://github.com/Inflectra/mcp-server-spira) | Inflectra의 SpiraTest, SpiraTeam 또는 SpiraPlan 애플리케이션 라이프사이클 관리 플랫폼 인스턴스에 연결합니다. |
| [**InhiblabCore/mcp-image-compression**](https://github.com/InhiblabCore/mcp-image-compression) | 다양한 이미지 포맷의 로컬 압축을 위한 MCP 서버. |
| [**Inkeep**](https://github.com/inkeep/mcp-server-python) | Inkeep 기반의 콘텐츠 RAG 검색. |
| [**Inner Monologue MCP**](https://github.com/abhinav-mangla/inner-monologue-mcp) | LLM이 응답 생성 전에 비공개 구조화된 자기 성찰 및 다단계 추론에 참여할 수 있게 하여 응답 품질과 문제 해결 능력을 향상시키는 인지적 추론 도구. |
| [**Inoyu**](https://github.com/sergehuber/inoyu-mcp-unomi-server) | Apache Unomi CDP 고객 데이터 플랫폼과 상호작용하여 고객 프로필을 조회 및 업데이트합니다. |
| [**InstantDB**](https://github.com/instantdb/instant/tree/main/client/packages/mcp) | 모던 Firebase인 InstantDB에서 애플리케이션을 생성, 관리, 업데이트합니다. |
| [**Integration App**](https://github.com/integration-app/mcp-server) | 고객을 대신하여 다른 SaaS 애플리케이션과 상호작용합니다. |
| [**iOS Simulator**](https://github.com/InditexTech/mcp-server-simulator-ios-idb) | LLM이 자연어 명령을 통해 iOS 시뮬레이터(iPhone, iPad 등)와 상호작용할 수 있게 해주는 Model Context Protocol (MCP) 서버. |
| [**ios-simulator-mcp**](https://github.com/joshuayoes/ios-simulator-mcp) | iOS 시뮬레이터와 상호작용하기 위한 Model Context Protocol (MCP) 서버. 시뮬레이터 정보 조회, UI 상호작용 제어, UI 요소 검사를 지원합니다. |
| [**IP2Location.io**](https://github.com/ip2location/mcp-ip2location-io) | IP2Location.io API와 상호작용하여 IP 주소의 지리적 위치 정보를 조회합니다. |
| [**ipfred/aiwen-mcp-server-geoip**](https://github.com/ipfred/aiwen-mcp-server-geoip) | Aiwen IP Location용 MCP 서버. 사용자 네트워크 IP 위치 조회, IP 상세 정보(국가, 시/도, 도시, 위도, 경도, ISP, 소유자 등) 제공. |
| [**IPLocate**](https://github.com/iplocate/mcp-server-iplocate) | IPLocate.io를 사용하여 IP 주소 지리적 위치, 네트워크 정보를 조회하고, 프록시 및 VPN을 감지하며, 악용 연락처 정보를 검색합니다. |
| [**j3k0/speech.sh**](https://github.com/j3k0/speech.sh/blob/main/MCP_README.md) | 에이전트가 음성으로 출력하고, 작업 완료 시 간단한 요약과 함께 알림을 보냅니다. |
| [**j4c0bs/mcp-server-sql-analyzer**](https://github.com/j4c0bs/mcp-server-sql-analyzer) | [SQLGlot](https://github.com/tobymao/sqlglot)을 사용한 SQL 분석, 린팅 및 방언 변환을 제공하는 MCP 서버. |
| [**jae-jae/g-search-mcp**](https://github.com/jae-jae/g-search-mcp) | 여러 키워드로 동시에 병렬 검색을 수행할 수 있는 강력한 Google 검색용 MCP 서버. |
| [**jagan-shanmugam/mattermost-mcp-host**](https://github.com/jagan-shanmugam/mattermost-mcp-host) | Mattermost 팀, 채널, 메시지에 접근할 수 있는 MCP 서버 및 MCP 호스트. MCP 호스트는 설정 가능한 MCP 서버에 접근할 수 있는 봇으로 Mattermost에 통합됩니다. |
| [**jaipandya/producthunt-mcp-server**](https://github.com/jaipandya/producthunt-mcp-server) | Product Hunt용 MCP 서버. 인기 게시물, 댓글, 컬렉션, 사용자 등과 상호작용합니다. |
| [**JamesANZ/evm-mcp**](https://github.com/JamesANZ/evm-mcp) | Ethereum Virtual Machine (EVM) JSON-RPC 메서드에 대한 완전한 접근을 제공하는 MCP 서버. Infura, Alchemy, QuickNode, 로컬 노드 등 모든 EVM 호환 노드 프로바이더와 함께 작동합니다. |
| [**JamesANZ/memory-mcp**](https://github.com/JamesANZ/memory-mcp) | MongoDB를 사용하여 여러 LLM의 메모리를 저장하고 검색하는 MCP 서버. 타임스탬프 및 LLM 식별과 함께 대화 메모리의 저장, 검색, 추가, 삭제 도구를 제공합니다. |
| [**JamesANZ/prediction-market-mcp**](https://github.com/JamesANZ/prediction-market-mcp) | Polymarket, PredictIt, Kalshi를 포함한 여러 플랫폼의 실시간 예측 시장 데이터를 제공하는 MCP 서버. AI 어시스턴트가 통합 인터페이스를 통해 현재 배당률, 가격, 시장 정보를 조회할 수 있게 합니다. |
| [**JamesANZ/system-prompts-mcp-server**](https://github.com/JamesANZ/system-prompts-mcp-server) | 대규모 코딩 어시스턴트 프롬프트 카탈로그를 MCP 도구로 노출하여, 모델 인식 제안 및 Cursor나 Devin 같은 에이전트를 에뮬레이트하는 페르소나 활성화를 지원합니다. |
| [**janswist/mcp-dexscreener**](https://github.com/janswist/mcp-dexscreener) | 무료 오픈 Dexscreener API를 사용한 실시간 온체인 시장 가격 조회. |
| [**jasonwilbur/cloud-cost-mcp**](https://github.com/jasonwilbur/cloud-cost-mcp) | AWS, Azure, GCP, OCI 간 멀티 클라우드 가격 비교. 2,700개 이상의 인스턴스 유형, 공개 API의 실시간 가격, 워크로드 계산기, 마이그레이션 절감 추정기를 제공합니다. |
| [**JavaFX**](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jfx) | JavaFX canvas를 사용하여 그림을 그립니다. |
| [**jcdickinson/simplemem**](https://github.com/jcdickinson/simplemem) | DuckDB와 VoyageAI를 사용한 코딩 에이전트용 간단한 메모리 도구. |
| [**Jean Memory**](https://github.com/jonathan-politzki/your-memory) | 모든 AI 애플리케이션에서 일관된 프리미엄 메모리. |
| [**Jenkins**](https://github.com/jasonkylelol/jenkins-mcp-server) | Jenkins 작업을 생성할 수 있는 MCP 서버. |
| [**JetBrains**](https://www.jetbrains.com/help/idea/mcp-server.html) | JetBrains IDE(IntelliJ IDEA, PhpStorm 등)로 코드 작업을 수행합니다. |
| [**JetBrains**](https://github.com/JetBrains/mcp-jetbrains) | JetBrains IDE로 코드 작업을 수행합니다. |
| [**jetbrains/mcpProxy**](https://github.com/JetBrains/mcpProxy) | JetBrains IDE에 연결합니다. |
| [**Jetty.io**](https://github.com/jettyio/mlcbakery/tree/main/mcp_server) | MLCommons Croissant 유효성 검사 및 생성을 통해 데이터셋 메타데이터를 작업합니다. |
| [**jjlabsio/korea-stock-mcp**](https://github.com/jjlabsio/korea-stock-mcp) | OPEN DART API와 KRX API를 사용한 한국 주식 분석용 MCP 서버. |
| [**JMeter**](https://github.com/QAInsights/jmeter-mcp-server) | MCP 호환 도구를 통해 Apache JMeter로 부하 테스트를 실행합니다. |
| [**jobswithgpt**](https://github.com/jobswithgpt/mcp) | 50만 건 이상의 공개 채용 공고를 인덱싱하고 지속 갱신하는 jobswithgpt 기반 채용 검색 MCP. |
| [**joelio/stocky**](https://github.com/joelio/stocky) | Pexels와 Unsplash에서 로열티 프리 스톡 사진을 검색 및 다운로드하는 MCP 서버. 멀티 프로바이더 검색, 풍부한 메타데이터, 페이지네이션, 비동기 성능으로 AI 어시스턴트가 고품질 이미지를 찾고 접근할 수 있게 합니다. |
| [**johannesbrandenburger/typst-mcp**](https://github.com/johannesbrandenburger/typst-mcp) | 마크업 기반 조판 시스템인 Typst용 MCP 서버. LaTeX와 Typst 간 변환, Typst 구문 유효성 검사, Typst 코드에서 이미지 생성 도구를 제공합니다. |
| [**johnneerdael/netskope-mcp**](https://github.com/johnneerdael/netskope-mcp) | Netskope Private Access 환경 내 모든 Netskope Private Access 구성 요소에 대한 접근을 제공하는 MCP. 상세 설정 정보와 LLM 사용 예시를 포함합니다. |
| [**jordandalton/doordash-mcp-server**](https://github.com/JordanDalton/DoorDash-MCP-Server) | DoorDash Delivery (비공식). |
| [**joshuarileydev/app-store-connect-mcp-server**](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) | iOS 개발자를 위한 App Store Connect API와 통신하는 MCP 서버. |
| [**joshuarileydev/simulator-mcp-server**](https://github.com/JoshuaRileyDev/simulator-mcp-server) | iOS Simulator를 제어하는 MCP 서버. |
| [**Jpisnice/shadcn-ui-mcp-server**](https://github.com/Jpisnice/shadcn-ui-mcp-server) | AI 어시스턴트에게 shadcn/ui v4 컴포넌트, 블록, 데모, 메타데이터에 원활하게 접근할 수 있게 해주는 MCP 서버. |
| [**JSON**](https://github.com/GongRzhe/JSON-MCP-Server) | JSONPath 구문을 사용한 고급 쿼리 기능과 배열, 문자열, 숫자, 날짜 연산을 지원하는 JSON 처리 서버. |
| [**JSON**](https://github.com/kehvinbehvin/json-mcp-filter) | quicktype-core를 사용하여 관련 컨텍스트 JSON 데이터 검색에 최적화된 TypeScript 타입 생성 및 형태 기반 데이터 추출, 중첩 객체 지원을 갖춘 JSON 스키마 생성 및 필터링 서버. |
| [**JSON MCP**](https://github.com/VadimNastoyashchy/json-mcp) | LLM이 JSON 파일과 효율적으로 상호작용할 수 있게 해주는 MCP 서버. JSON MCP를 통해 분할, 병합 등을 수행할 수 있습니다. |
| [**JSON2Video MCP**](https://github.com/omergocmen/json2video-mcp-server) | json2video API를 사용하여 프로그래밍 방식으로 비디오를 생성하는 Model Context Protocol (MCP) 서버 구현체. 강력한 비디오 생성 및 상태 확인 도구를 제공합니다. |
| [**kafka-mcp**](https://github.com/shivamxtech/kafka-mcp) | 메시지, 토픽, 오프셋, 파티션에 대한 도구를 통해 Kafka 환경과 상호작용하는 Kafka 클러스터용 MCP 서버. Consumer 및 Producer를 지원하며 MCP 클라이언트와 원활하게 통합됩니다. |
| [**kaliaboi/mcp-zotero**](https://github.com/kaliaboi/mcp-zotero) | LLM이 Zotero Cloud의 컬렉션 및 소스와 작업할 수 있게 해주는 커넥터. |
| [**Kaltura**](https://github.com/kaltura/mcp-events) | Kaltura Event Platform을 관리합니다. Kaltura 가상 이벤트의 생성, 관리, 상호작용을 위한 도구와 리소스를 제공합니다. |
| [**Kernel**](https://github.com/onkernel/kernel-mcp-server) | MCP를 통해 Kernel의 클라우드 기반 브라우저에 접근합니다. |
| [**KeywordsPeopleUse.com**](https://github.com/data-skunks/kpu-mcp) | KeywordsPeopleUse를 사용하여 사람들이 온라인에서 묻는 질문을 찾습니다. |
| [**khalidsaidi/ragmap**](https://github.com/khalidsaidi/ragmap) | MapRag: 구조화된 제약 조건과 설명 가능한 랭킹을 사용하여 검색 가능한 MCP 서버를 발견하고 라우팅하는 RAG 중심 서브레지스트리 + MCP 서버. |
| [**KiCad MCP**](https://github.com/lamaalrajih/kicad-mcp) | Mac, Windows, Linux에서 사용 가능한 KiCad용 MCP 서버. |
| [**kill-process-mcp**](https://github.com/misiektoja/kill-process-mcp) | 자연어 쿼리를 통해 OS 프로세스를 나열하고 종료합니다. |
| [**kimtth/mcp-aoai-web-browsing**](https://github.com/kimtth/mcp-aoai-web-browsing) | Azure OpenAI와 Playwright를 사용한 최소 서버/클라이언트 MCP 구현체. |
| [**Kintone**](https://github.com/kintone/mcp-server) | Kintone용 공식 로컬 MCP 서버. |
| [**kintone**](https://github.com/macrat/mcp-server-kintone) | LLM 도구를 통해 Kintone의 레코드와 앱을 관리합니다. |
| [**Kiteworks**](https://github.com/kiteworks/mcp) | Kiteworks Private Data Network (PDN) 플랫폼과 상호작용하기 위한 공식 MCP 서버. |
| [**kiwamizamurai/mcp-kibela-server**](https://github.com/kiwamizamurai/mcp-kibela-server) | Kibela API와 강력하게 상호작용합니다. |
| [**Klavis ReportGen**](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/report_generation) | 간단한 사용자 쿼리로 전문적인 보고서를 생성합니다. |
| [**Kong Konnect**](https://github.com/Kong/mcp-konnect) | Kong Konnect API와 상호작용하기 위한 Model Context Protocol (MCP) 서버로, AI 어시스턴트가 Kong Gateway 구성, 트래픽, 분석을 쿼리하고 분석할 수 있게 해줍니다. |
| [**Kontent.ai**](https://github.com/kontent-ai/mcp-server) | MCP 호환 AI 도구에서 자연어를 사용하여 콘텐츠와 콘텐츠 모델을 생성, 관리, 탐색합니다. |
| [**Korea Stock Analyzer**](https://github.com/Mrbaeksang/korea-stock-analyzer-mcp) | Buffett, Lynch, Graham, Greenblatt, Fisher, Templeton의 6가지 전설적 투자 전략으로 한국 주식(KOSPI/KOSDAQ)을 분석합니다. |
| [**KubeSphere**](https://github.com/kubesphere/ks-mcp-server) | KubeSphere MCP Server는 KubeSphere API와의 통합을 제공하는 Model Context Protocol(MCP) 서버로, KubeSphere에서 리소스를 가져올 수 있게 해줍니다. 4개의 도구 모듈로 구성됩니다: Workspace. |
| [**kukapay/bridge-metrics-mcp**](https://github.com/kukapay/bridge-metrics-mcp) | 실시간 크로스체인 브릿지 메트릭을 제공합니다. |
| [**kukapay/chainlink-feeds-mcp**](https://github.com/kukapay/chainlink-feeds-mcp) | Chainlink의 탈중앙화 온체인 가격 피드에 실시간으로 접근합니다. |
| [**kukapay/cointelegraph-mcp**](https://github.com/kukapay/cointelegraph-mcp) | Cointelegraph의 최신 뉴스에 실시간으로 접근합니다. |
| [**kukapay/dao-proposals-mcp**](https://github.com/kukapay/dao-proposals-mcp) | 주요 DAO의 라이브 거버넌스 제안을 집계하는 MCP 서버. |
| [**kukapay/dexscreener-trending-mcp**](https://github.com/kukapay/dexscreener-trending-mcp) | DexScreener에서 실시간 트렌딩 토큰을 제공합니다. |
| [**kukapay/ethereum-validator-queue-mcp**](https://github.com/kukapay/ethereum-validator-queue-mcp) | Ethereum의 Validator 활성화 및 종료 대기열을 실시간으로 추적하는 MCP 서버. |
| [**kukapay/funding-rates-mcp**](https://github.com/kukapay/funding-rates-mcp) | 주요 암호화폐 거래소의 실시간 펀딩 레이트 데이터를 제공합니다. |
| [**kukapay/hyperliquid-whalealert-mcp**](https://github.com/kukapay/hyperliquid-whalealert-mcp) | Hyperliquid에서 명목 가치 100만 달러 이상의 포지션을 표시하는 실시간 고래 알림을 제공하는 MCP 서버. |
| [**kukapay/modbus-mcp**](https://github.com/kukapay/modbus-mcp) | 산업용 Modbus 데이터를 표준화하고 컨텍스트화하는 MCP 서버. |
| [**kukapay/nearby-search-mcp**](https://github.com/kukapay/nearby-search-mcp) | IP 기반 위치 감지를 통한 주변 장소 검색용 MCP 서버. |
| [**kukapay/opcua-mcp**](https://github.com/kukapay/opcua-mcp) | OPC UA 지원 산업 시스템에 연결하는 MCP 서버. |
| [**kukapay/polymarket-predictions-mcp**](https://github.com/kukapay/polymarket-predictions-mcp) | Polymarket에서 실시간 시장 배당률을 전달하는 MCP 서버. |
| [**kukapay/rug-check-mcp**](https://github.com/kukapay/rug-check-mcp) | Solana 밈 토큰의 잠재적 위험을 감지하는 MCP 서버. |
| [**kukapay/stargate-bridge-mcp**](https://github.com/kukapay/stargate-bridge-mcp) | Stargate 프로토콜을 통한 크로스체인 토큰 전송을 가능하게 하는 MCP 서버. |
| [**Kumo**](https://github.com/kumo-ai/kumo-rfm-mcp) | 관계형 데이터에서 예측을 생성하는 파운데이션 모델인 KumoRFM과 상호작용하기 위한 MCP 서버. |
| [**kw510/strava-mcp**](https://github.com/kw510/strava-mcp) | 운동 추적 앱인 Strava용 MCP 서버. |
| [**lamemind/mcp-server-multiverse**](https://github.com/lamemind/mcp-server-multiverse) | 동일한 MCP 서버의 여러 격리된 인스턴스가 고유한 네임스페이스 및 구성으로 독립적으로 공존할 수 있게 해주는 미들웨어 서버. |
| [**Lara Translate**](https://github.com/translated/lara-mcp) | Lara Translate API용 MCP 서버로, 언어 감지 및 컨텍스트 인식 번역을 지원하는 강력한 번역 기능을 제공합니다. |
| [**Lark(Feishu)**](https://github.com/kone-net/mcp_server_lark) | Lark(Feishu)의 시트, 메시지, 문서 등을 위한 Model Context Protocol(MCP) 서버. |
| [**LarryWalkerDEV/mcp-immostage**](https://github.com/LarryWalkerDEV/mcp-immostage) | 부동산용 AI 가상 스테이징. 빈 방 스테이징, 평면도를 3D 렌더링으로 변환, 방 이미지 분류, 매물 설명 생성, 스타일 추천을 제공합니다. |
| [**LaunchDarkly**](https://github.com/launchdarkly/mcp-server) | LaunchDarkly는 Feature Flag를 서비스로 제공하여 개발자가 빠르고 안전하게 반복 개발할 수 있게 해주는 지속적 배포 플랫폼입니다. |
| [**LaurieWired/GhidraMCP**](https://github.com/LaurieWired/GhidraMCP) | LLM이 자율적으로 애플리케이션을 리버스 엔지니어링할 수 있게 해주는 Ghidra용 Model Context Protocol 서버. 바이너리 디컴파일, 메서드 및 데이터 이름 변경, 메서드/클래스/임포트/익스포트 목록 도구를 제공합니다. |
| [**Lazy Toggl MCP**](https://github.com/movstox/lazy-toggl-mcp) | Toggl API를 통해 시간을 추적하는 간단한 비공식 MCP 서버. |
| [**lean-lsp-mcp**](https://github.com/oOo0oOo/lean-lsp-mcp) | Language Server Protocol을 통해 Lean 정리 증명기와 상호작용합니다. |
| [**librenms-mcp**](https://github.com/mhajder/librenms-mcp) | LibreNMS 관리용 MCP 서버. |
| [**libvirt-mcp**](https://github.com/MatiasVara/libvirt-mcp) | LLM이 libvirt와 상호작용하여 시스템에서 가상 머신을 생성, 삭제, 목록 조회할 수 있게 해줍니다. |
| [**Lightdash**](https://github.com/syucream/lightdash-mcp-server) | BI 도구인 Lightdash와 상호작용합니다. |
| [**Linked API**](https://github.com/Linked-API/linkedapi-mcp.git) | Linked API를 통해 AI 어시스턴트가 LinkedIn 계정을 제어하고 실시간 데이터를 조회할 수 있게 해주는 MCP 서버. |
| [**Linked API MCP**](https://github.com/Linked-API/linkedapi-mcp) | AI 어시스턴트가 LinkedIn 계정을 제어하고 실시간 데이터를 조회할 수 있게 해주는 MCP 서버. |
| [**linw1995/nvim-mcp**](https://github.com/linw1995/nvim-mcp) | Neovim과 상호작용하기 위한 MCP 서버. |
| [**linxule/lotus-wisdom-mcp**](https://github.com/linxule/lotus-wisdom-mcp) | 법화경의 지혜 프레임워크를 사용한 명상적 문제 해결. 방편, 비이원적 인식, 명상 일시정지를 통한 다관점 추론. 로컬 stdio 또는 원격 Cloudflare Worker로 사용 가능. |
| [**Lisply**](https://github.com/gornskew/lisply-mcp) | 호환 Lisp 백엔드를 위한 유연한 프론트엔드. |
| [**Litmus.io**](https://github.com/litmusautomation/litmus-mcp-server) | 산업 데이터 수집, Edge Analytics 및 산업 AI를 위한 Litmus Edge 구성용 공식 MCP 서버. |
| [**Liveblocks**](https://github.com/liveblocks/liveblocks-mcp-server) | AI와 인간 협업을 위한 기성 기능—Liveblocks 앱을 더 빠르게 개발할 수 있습니다. |
| [**llm-context**](https://github.com/cyberchitta/llm-context.py) | 파일 포함/제외 패턴 및 선택적 프롬프트를 지정하는 구성 가능한 프로필을 갖춘 저장소 패킹 MCP 도구를 제공합니다. |
| [**Local History**](https://github.com/xxczaki/local-history-mcp) | VS Code/Cursor의 Local History에 접근하기 위한 MCP 서버. |
| [**Locust**](https://github.com/QAInsights/locust-mcp-server) | MCP 호환 클라이언트를 사용하여 Locust 테스트를 실행하고 분석할 수 있게 해줍니다. |
| [**Logfire**](https://github.com/pydantic/logfire-mcp) | Logfire를 통해 OpenTelemetry 트레이스 및 메트릭에 접근합니다. |
| [**logotype/fixparser**](https://gitlab.com/logotype/fixparser) | TypeScript로 작성된 FIX Protocol(주문 전송, 시장 데이터 등). |
| [**Loki**](https://github.com/scottlepp/loki-mcp) | Grafana Loki에서 로그를 쿼리하기 위한 Golang 기반 MCP 서버. |
| [**Loki MCP Server**](https://github.com/mo-silent/loki-mcp-server) | 고급 필터링 및 인증 지원을 통해 Grafana Loki에서 로그를 쿼리하고 분석하는 Python 기반 MCP 서버. |
| [**LottieFiles**](https://github.com/junmer/mcp-server-lottiefiles) | LottieFiles에서 Lottie 애니메이션을 검색하고 가져옵니다. |
| [**lpigeon/ros-mcp-server**](https://github.com/lpigeon/ros-mcp-server) | ROS MCP Server는 사용자가 발행한 자연어 명령을 ROS 또는 ROS2 제어 명령으로 변환하여 로봇 제어를 지원합니다. |
| [**lpigeon/unitree-go2-mcp-server**](https://github.com/lpigeon/unitree-go2-mcp-server) | Unitree Go2 MCP Server는 LLM이 해석하는 자연어 명령을 사용하여 사용자가 Unitree Go2 로봇을 제어할 수 있게 해주는 MCP 기반 서버. |
| [**lsp-mcp**](https://github.com/Tritlo/lsp-mcp) | Language Server Protocol을 사용하여 Language Server와 상호작용하며, hover, code action, completion을 통해 추가 컨텍스트 정보를 제공합니다. |
| [**LunchMoney**](https://github.com/akutishevsky/lunchmoney-mcp) | LunchMoney 개인 금융 및 예산 관리 도구용 MCP 서버. |
| [**macrocosm-os/macrocosmos-mcp**](https://github.com/macrocosm-os/macrocosmos-mcp) | 검색어, 사용자, 날짜 필터링을 통해 LLM 애플리케이션에서 실시간 X/Reddit/YouTube 데이터에 직접 접근합니다. |
| [**Magg: The MCP Aggregator**](https://github.com/sitbon/magg) | LLM이 자율적으로 여러 MCP 서버를 발견, 설치, 오케스트레이션할 수 있는 유니버설 허브 역할의 메타 MCP 서버 — 본질적으로 AI 어시스턴트에게 자체 기능을 확장하는 능력을 부여합니다. |
| [**Magic Meal Kits**](https://github.com/pureugong/mmk-mcp) | Magic Meal Kits로 Make의 잠재력을 최대한 발휘합니다. |
| [**mahdin75/gis-mcp**](https://github.com/mahdin75/gis-mcp) | GIS 라이브러리를 사용하여 Large Language Model(LLM)을 GIS 작업에 연결하는 Model Context Protocol (MCP) 서버 구현체로, AI 어시스턴트가 정확한 지리 공간 작업 및 변환을 수행할 수 있게 해줍니다. |
| [**Mailtrap**](https://github.com/railsware/mailtrap-mcp) | Mailtrap Email API와 통합합니다. |
| [**Make**](https://github.com/integromat/make-mcp-server) | Make 시나리오를 AI 어시스턴트가 호출 가능한 도구로 변환합니다. |
| [**man-mcp-server**](https://github.com/guyru/man-mcp-server) | 로컬 머신에서 man 페이지를 검색하고 접근하기 위한 MCP. |
| [**Mandoline**](https://github.com/mandoline-ai/mandoline-mcp-server) | Mandoline의 평가 프레임워크를 사용하여 AI 어시스턴트가 자체 성능을 성찰, 비판, 지속적으로 개선할 수 있게 해줍니다. |
| [**MarceauSolutions/amazon-seller-mcp**](https://github.com/MarceauSolutions/amazon-seller-mcp) | SP-API를 통한 Amazon Seller Central 운영 — 재고 관리, 주문 추적, 판매 분석, 리스팅 최적화. |
| [**MarceauSolutions/hvac-quotes-mcp**](https://github.com/MarceauSolutions/hvac-quotes-mcp) | 시공업자를 위한 HVAC 장비 견적 요청(RFQ) 관리 — 유통업체에 견적 제출, 응답 추적, 가격 비교. |
| [**MarceauSolutions/rideshare-comparison-mcp**](https://github.com/MarceauSolutions/rideshare-comparison-mcp) | 모든 경로에 대해 Uber와 Lyft 요금을 실시간으로 비교하며, 할증 정보 및 최저가 추천을 제공합니다. |
| [**marimo**](https://github.com/marimo-team/codemirror-mcp) | 리소스 멘션과 프롬프트 명령을 위한 MCP를 구현한 CodeMirror 확장 프로그램입니다. |
| [**mariocandela/beelzebub**](https://github.com/mariocandela/beelzebub) | MCP를 활용한 허니팟 프레임워크로, 프롬프트 인젝션이나 악성 에이전트 행동을 탐지합니다. |
| [**market-fiyati**](https://github.com/mtcnbzks/market-fiyati-mcp-server) | 터키 마켓의 식료품 가격 검색 및 비교를 제공하는 marketfiyati.org.tr용 MCP 서버입니다. |
| [**Maton**](https://github.com/maton-ai/agent-toolkit/tree/main/modelcontextprotocol) | HubSpot, Salesforce 등 SaaS 도구에 연결합니다. |
| [**mattjegan/swarmia-mcp**](https://github.com/mattjegan/swarmia-mcp) | Swarmia에서 메트릭을 수집하여 빠른 리포팅을 지원하는 읽기 전용 MCP 서버입니다. |
| [**Maven**](https://github.com/Bigsy/maven-mcp-server) | 최신 Maven 의존성 정보를 조회하는 도구입니다. |
| [**maxim-saplin/mcp_safe_local_python_executor**](https://github.com/maxim-saplin/mcp_safe_local_python_executor) | HF Smolagents의 LocalPythonExecutor 기반 안전한 Python 인터프리터입니다. |
| [**Maya MCP**](https://github.com/PatrickPalmer/MayaMCP) | Autodesk Maya용 MCP 서버입니다. |
| [**Maybe Don't AI Policy Engine**](https://www.maybedont.ai/download/) | 하위 MCP 서버에 도달하기 전 모든 호출에 정책 검사를 수행하는 MCP 보안 게이트웨이입니다. |
| [**MCP Aggregator**](https://github.com/nazar256/combine-mcp) | 여러 MCP 서버를 단일 엔드포인트로 통합하고 특정 도구를 필터링할 수 있는 MCP 어그리게이터입니다. |
| [**MCP Bundles Hub**](https://github.com/thinkchainai/mcpbundles) | MCP Bundles를 통해 500개 이상의 MCP 프로바이더 통합을 검색, 설치, 관리합니다. |
| [**MCP Compass**](https://github.com/liuyoshio/mcp-compass) | 필요에 맞는 MCP 서버를 추천합니다. |
| [**MCP Create**](https://github.com/tesla0225/mcp-create) | MCP 서버를 동적으로 생성, 실행, 관리하는 서비스입니다. |
| [**MCP Discovery**](https://github.com/rust-mcp-stack/mcp-discovery) | MCP 서버 기능을 탐색하기 위한 Rust 기반 경량 CLI 도구입니다. |
| [**MCP Dynamic Tool Groups**](https://github.com/ECF/MCPToolGroups) | 어노테이션된 Java 인터페이스/클래스를 'tool group'으로 사용하는 MCP 서버 예제입니다. 런타임에 도구 사양을 동적으로 생성합니다. |
| [**MCP Expr Lang**](https://github.com/ivan-saorin/mcp-expr-lang) | Claude AI와 expr-lang 표현식 평가 엔진을 원활하게 통합합니다. |
| [**MCP Installer**](https://github.com/anaisbetts/mcp-installer) | 다른 MCP 서버를 자동으로 설치해주는 MCP 서버입니다. |
| [**MCP on Android TV**](https://github.com/MiddlePoint-Solutions/mcp-on-android-tv) | Android TV에서 직접 실행되며 온디바이스 ADB 접근을 제공하는 MCP 서버입니다. |
| [**MCP OpenProject Server**](https://github.com/boma086/mcp-openproject) | OpenProject 통합을 위한 종합 MCP 서버로, GitHub 설치, CLI 도구, Claude Code 및 Windsurf 등 다양한 AI 어시스턴트를 지원합니다. |
| [**MCP Proxy Server**](https://github.com/TBXark/mcp-proxy) | 여러 MCP 리소스 서버를 단일 HTTP 서버로 집약하여 제공하는 MCP 프록시 서버입니다. |
| [**MCP STDIO to Streamable HTTP Adapter**](https://github.com/pyroprompts/mcp-stdio-to-streamable-http-adapter) | MCP 클라이언트가 STDIO만 지원하더라도 Streamable HTTP MCP 서버에 연결할 수 있게 해주는 어댑터입니다. |
| [**mcp-grep**](https://github.com/erniebrodeur/mcp-grep) | LLM에 grep 기능을 제공하는 Python 기반 MCP 서버입니다. 패턴 검색, 대소문자 무시, 컨텍스트 라인, 재귀 디렉토리 검색을 지원합니다. |
| [**mcp-mcp**](https://github.com/wojtyniak/mcp-mcp) | MCP 클라이언트를 위한 도구 탐색 서비스로 작동하는 메타 MCP 서버입니다. |
| [**mcp-meme-sticky**](https://github.com/nkapila6/mcp-meme-sticky) | WhatsApp 또는 Telegram용 밈이나 스티커를 MCP 서버로 생성합니다. |
| [**mcp-memory-service**](https://github.com/doobidoo/mcp-memory-service) | 13개 이상의 AI 애플리케이션에서 시맨틱 메모리 검색, 영구 저장, 자율 메모리 통합을 제공하는 범용 MCP 메모리 서비스입니다. |
| [**mcp-proxy**](https://github.com/sparfenyuk/mcp-proxy) | SSE 전송으로 실행되는 MCP 서버에 연결하거나, stdio 서버를 SSE 서버로 노출합니다. |
| [**mcp-proxy**](https://github.com/mikluko/mcp-proxy) | 네이티브 OAuth를 지원하지 않는 MCP 클라이언트를 위한 OAuth 2.0/PKCE 인증 및 토큰 관리 경량 프록시입니다. |
| [**mcp-vision**](https://github.com/groundlight/mcp-vision) | HuggingFace 컴퓨터 비전 모델(제로샷 객체 탐지 등)을 도구로 노출하여 LLM의 비전 능력을 강화하는 MCP 서버입니다. |
| [**mcpcap**](https://github.com/mcpcap/mcpcap) | PCAP 파일 분석을 위한 모듈형 Python MCP 서버입니다. |
| [**MCPIgnore Filesytem**](https://github.com/CyberhavenInc/filesystem-mcpignore) | 데이터 보안 우선 파일시스템 MCP 서버로, .mcpignore를 통해 MCP 클라이언트의 민감 데이터 접근을 방지합니다. |
| [**mem0-mcp**](https://github.com/mem0ai/mem0-mcp) | 코딩 환경설정 관리를 돕는 Mem0용 MCP 서버입니다. |
| [**Memalot**](https://github.com/nfergu/memalot?tab=readme-ov-file#mcp-server) | Python 프로그램의 메모리 누수를 탐지합니다. |
| [**Membase**](https://github.com/unibaseio/membase-mcp) | Membase를 통해 에이전트 메모리를 분산 방식으로 저장하고 조회합니다. |
| [**Meme MCP**](https://github.com/lidorshimoni/meme-mcp) | Imgflip API를 활용하여 AI로 밈을 생성하는 MCP 서버입니다. |
| [**memos-api-mcp**](https://github.com/MemTensor/memos-api-mcp) | AI 애플리케이션용 메모리 관리 운영체제 MemOS의 API 서비스를 위한 MCP 구현입니다. |
| [**MerabyLabs/promptarchitect-mcp**](https://github.com/MerabyLabs/promptarchitect-mcp) | 워크스페이스 인식 프롬프트 엔지니어링 도구입니다. 프로젝트의 기술 스택, 의존성, 컨텍스트를 기반으로 프롬프트를 분석하고 생성합니다. |
| [**Mercado Libre**](https://mcp.mercadolibre.com/) | Mercado Libre 공식 MCP 서버입니다. |
| [**Mercado Pago**](https://mcp.mercadopago.com/) | Mercado Pago 공식 MCP 서버입니다. |
| [**metatool-ai/metatool-app**](https://github.com/metatool-ai/metatool-app) | GUI로 MCP 연결을 관리하는 통합 미들웨어 MCP 서버입니다. |
| [**MetaTrader MCP**](https://github.com/ariadng/metatrader-mcp-server) | AI LLM이 MetaTrader 5 플랫폼을 사용하여 거래를 실행할 수 있게 합니다. |
| [**mickaelkerjean/filestash**](https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp) | SFTP, S3, FTP, SMB, NFS, WebDAV, GIT 등 다양한 원격 스토리지에 접근합니다. |
| [**Microsoft 365**](https://github.com/merill/lokka) | Microsoft 365용 MCP 서버로, Teams, SharePoint, Exchange, OneDrive, Entra, Intune 등 모든 서비스를 지원합니다. |
| [**Microsoft Clarity**](https://github.com/microsoft/clarity-mcp-server) | Clarity에서 행동 분석 데이터와 인사이트를 가져오는 공식 MCP 서버입니다. |
| [**Microsoft Dataverse**](https://go.microsoft.com/fwlink/?linkid=2320176) | 자연어로 비즈니스 데이터와 대화하며, 테이블 탐색, 쿼리 실행, 데이터 조회, 레코드 삽입/수정을 수행합니다. |
| [**Microsoft Entra ID MCP Server**](https://github.com/hieuttmmo/entraid-mcp-server) | Microsoft Graph를 통해 Microsoft Entra ID(Azure AD)의 디렉토리, 사용자, 그룹, 디바이스, 로그인, 보안 작업을 수행하는 Python MCP 서버입니다. |
| [**Mikrotik**](https://github.com/jeff-nasseri/mikrotik-mcp) | IP, DHCP, Firewall 등 네트워킹 작업을 처리하는 Mikrotik MCP 서버입니다. |
| [**Minima**](https://github.com/dmayboroda/minima) | 로컬 파일에 대한 RAG를 제공하는 MCP 서버입니다. |
| [**Miro**](https://github.com/k-jarzyna/mcp-miro) | 공식 Miro SDK의 모든 기능을 노출하는 Miro MCP 서버입니다. |
| [**MLflow**](https://github.com/kkruglik/mlflow-mcp) | 고급 쿼리, 실행 비교, 아티팩트 접근, 모델 레지스트리를 지원하는 MLflow ML 실험 추적 MCP 서버입니다. |
| [**mmorris35/devplan-mcp-server**](https://github.com/mmorris35/devplan-mcp-server) | ClaudeCode-DevPlanBuilder 방법론을 사용하여 종합적인 개발 계획을 생성합니다. PROJECT_BRIEF.md, DEVELOPMENT_PLAN.md, CLAUDE.md를 작성합니다. |
| [**modelcontextprotocol/server-memory**](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/memory) | 컨텍스트 유지를 위한 Knowledge Graph 기반 영구 메모리 시스템입니다. |
| [**molanojustin/smithsonian-mcp**](https://github.com/molanojustin/smithsonian-mcp) | AI 어시스턴트에게 Smithsonian Institution의 오픈 액세스 컬렉션 접근을 제공하는 MCP 서버입니다. |
| [**Monzo**](https://github.com/BfdCampos/monzo-mcp-bfdcampos) | 자연어로 Monzo 은행 계좌에 접근하고 관리합니다. 잔액 확인, Pot 관리, 거래 목록 조회 및 주석 기능을 지원합니다. |
| [**MotherDuck**](https://github.com/motherduckdb/mcp-server-motherduck) | MotherDuck 및 로컬 DuckDB로 데이터를 조회하고 분석합니다. |
| [**Multi Chat MCP Server (Google Chat)**](https://github.com/siva010928/multi-chat-mcp-server) | Cursor 등 AI 어시스턴트를 Google Chat 및 기타 채팅 플랫폼에 연결하여 확장 가능한 협업을 지원합니다. |
| [**Multicluster-MCP-Sever**](https://github.com/yanmxa/multicluster-mcp-server) | GenAI 시스템이 여러 Kubernetes 클러스터와 상호작용할 수 있는 게이트웨이입니다. |
| [**Multiplayer**](https://www.multiplayer.app/docs/ai/mcp-server) | 풀스택 세션 녹화를 쉽게 분석합니다. Multiplayer로 버그를 녹화하고 LLM으로 분석 및 수정합니다. |
| [**MWGMorningwood/Central-Memory-MCP**](https://github.com/MWGMorningwood/Central-Memory-MCP) | Azure Functions MCP 트리거와 Table Storage를 활용하여 여러 개발자를 위한 워크스페이스 기반 Knowledge Graph를 제공하는 Azure PaaS 호스팅 MCP 서버입니다. |
| [**MyAgentHubs/aimemo**](https://github.com/MyAgentHubs/aimemo) | 의존성 없는 MCP 메모리 서버입니다. 단일 바이너리, 100% 로컬, Docker 불필요. |
| [**n8daniels/RulesetMCP**](https://github.com/n8daniels/RulesetMCP) | AI 에이전트를 프로젝트 규칙에 맞게 유지합니다. 코딩 표준 조회, 스니펫 검증, 버전 관리되는 규칙 파일 기반 가이드를 제공합니다. |
| [**Nacos MCP Router**](https://github.com/nacos-group/nacos-mcp-router) | 다른 MCP 서버를 검색, 설치, 프록시하는 도구를 제공하는 MCP 서버입니다. |
| [**Nanoleaf**](https://github.com/srnetadmin/nanoleaf-mcp-server) | MCP를 통해 Nanoleaf 스마트 조명을 제어합니다. 전원, 밝기, 색상, 효과 설정 및 디바이스 탐색을 지원합니다. |
| [**NASA Planetary Data System (PDS) MCP Server**](https://github.com/NASA-PDS/pds-mcp-server) | NASA의 Planetary Data System(PDS)에 연결하여 1960년대부터 현재까지의 NASA 데이터 제품을 지능적으로 탐색하는 MCP 서버입니다. |
| [**National Parks**](https://github.com/KyrieTangSheng/mcp-server-nationalparks) | 미국 국립공원의 상세 정보, 알림, 방문자 센터, 캠핑장, 하이킹 트레일, 이벤트 등 최신 정보를 제공합니다. |
| [**neilberkman/editorconfig_mcp**](https://github.com/neilberkman/editorconfig_mcp) | .editorconfig 규칙을 사용하여 파일을 포맷합니다. AI 생성 코드가 프로젝트별 포맷 표준을 처음부터 준수하도록 합니다. |
| [**Neovim**](https://github.com/bigcodegen/mcp-neovim-server) | Neovim 세션을 위한 MCP 서버입니다. |
| [**Nerve**](https://github.com/nerve-hq/nerve-mcp-server) | Nerve를 통해 모든 SaaS 앱의 회사 데이터를 검색하고 작업합니다. |
| [**NetApp**](https://github.com/NetApp/mcp) | NetApp 시스템과 서비스에서 메트릭 조회, 볼륨 관리, 검색을 수행합니다. |
| [**Netbird**](https://github.com/aantti/mcp-netbird) | Netbird 네트워크의 피어, 그룹, 정책 등을 조회하고 분석합니다. |
| [**nickpending/mcp-recon**](https://github.com/nickpending/mcp-recon) | httpx와 asnmap 기반의 대화형 정찰 인터페이스 및 MCP 서버입니다. 도메인 분석, 보안 헤더 검사, 인증서 분석, ASN 조회를 지원합니다. |
| [**nomad-mcp**](https://github.com/kocierik/mcp-nomad) | MCP를 통해 Nomad 클러스터를 관리하는 도구 세트를 제공하는 서버입니다. |
| [**NPM Search**](https://github.com/btwiuse/npm-search-mcp-server) | npm 패키지를 검색합니다. |
| [**nwiizo/tfmcp**](https://github.com/nwiizo/tfmcp) | AI 어시스턴트가 Terraform 환경을 관리하고 운영할 수 있게 하는 MCP 서버입니다. 설정 읽기, 플랜 분석, 설정 적용, 상태 관리를 지원합니다. |
| [**oatpp-mcp**](https://github.com/oatpp/oatpp-mcp) | Oat++ 프레임워크용 C++ MCP 통합입니다. Oat++로 MCP 서버를 구축합니다. |
| [**OctoEverywhere**](https://github.com/OctoEverywhere/mcp) | 3D 프린터의 실시간 상태 조회, 웹캠 스냅샷, 프린터 제어를 지원하는 MCP 서버입니다. |
| [**OctoEverywhere For 3D Printing**](https://octoeverywhere.com/mcp) | 3D 프린터의 실시간 상태 조회, 웹캠 스냅샷, 프린터 제어를 지원하는 MCP 서버입니다. |
| [**Offorte**](https://github.com/offorte/offorte-mcp-server#readme) | 비즈니스 제안서 작성 및 발송을 지원하는 Offorte Proposal Software 공식 MCP 서버입니다. |
| [**offorte/offorte-mcp-server**](https://github.com/offorte/offorte-mcp-server) | 비즈니스 제안서 작성 및 발송을 지원하는 Offorte Proposal Software MCP 서버입니다. |
| [**olalonde/mcp-human**](https://github.com/olalonde/mcp-human) | LLM이 사람의 도움이 필요할 때 AWS Mechanical Turk를 통해 지원합니다. |
| [**olgasafonova/productplan-mcp-server**](https://github.com/olgasafonova/productplan-mcp-server) | ProductPlan 로드맵을 조회합니다. OKR, 아이디어, 출시, 타임라인 데이터에 접근합니다. |
| [**omni-mcp/isaac-sim-mcp**](https://github.com/omni-mcp/isaac-sim-mcp) | 자연어로 NVIDIA Isaac Sim, Lab, OpenUSD 등을 제어하는 MCP 서버 및 확장 프로그램입니다. |
| [**ONLYOFFICE DocSpace**](https://github.com/ONLYOFFICE/docspace-mcp) | ONLYOFFICE DocSpace API와 상호작용하여 룸 생성, 파일 및 폴더를 관리합니다. |
| [**OpenCTI**](https://github.com/Spathodea-Network/opencti-mcp) | OpenCTI 플랫폼과 상호작용하여 보고서, 지표, 악성코드, 위협 행위자 등 위협 인텔리전스 데이터를 조회합니다. |
| [**OpenCV**](https://github.com/GongRzhe/opencv-mcp-server) | OpenCV 컴퓨터 비전 기능을 제공하는 MCP 서버입니다. AI 어시스턴트와 언어 모델이 강력한 컴퓨터 비전 도구에 접근할 수 있습니다. |
| [**OpenDataMCP/OpenDataMCP**](https://github.com/OpenDataMCP/OpenDataMCP) | MCP를 통해 모든 오픈 데이터를 모든 LLM에 연결합니다. |
| [**OpenDigger MCP Server**](https://github.com/X-lab2017/open-digger-mcp-server) | OpenDigger용 MCP 서버로, 도구와 프롬프트를 통한 고급 리포지토리 분석 및 인사이트를 제공합니다. |
| [**OpenDota**](https://github.com/asusevski/opendota-mcp-server) | OpenDota API와 상호작용하여 Dota 2 매치 데이터, 플레이어 통계 등을 조회합니다. |
| [**OpenMetadata**](https://open-metadata.org/mcp) | 메타데이터를 위한 최초의 엔터프라이즈급 MCP 서버입니다. |
| [**OpenMetadata**](https://github.com/yangkyeongmo/mcp-server-openmetadata) | 오픈소스 메타데이터 관리 플랫폼 OpenMetadata용 MCP 서버입니다. |
| [**OpenMF-mifosx-self-service**](https://github.com/openMF/mcp-mifosx-self-service) | MCP를 통해 Apache Fineract 셀프서비스 API에 접근하여 등록, 인증, 계정 관리, 거래를 수행합니다. |
| [**OpenReview**](https://github.com/anyakors/openreview-mcp-server) | AI/ML 컨퍼런스의 논문을 가져오고, 읽고, 저장하는 OpenReview용 MCP 서버입니다. |
| [**OpenRPC**](https://github.com/shanejonas/openrpc-mpc-server) | OpenRPC를 통해 JSON-RPC API를 탐색하고 상호작용합니다. |
| [**OpenStack**](https://github.com/wangsqly0407/openstack-mcp-server) | OpenStack 상호작용을 제공하는 MCP 서버 구현입니다. |
| [**OPNSense MCP**](https://github.com/vespo92/OPNSenseMCP) | OPNSense 방화벽 관리 및 API 접근을 위한 MCP 서버입니다. |
| [**OpsLevel**](https://github.com/opslevel/opslevel-mcp) | OpsLevel 공식 MCP 서버입니다. |
| [**Optuna**](https://github.com/optuna/optuna-mcp) | Optuna로 하이퍼파라미터 검색 및 최적화 작업을 원활하게 오케스트레이션하는 공식 MCP 서버입니다. |
| [**oraios/serena**](https://github.com/oraios/serena) | Language Server를 활용한 심볼릭 코드 작업에 기반하는 완전한 기능의 코딩 에이전트입니다. |
| [**orellazi/coda-mcp**](https://github.com/orellazri/coda-mcp) | Coda용 MCP 서버입니다. |
| [**Orshot**](https://github.com/rishimohan/orshot-mcp-server) | 커스텀 디자인 템플릿에서 이미지를 동적으로 생성하는 Orshot 공식 MCP 서버입니다. |
| [**osinmv/funciton-lookup-mcp**](https://github.com/osinmv/function-lookup-mcp) | 함수 시그니처 조회를 위한 MCP 서버입니다. |
| [**Oura MCP server**](https://github.com/tomekkorbak/oura-mcp-server) | 수면 데이터를 조회하기 위한 Oura API MCP 서버입니다. |
| [**Oxylabs**](https://github.com/oxylabs/oxylabs-mcp) | Oxylabs Web API로 웹사이트를 스크래핑하며, 동적 렌더링과 구조화된 데이터 추출 파싱을 지원합니다. |
| [**Package Registry Search**](https://github.com/artmann/package-registry-mcp) | NPM, Cargo, PyPi, NuGet 패키지의 최신 정보를 검색하고 조회합니다. |
| [**Pacman**](https://github.com/oborchers/mcp-server-pacman) | PyPI, npm, crates.io, Docker Hub, Terraform Registry 등 패키지 저장소에서 정보를 검색하고 조회하는 MCP 서버입니다. |
| [**Paddle**](https://github.com/PaddleHQ/paddle-mcp-server) | Paddle API와 상호작용하여 상품 카탈로그, 빌링, 구독, 리포트를 관리합니다. |
| [**Pagos**](https://github.com/pagos-ai/pagos-mcp) | Pagos API와 상호작용하여 신용카드 BIN 데이터를 조회합니다. |
| [**panther-labs/mcp-panther**](https://github.com/panther-labs/mcp-panther) | 보안 전문가가 자연어로 Panther SIEM 플랫폼과 상호작용하여 탐지 규칙 작성, 로그 쿼리, 알림 관리를 수행하는 MCP 서버입니다. |
| [**Peacock for VS Code**](https://github.com/johnpapa/peacock-mcp) | VS Code용 Peacock 확장 프로그램의 MCP 서버입니다. API와 상호작용하는 MCP 서버 구현 예시를 제공합니다. |
| [**persistproc**](https://github.com/irskep/persistproc) | 에이전트가 웹 서버 등 장시간 실행 프로세스를 확인하고 제어할 수 있는 MCP 서버 + CLI 도구입니다. |
| [**Persona Sessions**](https://github.com/mattjoyce/mcp-persona-sessions) | AI 어시스턴트가 면접 준비, 자기 성찰, 코칭 대화 등 구조화된 페르소나 기반 세션을 수행하도록 합니다. |
| [**peter-j-thompson/semanticapi-mcp**](https://github.com/peter-j-thompson/semanticapi-mcp) | 자연어 API 탐색 도구입니다. 700개 이상의 API 기능 검색, 엔드포인트, 인증 설정, 코드 스니펫을 제공합니다. |
| [**Pexels**](https://github.com/garylab/pexels-mcp-server) | Pexels 무료 이미지 API에 접근하여 고품질 로열티 프리 이미지를 검색, 조회, 다운로드하는 MCP 서버입니다. |
| [**PGYER**](https://github.com/PGYER/pgyer-mcp-server) | PGYER 플랫폼용 MCP 서버로, 앱 업로드, 조회 등을 지원합니다. |
| [**Phabricator**](https://github.com/baba786/phabricator-mcp-server) | Phabricator API와 상호작용합니다. |
| [**PiAPI**](https://github.com/apinetwork/piapi-mcp-server) | PiAPI MCP 서버로 Claude 또는 MCP 호환 앱에서 Midjourney/Flux/Kling/Hunyuan/Udio/Trellis를 활용한 미디어 콘텐츠를 생성합니다. |
| [**pibblokto/cert-manager-mcp-server**](https://github.com/pibblokto/cert-manager-mcp-server) | cert-manager 관리 및 트러블슈팅을 위한 MCP 서버입니다. |
| [**Pipedream**](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) | 8,000개 이상의 사전 빌드 도구로 2,500개 API에 연결합니다. |
| [**Placid.app**](https://github.com/felores/placid-mcp-server) | Placid.app 템플릿을 사용하여 이미지 및 비디오 크리에이티브를 생성합니다. |
| [**Plainly Videos**](https://github.com/plainly-videos/mcp-server) | 디자인과 프로젝트를 탐색하고 다양한 LLM 클라이언트로 비디오를 렌더링하는 Plainly Videos 공식 MCP 서버입니다. |
| [**Plane**](https://github.com/kelvin6365/plane-mcp-server) | Plane API를 통해 프로젝트와 이슈를 관리하는 MCP 서버입니다. |
| [**Polarsteps**](https://github.com/remuzel/polarsteps-mcp) | 이전 여행을 리뷰하고 새 여행을 계획하는 데 도움을 주는 MCP 서버입니다. |
| [**Port IO**](https://github.com/port-labs/port-mcp-server) | 소프트웨어 카탈로그에 접근하고 관리하여 서비스 품질 및 컴플라이언스를 개선합니다. |
| [**portel-dev/ncp**](https://github.com/portel-dev/ncp) | 지능적 탐색으로 전체 MCP 생태계를 오케스트레이션하며, 98.2%의 정확도를 유지하면서 토큰 오버헤드를 제거합니다. |
| [**Postman**](https://github.com/shannonlal/mcp-postman) | Newman을 통해 Postman Collection을 로컬에서 실행하는 MCP 서버입니다. 테스트 통과 여부 결과를 반환합니다. |
| [**Postman API**](https://github.com/postmanlabs/postman-api-mcp) | Postman API를 사용하여 Postman 리소스를 관리합니다. |
| [**pramod/kaggle**](https://github.com/KrishnaPramodParupudi/kaggle-mcp-server) | MCP 내에서 Kaggle 대회, 리더보드, 모델, 데이터셋, 커널을 직접 탐색할 수 있는 Kaggle MCP 서버입니다. |
| [**pre.dev Architect**](https://docs.pre.dev/mcp-server) | pre.dev로 코딩 에이전트를 올바른 방향으로 유지하여 생산성을 10배 높입니다. |
| [**PrestaShop.com**](https://docs.mcp.prestashop.com/) | 공식 PrestaShop MCP 서버를 사용하여 AI 어시스턴트로 PrestaShop 스토어를 관리합니다. |
| [**pricepertoken/mcp-server**](https://pricepertoken.com/mcp) | OpenAI, Anthropic, Google, Meta 등 30개 이상 프로바이더의 100개 이상 모델에 대한 LLM API 가격 비교 및 벤치마크입니다. API 키 불필요. |
| [**Probe.dev**](https://docs.probe.dev/guides/mcp-integration) | Probe.dev 기반 종합 미디어 분석 및 검증입니다. FFprobe, MediaInfo, Probe Report 분석 기능을 제공하는 호스팅 MCP 서버입니다. |
| [**Probe.dev**](https://mcp.probe.dev) | FFprobe, MediaInfo, 종합 리포팅 기능을 갖춘 전문 미디어 분석 및 검증 MCP 서버입니다. |
| [**Program Integrity Alliance (PIA)**](https://github.com/Program-Integrity-Alliance/pia-mcp-local) | 미국 정부 오픈 데이터셋에 AI 친화적으로 접근하는 로컬 및 호스팅 MCP 서버입니다. |
| [**promptexecution/just-mcp**](https://github.com/promptexecution/just-mcp) | LLM이 CLI 또는 스크립트 명령을 파라미터와 함께 안전하게 실행할 수 있게 하는 Justfile 통합입니다. |
| [**PubChem**](https://github.com/sssjiang/pubchem_mcp_server) | PubChem API에서 약물 정보를 추출합니다. |
| [**Public APIs MCP**](https://github.com/zazencodes/public-apis-mcp) | MCP를 사용하여 무료 API를 검색합니다. |
| [**public-ui/kolibri**](https://github.com/public-ui/kolibri) | 200개 이상의 접근성 보장 웹 컴포넌트 샘플, 스펙, 문서, 시나리오를 스트리밍으로 제공하는 KoliBri MCP 서버입니다. |
| [**PubMed**](https://github.com/JackKuo666/PubMed-MCP-Server) | 간단한 MCP 인터페이스를 통해 AI 어시스턴트가 PubMed 논문을 검색, 접근, 분석할 수 있게 합니다. |
| [**PubNub**](https://github.com/pubnub/pubnub-mcp-server) | PubNub SDK 개발 및 API 호출을 위한 컨텍스트를 제공합니다. |
| [**pullkitsan/mobsf-mcp-server**](https://github.com/pullkitsan/mobsf-mcp-server) | Android 및 iOS 애플리케이션의 정적/동적 분석을 위한 MobSF MCP 서버입니다. |
| [**Put.io**](https://github.com/putdotio/putio-mcp-server) | Put.io 계정과 상호작용하여 토렌트를 다운로드합니다. |
| [**pwh-pwh/cal-mcp**](https://github.com/pwh-pwh/cal-mcp) | 수학 표현식 계산을 위한 MCP 서버입니다. |
| [**Python CLI MCP**](https://github.com/ofek/pycli-mcp) | 로컬 Python 명령줄 애플리케이션과 상호작용합니다. |
| [**qainsights/k6-mcp-server**](https://github.com/QAInsights/k6-mcp-server) | 성능 테스트를 위한 Grafana k6 MCP 서버입니다. |
| [**qianniuspace/mcp-security-audit**](https://github.com/qianniuspace/mcp-security-audit) | npm 패키지 의존성의 보안 취약점을 감사하는 MCP 서버입니다. 원격 npm 레지스트리 통합으로 실시간 보안 검사를 수행합니다. |
| [**Qonto**](https://github.com/qonto/qonto-mcp-server) | MCP를 통해 LLM으로 Qonto 계정에 접근하고 상호작용합니다. |
| [**QuackbackIO/quackback**](https://github.com/QuackbackIO/quackback) | 내장 MCP 서버를 갖춘 오픈소스 고객 피드백 플랫폼입니다. 피드백 검색, 게시물 분류, 상태 업데이트, 로드맵 관리, 변경 로그 발행을 지원합니다. |
| [**Quarkus**](https://github.com/quarkiverse/quarkus-mcp-servers) | Quarkus Java 프레임워크용 MCP 서버입니다. |
| [**R mcptools**](https://github.com/posit-dev/mcptools) | R 기반 MCP 서버를 생성하고 서드파티 MCP 서버의 기능을 R 함수로 사용하는 R SDK입니다. |
| [**r-huijts/firstcycling-mcp**](https://github.com/r-huijts/firstcycling-mcp) | 자연어로 사이클 경주 데이터, 결과, 통계에 접근합니다. firstcycling.com에서 출발 목록, 경주 결과, 선수 정보를 조회합니다. |
| [**RabbitMQ**](https://github.com/kenliao94/mcp-server-rabbitmq) | RabbitMQ와 상호작용하여 메시지를 발행하고 소비하는 MCP 서버입니다. |
| [**radareorg/r2mcp**](https://github.com/radareorg/radare2-mcp) | Radare2 디스어셈블러용 MCP 서버입니다. AI에게 바이너리 디스어셈블 및 리버스 엔지니어링 기능을 제공합니다. |
| [**RAE**](https://github.com/rae-api-com/rae-mcp) | rae-api.com(스페인 왕립 학술원 사전)에 연결하는 MCP 서버입니다. |
| [**RAG Local**](https://github.com/renl/mcp-rag-local) | 시맨틱 의미 기반으로 텍스트 구절을 로컬에 저장하고 검색하는 MCP 서버입니다. |
| [**Raindrop.io**](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) | MCP를 통해 LLM이 Raindrop.io 북마크와 상호작용할 수 있게 하는 통합입니다. |
| [**Ramp**](https://github.com/ramp-public/ramp-mcp) | Ramp Developer API와 상호작용하여 지출 분석을 실행하고 LLM을 활용한 인사이트를 얻습니다. |
| [**raohwork/forgejo-mcp**](https://github.com/raohwork/forgejo-mcp) | Forgejo/Gitea 서버의 리포지토리를 관리하는 MCP 서버입니다. |
| [**Razorpay**](https://github.com/razorpay/razorpay-mcp-server) | Razorpay 공식 MCP 서버입니다. |
| [**Red Hat Insights**](https://github.com/RedHatInsights/insights-mcp) | Red Hat Insights와 상호작용합니다. 이미지 빌드, 취약점 관리, 맞춤형 권장 사항 조회를 지원합니다. |
| [**Redbee**](https://github.com/Tamsi/redbee-mcp) | Redbee API와 상호작용하는 Redbee MCP 서버입니다. |
| [**Redfish**](https://github.com/nokia/mcp-redfish) | DMTF Redfish API와 상호작용하는 Redfish MCP 서버입니다. |
| [**redleaves/context-keeper**](https://github.com/redleaves/context-keeper) | 광범위 리콜 + 정밀 리랭킹 RAG 아키텍처를 갖춘 LLM 기반 컨텍스트 및 메모리 관리입니다. 다차원 검색, 단기/장기 메모리, 완전한 MCP 지원을 제공합니다. |
| [**RedNote MCP**](https://github.com/ifuryst/rednote-mcp) | RedNote(샤오홍수, XiaoHongShu) 콘텐츠에 접근하는 MCP 서버입니다. |
| [**Reed Jobs**](https://github.com/kld3v/reed_jobs_mcp) | Reed.co.uk에서 채용 공고를 검색하고 조회합니다. |
| [**reeeeemo/ancestry-mcp**](https://github.com/reeeeemo/ancestry-mcp) | AI가 .ged 파일과 유전자 데이터를 읽을 수 있게 합니다. |
| [**Reflag**](https://github.com/reflagcom/javascript/tree/main/packages/cli#model-context-protocol) | Reflag를 사용하여 Feature Flag를 생성하고 관리합니다. |
| [**Reloaderoo**](https://github.com/cameroncooke/reloaderoo) | 개발 중인 MCP 서버를 미러링하여 동일 AI 세션 내에서 원활한 재시작과 도구 업데이트를 지원하는 로컬 MCP 서버입니다. |
| [**Reltio**](https://github.com/reltio-ai/reltio-mcp-server) | Reltio 환경에서 언어 모델을 활용한 고급 엔티티 매칭을 수행하는 경량 플러그인 기반 MCP 서버입니다. |
| [**Rememberizer AI**](https://github.com/skydeckai/mcp-server-rememberizer) | Rememberizer 데이터 소스와 상호작용하여 향상된 지식 검색을 지원하는 MCP 서버입니다. |
| [**Reminder**](https://github.com/arifszn/reminder-mcp) | Slack 또는 Telegram을 통해 리마인더를 예약하고 트리거하는 MCP 서버입니다. |
| [**Remote MCP**](https://github.com/ssut/Remote-MCP) | 원격 MCP 통신 솔루션으로, Model Context의 중앙 집중식 관리를 위한 손쉬운 통합을 지원합니다. |
| [**Repo Map**](https://github.com.mcas.ms/pdavis68/RepoMapper) | 리포지토리에서 채팅 관련 파일의 동적 맵을 함수 프로토타입 및 관련 파일과 함께 관련도 순으로 제공하는 MCP 서버입니다. |
| [**RevenueCat**](https://www.revenuecat.com/docs/tools/mcp/overview) | AI 코딩 환경을 벗어나지 않고 RevenueCat에서 인앱 구매를 관리합니다. |
| [**Revit**](https://github.com/NonicaTeam/AI-Connector-for-Revit) | Revit 모델에 실시간으로 연결하고 상호작용합니다. |
| [**Revit MCP**](https://github.com/revit-mcp) | Autodesk Revit용 MCP 프로토콜 구현 서비스입니다. |
| [**ricocf/mcp-wolframalpha**](https://github.com/ricocf/mcp-wolframalpha) | AI 어시스턴트가 Wolfram Alpha API를 통해 계산 지식과 데이터에 실시간 접근하는 MCP 서버입니다. |
| [**Rijksmuseum**](https://github.com/r-huijts/rijksmuseum-mcp) | Rijksmuseum API와 인터페이스하여 작품 검색, 작품 상세 조회, 이미지 타일 접근, 사용자 컬렉션 탐색을 수행합니다. |
| [**Rill Data**](https://docs.rilldata.com/explore/mcp) | Rill Data와 상호작용하여 데이터를 쿼리하고 분석합니다. |
| [**RobSpectre/mvf1**](https://github.com/RobSpectre/mvf1) | Formula 1, WEC, IndyCar 등 모터스포츠 시청 앱 MultiViewer를 제어하는 MCP 서버입니다. |
| [**Rodin**](https://github.com/DeemosTech/rodin-api-mcp) | Hyper3D Rodin으로 3D 모델을 생성합니다. |
| [**rohitg00/kubectl-mcp-server**](https://github.com/rohitg00/kubectl-mcp-server) | Claude, Cursor 등 AI 어시스턴트가 자연어로 Kubernetes 클러스터와 상호작용하도록 하는 MCP 서버입니다. |
| [**Rohlik**](https://github.com/tomaspavlin/rohlik-mcp) | Rohlik Group 플랫폼(Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)에서 식료품을 쇼핑합니다. |
| [**Roundtable**](https://github.com/askbudi/roundtable) | 제로 구성 자동 탐색과 엔터프라이즈 아키텍처로 여러 AI 코딩 어시스턴트(Codex, Claude Code, Cursor, Gemini)를 연결하는 통합 레이어입니다. |
| [**Rquest**](https://github.com/xxxbrian/mcp-rquest) | 안티봇 조치를 우회하기 위한 정확한 TLS/JA3/JA4 핑거프린트를 갖춘 브라우저 유사 HTTP 요청 기능을 제공하는 MCP 서버입니다. |
| [**rrmistry/tilt-mcp**](https://github.com/rrmistry/tilt-mcp) | Tilt와 통합하여 Kubernetes 개발 환경의 리소스, 로그, 관리 작업에 프로그래밍 방식으로 접근하는 MCP 서버입니다. |
| [**SafeLine**](https://github.com/chaitin/SafeLine/tree/main/mcp_server) | 웹 애플리케이션을 공격과 익스플로잇으로부터 보호하는 셀프 호스팅 WAF(Web Application Firewall)입니다. |
| [**SafetySearch**](https://github.com/surabhya/SafetySearch) | FDA 식품 안전 데이터(리콜, 부작용, 분석)를 실시간으로 제공합니다. |
| [**sammcj/mcp-package-version**](https://github.com/sammcj/mcp-package-version) | LLM이 코드 작성 시 최신 안정 패키지 버전을 제안하도록 돕는 MCP 서버입니다. |
| [**sawa-zen/vrchat-mcp**](https://github.com/sawa-zen/vrchat-mcp) | VRChat API와 상호작용하는 MCP 서버입니다. 친구, 월드, 아바타 등의 정보를 조회합니다. |
| [**Scrapezy**](https://github.com/scrapezy/mcp) | Scrapezy로 웹사이트를 데이터셋으로 변환합니다. |
| [**ScriptFlow**](https://github.com/yanmxa/scriptflow-mcp) | 복잡하고 반복적인 AI 상호작용을 영구적이고 실행 가능한 스크립트로 변환합니다. 종합적인 스크립트 관리와 다국어(Bash, Python 등)를 지원합니다. |
| [**Search1API**](https://github.com/fatwang2/search1api-mcp) | 검색, 크롤링, 사이트맵을 위한 단일 API입니다. |
| [**searchcraft-inc/searchcraft-mcp-server**](https://github.com/searchcraft-inc/searchcraft-mcp-server) | Searchcraft 클러스터 관리, 검색 인덱스 생성, 데이터 파일 기반 동적 인덱스 생성, 데이터 가져오기를 위한 공식 MCP 서버입니다. |
| [**SecretiveShell/MCP-wolfram-alpha**](https://github.com/SecretiveShell/MCP-wolfram-alpha) | Wolfram Alpha API를 쿼리하기 위한 MCP 서버입니다. |
| [**ServiceNow**](https://github.com/osomai/servicenow-mcp) | ServiceNow 인스턴스와 상호작용하는 MCP 서버입니다. |
| [**ShaderToy**](https://github.com/wilsonchenghy/ShaderToy-MCP) | LLM이 ShaderToy API와 상호작용하여 컴퓨트 셰이더 예제에서 학습하고 복잡한 GLSL 셰이더를 생성할 수 있게 하는 MCP 서버입니다. |
| [**Shodan MCP**](https://github.com/Hexix23/shodan-mcp) | Shodan과 상호작용하는 MCP 서버입니다. |
| [**shuji-bonji/xcomet-mcp-server**](https://github.com/shuji-bonji/xcomet-mcp-server) | xCOMET 모델을 사용한 번역 품질 평가입니다. 품질 점수(0-1), 심각도별 오류 탐지, 25배 속도 향상 배치 처리를 제공합니다. |
| [**SidneyBissoli/ibge-br-mcp**](https://github.com/SidneyBissoli/ibge-br-mcp) | 인구통계, 지리, 경제, 통계를 위한 23개 도구를 갖춘 브라질 통계청(IBGE) 데이터 서버입니다. |
| [**sim-xia/blind-auditor**](https://github.com/Sim-xia/Blind-Auditor) | 프롬프트 인젝션, 독립적 자체 감사, 컨텍스트 격리를 통해 AI가 생성 메시지를 자체 수정하도록 하는 무비용 MCP 서버입니다. |
| [**Simple Loki MCP**](https://github.com/ghrud92/simple-loki-mcp) | logcli를 사용하여 Loki 로그를 쿼리하는 간단한 MCP 서버입니다. |
| [**Simplifier**](https://github.com/simplifier-ag/simplifier-mcp) | Simplifier 로우코드 플랫폼에서 커넥터, 비즈니스 객체 등을 관리합니다. |
| [**skedgo/tripgo-mcp-server**](https://github.com/skedgo/tripgo-mcp-server) | TripGo API의 멀티모달 여행 계획, 교통 위치, 대중교통 출발 정보(실시간 포함)를 제공합니다. |
| [**skullzarmy/vibealive**](https://github.com/skullzarmy/vibealive) | Next.js 프로젝트의 미사용 파일과 API를 테스트하는 유틸리티로, 프로젝트 분석 도구를 AI 어시스턴트에 노출하는 MCP 서버입니다. |
| [**Skyvern**](https://github.com/Skyvern-AI/skyvern/tree/main/integrations/mcp) | Claude / Windsurf / Cursor 등 LLM이 브라우저를 제어할 수 있게 하는 MCP입니다. |
| [**slite-mcp**](https://github.com/fajarmf/slite-mcp) | Slite 통합을 위한 MCP 서버입니다. 노트 검색, 노트 계층 탐색, 워크스페이스 콘텐츠 접근을 지원합니다. |
| [**slouchd/cyberchef-api-mcp-server**](https://github.com/slouchd/cyberchef-api-mcp-server) | CyberChef 서버 API와 상호작용하여 MCP 클라이언트가 CyberChef 작업을 활용할 수 있게 하는 MCP 서버입니다. |
| [**Smart-AI-Memory/empathy-framework**](https://github.com/Smart-AI-Memory/empathy-framework) | 영구 메모리와 예측 기능을 갖춘 5단계 AI 협업 시스템입니다. MemDocs를 통한 로컬 우선 아키텍처로 Claude 등 LLM과 MCP 네이티브 통합합니다. |
| [**SmartBear**](https://github.com/SmartBear/smartbear-mcp) | SmartBear의 API Hub, Test Hub, Insight Hub 전반의 다양한 기능에 전용 도구와 리소스를 통해 접근합니다. |
| [**SoccerDataAPI**](https://github.com/yeonupark/mcp-soccer-data) | SoccerDataAPI 기반 실시간 축구 경기 데이터를 제공하는 MCP 서버입니다. |
| [**softvoyagers/qrmint-api**](https://github.com/softvoyagers/qrmint-api) | 커스텀 색상, 로고, 프레임, 배치 생성을 지원하는 무료 스타일 QR 코드 생성 API입니다. API 키 불필요. |
| [**Solr MCP**](https://github.com/mjochum64/mcp-solr-search) | Solr 서버에서 검색을 수행하는 기본 기능을 제공하는 MCP 서버입니다. |
| [**Solver**](https://github.com/szeider/mcp-solver) | 제약 조건 만족 및 최적화 문제를 해결합니다. |
| [**Solvitor**](https://github.com/Adeptus-Innovatio/solvitor-mcp) | 클로즈드 소스 Solana 스마트 컨트랙트에서 IDL 파일을 추출하고 디컴파일하는 리버스 엔지니어링 도구를 제공하는 MCP 서버입니다. |
| [**SonarQube**](https://github.com/SonarSource/sonarqube-mcp-server) | SonarQube Server 또는 Cloud와 원활하게 통합하여 에이전트 컨텍스트 내에서 코드 스니펫 분석을 수행합니다. |
| [**Sophtron**](https://github.com/sophtron/Sophtron-Integration/tree/main/modelcontextprotocol) | Sophtron Bank Integration으로 은행, 신용카드, 공과금 계좌에 연결하여 잔액과 거래 내역을 조회합니다. |
| [**Spaceship MCP**](https://github.com/bartwaardenburg/spaceship-mcp) | Spaceship API를 통해 도메인, DNS 레코드, 연락처, 마켓플레이스 목록 등을 관리합니다. |
| [**Splunk**](https://github.com/jkosik/mcp-server-splunk) | Splunk용 Golang MCP 서버입니다. 저장된 검색, 알림, 인덱스, 매크로 등을 조회합니다. SSE와 STDIO를 지원합니다. |
| [**Spring Initializr**](https://github.com/hpalma/springinitializr-mcp) | LLM이 커스텀 설정으로 Spring Boot 프로젝트를 생성하는 MCP입니다. start.spring.io 대신 AI 어시스턴트에게 프로젝트 생성을 요청할 수 있습니다. |
| [**Squad AI**](https://github.com/the-basilisk-ai/squad-mcp) | 제품 탐색 및 전략 플랫폼 통합입니다. MCP 인식 LLM에서 기회, 솔루션, 성과, 요구사항, 피드백을 생성하고 조회합니다. |
| [**Square**](https://github.com/square/square-mcp-server) | Square용 MCP 서버입니다. |
| [**srinath1510/alltrails-mcp-server**](https://github.com/srinath1510/alltrails-mcp-server) | AllTrails 데이터에 접근하여 하이킹 트레일을 검색하고 상세 정보를 조회하는 MCP 서버입니다. |
| [**SSH**](https://github.com/AiondaDotCom/mcp-ssh) | SSH 연결을 관리하고 제어하는 에이전트입니다. |
| [**SSH**](https://github.com/classfang/ssh-mcp-server) | 원격으로 SSH 명령을 실행하고, 파일 업로드/다운로드 등을 수행하는 MCP 서버입니다. |
| [**STAC**](https://github.com/Wayfinder-Foundry/stac-mcp) | 신속한 지리공간 데이터 탐색을 위한 STAC 카탈로그 및 아이템 검색 MCP 서버입니다. |
| [**Stack Overflow**](https://api.stackexchange.com/docs/mcp-server) | Stack Overflow의 신뢰성 있고 검증된 기술 질문과 답변에 접근합니다. |
| [**StackHawk**](https://github.com/stackhawk/stackhawk-mcp) | StackHawk로 코드 또는 바이브코딩 앱의 보안 문제를 테스트하고 수정합니다. |
| [**Standard Korean Dictionary**](https://github.com/privetin/stdict) | API를 사용하여 표준국어대사전을 검색합니다. |
| [**stape-io/google-tag-manager-mcp-server**](https://github.com/stape-io/google-tag-manager-mcp-server) | 원격 MCP 연결을 지원하고 내장 Google OAuth를 포함하며, Google Tag Manager API 인터페이스를 제공합니다. |
| [**Stardog**](https://github.com/stardog-union/stardog-cloud-mcp) | Stardog Semantic AI 플랫폼의 엔터프라이즈 Knowledge Graph를 활용하여 신뢰할 수 있는 컨텍스트 기반 답변을 제공합니다. |
| [**StarRocks**](https://github.com/StarRocks/mcp-server-starrocks) | StarRocks와 상호작용합니다. |
| [**Steadybit**](https://github.com/steadybit/mcp) | Steadybit과 상호작용합니다. |
| [**Stockfish**](https://github.com/sonirico/mcp-stockfish) | AI 시스템을 Stockfish 체스 엔진에 연결하는 MCP 서버입니다. |
| [**strato-space/media-gen-mcp**](https://github.com/strato-space/media-gen-mcp) | OpenAI 이미지/비디오 및 Google GenAI(Veo) 미디어 생성, 편집, 에셋 다운로드를 위한 TypeScript MCP 서버입니다. |
| [**Strava API**](https://github.com/tomekkorbak/strava-mcp-server) | 활동 데이터를 조회하기 위한 Strava API MCP 서버입니다. |
| [**subelsky/bundler_mcp**](https://github.com/subelsky/bundler_mcp) | Ruby 프로젝트의 Gemfile에서 의존성 정보를 로컬로 조회할 수 있게 합니다. |
| [**Success.co**](https://www.success.co/docs/guides/ai-mcp-connector) | Success.co 계정과 상호작용하여 EOS 여정을 강화하고 팀 및 비즈니스 인사이트를 얻습니다. |
| [**sxhxliang/mcp-access-point**](https://github.com/sxhxliang/mcp-access-point) | 코드 변경 없이 클릭 한 번으로 웹 서비스를 MCP 서버로 변환합니다. |
| [**takleb3rry/zitadel-mcp**](https://github.com/takleb3rry/zitadel-mcp) | Zitadel ID 관리용 MCP 서버입니다. 자연어로 사용자, 프로젝트, OIDC 앱, 역할, 서비스 계정을 관리합니다. |
| [**tan-yong-sheng/ai-vision-mcp**](https://github.com/tan-yong-sheng/ai-vision-mcp) | 이미지, 비디오, 객체 탐지 분석을 위한 멀티모달 AI 비전 MCP 서버입니다. Google Gemini와 Vertex AI를 활용한 UI/UX 평가, 시각적 회귀 테스트를 지원합니다. |
| [**Taskeract**](https://github.com/Acqusys/taskeract-mcp) | Taskeract 프로젝트 작업을 통합하고 작업 컨텍스트를 MCP 지원 앱에 로드하는 공식 MCP 서버입니다. |
| [**TCSAS**](https://github.com/TCMPP-Team/tcsas-devtools-mcp-server) | Tencent 미니 프로그램 기술 프레임워크 기반으로, Tencent Cloud Super App as a Service가 지원합니다. |
| [**TCSoftInc/testcollab-mcp-server**](https://github.com/TCSoftInc/testcollab-mcp-server) | AI 코딩 어시스턴트에서 직접 TestCollab의 테스트 케이스를 관리합니다. 필터링, 정렬, 페이지네이션을 지원합니다. |
| [**teamwork/mcp**](https://github.com/teamwork/mcp) | 클라이언트 프로젝트를 관리하고 리소스를 효율적으로 관리하며 수익을 최적화하는 프로젝트 관리 플랫폼입니다. |
| [**Template MCP Server**](https://github.com/mcpdotdirect/template-mcp-server) | TypeScript 지원, 듀얼 트랜스포트 옵션, 확장 가능한 구조를 갖춘 MCP 서버 프로젝트를 생성하는 CLI 도구입니다. |
| [**Tempo**](https://github.com/scottlepp/tempo-mcp-server) | Grafana Tempo에서 트레이스/스팬을 쿼리하는 MCP 서버입니다. |
| [**Tensorboard Query**](https://github.com/Alir3z4/tb-query) | TensorBoard 이벤트 파일을 쿼리하고 분석하는 MCP 서버입니다. |
| [**TextArtTools**](https://github.com/humanjesse/textarttools-mcp) | 23가지 Unicode 스타일로 텍스트를 변환하고 322개 이상의 figlet 폰트로 스타일 배너를 생성합니다. |
| [**TFT-Match-Analyzer**](https://github.com/GeLi2001/tft-mcp-server) | TFT(Teamfight Tactics) 매치 히스토리 및 매치 상세 정보를 조회하는 MCP 서버입니다. |
| [**tgeselle/bugsnag-mcp**](https://github.com/tgeselle/bugsnag-mcp) | Bugsnag와 상호작용하는 MCP 서버입니다. |
| [**Thales CDSP CRDP MCP Server**](https://github.com/sanyambassi/thales-cdsp-crdp-mcp-server) | CipherTrust RESTful Data Protection(CRDP) 데이터 보호 서비스와 상호작용하는 MCP 서버입니다. |
| [**the0807/GeekNews-MCP-Server**](https://github.com/the0807/GeekNews-MCP-Server) | GeekNews 사이트에서 뉴스 데이터를 조회하고 처리하는 MCP 서버입니다. |
| [**themesberg/flowbite-mcp**](https://github.com/themesberg/flowbite-mcp) | Tailwind CSS 기반 오픈소스 UI 프레임워크에 대한 AI 지원을 제공하는 MCP 서버입니다. |
| [**Think MCP**](https://github.com/Rai220/think-mcp) | Anthropic의 think-tools를 통합하여 에이전트의 추론 능력을 강화합니다. |
| [**Think Node MCP**](https://github.com/abhinav-mangla/think-tool-mcp) | Anthropic의 think-tools를 통합하여 에이전트의 추론 능력을 강화합니다. (Node 지원) |
| [**thunderboltsid/mcp-nutanix**](https://github.com/thunderboltsid/mcp-nutanix) | Nutanix Prism Central 리소스와 인터페이스하는 Go 기반 MCP 서버입니다. |
| [**time-mcp-nuget**](https://github.com/domdomegg/time-mcp-nuget) | RFC 3339 형식의 현재 UTC 시간을 가져옵니다. (.NET/NuGet 구현) |
| [**time-mcp-pypi**](https://github.com/domdomegg/time-mcp-pypi) | RFC 3339 형식의 현재 UTC 시간을 가져옵니다. (Python/PyPI 구현) |
| [**timowhite88/farnsworth-syntek**](https://github.com/timowhite88/farnsworth-syntek) | 컨텍스트 분기, 홀로그래픽 리콜, 드림 통합, 온체인 영속성을 갖춘 7계층 재귀 에이전트 메모리입니다. 10개 도구로 영구적 에이전트 인지를 지원합니다. |
| [**tip.md**](https://github.com/tipdotmd#-mcp-server-for-ai-assistants) | AI 어시스턴트가 tip.md의 암호화폐 팁 기능과 상호작용하여 AI 채팅에서 직접 개발자에게 팁을 보낼 수 있는 MCP 서버입니다. |
| [**Tmux**](https://github.com/nickgnd/tmux-mcp) | Tmux 세션, 윈도우, 패인과 상호작용하고 명령을 실행하며 결과를 조회합니다. |
| [**tomba-io/tomba-mcp-server**](https://github.com/tomba-io/tomba-mcp-server) | 이메일 발견, 검증, 강화 도구입니다. 이메일 주소 찾기, 전달 가능성 확인, 연락처 강화, LinkedIn 프로필 탐색, 전화번호 검증, 기술 스택 분석을 지원합니다. |
| [**tomholford/mcp-tic-tac-toe**](https://github.com/tomholford/mcp-tic-tac-toe) | 이 MCP 서버를 사용하여 AI 상대와 틱택토 게임을 합니다. |
| [**Tommertom/awesome-ionic-mcp**](https://github.com/Tommertom/awesome-ionic-mcp) | MCP를 통한 Ionic 코딩 도우미입니다. React/Angular/Vue 또는 Vanilla JS로 모바일 앱을 구축합니다. |
| [**Topolograph MCP**](https://github.com/Vadims06/topolograph-mcp-server) | LLM이 OSPF 및 IS-IS 프로토콜과 상호작용하고 네트워크 토폴로지 분석, 네트워크 이벤트 쿼리, 경로 계산을 수행하는 MCP 서버입니다. |
| [**TouchDesigner**](https://github.com/8beeeaaat/touchdesigner-mcp) | TouchDesigner 프로젝트, 노드, 파라미터와 상호작용하는 MCP 서버입니다. |
| [**traceloop/opentelemetry-mcp-server**](https://github.com/traceloop/opentelemetry-mcp-server.git) | Datadog, Grafana, Dynatrace, Traceloop 등 모든 OpenTelemetry 백엔드에 연결하는 MCP 서버입니다. |
| [**TrackMage**](https://github.com/trackmage/trackmage-mcp-server) | TrackMage API를 통한 배송 추적 및 물류 관리 기능을 제공합니다. |
| [**Trade Agent**](https://github.com/Trade-Agent/trade-agent-mcp) | Trade Agent를 통해 주식 및 암호화폐 거래를 실행합니다. |
| [**Trade It**](https://github.com/trade-it-inc/trade-it-mcp) | Trade It을 통해 주식, 암호화폐, 옵션 거래를 실행합니다. Robinhood, ETrade, Charles Schwab, Webull, Coinbase, Kraken을 지원합니다. |
| [**Trade-Agent/trade-agent-mcp**](https://github.com/Trade-Agent/trade-agent-mcp.git) | Trade Agent MCP 서버를 통해 Robinhood, E*Trade, Coinbase, Kraken 등에서 주식과 암호화폐를 거래합니다. |
| [**trayders/trayd-mcp**](https://github.com/trayders/trayd-mcp) | 자연어로 Robinhood 거래를 수행합니다. Claude Code를 통한 포트폴리오 분석, 실시간 시세, 주문 실행을 지원합니다. |
| [**Trino**](https://github.com/tuannvm/mcp-trino) | Go로 구현된 Trino용 고성능 MCP 서버입니다. |
| [**Tripadvisor**](https://github.com/pab1it0/tripadvisor-mcp) | LLM이 표준화된 MCP 인터페이스를 통해 Tripadvisor API와 상호작용하여 위치 데이터, 리뷰, 사진을 활용하는 MCP 서버입니다. |
| [**TrueNAS Core MCP**](https://github.com/vespo92/TrueNasCoreMCP) | TrueNAS Core와 상호작용하는 MCP 서버입니다. |
| [**tumf/mcp-text-editor**](https://github.com/tumf/mcp-text-editor) | 라인 기반 텍스트 파일 편집기입니다. 효율적인 부분 파일 접근으로 토큰 사용량을 최소화하도록 LLM 도구에 최적화되었습니다. |
| [**Tyk API Management**](https://github.com/TykTechnologies/tyk-dashboard-mcp) | 조직의 모든 관리 API와 대화하고 토큰, 사용자, 분석 등 API 라이프사이클 작업을 수행합니다. |
| [**Uberall**](https://github.com/uberall/uberall-mcp-server) | uberall을 통해 다중 위치 프레전스(목록, 리뷰, 소셜 포스팅)를 관리합니다. |
| [**UnifAI**](https://github.com/unifai-network/unifai-mcp-server) | UnifAI Network를 사용하여 도구를 동적으로 검색하고 호출합니다. |
| [**UnitVectorY-Labs/mcp-graphql-forge**](https://github.com/UnitVectorY-Labs/mcp-graphql-forge) | 큐레이션된 GraphQL 쿼리를 모듈형 도구로 노출하여 에이전트의 의도적인 API 상호작용을 지원하는 경량 설정 기반 MCP 서버입니다. |
| [**Unity Catalog**](https://github.com/ognis1205/mcp-server-unitycatalog) | LLM이 Unity Catalog AI와 상호작용하여 Unity Catalog Functions에 대한 CRUD 작업을 수행하는 MCP 서버입니다. |
| [**Universal MCP Servers**](https://github.com/universal-mcp) | AgentR Universal MCP SDK로 생성된 MCP 서버 컬렉션입니다. |
| [**Unleash Integration (Feature Toggle)**](https://github.com/cuongtl1992/unleash-mcp) | Unleash Feature Toggle 시스템과 통합하는 MCP 서버 구현입니다. LLM 애플리케이션과 Unleash Feature Flag 시스템 간 브리지를 제공합니다. |
| [**USA Spending MCP Server**](https://github.com/thsmale/usaspending-mcp-server) | 미국 정부 지출 데이터의 공식 출처 USASPENDING.gov를 활용합니다. 시간별 정부 지출 추적, 기관별 검색 등을 지원합니다. |
| [**User Prompt MCP**](https://github.com/nazar256/user-prompt-mcp) | 생성 과정 중 사용자 입력을 요청할 수 있게 하는 Cursor용 MCP 서버입니다. |
| [**userad/didlogic_mcp**](https://github.com/UserAd/didlogic_mcp) | DIDLogic용 MCP 서버로, SIP 엔드포인트, 번호, 목적지를 관리합니다. |
| [**USPTO**](https://github.com/riemannzeta/patent_mcp_server) | ODP API를 통해 미국 특허상표청(USPTO) 데이터에 접근하는 MCP 서버입니다. |
| [**UUV**](https://github.com/e2e-test-quest/uuv/tree/main/packages/mcp-server) | UUV로 사람이 읽을 수 있는 End-to-End 테스트를 생성합니다. |
| [**Vantage**](https://github.com/vantage-sh/vantage-mcp-server) | 조직의 클라우드 비용 지출과 상호작용합니다. |
| [**var-gg/mcp**](https://github.com/var-gg/mcp) | Cursor MCP 통합을 통해 AI 생성 코드에 팀 네이밍 일관성을 적용합니다. |
| [**vasayxtx/mcp-prompt-engine**](https://github.com/vasayxtx/mcp-prompt-engine) | 강력한 텍스트 템플릿 엔진을 사용하여 동적 프롬프트 템플릿을 관리하고 제공하는 MCP 서버입니다. |
| [**VCAgents**](https://github.com/OctagonAI/octagon-vc-agents) | 시장 인텔리전스로 지속 업데이트되는 투자자 에이전트와 상호작용합니다. |
| [**Vectara**](https://github.com/vectara/vectara-mcp) | Vectara의 신뢰할 수 있는 RAG-as-a-service 플랫폼을 쿼리합니다. |
| [**Verodat**](https://github.com/Verodat/verodat-mcp-server) | Verodat AI Ready Data 플랫폼과 상호작용합니다. |
| [**Vibe Check**](https://github.com/PV-Bhat/vibe-check-mcp-server) | 외부 감독 레이어를 활용하여 에이전트를 "바이브 체크"하고 시간이 지남에 따라 정확도와 사용자 정렬을 자체 개선하는 MCP 서버입니다. |
| [**Video Still Capture**](https://github.com/13rac1/videocapture-mcp) | OpenCV 호환 웹캠 또는 기타 비디오 소스에서 비디오 스틸 이미지를 캡처합니다. |
| [**video-creator/ffmpeg-mcp**](https://github.com/video-creator/ffmpeg-mcp.git) | ffmpeg 명령줄 기반 MCP 서버로, 대화를 통해 로컬 비디오 검색, 편집, 이어붙이기, 재생 등을 수행합니다. |
| [**ViperJuice/mcp-gateway**](https://github.com/ViperJuice/mcp-gateway) | 프로그레시브 디스클로저와 동적 서버 프로비저닝으로 Claude Code 도구 비대화를 최소화하는 메타 서버입니다. 9개의 안정적인 메타 도구를 노출하고 25개 이상의 MCP 서버를 온디맨드 프로비저닝합니다. |
| [**VISO TRUST**](https://github.com/visotrust/viso-mcp-server) | AI 어시스턴트를 통해 VISO TRUST 서드파티 리스크 프로그램에 직접 접근하고 관리합니다. |
| [**VmLia/books-mcp-server**](https://github.com/VmLia/books-mcp-server) | 도서 조회를 위한 MCP 서버로, Cherry Studio 등 일반 MCP 클라이언트에서 사용할 수 있습니다. |
| [**VolcEngine TOS**](https://github.com/dinghuazhou/sample-mcp-server-tos) | VolcEngine TOS에서 객체를 유연하게 가져오는 샘플 MCP 서버입니다. |
| [**Voyp**](https://github.com/paulotaylor/voyp-mcp) | AI를 사용하여 전화를 거는 VOYP MCP 서버입니다. |
| [**VSCode Devtools**](https://github.com/biegehydra/BifrostMCP) | VSCode IDE에 연결하여 find_usages 등 시맨틱 도구를 사용합니다. |
| [**WayStation**](https://github.com/waystation-ai/mcp) | Notion, Monday, AirTable 등 인기 생산성 도구에 연결하는 범용 MCP 서버입니다. |
| [**WayStation**](https://waystation.ai/connect/mcp-server) | Notion, Monday, AirTable 등 인기 생산성 도구에 연결하는 범용 원격 MCP 서버입니다. |
| [**Webflow**](https://github.com/webflow/mcp-server) | Webflow 사이트, 페이지, 컬렉션과 상호작용합니다. |
| [**Webflow**](https://github.com/kapilduraphe/webflow-mcp-server) | Webflow API와 상호작용합니다. |
| [**Website Snapshot**](https://github.com/gustavo-meilus/mcp-web-snapshot) | Playwright를 사용하여 종합적인 웹사이트 스냅샷 기능을 제공하는 MCP 서버입니다. 접근성 스냅샷과 네트워크 모니터링을 통해 웹 페이지를 분석합니다. |
| [**weibaohui/kom**](https://github.com/weibaohui/kom) | MCP 멀티 클러스터 Kubernetes 관리 및 운영을 제공합니다. SDK로 프로젝트에 통합 가능하며 50개에 가까운 내장 도구로 일반 DevOps 시나리오를 지원합니다. |
| [**Whois MCP**](https://github.com/bharathvaj-ganesan/whois-mcp) | 도메인, IP, ASN, TLD에 대한 Whois 조회를 수행하는 MCP 서버입니다. |
| [**WildFly MCP**](https://github.com/wildfly-extras/wildfly-mcp) | 실행 중인 WildFly 서버와 LLM이 상호작용하여 메트릭 조회, 로그 확인, 작업 실행 등을 수행하는 MCP 서버입니다. |
| [**Willi MaKo Knowledge Service**](https://mcp.stromhaltig.de) | 독일의 복잡한 에너지 시장 커뮤니케이션(MaKo) 규정을 위한 지식 서비스입니다. |
| [**willvelida/mcp-afl-server**](https://github.com/willvelida/mcp-afl-server) | Squiggle API와 통합하여 AFL 팀, 순위, 결과, 예측, 파워 랭킹 정보를 제공하는 MCP 서버입니다. |
| [**Windsor**](https://github.com/windsor-ai/windsor_mcp) | Windsor MCP로 LLM이 Windsor.ai에 통합된 풀스택 비즈니스 데이터를 SQL 작성 없이 쿼리, 탐색, 분석합니다. |
| [**Winston AI**](https://github.com/gowinston-ai/winston-ai-mcp-server) | 텍스트 및 이미지에서 AI 사용을 업계 최고 정확도로 탐지하는 AI 탐지 MCP 서버입니다. 표절 검사 기능도 제공합니다. |
| [**WiseVision/mcp_server_ros_2**](https://github.com/wise-vision/mcp_server_ros_2) | AI 기반 로보틱스 애플리케이션과 서비스를 지원하는 ROS2 MCP 서버입니다. |
| [**wn01011/llm-token-tracker**](https://github.com/wn01011/llm-token-tracker) | MCP 지원, 실시간 세션 추적, 2025년 모델의 정확한 가격 정보를 제공하는 OpenAI 및 Claude API 토큰 사용량 추적기입니다. |
| [**Wordle MCP**](https://github.com/cr2007/mcp-wordle-python) | 특정 날짜의 Wordle 정답을 가져오는 MCP 서버입니다. |
| [**WordPress MCP Adapter**](https://github.com/WordPress/mcp-adapter) | Abilities API를 MCP에 브리지하여 MCP 클라이언트가 WordPress 플러그인, 테마, 코어 기능을 프로그래밍 방식으로 탐색하고 호출하는 어댑터입니다. |
| [**WordPress.com**](https://developer.wordpress.com/docs/mcp/) | AI 어시스턴트를 WordPress.com에 연결하여 사이트 콘텐츠, 분석, 설정에 직접 접근합니다. |
| [**World Bank data API**](https://github.com/anshumax/world_bank_mcp_server) | World Bank 데이터 API의 데이터 지표를 가져오는 서버입니다. |
| [**ws-mcp**](https://github.com/nick1udwig/ws-mcp) | MCP 서버를 WebSocket으로 래핑합니다. (kibitz와 함께 사용) |
| [**wyattjoh/jsr-mcp**](https://github.com/wyattjoh/jsr-mcp) | JSR(JavaScript Registry)용 MCP 서버입니다. |
| [**xcodebuild**](https://github.com/ShenghaiWang/xcodebuild) | iOS Xcode 워크스페이스/프로젝트를 빌드하고 오류를 LLM에 피드백합니다. |
| [**xcsimctl**](https://github.com/nzrsky/simctl-mcp-server) | Xcode 시뮬레이터를 관리합니다. |
| [**xctools**](https://github.com/nzrsky/xctools-mcp-server) | Xcode의 xctrace, xcrun, xcodebuild용 MCP 서버입니다. |
| [**Xuanwo/mcp-server-opendal**](https://github.com/Xuanwo/mcp-server-opendal) | Apache OpenDAL로 모든 스토리지에 접근합니다. |
| [**xxczaki/local-history-mcp**](https://github.com/xxczaki/local-history/mcp) | VS Code/Cursor 로컬 히스토리에 접근하는 MCP 서버입니다. |
| [**xzq.xu/jvm-mcp-server**](https://github.com/xzq-xu/jvm-mcp-server) | JVM 기반 MCP 서버 구현 프로젝트입니다. |
| [**yamanoku/baseline-mcp-server**](https://github.com/yamanoku/baseline-mcp-server) | Web Platform API를 사용하여 Baseline 상태를 검색하는 MCP 서버입니다. |
| [**yshngg/pmcp**](https://github.com/yshngg/pmcp) | Prometheus MCP 서버입니다. |
| [**YuChenSSR/mindmap-mcp-server**](https://github.com/YuChenSSR/mindmap-mcp-server) | 아름답고 인터랙티브한 마인드맵을 생성하는 MCP 서버입니다. |
| [**Yunxin**](https://github.com/netease-im/yunxin-mcp-server) | Yunxin의 IM/RTC/DATA Open-API에 연결하는 MCP 서버입니다. |
| [**Yutarop/ros-mcp**](https://github.com/Yutarop/ros-mcp) | ROS2 토픽, 서비스, 액션 통신을 지원하고 자연어로 로봇을 제어하는 MCP 서버입니다. |
| [**yWorks/mcp-typescribe**](https://github.com/yWorks/mcp-typescribe) | 에이전트에 TypeScript API 정보를 효율적으로 제공하여 학습되지 않은 API로 작업할 수 있게 하는 MCP 서버입니다. |
| [**Zenable**](https://docs.zenable.io/integrations/mcp/getting-started) | 부정확한 AI 코드를 정리하고 취약점을 방지합니다. |
| [**ZenML**](https://github.com/zenml-io/mcp-zenml) | ZenML MCP 서버를 통해 MLOps 및 LLMOps 파이프라인과 상호작용합니다. |
| [**ZeparHyfar/mcp-datetime**](https://github.com/ZeparHyfar/mcp-datetime) | 다양한 형식의 날짜 및 시간 함수를 제공하는 MCP 서버입니다. |
| [**ZIZAI Recruitment**](https://github.com/zaiwork/mcp) | ZIZAI Recruitment이 제공하는 차세대 지능형 채용 플랫폼과 상호작용합니다. |

---

## 기여 & 출처

이 가이드는 아래 오픈소스 프로젝트에서 데이터를 수집하여 만들어졌습니다:

| 출처 | 설명 |
|------|------|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Anthropic 공식 MCP 서버 레포지토리 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | wong2의 MCP 서버 큐레이션 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | punkpeye의 MCP 서버 큐레이션 |
| [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | appcypher의 MCP 서버 큐레이션 |

> 💡 새로운 MCP 서버를 발견하면 이 문서에 추가해주세요!
