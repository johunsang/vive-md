# AI 코딩 도구 실전 사용법

> Claude Code, Kimi CLI/Codex, Codex CLI의 모델별 상세 사용법 가이드
> 
> 작성일: 2026-02-22

---

## 목차

1. [Claude Code 상세 사용법](#1-claude-code-상세-사용법)
2. [Kimi Code (Kimi CLI) 상세 사용법](#2-kimi-code-kimi-cli-상세-사용법)
3. [Codex CLI 상세 사용법](#3-codex-cli-상세-사용법)
4. [도구별 비교 및 선택 가이드](#4-도구별-비교-및-선택-가이드)

---

## 1. Claude Code 상세 사용법

### 1.1 설치 및 기본 설정

#### 설치 방법

```bash
# macOS / Linux (권장)
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Windows CMD
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

# Homebrew (macOS/Linux)
brew install --cask claude-code

# WinGet (Windows)
winget install Anthropic.ClaudeCode

# NPM (Deprecated - 권장하지 않음)
npm install -g @anthropic-ai/claude-code
```

#### 설치 확인

```bash
claude --version
```

### 1.2 모델별 사용법

Claude Code는 세 가지 주요 모델을 지원합니다:

| 모델 | 사용법 | 특징 | 사용 시점 |
|------|--------|------|-----------|
| **Claude Sonnet 4.6** | 기본 모델 | 균형 잡힌 성능과 속도 | 일반적인 코딩 작업 |
| **Claude Opus 4.5/4.6** | `--model opus` | 최고 성능, 복잡한 추론 | 복잡한 아키텍처, 리팩토링 |
| **Claude Haiku** | `--model haiku` | 빠른 응답, 저렴한 비용 | 간단한 작업, 빠른 피드백 |

#### 모델 전환 명령어

```bash
# 기본 실행 (Sonnet)
claude

# 특정 모델 지정
claude --model opus
claude --model sonnet
claude --model haiku

# 실행 중 모델 전환 (대화 모드에서)
/model
# 또는
Alt+P (Win/Linux) / Option+P (macOS)
```

#### Fast Mode (Opus 4.6 전용)

```bash
# Fast Mode 활성화 (2.5x 빠른 응답, 높은 비용)
/fast

# 또는 실행 시
claude --model opus --fast
```

**Fast Mode 가격** (per MTok):

| 모드 | Input (<200K) | Output | Input (>200K) | Output |
|------|---------------|--------|---------------|--------|
| Standard Opus 4.6 | $15 | $75 | $15 | $75 |
| Fast Mode | $30 | $150 | $60 | $225 |

### 1.3 실행 모드

#### 인터랙티브 모드 (기본)

```bash
# 기본 인터랙티브 모드
claude

# 특정 디렉토리에서 시작
claude --cwd /path/to/project

# 이전 세션 계속
claude --continue

# 특정 세션 복구
claude --resume <session-id>
```

#### Print 모드 (비대화형)

```bash
# 단일 명령 실행 후 종료
claude -p "fix the login bug"
claude --print "explain this function"

# 파이프 입력
echo "refactor this code" | claude -p

# JSON 출력
claude -p "analyze codebase" --output-format json

# 예산 제한
claude -p --max-budget-usd 5.00 "run tests"

# 턴 수 제한
claude -p --max-turns 3 "simple task"
```

#### 원격 세션 (Claude.ai 구독자)

```bash
# 웹 세션 생성
claude --remote "fix the login bug"

# 웹 세션을 로컬로 가져오기
claude --teleport
```

### 1.4 슬래시 명령어 (/commands)

#### 세션 관리

| 명령어 | 설명 |
|--------|------|
| `/help` | 사용 가능한 명령어 표시 |
| `/clear` | 현재 대화 컨텍스트 지우기 |
| `/compact` | 토큰 절약을 위해 대화 압축 |
| `/compact "keep auth work"` | 특정 컨텍스트 유지하며 압축 |
| `/exit` 또는 `/quit` | Claude Code 종료 |
| `/status` | 현재 세션 상태 표시 |

#### 파일 및 코드 작업

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `/add <파일>` | 파일을 대화 컨텍스트에 추가 | `/add src/auth.ts` |
| `/drop <파일>` | 컨텍스트에서 파일 제거 | `/drop src/old.ts` |
| `/files` | 현재 컨텍스트의 모든 파일 목록 | - |
| `/diff` | 보류 중인 변경사항 표시 | - |
| `/undo` | 마지막 파일 변경 취소 | - |

#### Git 통합

| 명령어 | 설명 |
|--------|------|
| `/commit` | AI 생성 메시지로 git 커밋 생성 |
| `/pr` | Pull Request 생성 |
| `/branch <이름>` | 새 브랜치 생성 및 전환 |

#### 모드 전환

| 명령어 | 설명 |
|--------|------|
| `/chat` | 파일 편집 없는 순수 채팅 모드 |
| `/code` | 코드 편집 모드 |
| `/plan` | 복잡한 작업을 위한 계획 모드 |

#### 고급 명령어

| 명령어 | 설명 |
|--------|------|
| `/config` | 설정 열기 |
| `/model` | Claude 모델 전환 |
| `/cost` | 토큰 사용량 및 비용 추정 표시 |
| `/history` | 대화 기록 보기 |
| `/resume` | 이전 세션 복구 |
| `/checkpoint` | 롤백 체크포인트 생성 |
| `/rollback` | 이전 체크포인트로 롤백 |
| `/bashes` | 백그라운드 프로세스 목록 |
| `/kill <id>` | 백그라운드 프로세스 중지 |

### 1.5 Thinking Mode (추론 모드)

```bash
# Thinking Mode 토글
Alt+T (Win/Linux) / Option+T (macOS)

# 또는 Tab 키 (고정 토글)
Tab

# 자연어로 활성화
> "think about this problem"
> "think harder about the architecture"
> "ultrathink about this security issue"
```

**Thinking 레벨:**

| 트리거 | Thinking Budget | 사용 사례 |
|--------|-----------------|-----------|
| `think` | Standard | 일반적인 추론, 코드 분석 |
| `think harder` | Extended | 복잡한 문제, 다양한 접근법 |
| `ultrathink` | Maximum | 중요한 결정, 심층 아키텍처 분석 |

### 1.6 Plan Mode (계획 모드)

```bash
# Plan Mode 진입
/plan

# 또는 Claude가 제안
> "Implement a complete authentication system"
# Claude: "This is a complex task. Would you like me to create a plan first?"
```

**Plan Mode 특징:**
- Opus로 계획 수립, Sonnet으로 실행
- SonnetPlan Mode: Sonnet으로 계획, Haiku로 실행 (비용 효율)
- Shift+Tab: Plan Mode에서 자동 편집 수락
- 계획은 `/clear` 후에도 지속됨

### 1.7 백그라운드 작업 및 에이전트

```bash
# 백그라운드로 명령 실행
Ctrl+B

# 또는 & 접두사 사용
> "& npm run dev"
> "& python manage.py runserver"

# 백그라운드 에이전트 실행
> "Have an Explore agent analyze the codebase architecture in background"

# 백그라운드 작업 보기
/tasks
/bashes

# 백그라운드 작업 종료
/kill <task-id>
```

### 1.8 키보드 단축키

#### 탐색 및 편집

| 단축키 | 동작 |
|--------|------|
| `Ctrl+R` | 명령어 기록 검색 |
| `Ctrl+O` | 트랜스크립트 보기 (thinking 블록 포함) |
| `Ctrl+G` | 시스템 텍스트 에디터에서 프롬프트 편집 |
| `Ctrl+Y` | Readline-style 붙여넣기 |
| `Alt+Y` | Yank-pop (kill ring 순환) |
| `Ctrl+B` | 현재 명령/에이전트 백그라운드 실행 |
| `Ctrl+Z` | 일시 중지/실행 취소 |

#### 모델 및 모드 전환

| 단축키 | 동작 |
|--------|------|
| `Alt+P` / `Option+P` | 입력 중 모델 전환 |
| `Alt+T` / `Option+T` | Thinking Mode 토글 |
| `Tab` | Thinking 토글 (고정) / 제안 수락 |
| `Shift+Tab` | 자동 편집 수락 (Plan Mode) / 모드 전환 (Windows) |

#### 입력 및 제출

| 단축키 | 동작 |
|--------|------|
| `Enter` | 프롬프트 제출 / 제안 즉시 수락 |
| `Shift+Enter` | 새 줄 (iTerm2, WezTerm, Ghostty, Kitty에서 작동) |

#### 이미지 및 파일 처리

| 단축키 | 동작 |
|--------|------|
| `Cmd+V` (macOS) / `Alt+V` (Windows) | 클립보드에서 이미지 붙여넣기 |
| `Cmd+N` / `Ctrl+N` | 새 대화 (VSCode) |

### 1.9 핵심 도구 (Core Tools)

| 도구 | 목적 | 권한 필요 |
|------|------|-----------|
| **Read** | 파일, 이미지, PDF 읽기 | 아니오 |
| **Write** | 새 파일 생성 | 예 |
| **Edit** | 기존 파일 수정 | 예 |
| **Bash** | 셸 명령 실행 | 예 |
| **Grep** | 정규식으로 콘텐츠 검색 | 아니오 |
| **Glob** | 패턴으로 파일 찾기 | 아니오 |
| **TodoWrite** | 작업 관리 | 아니오 |
| **Task** | 서브 에이전트 실행 | 아니오 |
| **WebFetch** | 웹 콘텐츠 가져오기 | 예 |
| **WebSearch** | 웹 검색 | 예 |
| **NotebookEdit** | Jupyter 노트북 편집 | 예 |
| **NotebookRead** | Jupyter 노트북 읽기 | 아니오 |
| **LSP** | 코드 인텔리전스 (go-to-definition 등) | 아니오 |

### 1.10 환경 변수

```bash
# 핵심 설정
export ANTHROPIC_API_KEY="your-api-key"
export CLAUDE_CODE_MODEL="sonnet"  # 기본 모델
export CLAUDE_CODE_CONFIG="/path/to/config"

# 디스플레이 및 UI
export CLAUDE_CODE_HIDE_ACCOUNT_INFO="1"

# Bash 및 명령어
export BASH_DEFAULT_TIMEOUT_MS="120000"
export BASH_MAX_TIMEOUT_MS="600000"

# 모델 설정
export ANTHROPIC_DEFAULT_SONNET_MODEL="claude-sonnet-4-6"
export ANTHROPIC_DEFAULT_OPUS_MODEL="claude-opus-4-6"
export MAX_THINKING_TOKENS="31999"

# 고급 기능
export CLAUDE_CODE_DISABLE_AUTO_MEMORY="1"  # 자동 메모리 비활성화
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS="1"  # 에이전트 팀 활성화
export CLAUDE_CODE_ENABLE_TELEMETRY="1"  # OpenTelemetry 수집 활성화
```

### 1.11 설정 파일 (settings.json)

```json
{
  "permissions": {
    "defaultMode": "ask",
    "allow": {
      "Bash": ["git status", "git diff", "git log", "npm test", "npm run*"],
      "Read": {},
      "Edit": {}
    },
    "deny": {
      "Write": ["*.env", ".env.*", ".git/*"],
      "Edit": ["*.env", ".env.*"]
    },
    "additionalDirectories": [
      "/path/to/other/project"
    ]
  },
  "language": "ko",
  "attribution": true,
  "respectGitignore": true,
  "showTurnDuration": true,
  "prefersReducedMotion": false,
  "fastMode": false,
  "plansDirectory": ".claude/plans"
}
```

### 1.12 실전 사용 예시

```bash
# 1. 프로젝트 분석
claude
> "Read the codebase and explain the project structure"

# 2. 특정 모델로 복잡한 리팩토링
claude --model opus
> "Refactor the authentication system to use JWT tokens"

# 3. 비용 제한된 자동화 작업
claude -p --max-budget-usd 10.00 --output-format json "analyze security issues"

# 4. 백그라운드에서 테스트 실행
> "& npm run test:watch"

# 5. 계획 모드로 신규 기능 개발
/plan
> "Implement a complete user management system with CRUD operations"

# 6. Git 워크플로우
> "Create a git commit for these changes"
> "/pr"

# 7. MCP 서버 사용
/mcp list
/mcp connect <server-name>
```

---

## 2. Kimi Code (Kimi CLI) 상세 사용법

### 2.1 개요

**Kimi Code**는 Moonshot AI가 개발한 AI 코딩 에이전트로, 터미널 기반 CLI 도구와 웹 인터페이스를 제공합니다. Kimi K2.5 모델을 기반으로 하며, 비전(이미지/비디오) 기반 코딩과 Agent Swarm(다중 에이전트) 기능이 특징입니다.

**제품 구성:**
- **Kimi Code CLI** - 터미널 기반 코딩 에이전트
- **Kimi Web** - 웹 인터페이스 (kimi.com)
- **Kimi API** - 개발자 API (platform.moonshot.ai)

### 2.2 설치 및 기본 설정

#### 설치 방법

```bash
# macOS / Linux (권장)
curl -LsSf https://code.kimi.com/install.sh | bash

# Windows (PowerShell)
Invoke-RestMethod https://code.kimi.com/install.ps1 | Invoke-Expression

# uv를 통한 설치 (이미 uv가 설치된 경우)
uv tool install --python 3.13 kimi-cli
```

#### 설치 확인

```bash
kimi --version
# -> kimi, version 1.6
```

#### 업그레이드 및 제거

```bash
# 업그레이드
uv tool upgrade kimi-cli --no-cache

# 제거
uv tool uninstall kimi-cli
```

### 2.3 로그인 및 설정

```bash
# Kimi CLI 시작
kimi

# 첫 실행 시 설정
/login
```

**로그인 옵션:**
1. **Kimi For Coding** - Kimi Code Plan 구독자 (OAuth 로그인)
   - 월 $9.99~$49.99 (약 49~249위안)
   - Claude Code 대비 1/7 가격, 3x 사용량
2. **Moonshot AI开放平台** - API Key 사용
   - Input: $0.60/1M tokens
   - Output: $2.50~$3.00/1M tokens

### 2.4 모델별 사용법

#### Kimi K2.5 모델 스펙

| 스펙 | 값 |
|------|-----|
| **총 파라미터** | 1조 (MoE) |
| **활성 파라미터** | 320억 |
| **컨텍스트 길이** | 256K tokens |
| **훈련 데이터** | 15조 mixed visual/text tokens |
| **라이선스** | Modified MIT |

#### 모델 전환

```bash
# 모델 확인 및 전환
/model
```

| 모델 | 특징 | 사용 시점 |
|------|------|-----------|
| **kimi-for-coding** | 기본 모델, Kimi K2.5 기반 | 일반적인 코딩 작업 |
| **kimi-k2.5** | 최신 모델, 1T 파라미터 | 복잡한 작업, 멀티모달 |

### 2.5 Kimi K2.5 4가지 운영 모드

Kimi K2.5는 4가지 운영 모드를 제공합니다:

| 모드 | 설명 | 사용 시점 | 특징 |
|------|------|-----------|------|
| **Instant** | 빠른 응답 | 간단한 조회, 100줄 이하 코드 | 3-8초 응답, reasoning 생략 |
| **Thinking** | 단계별 추론 | 수학 문제, 복잡한 논리 | 96.1% AIME 2025, reasoning_content 표시 |
| **Agent** | 도구 통합, 자율 워크플로우 | 200-300단계 도구 호출 | BrowseComp 74.9%, 안정적 실행 |
| **Agent Swarm** | 100개 병렬 에이전트 | 대규모 병렬 작업 | 4.5x 속도 향상, 78.4% BrowseComp |

### 2.6 실행 모드

#### Agent 모드 (기본)

```bash
# 기본 Agent 모드
kimi

# 자동 승인 모드 (YOLO)
kimi --yolo

# 또는 세션 내에서
/yolo
```

#### Shell 모드

```bash
# Shell 모드로 전환 (Ctrl+X)
# Agent 모드와 Shell 모드 간 전환
```

**모드 전환:**
- `Ctrl+X`: Agent ↔ Shell 모드 전환
- Agent 모드: 자연어로 AI에게 작업 요청
- Shell 모드: 일반 터미널처럼 직접 명령 실행

#### Web 모드

```bash
# 웹 인터페이스로 실행
kimi web
```

**Kimi Web 기능:**
- 이미지/비디오 업로드
- 실시간 미리보기
- 시각적 편집

### 2.7 슬래시 명령어 (/commands)

#### 계정 / 모델 / 설정

| 명령어 | 설명 |
|--------|------|
| `/login` | 로그인 및 플랫폼/자격 증명 설정 |
| `/model` | 모델 확인/전환 (thinking 모드 포함) |
| `/reload` | CLI 종료 없이 설정 다시 로드 |
| `/usage` | 사용량/할당량 확인 |

#### 세션 / 컨텍스트 관리

| 명령어 | 설명 |
|--------|------|
| `/sessions` 또는 `/resume` | 세션 목록, 전환/복구 |
| `/clear` 또는 `/reset` | 현재 세션 컨텍스트 비우기 |
| `/compact` | 컨텍스트 압축 (토큰 감소, 핵심 정보 유지) |
| `/debug` | 컨텍스트 디버그 정보 표시 (메시지 수, 토큰, 기록 등) |

#### 프로젝트 초기화

| 명령어 | 설명 |
|--------|------|
| `/init` | 현재 프로젝트 분석 및 `AGENTS.md` 생성 |

#### 자동 승인 / 실행 제어

| 명령어 | 설명 |
|--------|------|
| `/yolo` | YOLO 모드 전환 (자동 승인) |

#### 스킬 / 플로우

| 명령어 | 설명 |
|--------|------|
| `/skill:<name>` | 특정 스킬의 프롬프트/능력 로드 |
| `/flow:<name>` | 특정 플로우 실행 (작업 그룹) |

#### 도움말 / 종료 / 정보

| 명령어 | 설명 |
|--------|------|
| `/help` | 도움말 및 명령어 목록 |
| `/version` | 버전 정보 |
| `/changelog` | 업데이트 로그 |
| `/feedback` | 피드백 제출 |
| `/exit` | CLI 종료 |

### 2.8 MCP (Model Context Protocol) 설정

```bash
# MCP 설정 파일 예시 (mcp.json)
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}

# MCP 설정으로 Kimi 실행
kimi --mcp-config-file /path/to/mcp.json
```

#### MCP 서버 관리

```bash
# MCP 서버 추가 (HTTP)
kimi mcp add --transport http context7 https://mcp.context7.com/mcp \
  --header "CONTEXT7_API_KEY: ctx7sk-your-key"

# MCP 서버 추가 (stdio)
kimi mcp add --transport stdio chrome-devtools -- npx chrome-devtools-mcp@latest

# MCP 서버 목록
kimi mcp list

# MCP 서버 제거
kimi mcp remove chrome-devtools

# MCP 서버 인증
kimi mcp auth <server-name>
```

### 2.9 ACP (Agent Client Protocol) 연동

Zed, JetBrains 등 ACP 호환 IDE에서 사용:

```json
// ~/.config/zed/settings.json
{
  "agent_servers": {
    "Kimi CLI": {
      "command": "kimi",
      "args": ["acp"],
      "env": {}
    }
  }
}
```

### 2.10 Zsh 통합

```bash
# zsh-kimi-cli 플러그인 설치 (oh-my-zsh)
git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli

# ~/.zshrc에 플러그인 추가
plugins=(... kimi-cli)

# Zsh 재시작 후 Ctrl+K로 Kimi CLI 모드 진입
```

### 2.11 Agent Skills

```bash
# 스킬 생성
/skill:skill-creator

# 스킬 사용 예시
# 1. 스킬 디렉토리 생성
mkdir -p ~/.config/agents/skills/paper-translator

# 2. 스킬 파일 압축 해제
unzip paper-translator.skill -d ~/.config/agents/skills/paper-translator

# 3. 스킬 사용
# 이후 Kimi가 자동으로 관련 스킬 감지 및 사용
```

### 2.12 비전 코딩 (Vision Coding)

Kimi K2.5의 핵심 기능인 비전 코딩:

```bash
# 이미지에서 코드 생성
> "이 스크린샷을 보고 동일한 UI를 구현해줘"
# (이미지 붙여넣기)

# 비디오에서 웹사이트 복제
kimi web
# 비디오 업로드 후 "이 비디오의 웹사이트를 복제해줘"

# 디자인-투-코드
> "이 Figma 디자인을 React 컴포넌트로 변환해줘"
```

**비전 코딩 기능:**
- UI 스크린샷 → 작동하는 코드
- 비디오 녹화 → 완전한 웹사이트
- 디자인 목업 → 프로덕션 코드
- 자율적 시각 디버깅

### 2.13 Agent Swarm 사용법

```bash
# Agent Swarm 모드 활성화 (Kimi Web에서)
# 1. Kimi Web 접속 (kimi.com)
# 2. Agent Swarm (Beta) 모드 선택
# 3. 대규모 작업 요청

# 예시: 100개 도메인의 YouTube 크리에이터 조사
> "100개 틈새 도메인에서 상위 3명의 YouTube 크리에이터 식별"
# → 100개 서브 에이전트가 병렬 실행
```

**Agent Swarm 특징:**
- 최대 100개 서브 에이전트
- 1,500+ 병렬 도구 호출
- Critical Steps 메트릭으로 최적화
- 4.5x 실행 시간 단축

### 2.14 실전 사용 예시

```bash
# 1. 프로젝트 초기화
kimi
> /init

# 2. 웹사이트 복제 (비디오 기반)
kimi web
# 비디오 업로드 후 "이 비디오의 웹사이트를 복제해줘"

# 3. 게임 개발
> "레이싱 게임을 만들어줘"

# 4. 논문 번역 (LaTeX)
> "https://arxiv.org/abs/2602.02276 이 논문의 LaTeX 소스를 다운로드하고 영어를 중국어로 번역해줘"

# 5. 자동 승인 모드로 대규모 리팩토링
kimi --yolo
> "전체 코드베이스를 TypeScript로 마이그레이션해줘"

# 6. MCP 도구 사용
kimi --mcp-config-file ~/.config/kimi/mcp.json
> "Context7을 사용해 Django 문서를 검색해줘"

# 7. 비전 코딩
> "이 스크린샷의 UI를 React + Tailwind로 구현해줘"
# (스크린샷 붙여넣기)

# 8. Agent Swarm으로 대규모 리서치
# (Kimi Web에서)
> "50개 경쟁사를 20개 차원에서 비교 분석해줘"
```

### 2.15 Kimi Code 가격 비교

| 플랜 | 가격 | 특징 |
|------|------|------|
| **Individual Pro** | $9.99~$19.99/월 | 기본 기능 |
| **Professional** | $29.99~$49.99/월 | 고급 기능 |
| **Enterprise** | 맞춤형 | 엔터프라이즈 기능 |

**API 가격:**

| 토큰 유형 | 가격 |
|-----------|------|
| Input | $0.60/1M tokens |
| Output | $2.50~$3.00/1M tokens |

**Claude Code 대비:**
- 1/7 가격
- 3x 사용량
- Claude Opus 대비 76% 저렴

---

## 3. Codex CLI 상세 사용법

### 3.1 설치 및 기본 설정

#### 설치 방법

```bash
# NPM (권장)
npm install -g @openai/codex

# Homebrew (macOS/Linux)
brew install codex

# 업그레이드
npm install -g @openai/codex@latest
```

#### 설치 확인

```bash
codex --version
```

### 3.2 로그인 및 인증

```bash
# 첫 실행 시 인증
codex

# 명시적 로그인
codex login

# 로그인 상태 확인
codex login status

# 로그아웃
codex logout
```

**인증 방법:**
1. ChatGPT 계정 (OAuth)
2. OpenAI API Key

### 3.3 모델별 사용법

| 모델 | 사용법 | 특징 |
|------|--------|------|
| **GPT-5.3-Codex** | 기본 모델 | 최신 코딩 모델 |
| **GPT-5-Codex** | `--model gpt-5-codex` | 이전 버전 |
| **codex-mini** | API 전용 | 빠른 응답, 낮은 비용 |

#### 모델 전환

```bash
# 대화 모드에서
/model

# 실행 시 지정
codex --model gpt-5.3-codex
```

#### Reasoning 레벨 조정

```bash
# Reasoning 레벨 설정
# /model 명령어에서 조정 가능
```

### 3.4 실행 모드

#### 인터랙티브 모드 (TUI)

```bash
# 기본 인터랙티브 모드
codex

# 특정 디렉토리에서
codex /path/to/project

# 프롬프트와 함께 실행
codex "explain this codebase"
```

#### 비대화형 모드 (exec)

```bash
# 단일 명령 실행
codex exec "fix the CI failure"
codex e "refactor auth module"

# JSON 출력
codex exec --json "analyze code"

# 마지막 세션 계속
codex exec resume --last
codex exec resume --all

# 출력 포맷 지정
codex exec --output-format json "task"
```

#### Cloud 작업

```bash
# Cloud 작업 목록
codex cloud list

# Cloud 작업 실행
codex cloud exec "task description"

# 최근 diff 적용
codex apply
```

### 3.5 슬래시 명령어 (/commands)

#### 세션 및 흐름 제어

| 명령어 | 설명 | 사용 시점 |
|--------|------|-----------|
| `/new` | 새 세션 | 이전 작업 완료 후 새 작업 시작 |
| `/undo` | 마지막 작업 취소 | Codex가 잘못 수정했을 때 |
| `/exit` / `/quit` | 종료 | 작업 완료 |
| `/logout` | 로그아웃 | 계정 전환 |

#### 설정 및 권한

| 명령어 | 설명 | 모드 |
|--------|------|------|
| `/approvals` | 권한 모드 설정 | Auto (기본), Read Only, Full Access |
| `/model` | 모델 전환 및 reasoning 조정 | - |
| `/status` | 토큰 사용량, 컨텍스트 공간 확인 | - |
| `/mcp` | MCP 도구 관리 | - |

#### 컨텍스트 및 메모리

| 명령어 | 설명 | 사용 시점 |
|--------|------|-----------|
| `/init` | AGENTS.md 생성 | 프로젝트 초기화 |
| `/compact` | 대화 압축 | 토큰 절약 필요 시 |
| `/mention` | 파일/폴더를 컨텍스트에 추가 | 특정 모듈 집중 |
| `/diff` | Git Diff 표시 | 변경사항 확인 |

#### 작업 및 고급 기능

| 명령어 | 설명 |
|--------|------|
| `/review` | 코드 리뷰 |
| `/skills` | 실험적 스킬 탐색 |

### 3.6 Approval 모드 (권한 모드)

| 모드 | 설명 | 사용 시점 |
|------|------|-----------|
| **Auto** (기본) | 파일 읽기 자동, 수정/실행 시 확인 | 일반적인 개발 |
| **Read Only** | 읽기만 가능, 계획만 제시 | 민감한 코드 작업 |
| **Full Access** | 모든 작업 자동 실행 | CI/CD, 자동화 |

```bash
# 모드 전환
/approvals

# 또는 실행 시
claude --permission-mode full-access
```

### 3.7 CLI 플래그 및 옵션

#### 글로벌 플래그

```bash
# 출력 제어
codex --output-format json      # JSON 출력
codex --output-format text      # 텍스트 출력
codex --verbose                 # 상세 로깅
codex --quiet                   # 최소 출력

# 이미지 입력
codex -i screenshot.png "Explain this error"
codex --image img1.png,img2.jpg "Summarize these diagrams"

# 샌드박스
codex --sandbox                 # 샌드박스 모드
codex --dangerously-bypass-approvals-and-sandbox  # 주의!

# 추가 디렉토리
codex --add-dir /path/to/other/project

# 설정 파일
codex --settings ./settings.json
```

#### exec 모드 플래그

```bash
# JSON 이벤트 출력
codex exec --json "task"

# 마지막 메시지만 출력
codex exec --output-last-message "task"

# 전체 자동 모드
codex exec --full-auto "task"
```

### 3.8 MCP (Model Context Protocol)

```bash
# MCP 서버 추가 (stdio)
codex mcp add stdio-server-name -- command args

# MCP 서버 추가 (HTTP)
codex mcp add http-server-name --url https://example.com/mcp

# MCP 서버 목록
codex mcp list

# MCP 서버 제거
codex mcp remove server-name

# OAuth 로그인
codex mcp login server-name

# OAuth 로그아웃
codex mcp logout server-name
```

### 3.9 커스텀 슬래시 명령어

```bash
# 커스텀 명령어 디렉토리 생성
mkdir -p ~/.codex/prompts

# 커스텀 명령어 파일 생성
# ~/.codex/prompts/security-audit.md
```

**security-audit.md 예시:**

```markdown
# Security Audit

Please scan the current codebase for the following vulnerabilities:
1. SQL injection
2. Hardcoded secrets
3. XSS vulnerabilities

Generate a Markdown report with findings.
```

**사용:**

```bash
# 재시작 후 사용 가능
/security-audit
```

### 3.10 설정 파일 (config.toml)

```toml
# ~/.codex/config.toml

[model]
default = "gpt-5.3-codex"

[permissions]
mode = "auto"  # auto, read-only, full-access

[features]
web_search = true
multi_agent = false

[mcp.servers]
[.mcp.servers.my-server]
command = "npx"
args = ["-y", "my-mcp-server"]
```

### 3.11 실전 사용 예시

```bash
# 1. 코드베이스 분석
codex "explain this codebase"

# 2. 비대화형 작업
codex exec "fix all TypeScript errors in src/"

# 3. 이미지 입력
codex -i error.png "Explain this error and fix it"

# 4. 코드 리뷰
codex
> /review

# 5. 자동화 스크립트
codex exec --full-auto --json "run tests and fix failures" > results.json

# 6. MCP 도구 사용
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
codex
> /mcp

# 7. Cloud 작업
codex cloud exec "implement feature X"
codex apply  # 결과 적용
```

---

## 4. 도구별 비교 및 선택 가이드

### 4.1 핵심 비교

| 특성 | Claude Code | Kimi CLI | Codex CLI |
|------|-------------|----------|-----------|
| **개발사** | Anthropic | Moonshot AI | OpenAI |
| **기반 기술** | Node.js | Python (uv) | Rust |
| **라이선스** | Proprietary | Proprietary | Apache 2.0 (오픈소스) |
| **주요 모델** | Claude Sonnet/Opus | Kimi K2.5 | GPT-5.3-Codex |
| **가격** | $$$ | $ (가장 저렴) | $$ |

### 4.2 기능 비교

| 기능 | Claude Code | Kimi CLI | Codex CLI |
|------|-------------|----------|-----------|
| **Thinking Mode** | ✅ (3단계) | ✅ (4모드) | ✅ |
| **Plan Mode** | ✅ | ❌ | ❌ |
| **Fast Mode** | ✅ (Opus 4.6) | ✅ | ❌ |
| **Agent Swarm** | ❌ | ✅ (100개) | ❌ |
| **백그라운드 작업** | ✅ | ✅ | ❌ |
| **Web 인터페이스** | ✅ (claude.ai) | ✅ (kimi web) | ❌ |
| **MCP 지원** | ✅ | ✅ | ✅ |
| **ACP 지원** | ❌ | ✅ | ❌ |
| **커스텀 명령어** | ✅ (Skills) | ✅ (Skills) | ✅ (Markdown) |
| **오픈소스** | ❌ | ❌ | ✅ |

### 4.3 사용 사례별 추천

| 사용 사례 | 추천 도구 | 이유 |
|-----------|-----------|------|
| **대규모 레거시 코드 분석** | Claude Code (Opus) | 뛰어난 추론 능력, 긴 컨텍스트 |
| **빠른 프로토타이핑** | Kimi CLI | 저렴한 비용, Agent Swarm |
| **비용 민감 프로젝트** | Kimi CLI | 가장 저렴한 가격 |
| **오픈소스/커스터마이징** | Codex CLI | 오픈소스, 높은 확장성 |
| **엔터프라이즈/보안** | Claude Code | 강력한 보안, 세밀한 권한 제어 |
| **멀티모달 작업 (이미지/비디오)** | Kimi CLI | 뛰어난 비전 기능 |
| **CI/CD 통합** | Codex CLI | 비대화형 exec 모드 |
| **팀 협업** | Claude Code | 세션 공유, 강력한 Git 통합 |

### 4.4 선택 가이드

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI 코딩 도구 선택 가이드                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. 비용이 가장 중요한가?                                       │
│     → Kimi CLI (Claude 대비 1/7 가격, 3x 사용량)                │
│                                                                 │
│  2. 오픈소스가 필요한가?                                        │
│     → Codex CLI (Apache 2.0)                                    │
│                                                                 │
│  3. 최고의 추론 능력이 필요한가?                                │
│     → Claude Code (Opus 모델)                                   │
│                                                                 │
│  4. 멀티모달 (이미지/비디오) 작업이 많은가?                     │
│     → Kimi CLI (K2.5의 뛰어난 비전 기능)                        │
│                                                                 │
│  5. 엔터프라이즈 환경/보안이 중요한가?                          │
│     → Claude Code (세밀한 권한 제어, 감사 추적)                 │
│                                                                 │
│  6. CI/CD 자동화가 필요한가?                                    │
│     → Codex CLI (exec 모드, JSON 출력)                          │
│                                                                 │
│  7. 병렬 처리/Agent Swarm가 필요한가?                           │
│     → Kimi CLI (100개 병렬 에이전트)                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.5 워크플로우별 조합 추천

#### 개인 개발자 (프리랜서)

```bash
# 주요 도구: Kimi CLI
# 이유: 저렴한 비용, 충분한 성능

# 보조 도구: Codex CLI
# 이유: 오픈소스, CI/CD 통합
```

#### 스타트업 (소규모 팀)

```bash
# 주요 도구: Claude Code
# 이유: 빠른 개발, 강력한 추론

# 보조 도구: Kimi CLI
# 이유: 비용 절감용 대안
```

#### 엔터프라이즈 (대기업)

```bash
# 주요 도구: Claude Code
# 이유: 보안, 규정 준수, 지원

# 보조 도구: Codex CLI (내부 도구)
# 이유: 커스터마이징, 내부 인프라 통합
```

---

## 참고 자료

- [Claude Code 공식 문서](https://code.claude.com/docs)
- [Kimi CLI 공식 문서](https://moonshotai.github.io/kimi-cli/)
- [Codex CLI 공식 문서](https://developers.openai.com/codex/cli/)
- [Kimi K2.5 기술 보고서](https://arxiv.org/abs/2602.02276)

---

> 💡 **팁**: 각 도구는 고유한 강점이 있습니다. 프로젝트 요구사항과 예산에 맞게 선택하세요. 여러 도구를 병행 사용하는 것도 좋은 전략입니다.
