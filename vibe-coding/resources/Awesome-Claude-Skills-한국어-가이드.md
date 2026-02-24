# Awesome Claude Skills 한국어 종합 가이드

Claude Code의 Skills 생태계를 구성하는 공식 스킬, 커뮤니티 스킬, 워크플로우, 도구, 오케스트레이터 등을 한국어로 정리한 문서이다.

> **출처**: [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills), [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code), [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

---

## 목차

1. [Anthropic 공식 스킬](#1-anthropic-공식-스킬)
2. [기업 공식 스킬 (팀별)](#2-기업-공식-스킬-팀별)
3. [보안 전문 스킬 (Trail of Bits)](#3-보안-전문-스킬-trail-of-bits)
4. [커뮤니티 에이전트 스킬](#4-커뮤니티-에이전트-스킬)
5. [커뮤니티 개별 스킬](#5-커뮤니티-개별-스킬)
6. [워크플로우 & 지식 가이드](#6-워크플로우--지식-가이드)
7. [도구 (Tooling)](#7-도구-tooling)
8. [오케스트레이터](#8-오케스트레이터)
9. [Hooks](#9-hooks)
10. [슬래시 커맨드](#10-슬래시-커맨드)
11. [Status Line](#11-status-line)
12. [CLAUDE.md 파일 모음](#12-claudemd-파일-모음)

---

## 1. Anthropic 공식 스킬

### 문서 처리 스킬

| 스킬 | 설명 |
|------|------|
| [**docx**](https://github.com/anthropics/skills/tree/main/skills/docx) | Word 문서를 생성·편집·분석하며, 변경 추적·댓글·서식 보존 기능을 지원한다 |
| [**doc-coauthoring**](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | 실시간 협업 문서 편집을 지원하여 여러 사용자가 동시에 문서를 수정할 수 있다 |
| [**pdf**](https://github.com/anthropics/skills/tree/main/skills/pdf) | PDF에서 텍스트와 테이블을 추출하고, PDF 생성·병합·분할·양식 처리를 수행한다 |
| [**pptx**](https://github.com/anthropics/skills/tree/main/skills/pptx) | PowerPoint 프레젠테이션을 생성·편집·분석하며, 레이아웃·템플릿·차트를 활용한다 |
| [**xlsx**](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Excel 스프레드시트를 생성·편집·분석하고, 수식·서식·데이터 분석 기능을 제공한다 |

### 디자인 & 크리에이티브 스킬

| 스킬 | 설명 |
|------|------|
| [**algorithmic-art**](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | p5.js를 사용하여 시드 기반 랜덤성과 파티클 시스템으로 생성적 예술 작품을 만든다 |
| [**canvas-design**](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | 디자인 원칙을 적용하여 PNG 및 PDF 형식의 시각 예술 작품을 디자인한다 |
| [**slack-gif-creator**](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) | Slack의 파일 크기 제약에 최적화된 애니메이션 GIF를 생성한다 |
| [**theme-factory**](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | 전문적인 테마를 생성하고 커스텀 테마를 제작하는 도구를 제공한다 |

### 개발 스킬

| 스킬 | 설명 |
|------|------|
| [**frontend-design**](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 일반적인 미학을 피하고 React와 Tailwind를 사용한 과감한 디자인 결정을 내린다 |
| [**web-artifacts-builder**](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | React, Tailwind CSS, shadcn/ui를 활용하여 복잡한 HTML 아티팩트를 구축한다 |
| [**mcp-builder**](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | API 통합을 위한 고품질 MCP 서버를 생성하는 가이드를 제공한다 |
| [**webapp-testing**](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Playwright를 사용하여 로컬 웹 애플리케이션의 UI를 테스트하고 검증한다 |

### 커뮤니케이션 & 유틸리티 스킬

| 스킬 | 설명 |
|------|------|
| [**brand-guidelines**](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | 공식 브랜드 색상과 타이포그래피를 아티팩트에 적용한다 |
| [**internal-comms**](https://github.com/anthropics/skills/tree/main/skills/internal-comms) | 상태 보고서, 뉴스레터, FAQ, 내부 커뮤니케이션 문서를 작성한다 |
| [**skill-creator**](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Q&A 방식의 대화형 도구로 사용자가 새로운 스킬을 단계별로 생성할 수 있도록 안내한다 |
| [**template**](https://github.com/anthropics/skills/tree/main/template) | 새로운 스킬 개발의 출발점이 되는 스타터 템플릿을 제공한다 |

---

## 2. 기업 공식 스킬 (팀별)

### Vercel 엔지니어링 팀

| 스킬 | 설명 |
|------|------|
| [**react-best-practices**](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | React의 권장 패턴과 모범 사례를 적용하여 코드 품질을 높인다 |
| [**vercel-deploy-claimable**](https://github.com/vercel-labs/agent-skills/tree/main/skills/claude.ai/vercel-deploy-claimable) | Vercel 프로젝트를 배포하고 관리하는 과정을 자동화한다 |
| [**web-design-guidelines**](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | 웹 디자인 표준과 원칙을 적용하여 일관된 UI를 구현한다 |
| [**composition-patterns**](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) | 재사용 가능한 React 컴포넌트 합성 패턴을 가이드한다 |
| [**next-best-practices**](https://github.com/vercel-labs/next-skills/tree/main/skills/next-best-practices) | Next.js의 권장 접근 방식과 최적화 기법을 적용한다 |
| [**next-cache-components**](https://github.com/vercel-labs/next-skills/tree/main/skills/next-cache-components) | Next.js에서 캐싱 전략을 구현하여 성능을 최적화한다 |
| [**next-upgrade**](https://github.com/vercel-labs/next-skills/tree/main/skills/next-upgrade) | Next.js 버전 업그레이드를 안전하게 수행하는 절차를 안내한다 |
| [**react-native-skills**](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-native-skills) | React Native 앱의 최적화와 성능 향상 기법을 제공한다 |

### Cloudflare 팀

| 스킬 | 설명 |
|------|------|
| [**agents-sdk**](https://github.com/cloudflare/skills/tree/main/skills/agents-sdk) | 스케줄링, RPC, MCP 서버를 갖춘 상태 기반 AI 에이전트를 구축한다 |
| [**building-ai-agent-on-cloudflare**](https://github.com/cloudflare/skills/tree/main/skills/building-ai-agent-on-cloudflare) | 상태 관리와 WebSocket 기반 에이전트를 Cloudflare 위에 구축한다 |
| [**building-mcp-server-on-cloudflare**](https://github.com/cloudflare/skills/tree/main/skills/building-mcp-server-on-cloudflare) | Cloudflare에서 원격 MCP 서버를 개발하고 배포한다 |
| [**commands**](https://github.com/cloudflare/skills/tree/main/commands) | Cloudflare CLI 명령어 레퍼런스를 제공한다 |
| [**durable-objects**](https://github.com/cloudflare/skills/tree/main/skills/durable-objects) | RPC와 SQLite를 활용한 상태 기반 조정 패턴을 구현한다 |
| [**web-perf**](https://github.com/cloudflare/skills/tree/main/skills/web-perf) | Core Web Vitals를 분석하고 렌더링 차단 리소스를 감사한다 |
| [**wrangler**](https://github.com/cloudflare/skills/tree/main/skills/wrangler) | Workers, KV, R2, D1, Vectorize, Queues, Workflows를 배포하고 관리한다 |

### Supabase 팀

| 스킬 | 설명 |
|------|------|
| [**postgres-best-practices**](https://github.com/supabase/agent-skills/tree/main/skills/supabase-postgres-best-practices) | Supabase 환경에서 PostgreSQL을 사용할 때의 모범 사례를 적용한다 |

### Google Gemini

| 스킬 | 설명 |
|------|------|
| [**gemini-skills**](https://github.com/google-gemini/gemini-skills) | Gemini API 및 SDK와 상호작용하는 라이브러리를 제공한다 |

### Google Labs (Stitch)

| 스킬 | 설명 |
|------|------|
| [**design-md**](https://github.com/google-labs-code/stitch-skills/tree/main/skills/design-md) | DESIGN.md 파일을 생성하고 관리하여 디자인 시스템을 문서화한다 |
| [**enhance-prompt**](https://github.com/google-labs-code/stitch-skills/tree/main/skills/enhance-prompt) | 디자인 스펙을 반영하여 프롬프트를 개선한다 |
| [**react-components**](https://github.com/google-labs-code/stitch-skills/tree/main/skills/react-components) | Stitch 디자인을 React 컴포넌트로 변환한다 |
| [**remotion**](https://github.com/google-labs-code/stitch-skills/tree/main/skills/remotion) | 디자인 시안에서 워크스루 동영상을 생성한다 |
| [**shadcn-ui**](https://github.com/google-labs-code/stitch-skills/tree/main/skills/shadcn-ui) | shadcn/ui 컴포넌트를 활용한 UI 개발을 지원한다 |
| [**stitch-loop**](https://github.com/google-labs-code/stitch-skills/tree/main/skills/stitch-loop) | 디자인에서 코드로의 반복적 워크플로우를 자동화한다 |

### Hugging Face 팀

| 스킬 | 설명 |
|------|------|
| [**hugging-face-cli**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-cli) | HF Hub CLI를 통해 모델, 데이터셋, 리포, 컴퓨트 작업을 관리한다 |
| [**hugging-face-datasets**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-datasets) | SQL 쿼리를 지원하는 데이터셋을 생성하고 관리한다 |
| [**hugging-face-evaluation**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-evaluation) | vLLM과 lighteval을 사용하여 모델을 평가한다 |
| [**hugging-face-jobs**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-jobs) | 컴퓨트 작업과 Python 스크립트를 실행한다 |
| [**hugging-face-model-trainer**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-model-trainer) | SFT, DPO, GRPO 방식으로 모델을 학습시킨다 |
| [**hugging-face-paper-publisher**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-paper-publisher) | 모델과 데이터셋 링크를 포함한 논문을 게시한다 |
| [**hugging-face-tool-builder**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-tool-builder) | 재사용 가능한 HF API 스크립트를 생성한다 |
| [**hugging-face-trackio**](https://github.com/huggingface/skills/tree/main/skills/hugging-face-trackio) | 대시보드를 활용하여 ML 실험을 추적하고 모니터링한다 |

### Stripe 팀

| 스킬 | 설명 |
|------|------|
| [**stripe-best-practices**](https://github.com/stripe/ai/tree/main/skills/stripe-best-practices) | Stripe 결제 통합 시 모범 사례를 적용하여 안전하게 구현한다 |
| [**upgrade-stripe**](https://github.com/stripe/ai/tree/main/skills/upgrade-stripe) | Stripe SDK와 API 버전을 안전하게 업그레이드하는 절차를 안내한다 |

### CallStack 팀

| 스킬 | 설명 |
|------|------|
| [**react-native-best-practices**](https://github.com/callstackincubator/agent-skills/blob/main/skills/react-native-best-practices/SKILL.md) | React Native 앱의 성능 최적화 기법을 제공한다 |
| [**github**](https://github.com/callstackincubator/agent-skills/tree/main/skills/github) | GitHub 워크플로우 패턴과 CI/CD 통합을 가이드한다 |
| [**upgrading-react-native**](https://github.com/callstackincubator/agent-skills/tree/main/skills/upgrading-react-native) | React Native 버전 업그레이드 절차를 안전하게 수행한다 |

### Expo 팀

| 스킬 | 설명 |
|------|------|
| [**expo-app-design**](https://github.com/expo/skills/tree/main/plugins/expo-app-design) | Expo 프레임워크를 사용한 모바일 앱 설계를 지원한다 |
| [**expo-deployment**](https://github.com/expo/skills/tree/main/plugins/expo-deployment) | Expo 앱을 프로덕션 환경에 배포하는 과정을 자동화한다 |
| [**upgrading-expo**](https://github.com/expo/skills/tree/main/plugins/upgrading-expo) | Expo SDK 버전 업그레이드를 안전하게 수행한다 |

### Sentry 팀

| 스킬 | 설명 |
|------|------|
| [**agents-md**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/agents-md) | AGENTS.md 파일을 자동으로 생성하여 에이전트 설정을 문서화한다 |
| [**claude-settings-audit**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/claude-settings-audit) | Claude 설정을 감사하여 최적 구성을 확인한다 |
| [**code-review**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/code-review) | 코드 리뷰를 체계적으로 수행하고 피드백을 제공한다 |
| [**commit**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/commit) | 모범 사례를 적용한 커밋 메시지를 작성한다 |
| [**create-pr**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/create-pr) | 구조화된 풀 리퀘스트를 자동으로 생성한다 |
| [**find-bugs**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/find-bugs) | 코드에서 버그를 식별하고 분석한다 |
| [**iterate-pr**](https://github.com/getsentry/skills/tree/main/plugins/sentry-skills/skills/iterate-pr) | PR 피드백을 반영하여 반복적으로 개선한다 |

### Better Auth 팀

| 스킬 | 설명 |
|------|------|
| [**best-practices**](https://github.com/better-auth/skills/tree/main/better-auth/best-practices) | Better Auth 통합 시 모범 사례를 적용한다 |
| [**commands**](https://github.com/better-auth/skills/tree/main/better-auth/commands) | Better Auth CLI 명령어를 제공한다 |
| [**create-auth**](https://github.com/better-auth/skills/tree/main/better-auth/create-auth) | 인증 시스템 설정을 자동으로 생성한다 |

### Tinybird 팀

| 스킬 | 설명 |
|------|------|
| [**tinybird-best-practices**](https://github.com/tinybirdco/tinybird-agent-skills/tree/main/skills/tinybird-best-practices) | 데이터소스, 파이프, 엔드포인트, SQL에 대한 모범 사례를 적용한다 |

### Neon

| 스킬 | 설명 |
|------|------|
| [**using-neon**](https://github.com/neondatabase/agent-skills/tree/main/skills/neon-postgres) | Neon Postgres 서버리스 데이터베이스를 활용하는 모범 사례를 제공한다 |

### ClickHouse

| 스킬 | 설명 |
|------|------|
| [**agent-skills**](https://github.com/ClickHouse/agent-skills) | ClickHouse 분석 데이터베이스 활용 스킬을 제공한다 |

### fal.ai 팀

| 스킬 | 설명 |
|------|------|
| [**fal-audio**](https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-audio/SKILL.md) | fal.ai 플랫폼에서 오디오 생성 및 처리 기능을 제공한다 |
| [**fal-generate**](https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-generate/SKILL.md) | fal.ai를 활용한 이미지 생성 기능을 제공한다 |
| [**fal-image-edit**](https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-image-edit/SKILL.md) | fal.ai를 활용한 이미지 편집 기능을 제공한다 |
| [**fal-platform**](https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-platform/SKILL.md) | fal.ai 플랫폼 전반의 기능을 활용하는 가이드를 제공한다 |
| [**fal-upscale**](https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-upscale/SKILL.md) | fal.ai를 활용한 이미지 업스케일링 기능을 제공한다 |
| [**fal-workflow**](https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-workflow/SKILL.md) | fal.ai 워크플로우를 구성하고 실행하는 기능을 제공한다 |

### HashiCorp (Terraform)

| 스킬 | 설명 |
|------|------|
| [**terraform-code-generation**](https://github.com/hashicorp/agent-skills/tree/main/terraform/code-generation) | Terraform 코드를 자동으로 생성한다 |
| [**terraform-module-generation**](https://github.com/hashicorp/agent-skills/tree/main/terraform/module-generation) | 재사용 가능한 Terraform 모듈을 생성한다 |
| [**terraform-provider-development**](https://github.com/hashicorp/agent-skills/tree/main/terraform/provider-development) | Terraform 프로바이더를 개발하는 가이드를 제공한다 |

### Sanity 팀

| 스킬 | 설명 |
|------|------|
| [**sanity-best-practices**](https://github.com/sanity-io/agent-toolkit/tree/main/skills/sanity-best-practices) | Sanity CMS 통합 시 모범 사례를 적용한다 |
| [**content-modeling-best-practices**](https://github.com/sanity-io/agent-toolkit/tree/main/skills/content-modeling-best-practices) | 콘텐츠 모델링 설계 모범 사례를 제공한다 |
| [**seo-aeo-best-practices**](https://github.com/sanity-io/agent-toolkit/tree/main/skills/seo-aeo-best-practices) | SEO와 AEO(Answer Engine Optimization) 모범 사례를 적용한다 |
| [**content-experimentation-best-practices**](https://github.com/sanity-io/agent-toolkit/tree/main/skills/content-experimentation-best-practices) | 콘텐츠 실험과 A/B 테스트 모범 사례를 제공한다 |

### Remotion

| 스킬 | 설명 |
|------|------|
| [**remotion**](https://github.com/remotion-dev/skills/tree/main/skills/remotion) | Remotion을 활용한 프로그래밍 방식의 동영상 생성을 지원한다 |

### WordPress 개발 팀

| 스킬 | 설명 |
|------|------|
| [**wordpress-router**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wordpress-router) | WordPress 스킬 간 라우팅을 관리한다 |
| [**wp-project-triage**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage) | WordPress 프로젝트 이슈를 분류하고 우선순위를 지정한다 |
| [**wp-block-development**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-block-development) | WordPress 블록 에디터 커스텀 블록을 개발한다 |
| [**wp-block-themes**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-block-themes) | WordPress 블록 테마를 개발한다 |
| [**wp-plugin-development**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-plugin-development) | WordPress 플러그인을 개발하는 가이드를 제공한다 |
| [**wp-rest-api**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-rest-api) | WordPress REST API를 활용한 개발을 지원한다 |
| [**wp-interactivity-api**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-interactivity-api) | WordPress Interactivity API를 활용한 동적 UI를 구현한다 |
| [**wp-abilities-api**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-abilities-api) | WordPress Abilities API를 활용한 권한 관리를 구현한다 |
| [**wp-wpcli-and-ops**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-wpcli-and-ops) | WP-CLI를 활용한 WordPress 운영 자동화를 지원한다 |
| [**wp-performance**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-performance) | WordPress 성능 최적화 기법을 제공한다 |
| [**wp-phpstan**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan) | PHPStan을 활용한 WordPress 정적 분석을 수행한다 |
| [**wp-playground**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-playground) | WordPress Playground 환경을 구성하고 활용한다 |
| [**wpds**](https://github.com/WordPress/agent-skills/tree/trunk/skills/wpds) | WordPress Design System을 적용한 UI 개발을 지원한다 |

### Transloadit 팀

| 스킬 | 설명 |
|------|------|
| [**transloadit**](https://github.com/transloadit/skills/tree/main/skills/transloadit) | Transloadit 파일 처리 플랫폼을 활용한다 |
| [**docs-transloadit-robots**](https://github.com/transloadit/skills/tree/main/skills/docs-transloadit-robots) | Transloadit Robot 문서를 참조한다 |
| [**transform-generate-image**](https://github.com/transloadit/skills/tree/main/skills/transform-generate-image-with-transloadit) | Transloadit을 통한 이미지 생성 및 변환을 수행한다 |
| [**transform-encode-hls-video**](https://github.com/transloadit/skills/tree/main/skills/transform-encode-hls-video-with-transloadit) | Transloadit을 통한 HLS 비디오 인코딩을 수행한다 |
| [**integrate-uppy-s3-uploading**](https://github.com/transloadit/skills/tree/main/skills/integrate-uppy-transloadit-s3-uploading-to-nextjs) | Next.js에서 Uppy와 S3 업로드를 통합한다 |
| [**integrate-smartcdn-delivery**](https://github.com/transloadit/skills/tree/main/skills/integrate-asset-delivery-with-transloadit-smartcdn-in-nextjs) | Next.js에서 SmartCDN 에셋 딜리버리를 통합한다 |

### Firecrawl 팀

| 스킬 | 설명 |
|------|------|
| [**firecrawl-cli**](https://github.com/firecrawl/cli/tree/main/skills/firecrawl-cli) | Firecrawl CLI를 활용한 웹 크롤링과 스크래핑을 수행한다 |
| [**firecrawl-claude-plugin**](https://github.com/firecrawl/firecrawl-claude-plugin) | Firecrawl Claude 플러그인을 통한 웹 데이터 수집을 지원한다 |

### OpenAI

| 스킬 | 설명 |
|------|------|
| [**cloudflare-deploy**](https://github.com/openai/skills/tree/main/skills/.curated/cloudflare-deploy) | Cloudflare에 프로젝트를 배포한다 |
| [**develop-web-game**](https://github.com/openai/skills/tree/main/skills/.curated/develop-web-game) | 웹 게임을 개발하는 가이드를 제공한다 |
| [**doc**](https://github.com/openai/skills/tree/main/skills/.curated/doc) | 문서를 생성하고 관리한다 |
| [**figma-implement-design**](https://github.com/openai/skills/tree/main/skills/.curated/figma-implement-design) | Figma 디자인을 코드로 구현한다 |
| [**figma**](https://github.com/openai/skills/tree/main/skills/.curated/figma) | Figma 도구와 연동한다 |
| [**gh-address-comments**](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) | GitHub 코멘트를 분석하고 대응한다 |
| [**gh-fix-ci**](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) | GitHub CI 실패를 분석하고 수정한다 |
| [**imagegen**](https://github.com/openai/skills/tree/main/skills/.curated/imagegen) | 이미지를 생성한다 |
| [**jupyter-notebook**](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) | Jupyter Notebook을 생성하고 실행한다 |
| [**linear**](https://github.com/openai/skills/tree/main/skills/.curated/linear) | Linear 프로젝트 관리 도구와 연동한다 |
| [**netlify-deploy**](https://github.com/openai/skills/tree/main/skills/.curated/netlify-deploy) | Netlify에 프로젝트를 배포한다 |
| [**notion-knowledge-capture**](https://github.com/openai/skills/tree/main/skills/.curated/notion-knowledge-capture) | Notion에서 지식을 캡처하고 정리한다 |
| [**notion-meeting-intelligence**](https://github.com/openai/skills/tree/main/skills/.curated/notion-meeting-intelligence) | Notion 기반 회의 인텔리전스를 제공한다 |
| [**notion-research-documentation**](https://github.com/openai/skills/tree/main/skills/.curated/notion-research-documentation) | Notion에서 리서치 문서를 작성한다 |
| [**notion-spec-to-implementation**](https://github.com/openai/skills/tree/main/skills/.curated/notion-spec-to-implementation) | Notion 스펙 문서를 코드 구현으로 변환한다 |
| [**openai-docs**](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs) | OpenAI API 문서를 참조한다 |
| [**pdf**](https://github.com/openai/skills/tree/main/skills/.curated/pdf) | PDF 파일을 처리한다 |
| [**playwright**](https://github.com/openai/skills/tree/main/skills/.curated/playwright) | Playwright 브라우저 자동화를 수행한다 |
| [**security-best-practices**](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | 보안 모범 사례를 적용한다 |
| [**security-threat-model**](https://github.com/openai/skills/tree/main/skills/.curated/security-threat-model) | 위협 모델링을 수행한다 |
| [**sentry**](https://github.com/openai/skills/tree/main/skills/.curated/sentry) | Sentry 에러 모니터링을 통합한다 |
| [**sora**](https://github.com/openai/skills/tree/main/skills/.curated/sora) | Sora 비디오 생성 모델을 활용한다 |
| [**speech**](https://github.com/openai/skills/tree/main/skills/.curated/speech) | 음성 합성 기능을 제공한다 |
| [**spreadsheet**](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet) | 스프레드시트를 처리한다 |
| [**transcribe**](https://github.com/openai/skills/tree/main/skills/.curated/transcribe) | 음성을 텍스트로 변환한다 |
| [**vercel-deploy**](https://github.com/openai/skills/tree/main/skills/.curated/vercel-deploy) | Vercel에 프로젝트를 배포한다 |

### Replicate

| 스킬 | 설명 |
|------|------|
| [**replicate**](https://github.com/replicate/skills/tree/main/skills/replicate) | Replicate 플랫폼에서 ML 모델을 실행하고 관리한다 |

### Typefully

| 스킬 | 설명 |
|------|------|
| [**typefully**](https://github.com/typefully/agent-skills/tree/main/skills/typefully) | Typefully를 활용한 소셜 미디어 콘텐츠 관리를 지원한다 |

### Microsoft .NET 스킬

| 스킬 | 설명 |
|------|------|
| [**azure-ai-agents-persistent-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-agents-persistent-dotnet) | 스레드 기반의 영구 에이전트를 .NET으로 구축한다 |
| [**azure-ai-document-intelligence-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-document-intelligence-dotnet) | 문서에서 텍스트, 테이블, 구조화된 데이터를 추출한다 |
| [**azure-ai-openai-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-openai-dotnet) | GPT-4, 임베딩, DALL-E, Whisper 모델을 통합한다 |
| [**azure-ai-projects-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-projects-dotnet) | AI Foundry 프로젝트를 관리한다 |
| [**azure-ai-voicelive-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-voicelive-dotnet) | 실시간 음성 AI 기능을 구현한다 |
| [**azure-eventgrid-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventgrid-dotnet) | Event Grid 이벤트를 발행하고 구독한다 |
| [**azure-eventhub-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventhub-dotnet) | 이벤트 스트리밍 파이프라인을 구성한다 |
| [**azure-identity-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-identity-dotnet) | Entra ID (Azure AD) 인증을 구현한다 |
| [**azure-maps-search-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-maps-search-dotnet) | 지오코딩과 경로 탐색 기능을 제공한다 |
| [**azure-mgmt-apicenter-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-apicenter-dotnet) | API Center를 통한 API 거버넌스를 관리한다 |
| [**azure-mgmt-apimanagement-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-apimanagement-dotnet) | API Management 인스턴스를 프로비저닝하고 관리한다 |
| [**azure-mgmt-applicationinsights-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-applicationinsights-dotnet) | Application Insights 리소스를 관리한다 |
| [**azure-mgmt-arizeaiobservabilityeval-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-arizeaiobservabilityeval-dotnet) | Arize AI 관찰성 및 평가 리소스를 관리한다 |
| [**azure-mgmt-botservice-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-botservice-dotnet) | Azure Bot Service를 프로비저닝하고 관리한다 |
| [**azure-mgmt-fabric-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-fabric-dotnet) | Microsoft Fabric 리소스를 관리한다 |
| [**azure-mgmt-mongodbatlas-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-mongodbatlas-dotnet) | MongoDB Atlas 클러스터를 Azure에서 관리한다 |
| [**azure-mgmt-weightsandbiases-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-weightsandbiases-dotnet) | Weights & Biases 리소스를 Azure에서 관리한다 |
| [**azure-resource-manager-cosmosdb-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-cosmosdb-dotnet) | Cosmos DB 리소스를 프로비저닝한다 |
| [**azure-resource-manager-durabletask-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-durabletask-dotnet) | Durable Task 리소스를 관리한다 |
| [**azure-resource-manager-mysql-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-mysql-dotnet) | Azure MySQL 데이터베이스를 프로비저닝한다 |
| [**azure-resource-manager-playwright-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-playwright-dotnet) | Azure Playwright Testing 리소스를 관리한다 |
| [**azure-resource-manager-postgresql-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-postgresql-dotnet) | Azure PostgreSQL 데이터베이스를 프로비저닝한다 |
| [**azure-resource-manager-redis-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-redis-dotnet) | Azure Redis Cache 리소스를 관리한다 |
| [**azure-resource-manager-sql-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-resource-manager-sql-dotnet) | Azure SQL 데이터베이스를 프로비저닝한다 |
| [**azure-search-documents-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-search-documents-dotnet) | 전문 검색과 벡터 검색을 구현한다 |
| [**azure-security-keyvault-keys-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-security-keyvault-keys-dotnet) | Key Vault에서 암호화 키를 관리한다 |
| [**azure-servicebus-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-servicebus-dotnet) | 엔터프라이즈급 메시징 시스템을 구축한다 |
| [**m365-agents-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/m365-agents-dotnet) | Microsoft 365, Teams, Copilot Studio 에이전트를 개발한다 |
| [**microsoft-azure-webjobs-extensions-authentication-events-dotnet**](https://github.com/microsoft/skills/tree/main/.github/skills/microsoft-azure-webjobs-extensions-authentication-events-dotnet) | WebJobs 인증 이벤트 확장을 구현한다 |

### Microsoft Java 스킬

| 스킬 | 설명 |
|------|------|
| [**azure-ai-agents-persistent-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-agents-persistent-java) | 영구 에이전트 스레드를 Java로 구축한다 |
| [**azure-ai-anomalydetector-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-anomalydetector-java) | 이상 탐지 서비스를 Java에서 활용한다 |
| [**azure-ai-contentsafety-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-contentsafety-java) | 콘텐츠 모더레이션 기능을 구현한다 |
| [**azure-ai-formrecognizer-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-formrecognizer-java) | 문서 분석 및 양식 인식을 수행한다 |
| [**azure-ai-projects-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-projects-java) | AI 프로젝트를 Java에서 관리한다 |
| [**azure-ai-vision-imageanalysis-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-vision-imageanalysis-java) | 이미지 분석 기능을 Java에서 구현한다 |
| [**azure-ai-voicelive-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-voicelive-java) | 실시간 음성 AI를 Java에서 구현한다 |
| [**azure-appconfiguration-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-appconfiguration-java) | App Configuration 서비스를 Java에서 활용한다 |
| [**azure-communication-callautomation-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-communication-callautomation-java) | IVR과 AI 통화 자동화를 구현한다 |
| [**azure-communication-callingserver-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-communication-callingserver-java) | 통화 서버 기능을 Java에서 구현한다 |
| [**azure-communication-chat-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-communication-chat-java) | 실시간 채팅 스레드를 구성한다 |
| [**azure-communication-common-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-communication-common-java) | Communication Services 공통 라이브러리를 활용한다 |
| [**azure-communication-sms-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-communication-sms-java) | SMS 전송 기능을 Java에서 구현한다 |
| [**azure-compute-batch-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-compute-batch-java) | Azure Batch 컴퓨트 작업을 관리한다 |
| [**azure-cosmos-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-cosmos-java) | 글로벌 분산 NoSQL 데이터베이스를 활용한다 |
| [**azure-data-tables-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-data-tables-java) | Azure Table Storage를 Java에서 활용한다 |
| [**azure-eventgrid-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventgrid-java) | Event Grid를 Java에서 활용한다 |
| [**azure-eventhub-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventhub-java) | 대용량 스트리밍 파이프라인을 구축한다 |
| [**azure-identity-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-identity-java) | Entra ID 인증을 Java 환경에서 구현한다 |
| [**azure-messaging-webpubsub-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-messaging-webpubsub-java) | Web PubSub 실시간 메시징을 Java에서 구현한다 |
| [**azure-monitor-ingestion-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-ingestion-java) | Azure Monitor 데이터 수집을 Java에서 구현한다 |
| [**azure-monitor-opentelemetry-exporter-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-opentelemetry-exporter-java) | OpenTelemetry 데이터를 Azure Monitor로 내보낸다 |
| [**azure-monitor-query-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-query-java) | Azure Monitor 로그와 메트릭을 쿼리한다 |
| [**azure-security-keyvault-keys-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-security-keyvault-keys-java) | Key Vault 암호화 키를 Java에서 관리한다 |
| [**azure-security-keyvault-secrets-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-security-keyvault-secrets-java) | Key Vault 시크릿을 Java에서 관리한다 |
| [**azure-storage-blob-java**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-blob-java) | Blob 스토리지를 관리하고 파일을 처리한다 |

### Microsoft Python 스킬

| 스킬 | 설명 |
|------|------|
| [**agent-framework-azure-ai-py**](https://github.com/microsoft/skills/tree/main/.github/skills/agent-framework-azure-ai-py) | Azure AI 에이전트 프레임워크를 Python에서 활용한다 |
| [**agents-v2-py**](https://github.com/microsoft/skills/tree/main/.github/skills/agents-v2-py) | v2 에이전트를 Python에서 구현한다 |
| [**azure-ai-contentsafety-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-contentsafety-py) | 콘텐츠 안전 서비스를 Python에서 활용한다 |
| [**azure-ai-contentunderstanding-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-contentunderstanding-py) | 콘텐츠 이해 서비스를 Python에서 활용한다 |
| [**azure-ai-ml-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-ml-py) | Azure ML 서비스를 Python에서 활용한다 |
| [**azure-ai-projects-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-projects-py) | Azure AI 프로젝트를 Python으로 관리한다 |
| [**azure-ai-textanalytics-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-textanalytics-py) | 텍스트 분석 서비스를 Python에서 활용한다 |
| [**azure-ai-transcription-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-transcription-py) | 음성 전사 서비스를 Python에서 활용한다 |
| [**azure-ai-translation-document-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-translation-document-py) | 문서 번역 서비스를 Python에서 활용한다 |
| [**azure-ai-translation-text-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-translation-text-py) | 텍스트 번역 서비스를 Python에서 활용한다 |
| [**azure-ai-vision-imageanalysis-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-vision-imageanalysis-py) | 이미지 분석 서비스를 Python에서 활용한다 |
| [**azure-ai-voicelive-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-voicelive-py) | 실시간 음성 AI를 Python에서 구현한다 |
| [**azure-appconfiguration-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-appconfiguration-py) | App Configuration을 Python에서 활용한다 |
| [**azure-containerregistry-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-containerregistry-py) | Container Registry를 Python에서 관리한다 |
| [**azure-cosmos-db-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-cosmos-db-py) | Cosmos DB를 Python에서 활용한다 (MongoDB API) |
| [**azure-cosmos-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-cosmos-py) | Cosmos DB를 Python에서 활용한다 (SQL API) |
| [**azure-data-tables-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-data-tables-py) | Azure Table Storage를 Python에서 활용한다 |
| [**azure-eventgrid-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventgrid-py) | Event Grid를 Python에서 활용한다 |
| [**azure-eventhub-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventhub-py) | Event Hub 스트리밍을 Python에서 구현한다 |
| [**azure-identity-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-identity-py) | Entra ID 인증을 Python에서 구현한다 |
| [**azure-keyvault-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-keyvault-py) | Key Vault를 Python에서 활용한다 |
| [**azure-messaging-webpubsubservice-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-messaging-webpubsubservice-py) | Web PubSub 서비스를 Python에서 활용한다 |
| [**azure-mgmt-apicenter-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-apicenter-py) | API Center를 Python에서 관리한다 |
| [**azure-mgmt-apimanagement-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-apimanagement-py) | API Management를 Python에서 관리한다 |
| [**azure-mgmt-botservice-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-botservice-py) | Bot Service를 Python에서 관리한다 |
| [**azure-mgmt-fabric-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-mgmt-fabric-py) | Microsoft Fabric을 Python에서 관리한다 |
| [**azure-monitor-ingestion-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-ingestion-py) | Monitor 데이터 수집을 Python에서 구현한다 |
| [**azure-monitor-opentelemetry-exporter-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-opentelemetry-exporter-py) | OpenTelemetry Exporter를 Python에서 구성한다 |
| [**azure-monitor-opentelemetry-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-opentelemetry-py) | OpenTelemetry를 Python에서 구성한다 |
| [**azure-monitor-query-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-query-py) | Monitor 로그/메트릭을 Python에서 쿼리한다 |
| [**azure-search-documents-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-search-documents-py) | Azure Search를 Python에서 활용한다 |
| [**azure-servicebus-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-servicebus-py) | Service Bus를 Python에서 활용한다 |
| [**azure-speech-to-text-rest-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-speech-to-text-rest-py) | Speech-to-Text REST API를 Python에서 활용한다 |
| [**azure-storage-blob-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-blob-py) | Blob 스토리지를 Python에서 관리한다 |
| [**azure-storage-file-datalake-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-file-datalake-py) | Data Lake Storage를 Python에서 관리한다 |
| [**azure-storage-file-share-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-file-share-py) | File Share를 Python에서 관리한다 |
| [**azure-storage-queue-py**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-queue-py) | Queue Storage를 Python에서 활용한다 |
| [**fastapi-router-py**](https://github.com/microsoft/skills/tree/main/.github/skills/fastapi-router-py) | FastAPI 라우터를 구성한다 |
| [**hosted-agents-v2-py**](https://github.com/microsoft/skills/tree/main/.github/skills/hosted-agents-v2-py) | 호스팅 에이전트 v2를 Python에서 구현한다 |
| [**m365-agents-py**](https://github.com/microsoft/skills/tree/main/.github/skills/m365-agents-py) | M365 에이전트를 Python으로 개발한다 |
| [**pydantic-models-py**](https://github.com/microsoft/skills/tree/main/.github/skills/pydantic-models-py) | Pydantic 모델을 설계하고 구현한다 |

### Microsoft Rust 스킬

| 스킬 | 설명 |
|------|------|
| [**azure-cosmos-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-cosmos-rust) | Cosmos DB를 Rust에서 활용한다 |
| [**azure-eventhub-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventhub-rust) | Event Hub 스트리밍을 Rust에서 구현한다 |
| [**azure-identity-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-identity-rust) | Entra ID 인증을 Rust에서 구현한다 |
| [**azure-keyvault-certificates-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-keyvault-certificates-rust) | Key Vault 인증서를 Rust에서 관리한다 |
| [**azure-keyvault-keys-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-keyvault-keys-rust) | Key Vault 암호화 키를 Rust에서 관리한다 |
| [**azure-keyvault-secrets-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-keyvault-secrets-rust) | Key Vault 시크릿을 Rust에서 관리한다 |
| [**azure-storage-blob-rust**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-blob-rust) | Blob 스토리지를 Rust에서 관리한다 |

### Microsoft TypeScript 스킬

| 스킬 | 설명 |
|------|------|
| [**azure-ai-contentsafety-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-contentsafety-ts) | 콘텐츠 안전 서비스를 TypeScript에서 활용한다 |
| [**azure-ai-document-intelligence-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-document-intelligence-ts) | 문서 인텔리전스를 TypeScript에서 활용한다 |
| [**azure-ai-projects-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-projects-ts) | AI 프로젝트를 TypeScript에서 관리한다 |
| [**azure-ai-translation-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-translation-ts) | 번역 서비스를 TypeScript에서 활용한다 |
| [**azure-ai-voicelive-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-ai-voicelive-ts) | 실시간 음성 AI를 TypeScript에서 구현한다 |
| [**azure-appconfiguration-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-appconfiguration-ts) | App Configuration을 TypeScript에서 활용한다 |
| [**azure-cosmos-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-cosmos-ts) | Cosmos DB를 TypeScript에서 활용한다 |
| [**azure-eventhub-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-eventhub-ts) | Event Hub 스트리밍을 TypeScript에서 구현한다 |
| [**azure-identity-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-identity-ts) | Entra ID 인증을 TypeScript에서 구현한다 |
| [**azure-keyvault-keys-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-keyvault-keys-ts) | Key Vault 암호화 키를 TypeScript에서 관리한다 |
| [**azure-keyvault-secrets-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-keyvault-secrets-ts) | Key Vault 시크릿을 TypeScript에서 관리한다 |
| [**azure-microsoft-playwright-testing-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-microsoft-playwright-testing-ts) | Azure Playwright Testing을 TypeScript에서 활용한다 |
| [**azure-monitor-opentelemetry-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-monitor-opentelemetry-ts) | OpenTelemetry를 TypeScript에서 구성한다 |
| [**azure-postgres-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-postgres-ts) | Azure PostgreSQL을 TypeScript에서 활용한다 |
| [**azure-search-documents-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-search-documents-ts) | Azure Search를 TypeScript에서 활용한다 |
| [**azure-servicebus-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-servicebus-ts) | Service Bus를 TypeScript에서 활용한다 |
| [**azure-storage-blob-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-blob-ts) | Blob 스토리지를 TypeScript에서 관리한다 |
| [**azure-storage-file-share-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-file-share-ts) | File Share를 TypeScript에서 관리한다 |
| [**azure-storage-queue-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-storage-queue-ts) | Queue Storage를 TypeScript에서 활용한다 |
| [**azure-web-pubsub-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/azure-web-pubsub-ts) | Web PubSub를 TypeScript에서 활용한다 |
| [**frontend-ui-dark-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/frontend-ui-dark-ts) | 다크 모드 UI 프론트엔드를 TypeScript로 구현한다 |
| [**m365-agents-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/m365-agents-ts) | M365 에이전트를 TypeScript로 개발한다 |
| [**react-flow-node-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/react-flow-node-ts) | React Flow 노드를 TypeScript로 구현한다 |
| [**zustand-store-ts**](https://github.com/microsoft/skills/tree/main/.github/skills/zustand-store-ts) | Zustand 상태 관리 스토어를 구현한다 |

### Microsoft 일반 스킬

| 스킬 | 설명 |
|------|------|
| [**azd-deployment**](https://github.com/microsoft/skills/tree/main/.github/skills/azd-deployment) | Azure Developer CLI를 통한 배포를 수행한다 |
| [**github-issue-creator**](https://github.com/microsoft/skills/tree/main/.github/skills/github-issue-creator) | GitHub 이슈를 자동으로 생성한다 |
| [**mcp-builder**](https://github.com/microsoft/skills/tree/main/.github/skills/mcp-builder) | MCP 서버를 구축하는 가이드를 제공한다 |
| [**podcast-generation**](https://github.com/microsoft/skills/tree/main/.github/skills/podcast-generation) | 팟캐스트 콘텐츠를 자동으로 생성한다 |
| [**skill-creator**](https://github.com/microsoft/skills/tree/main/.github/skills/skill-creator) | 새로운 스킬을 생성하는 도구를 제공한다 |

---

## 3. 보안 전문 스킬 (Trail of Bits)

| 스킬 | 설명 |
|------|------|
| [**ask-questions-if-underspecified**](https://github.com/trailofbits/skills/tree/main/plugins/ask-questions-if-underspecified) | 요구사항이 모호할 때 명확화 질문을 자동으로 생성한다 |
| [**audit-context-building**](https://github.com/trailofbits/skills/tree/main/plugins/audit-context-building) | 세밀한 코드 분석을 위한 감사 컨텍스트를 구축한다 |
| [**building-secure-contracts**](https://github.com/trailofbits/skills/tree/main/plugins/building-secure-contracts) | 스마트 컨트랙트 보안 개발을 위한 툴킷을 제공한다 |
| [**burpsuite-project-parser**](https://github.com/trailofbits/skills/tree/main/plugins/burpsuite-project-parser) | Burp Suite 프로젝트 데이터를 추출하고 분석한다 |
| [**claude-in-chrome-troubleshooting**](https://github.com/trailofbits/skills/tree/main/plugins/claude-in-chrome-troubleshooting) | Claude in Chrome MCP 확장 프로그램의 문제를 진단한다 |
| [**constant-time-analysis**](https://github.com/trailofbits/skills/tree/main/plugins/constant-time-analysis) | 타이밍 사이드 채널 공격 취약점을 탐지한다 |
| [**culture-index**](https://github.com/trailofbits/skills/tree/main/plugins/culture-index) | 조직 문화 관련 문서를 인덱싱하고 검색한다 |
| [**differential-review**](https://github.com/trailofbits/skills/tree/main/plugins/differential-review) | 보안 관점에서 코드 변경 사항을 분석한다 |
| [**dwarf-expert**](https://github.com/trailofbits/skills/tree/main/plugins/dwarf-expert) | DWARF 디버깅 포맷에 대한 전문 지식을 제공한다 |
| [**entry-point-analyzer**](https://github.com/trailofbits/skills/tree/main/plugins/entry-point-analyzer) | 스마트 컨트랙트의 진입점을 식별하고 분석한다 |
| [**firebase-apk-scanner**](https://github.com/trailofbits/skills/tree/main/plugins/firebase-apk-scanner) | Android APK 파일의 보안 취약점을 스캐닝한다 |
| [**fix-review**](https://github.com/trailofbits/skills/tree/main/plugins/fix-review) | 보안 감사에서 발견된 취약점의 수정 사항을 검증한다 |
| [**insecure-defaults**](https://github.com/trailofbits/skills/tree/main/plugins/insecure-defaults) | 안전하지 않은 기본 설정값을 탐지하고 경고한다 |
| [**modern-python**](https://github.com/trailofbits/skills/tree/main/plugins/modern-python) | uv, ruff, pytest 등 최신 Python 도구 사용법을 안내한다 |
| [**property-based-testing**](https://github.com/trailofbits/skills/tree/main/plugins/property-based-testing) | 속성 기반 테스트 프레임워크를 활용한 테스트를 작성한다 |
| [**semgrep-rule-creator**](https://github.com/trailofbits/skills/tree/main/plugins/semgrep-rule-creator) | 취약점 탐지를 위한 Semgrep 규칙을 생성한다 |
| [**semgrep-rule-variant-creator**](https://github.com/trailofbits/skills/tree/main/plugins/semgrep-rule-variant-creator) | Semgrep 규칙을 다른 프로그래밍 언어로 포팅한다 |
| [**sharp-edges**](https://github.com/trailofbits/skills/tree/main/plugins/sharp-edges) | 오류 발생 가능성이 높은 API를 식별하고 경고한다 |
| [**spec-to-code-compliance**](https://github.com/trailofbits/skills/tree/main/plugins/spec-to-code-compliance) | 코드가 사양 문서에 부합하는지 검증한다 |
| [**static-analysis**](https://github.com/trailofbits/skills/tree/main/plugins/static-analysis) | CodeQL, Semgrep, SARIF 도구를 활용한 정적 분석을 수행한다 |
| [**testing-handbook-skills**](https://github.com/trailofbits/skills/tree/main/plugins/testing-handbook-skills) | 퍼징과 새니타이저 도구를 활용한 테스트 기법을 제공한다 |
| [**variant-analysis**](https://github.com/trailofbits/skills/tree/main/plugins/variant-analysis) | 패턴 기반으로 코드베이스 전체에서 유사 취약점을 발견한다 |

---

## 4. 커뮤니티 에이전트 스킬

### 종합 스킬 컬렉션

| 스킬 | 설명 |
|------|------|
| [**AgentSys**](https://github.com/avifenesh/agentsys) | 플러그인, 에이전트, 스킬을 활용한 워크플로우 자동화 도구로, PR 관리·코드 정리·성능 조사·드리프트 감지·멀티에이전트 코드 리뷰를 지원한다 |
| [**Book Factory**](https://github.com/robertguss/claude-skills) | 비소설 도서 제작을 위한 전통적 출판 인프라를 복제하는 종합 스킬 파이프라인이다 |
| [**cc-devops-skills**](https://github.com/akin-ozer/cc-devops-skills) | 여러 플랫폼에 걸친 인프라스트럭처 애즈 코드를 위한 검증·생성기·셸 스크립트를 포함하는 DevOps 스킬 세트이다 |
| [**Claude Code Agents**](https://github.com/undeadlist/claude-code-agents) | 서브에이전트 프롬프트, 병렬 감사, 마이크로 체크포인트 프로토콜, 브라우저 기반 QA를 갖춘 E2E 개발 워크플로우를 제공한다 |
| [**Claude Codex Settings**](https://github.com/fcakyon/claude-codex-settings) | GitHub, Azure, MongoDB, Tavily, Playwright 통합을 포괄하는 잘 조직된 플러그인 모음이다 |
| [**Claude Mountaineering Skills**](https://github.com/dreamiurg/claude-mountaineering-skills) | 10개 이상의 산악 정보 출처에서 데이터를 수집하여 등산 루트 조사를 자동화한다 |
| [**Codex Skill**](https://github.com/skills-directory/skill-codex) | Claude Code에서 OpenAI Codex를 호출할 수 있게 하며, 모델·추론 노력·샌드박싱 등의 매개변수를 자동 추론한다 |
| [**Compound Engineering Plugin**](https://github.com/EveryInc/compound-engineering-plugin) | 실수를 개선 기회로 전환하는 실용적인 에이전트와 스킬을 제공한다 |
| [**Context Engineering Kit**](https://github.com/NeoLabHQ/context-engineering-kit) | 최소한의 토큰 사용량으로 고급 컨텍스트 엔지니어링 기법과 패턴을 구현한다 |
| [**Everything Claude Code**](https://github.com/affaan-m/everything-claude-code) | 핵심 엔지니어링 도메인을 포괄하는 독립적 가치를 지닌 종합 리소스 모음이다 |
| [**Fullstack Dev Skills**](https://github.com/jeffallan/claude-skills) | 65개 전문 스킬과 9개 프로젝트 워크플로우 커맨드를 포함하는 풀스택 개발 스킬 세트이다 |
| [**read-only-postgres**](https://github.com/jawwadfirdousi/agent-skills) | 엄격한 유효성 검증, 타임아웃, 행 제한을 갖춘 읽기 전용 PostgreSQL 쿼리 스킬이다 |
| [**Superpowers**](https://github.com/obra/superpowers) | 계획, 리뷰, 테스트, 디버깅을 포함하는 소프트웨어 엔지니어링 핵심 역량 스킬이다 |
| [**TÂCHES Claude Code Resources**](https://github.com/glittercowboy/taches-cc-resources) | skill-auditor, hook 생성 등의 메타 스킬을 포함한 균형 잡힌 서브에이전트와 스킬 모음이다 |
| [**Web Assets Generator Skill**](https://github.com/alonw0/web-asset-generator) | 파비콘, PWA 앱 아이콘, 소셜 미디어 메타 이미지 등 웹 에셋을 생성한다 |

---

## 5. 커뮤니티 개별 스킬

### 개발 도구

| 스킬 | 설명 |
|------|------|
| [**obra/superpowers**](https://github.com/obra/superpowers) | TDD, 디버깅, 협업 패턴을 포함하는 20개 이상의 실전 검증된 핵심 스킬 모음이다 |
| [**obra/superpowers-lab**](https://github.com/obra/superpowers-lab) | 정제된 기법을 사용하는 실험적 스킬 모음이다 |
| [**ios-simulator-skill**](https://github.com/conorluddy/ios-simulator-skill) | iOS 앱을 자동화를 통해 빌드하고 시뮬레이터에서 테스트한다 |
| [**playwright-skill**](https://github.com/lackeyjb/playwright-skill) | 범용 브라우저 자동화 기능을 제공한다 |
| [**claude-d3js-skill**](https://github.com/chrisvoncsefalvay/claude-d3js-skill) | D3.js를 활용한 데이터 시각화를 생성한다 |
| [**claude-scientific-skills**](https://github.com/K-Dense-AI/claude-scientific-skills) | 과학 라이브러리와 데이터베이스 작업을 지원한다 |
| [**loki-mode**](https://github.com/asklokesh/claudeskill-loki-mode) | 37개의 AI 에이전트를 조율하는 멀티에이전트 자율 스타트업 시스템이다 |
| [**Skill_Seekers**](https://github.com/yusufkaraaslan/Skill_Seekers) | 문서 웹사이트를 Claude Skills로 변환하는 도구이다 |
| [**terraform-skill**](https://github.com/antonbabenko/terraform-skill) | Terraform 인프라 코드를 작성하고 관리하는 스킬이다 |
| [**aws-skills**](https://github.com/zxkane/aws-skills) | AWS 서비스를 활용한 개발과 인프라 관리를 지원한다 |
| [**ui-skills**](https://github.com/ibelick/ui-skills) | UI 컴포넌트 개발을 위한 스킬 모음이다 |
| [**ui-ux-pro-max-skill**](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 전문 디자인 스킬을 제공한다 |
| [**threejs-skills**](https://github.com/CloudAI-X/threejs-skills) | Three.js를 활용한 3D 웹 개발을 지원한다 |
| [**swiftui-expert-skill**](https://github.com/AvdLee/SwiftUI-Agent-Skill/tree/main/swiftui-expert-skill) | SwiftUI 전문 개발 스킬을 제공한다 |
| [**swift-patterns-skill**](https://github.com/efremidze/swift-patterns-skill/tree/main/swift-patterns) | Swift 디자인 패턴을 적용하는 스킬이다 |
| [**makepad-skills**](https://github.com/ZhangHanDong/makepad-skills) | Makepad 프레임워크를 활용한 개발을 지원한다 |
| [**skill-rails-upgrade**](https://github.com/robzolkos/skill-rails-upgrade) | Rails 업그레이드를 안전하게 수행하는 스킬이다 |
| [**claude-bootstrap**](https://github.com/alinaqi/claude-bootstrap) | 프로젝트 부트스트래핑을 자동화하는 스킬이다 |
| [**dev-agent-skills**](https://github.com/fvadicamo/dev-agent-skills) | 개발 에이전트를 위한 범용 스킬 모음이다 |
| [**claude-code-startup-skills**](https://github.com/rameerez/claude-code-startup-skills) | 스타트업 프로젝트 초기 설정을 위한 스킬이다 |

### 보안

| 스킬 | 설명 |
|------|------|
| [**ffuf-web-fuzzing**](https://github.com/jthack/ffuf_claude_skill) | 침투 테스트 시 웹 퍼징을 수행하기 위한 전문 가이드를 제공한다 |
| [**clawsec**](https://github.com/prompt-security/clawsec) | 보안 분석 및 취약점 탐지 스킬을 제공한다 |
| [**security-bluebook-builder**](https://github.com/SHADOWPR0/security-bluebook-builder) | 보안 블루북을 작성하는 도구를 제공한다 |

### 마케팅 & 콘텐츠

| 스킬 | 설명 |
|------|------|
| [**marketingskills**](https://github.com/coreyhaines31/marketingskills) | 마케팅 워크플로우를 자동화하는 스킬 모음이다 |
| [**ai-marketing-skills**](https://github.com/BrianRWagner/ai-marketing-skills) | AI 기반 마케팅 전략 수립을 지원한다 |
| [**claude-seo**](https://github.com/AgriciDaniel/claude-seo) | SEO 최적화를 자동화하는 스킬이다 |
| [**content-research-writer**](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/content-research-writer) | 콘텐츠 리서치와 작성을 자동화한다 |
| [**email-marketing-bible**](https://github.com/CosmoBlk/email-marketing-bible) | 이메일 마케팅 전략과 모범 사례를 제공한다 |
| [**x-article-publisher-skill**](https://github.com/wshuyi/x-article-publisher-skill) | X(Twitter)에 기사를 발행하는 스킬이다 |

### 생산성

| 스킬 | 설명 |
|------|------|
| [**NanoBanana-PPT-Skills**](https://github.com/op7418/NanoBanana-PPT-Skills) | PowerPoint 프레젠테이션을 자동 생성하는 스킬이다 |
| [**frontend-slides**](https://github.com/zarazhangrui/frontend-slides) | 프론트엔드 기반 슬라이드를 생성하는 스킬이다 |
| [**notebooklm-skill**](https://github.com/PleasePrompto/notebooklm-skill) | NotebookLM과 연동하여 노트를 관리한다 |
| [**Youtube-clipper-skill**](https://github.com/op7418/Youtube-clipper-skill) | YouTube 영상에서 클립을 추출하는 스킬이다 |
| [**founder-skills**](https://github.com/ognjengt/founder-skills) | 스타트업 창업자를 위한 종합 스킬 모음이다 |
| [**charlie-cfo-skill**](https://github.com/EveryInc/charlie-cfo-skill) | CFO 업무를 지원하는 재무 분석 스킬이다 |
| [**linear-claude-skill**](https://github.com/wrsmith108/linear-claude-skill) | Linear 프로젝트 관리 도구와 연동한다 |
| [**claude-memory-skill**](https://github.com/hanfang/claude-memory-skill) | Claude의 메모리 관리를 강화하는 스킬이다 |
| [**ResumeSkills**](https://github.com/Paramchoudhary/ResumeSkills) | 이력서 작성과 최적화를 지원하는 스킬이다 |

### 컨텍스트 엔지니어링

| 스킬 | 설명 |
|------|------|
| [**context-fundamentals**](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) | 컨텍스트 엔지니어링의 기본 원칙을 제공한다 |
| [**context-degradation**](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) | 컨텍스트 성능 저하를 분석하고 대응한다 |
| [**context-compression**](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) | 컨텍스트를 효율적으로 압축하는 기법을 제공한다 |
| [**context-optimization**](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization) | 컨텍스트 활용을 최적화하는 전략을 제공한다 |
| [**multi-agent-patterns**](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns) | 멀티에이전트 컨텍스트 패턴을 설계한다 |
| [**memory-systems**](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems) | 에이전트 메모리 시스템을 설계하고 구현한다 |

### n8n 자동화

| 스킬 | 설명 |
|------|------|
| [**n8n-code-javascript**](https://github.com/czlonkowski/n8n-skills/tree/main/skills/n8n-code-javascript) | n8n에서 JavaScript 코드 노드를 작성한다 |
| [**n8n-code-python**](https://github.com/czlonkowski/n8n-skills/tree/main/skills/n8n-code-python) | n8n에서 Python 코드 노드를 작성한다 |
| [**n8n-workflow-patterns**](https://github.com/czlonkowski/n8n-skills/tree/main/skills/n8n-workflow-patterns) | n8n 워크플로우 설계 패턴을 적용한다 |
| [**n8n-mcp-tools-expert**](https://github.com/czlonkowski/n8n-skills/tree/main/skills/n8n-mcp-tools-expert) | n8n에서 MCP 도구를 전문적으로 활용한다 |

### 특수 도메인

| 스킬 | 설명 |
|------|------|
| [**apple-hig-skills**](https://github.com/raintree-technology/apple-hig-skills) | Apple Human Interface Guidelines를 적용한 디자인을 지원한다 |
| [**claude-skill-homeassistant**](https://github.com/komal-SkyNET/claude-skill-homeassistant) | Home Assistant 스마트홈 자동화를 지원한다 |
| [**awesome-legal-skills**](https://github.com/lawvable/awesome-legal-skills) | 법률 문서 작성과 분석을 지원하는 스킬 모음이다 |
| [**AI-research-SKILLs**](https://github.com/zechenzhangAGI/AI-research-SKILLs) | AI 연구를 지원하는 스킬 모음이다 |
| [**Claude-Ally-Health**](https://github.com/huifer/Claude-Ally-Health) | 건강 관련 정보 제공을 지원하는 스킬이다 |
| [**materials-simulation-skills**](https://github.com/HeshamFS/materials-simulation-skills) | 재료 과학 시뮬레이션을 지원하는 스킬이다 |

---

## 6. 워크플로우 & 지식 가이드

### 개발 워크플로우

| 워크플로우 | 설명 |
|------------|------|
| [**AB Method**](https://github.com/ayoubben18/ab-method) | 스펙 기반 워크플로우로, 대규모 문제를 전문 서브에이전트를 활용한 집중적이고 점진적인 미션으로 변환한다 |
| [**Agentic Workflow Patterns**](https://github.com/ThibautMelen/agentic-workflow-patterns) | Mermaid 다이어그램을 포함하는 종합 컬렉션으로, 서브에이전트 오케스트레이션·병렬 도구 호출 등의 패턴을 다룬다 |
| [**Claude Code PM**](https://github.com/automazeio/ccpm) | Claude Code를 위한 포괄적이고 기능이 풍부한 프로젝트 관리 워크플로우이다 |
| [**Claude CodePro**](https://github.com/maxritter/claude-codepro) | 스펙 기반 워크플로우, TDD 적용, 크로스 세션 메모리, 시맨틱 검색을 갖춘 전문 개발 환경이다 |
| [**Context Priming**](https://github.com/disler/just-prompt) | 다양한 프로젝트 시나리오에 맞는 전문 커맨드를 통한 체계적 컨텍스트 프라이밍 접근법이다 |
| [**Design Review Workflow**](https://github.com/OneRedOak/claude-code-workflows) | 전문 서브에이전트를 활용한 자동화된 UI/UX 디자인 리뷰 워크플로우이다 |
| [**RIPER Workflow**](https://github.com/tony/claude-code-riper-5) | Research·Innovate·Plan·Execute·Review 단계를 강제하는 구조화된 개발 워크플로우이다 |
| [**Simone**](https://github.com/Helmi/claude-simone) | 문서, 가이드라인, 프로세스를 포괄하는 광범위한 프로젝트 관리 워크플로우이다 |
| [**n8n_agent**](https://github.com/kingler/n8n_agent) | 코드 분석, QA, 디자인, 문서화, 최적화를 위한 종합 커맨드 세트를 제공한다 |
| [**Project Bootstrapping**](https://github.com/steadycursor/steadystart) | 새 프로젝트의 부트스트래핑과 태스크 관리를 위한 구조화된 커맨드를 제공한다 |
| [**ScopeCraft Command**](https://github.com/scopecraft/command) | SDLC 전 과정을 포괄하는 프로젝트 관리, 구현, 계획, 릴리스 커맨드이다 |

### Ralph Wiggum 기법

| 리소스 | 설명 |
|--------|------|
| [**awesome-ralph**](https://github.com/snwfdhmp/awesome-ralph) | Ralph 기법에 대한 큐레이션된 리소스 목록이다 |
| [**Ralph for Claude Code**](https://github.com/frankbria/ralph-claude-code) | 안전 장치를 갖추고 Claude Code가 완료될 때까지 반복 작업하도록 하는 자율 프레임워크이다 |
| [**Ralph Wiggum Marketer**](https://github.com/muratcankoylan/ralph-wiggum-marketer) | Ralph 루프와 맞춤형 지식 베이스를 통합하는 자율 AI 카피라이터 플러그인이다 |
| [**ralph-orchestrator**](https://github.com/mikeyobrien/ralph-orchestrator) | 견고한 오케스트레이션을 갖춘 자율 작업 완료를 위한 Ralph Wiggum 기법을 구현한다 |
| [**ralph-wiggum-bdd**](https://github.com/marcindulak/ralph-wiggum-bdd) | Ralph Wiggum 루프를 활용한 행동 주도 개발(BDD)용 독립형 Bash 스크립트이다 |
| [**The Ralph Playbook**](https://github.com/ClaytonFarr/ralph-playbook) | Ralph Wiggum 기법에 대한 상세하고 포괄적인 가이드이다 |

### 지식 가이드

| 가이드 | 설명 |
|--------|------|
| [**Claude Code Documentation Mirror**](https://github.com/ericbuess/claude-code-docs) | 수 시간마다 업데이트되는 Anthropic 공식 문서의 미러이다 |
| [**Claude Code Handbook**](https://nikiforovall.blog/claude-code-rules/) | 개발 워크플로우를 위한 모범 사례, 팁, 기법 모음이다 |
| [**Claude Code Infrastructure Showcase**](https://github.com/diet103/claude-code-infrastructure-showcase) | Hook을 사용하여 적절한 스킬을 지능적으로 선택하고 활성화하는 혁신적 접근 방식이다 |
| [**Claude Code System Prompts**](https://github.com/Piebald-AI/claude-code-system-prompts) | 버전별로 업데이트되는 시스템 프롬프트, 내장 도구 설명, 서브에이전트 프롬프트 전체를 수록한다 |
| [**Claude Code Tips**](https://github.com/ykdojo/claude-code-tips) | 음성 입력, 컨테이너 워크플로우, 멀티모델 오케스트레이션 등 35개 이상의 팁을 제공한다 |
| [**Claude Code Ultimate Guide**](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | 초보자부터 파워 유저까지 아우르는 프로덕션 레디 템플릿을 포함한 종합 가이드이다 |
| [**Learn Claude Code**](https://github.com/shareAI-lab/learn-claude-code) | 코딩 에이전트를 기본 구성 요소로 분해하여 최소한의 코드로 재구성하는 분석 자료이다 |
| [**Claude Code Repos Index**](https://github.com/danielrosehill/Claude-Code-Repos-Index) | 75개 이상의 Claude Code 리포지토리를 CMS, 시스템 설계, 연구 등으로 분류한 인덱스이다 |

---

## 7. 도구 (Tooling)

### 세션 & 유틸리티

| 도구 | 설명 |
|------|------|
| [**cc-sessions**](https://github.com/GWUDCAP/cc-sessions) | Claude Code로 생산적인 개발을 위한 체계적 세션 관리 접근 방식을 제공한다 |
| [**cc-tools**](https://github.com/Veraticus/cc-tools) | 스마트 린팅과 테스팅을 갖춘 Hook 및 유틸리티의 고성능 Go 구현체이다 |
| [**ccexp**](https://github.com/nyatinte/ccexp) | 설정 파일과 슬래시 커맨드를 탐색하고 관리하는 대화형 CLI 도구이다 |
| [**cchistory**](https://github.com/eckardt/cchistory) | Claude Code 세션의 Bash 명령어 히스토리를 참조할 수 있는 도구이다 |
| [**cclogviewer**](https://github.com/Brads3290/cclogviewer) | Claude Code의 `.jsonl` 대화 파일을 HTML UI로 열람하는 유틸리티이다 |
| [**Claude Session Restore**](https://github.com/ZENG3LD/claude-session-restore) | 세션 파일과 git 히스토리를 활용하여 이전 세션의 컨텍스트를 복원한다 |
| [**claude-code-tools**](https://github.com/pchalasani/claude-code-tools) | 세션 연속성, 빠른 전문 검색, 크로스 에이전트 핸드오프를 위한 도구 세트이다 |
| [**claudekit**](https://github.com/carlrannaberg/claudekit) | 자동 저장 체크포인팅, 코드 품질 훅, 20개 이상의 전문 서브에이전트를 제공하는 CLI 툴킷이다 |
| [**recall**](https://github.com/zippoxer/recall) | 터미널 UI를 통해 Claude Code 세션을 전문 검색하는 도구이다 |
| [**Vibe-Log**](https://github.com/vibe-log/vibe-log-cli) | 프롬프트를 로컬에서 분석하고 HTML 리포트를 생성하는 세션 분석 도구이다 |

### 컨테이너 & 환경

| 도구 | 설명 |
|------|------|
| [**Container Use**](https://github.com/dagger/container-use) | 코딩 에이전트가 안전하고 독립적으로 작업할 수 있는 개발 환경을 제공한다 |
| [**run-claude-docker**](https://github.com/icanhasjonas/run-claude-docker) | 워크스페이스를 격리된 컨테이너로 전달하는 자체 완결형 Docker 실행기이다 |
| [**viwo-cli**](https://github.com/OverseedAI/viwo) | git worktree와 Docker를 활용하여 Claude Code를 안전하게 실행하는 CLI이다 |

### 설정 & 프레임워크

| 도구 | 설명 |
|------|------|
| [**Claude Code Templates**](https://github.com/davila7/claude-code-templates) | 사용량 대시보드, 분석, 다양한 리소스 카테고리를 갖춘 세련된 템플릿 모음이다 |
| [**claude-starter-kit**](https://github.com/serpro69/claude-starter-kit) | 사전 구성된 MCP 서버와 도구를 포함하는 스타터 템플릿이다 |
| [**ContextKit**](https://github.com/FlineDev/ContextKit) | Claude Code를 4단계 계획 프레임워크로 능동적 파트너로 변환한다 |
| [**Rulesync**](https://github.com/dyoshikawa/rulesync) | 다양한 AI 코딩 에이전트용 설정을 자동 생성하는 Node.js CLI이다 |
| [**SuperClaude**](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 전문 커맨드와 인지 페르소나를 갖춘 다재다능한 설정 프레임워크이다 |
| [**ClaudeCTX**](https://github.com/foxj77/claudectx) | 단일 명령으로 전체 Claude Code 설정을 전환하는 도구이다 |
| [**claude-rules-doctor**](https://github.com/nulone/claude-rules-doctor) | 경로 glob이 실제 리포 파일과 일치하는지 확인하여 죽은 `.claude/rules/` 파일을 탐지하는 CLI이다 |
| [**tweakcc**](https://github.com/Piebald-AI/tweakcc) | Claude Code 스타일링을 커스터마이징하는 커맨드 라인 도구이다 |

### IDE 통합

| 도구 | 설명 |
|------|------|
| [**Claude Code Chat**](https://marketplace.visualstudio.com/items?itemName=AndrePimenta.claude-code-chat) | VS Code에서 Claude Code와 대화할 수 있는 세련된 인터페이스이다 |
| [**claude-code-ide.el**](https://github.com/manzaltu/claude-code-ide.el) | ediff 기반 코드 제안과 LSP 진단을 제공하는 Emacs 통합이다 |
| [**claude-code.el**](https://github.com/stevemolitor/claude-code.el) | Claude Code CLI를 위한 Emacs 인터페이스이다 |
| [**claude-code.nvim**](https://github.com/greggh/claude-code.nvim) | Claude Code와 Neovim 간의 원활한 통합을 제공한다 |
| [**Claudix**](https://github.com/Haleclipse/Claudix) | 채팅 인터페이스, 세션 관리, 터미널 실행을 갖춘 VS Code 확장이다 |

### 사용량 모니터

| 도구 | 설명 |
|------|------|
| [**CC Usage**](https://github.com/ryoppippi/ccusage) | Claude Code 사용량을 관리하고 분석하는 대시보드가 포함된 CLI 도구이다 |
| [**ccflare**](https://github.com/snipeship/ccflare) | 종합적인 메트릭과 웹 UI를 갖춘 Claude Code 사용량 대시보드이다 |
| [**better-ccflare**](https://github.com/tombii/better-ccflare/) | 성능 향상과 확장된 프로바이더 지원을 갖춘 ccflare의 개선된 포크이다 |
| [**Claude Code Usage Monitor**](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 토큰 사용량과 소모율을 실시간으로 모니터링하는 터미널 기반 도구이다 |
| [**Claudex**](https://github.com/kunwar-shah/claudex) | 전문 검색을 지원하는 웹 기반 Claude Code 대화 히스토리 브라우저이다 |
| [**viberank**](https://github.com/sculptdotfun/viberank) | Claude Code 사용 통계를 시각화하는 커뮤니티 기반 리더보드 도구이다 |

### 음성 & 멀티미디어

| 도구 | 설명 |
|------|------|
| [**VoiceMode MCP**](https://github.com/mbailey/voicemode) | OpenAI API 호환 음성 서비스를 지원하는 자연스러운 음성 대화를 제공한다 |
| [**stt-mcp-server-linux**](https://github.com/marcindulak/stt-mcp-server-linux) | Linux에서 Python MCP 서버를 사용한 푸시 투 토크 음성 전사 설정이다 |
| [**Claude Composer**](https://github.com/possibilities/claude-composer) | Claude Code에 작은 기능 향상을 추가하는 도구이다 |
| [**Claude Hub**](https://github.com/claude-did-this/claude-hub) | Claude Code를 GitHub 리포지토리에 연결하는 Webhook 서비스이다 |

---

## 8. 오케스트레이터

| 오케스트레이터 | 설명 |
|----------------|------|
| [**Auto-Claude**](https://github.com/AndyMik90/Auto-Claude) | 칸반 스타일 UI와 함께 전체 SDLC를 통합하는 자율 멀티에이전트 프레임워크이다 |
| [**Claude Code Flow**](https://github.com/ruvnet/claude-code-flow) | 재귀적 에이전트 사이클에 걸친 자율 코드 작업을 위한 코드 퍼스트 오케스트레이션 레이어이다 |
| [**Claude Squad**](https://github.com/smtg-ai/claude-squad) | 별도의 워크스페이스에서 여러 Claude Code 인스턴스를 관리하는 터미널 앱이다 |
| [**Claude Swarm**](https://github.com/parruda/claude-swarm) | Claude Code 에이전트 군집에 연결된 Claude Code를 실행한다 |
| [**Claude Task Master**](https://github.com/eyaltoledano/claude-task-master) | Cursor AI 통합을 지원하는 AI 기반 개발을 위한 태스크 관리 시스템이다 |
| [**Claude Task Runner**](https://github.com/grahama1970/claude-task-runner) | 컨텍스트 격리와 집중된 태스크 실행을 관리하는 전문 도구이다 |
| [**Happy Coder**](https://github.com/slopus/happy) | 휴대폰이나 데스크톱에서 여러 Claude Code를 병렬로 생성하고 제어한다 |
| [**The Agentic Startup**](https://github.com/rsmdt/the-startup) | 종합 에이전트와 커맨드를 갖춘 또 하나의 Claude 오케스트레이터이다 |
| [**TSK**](https://github.com/dtormoen/tsk) | Docker 샌드박스 환경에서 AI 에이전트에게 작업을 위임하는 Rust CLI 태스크 매니저이다 |

---

## 9. Hooks

| 훅 | 설명 |
|----|------|
| [**Britfix**](https://github.com/Talieisin/britfix) | 미국식 철자를 영국식 영어로 변환하는 컨텍스트 인식 훅으로, 자동 변환을 수행한다 |
| [**CC Notify**](https://github.com/dazuiba/CCNotify) | 입력 필요 또는 작업 완료 시 데스크톱 알림을 보내며, VS Code 점프백 기능을 지원한다 |
| [**cchooks**](https://github.com/GowayLee/cchooks) | 깔끔한 API로 훅 작성과 통합을 단순화하는 경량 Python SDK이다 |
| [**Claude Code Hook Comms (HCOM)**](https://github.com/aannoo/claude-hook-comms) | Claude Code 서브에이전트 간 실시간 통신을 위한 경량 CLI이다 |
| [**claude-code-hooks-sdk**](https://github.com/beyondcode/claude-hooks-sdk) | 유려한 API를 갖춘 Laravel 스타일의 PHP SDK로, 훅 응답을 빌드한다 |
| [**claude-hooks**](https://github.com/johnlindquist/claude-hooks) | TypeScript 기반의 Claude Code 훅 설정 및 커스터마이징 시스템이다 |
| [**Claudio**](https://github.com/ctoth/claudio) | Claude Code 훅 확장 도구이다 |
| [**TDD Guard**](https://github.com/nizos/tdd-guard) | TDD 워크플로우를 강제하는 테스트 가드 훅이다 |
| [**TypeScript Quality Hooks**](https://github.com/bartolli/claude-code-typescript-hooks) | TypeScript 코드 품질을 보장하는 훅 모음이다 |

---

## 10. 슬래시 커맨드

### 버전 관리 & Git

| 커맨드 | 설명 |
|--------|------|
| [**/commit**](https://github.com/evmts/tevm-monorepo) | 모범 사례를 적용한 git 커밋을 수행한다 |
| [**/commit-fast**](https://github.com/steadycursor/steadystart) | 빠른 커밋을 수행한다 |
| [**/create-pr**](https://github.com/toyamarinyon/giselle) | 풀 리퀘스트를 자동으로 생성한다 |
| [**/create-pull-request**](https://github.com/liam-hq/liam) | 풀 리퀘스트 생성을 위한 대안 커맨드이다 |
| [**/create-worktrees**](https://github.com/evmts/tevm-monorepo) | git worktree를 생성한다 |
| [**/fix-github-issue**](https://github.com/jeremymailen/kotlinter-gradle) | GitHub 이슈를 분석하고 수정한다 |
| [**/husky**](https://github.com/evmts/tevm-monorepo) | Husky git 훅을 설정하고 관리한다 |

### 코드 분석 & 테스트

| 커맨드 | 설명 |
|--------|------|
| [**/code_analysis**](https://github.com/kingler/n8n_agent) | 코드를 체계적으로 분석한다 |
| [**/optimize**](https://github.com/to4iki/ai-project-rules) | 코드 최적화를 수행한다 |
| [**/tdd**](https://github.com/zscott/pane) | TDD 방식으로 개발을 수행한다 |
| [**/tdd-implement**](https://github.com/jerseycheese/Narraitor) | TDD 기반 구현을 수행한다 |

### 문서화 & 기타

| 커맨드 | 설명 |
|--------|------|
| [**/add-to-changelog**](https://github.com/berrydev-ai/blockdoc-python) | CHANGELOG에 항목을 추가한다 |
| [**/create-docs**](https://github.com/jerseycheese/Narraitor) | 문서를 자동으로 생성한다 |
| [**/context-prime**](https://github.com/elizaOS/elizaos.github.io) | 프로젝트 컨텍스트를 프라이밍한다 |
| [**/run-ci**](https://github.com/hackdays-io/toban-contribution-viewer) | CI 파이프라인을 실행한다 |
| [**/prd-generator**](https://github.com/dredozubov/prd-generator) | PRD(Product Requirements Document)를 생성한다 |
| [**/todo**](https://github.com/chrisleyva/todo-slash-command) | 할 일 목록을 관리한다 |

---

## 11. Status Line

| 도구 | 설명 |
|------|------|
| [**CCometixLine**](https://github.com/Haleclipse/CCometixLine) | Rust로 작성된 고성능 Claude Code 상태표시줄 도구로, Git 통합을 지원한다 |
| [**ccstatusline**](https://github.com/sirmalloc/ccstatusline) | 모델 정보와 토큰 사용량을 표시하는 고도로 커스터마이징 가능한 상태표시줄 포매터이다 |
| [**claude-code-statusline**](https://github.com/rz1989s/claude-code-statusline) | 테마, 비용 추적, MCP 서버 모니터링을 갖춘 강화된 4라인 상태표시줄이다 |
| [**claude-powerline**](https://github.com/Owloops/claude-powerline) | 실시간 사용량 추적과 git 통합을 갖춘 Vim 스타일 파워라인 상태표시줄이다 |
| [**claudia-statusline**](https://github.com/hagan/claudia-statusline) | 영구 통계, 프로그레스 바, 선택적 클라우드 동기화를 지원하는 고성능 Rust 기반 상태표시줄이다 |

---

## 12. CLAUDE.md 파일 모음

### 언어별

| 프로젝트 | 설명 |
|----------|------|
| [**AI IntelliJ Plugin**](https://github.com/didalgolab/ai-intellij-plugin) | IntelliJ 플러그인 개발용 CLAUDE.md이다 |
| [**LangGraphJS**](https://github.com/langchain-ai/langgraphjs) | LangGraph JavaScript 프로젝트용 CLAUDE.md이다 |
| [**SPy**](https://github.com/spylang/spy) | SPy 언어 프로젝트용 CLAUDE.md이다 |

### 도메인별

| 프로젝트 | 설명 |
|----------|------|
| [**Comm**](https://github.com/CommE2E/comm) | 커뮤니케이션 앱 프로젝트용 CLAUDE.md이다 |
| [**Course Builder**](https://github.com/badass-courses/course-builder) | 온라인 강좌 빌더 프로젝트용 CLAUDE.md이다 |
| [**Network Chronicles**](https://github.com/Fimeg/NetworkChronicles) | 네트워크 관련 프로젝트용 CLAUDE.md이다 |
| [**Pareto Mac**](https://github.com/ParetoSecurity/pareto-mac) | macOS 보안 앱 프로젝트용 CLAUDE.md이다 |
| [**SteadyStart**](https://github.com/steadycursor/steadystart) | 프로젝트 스캐폴딩용 CLAUDE.md이다 |

### 프로젝트 스캐폴딩 & MCP

| 프로젝트 | 설명 |
|----------|------|
| [**Basic Memory**](https://github.com/basicmachines-co/basic-memory) | 메모리 관리 시스템용 CLAUDE.md이다 |
| [**claude-code-mcp-enhanced**](https://github.com/grahama1970/claude-code-mcp-enhanced) | 강화된 MCP 설정용 CLAUDE.md이다 |

---

## 대체 클라이언트

| 클라이언트 | 설명 |
|------------|------|
| [**Claudable**](https://github.com/opactorai/Claudable) | Claude Code의 대체 데스크톱 클라이언트이다 |
| [**crystal**](https://github.com/stravu/crystal) | Claude Code의 대체 인터페이스이다 |

---

## 공식 문서

| 리소스 | 설명 |
|--------|------|
| [**Anthropic Documentation**](https://docs.claude.com/en/home) | Claude Code 공식 문서이다 |
| [**Anthropic Quickstarts**](https://github.com/anthropics/claude-quickstarts) | Claude 퀵스타트 가이드이다 |
| [**Claude Code GitHub Actions**](https://github.com/anthropics/claude-code-action) | Claude Code GitHub Actions 통합이다 |

---

## 참고 링크

| 리포지토리 | 설명 |
|------------|------|
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Claude Skills 큐레이션 목록 (공식 + 커뮤니티) |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code 생태계 종합 리소스 |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 380개 이상의 에이전트 스킬 (기업 팀 + 커뮤니티) |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Claude Skills 큐레이션 목록 |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | 135개 에이전트, 35개 스킬, 42개 커맨드를 포함하는 최대 규모 툴킷 |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50개 이상의 검증된 스킬 모음 |
