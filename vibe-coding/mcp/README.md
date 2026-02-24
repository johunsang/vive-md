# MCP (Model Context Protocol) 종합 가이드

> AI 모델과 외부 도구/데이터 소스를 연결하는 표준 프로토콜 MCP의 핵심 개념부터 실전 설정까지.
> 아키텍처 이해, Transport 계층, 프리미티브 활용, 트러블슈팅을 포괄하는 종합 레퍼런스.

---

## 목차

1. [MCP 개요 및 핵심 개념](#1-mcp-개요-및-핵심-개념)
2. [아키텍처 심층 분석](#2-아키텍처-심층-분석)
3. [Transport 계층](#3-transport-계층)
4. [MCP 서버 설정 (Claude Code 기준)](#4-mcp-서버-설정-claude-code-기준)
5. [MCP 프리미티브 상세](#5-mcp-프리미티브-상세)
6. [도구 탐색 및 관리](#6-도구-탐색-및-관리)
7. [실전 설정 가이드](#7-실전-설정-가이드)
8. [환경변수 및 시크릿 관리](#8-환경변수-및-시크릿-관리)
9. [트러블슈팅](#9-트러블슈팅)
10. [관련 문서 링크](#10-관련-문서-링크)

---

## 1. MCP 개요 및 핵심 개념

### MCP란 무엇인가

MCP(Model Context Protocol)는 Anthropic이 제안하고 오픈 소스로 공개한 **AI 모델과 외부 도구/데이터 소스를 연결하는 표준 프로토콜**이다. USB-C가 다양한 디바이스를 하나의 커넥터로 통합한 것처럼, MCP는 AI 모델이 파일 시스템, 데이터베이스, API, 개발 도구 등 외부 시스템과 상호작용하는 방법을 표준화한다.

```mermaid
graph LR
    subgraph "MCP 이전: N×M 통합 문제"
        A1[Claude] --> T1[GitHub 커넥터]
        A1 --> T2[DB 커넥터]
        A1 --> T3[Slack 커넥터]
        A2[GPT] --> T4[GitHub 커넥터]
        A2 --> T5[DB 커넥터]
        A2 --> T6[Slack 커넥터]
        A3[Gemini] --> T7[GitHub 커넥터]
        A3 --> T8[DB 커넥터]
        A3 --> T9[Slack 커넥터]
    end

    subgraph "MCP 이후: N+M 통합"
        B1[Claude] --> MCP[MCP 프로토콜]
        B2[GPT] --> MCP
        B3[Gemini] --> MCP
        MCP --> S1[GitHub 서버]
        MCP --> S2[DB 서버]
        MCP --> S3[Slack 서버]
    end
```

### 왜 MCP가 필요한가

AI 모델이 외부 도구와 통합할 때 발생하는 근본적인 문제를 해결한다.

| 문제 | MCP 이전 | MCP 이후 |
|------|---------|---------|
| **통합 복잡도** | N개 모델 × M개 도구 = N×M 커넥터 | N개 모델 + M개 도구 = N+M 어댑터 |
| **프로토콜 파편화** | 각 도구마다 고유한 API 형식 | 단일 JSON-RPC 2.0 표준 |
| **컨텍스트 제공** | 수동 복사/붙여넣기 | 자동 리소스 탐색 및 제공 |
| **보안 모델** | 도구별 개별 인증 체계 | 통합 인증/인가 프레임워크 |
| **도구 발견** | 하드코딩된 도구 목록 | 동적 capability 교환 |
| **재사용성** | 모델별 전용 플러그인 | 모든 MCP 호환 클라이언트에서 재사용 |

### MCP 생태계 현황 (2025-2026)

MCP는 2024년 11월 공개 이후 급속하게 성장하고 있다.

**주요 클라이언트 (Host)**:
- **Claude Desktop** — Anthropic의 데스크톱 앱, MCP 네이티브 지원
- **Claude Code** — CLI 기반 에이전틱 코딩 도구, MCP 서버 관리 내장
- **Cursor** — AI 코드 에디터, MCP 서버 연동 지원
- **Windsurf** — Codeium의 AI IDE, MCP 통합
- **Zed** — 고성능 코드 에디터, MCP 플러그인

**주요 서버 생태계**:
- **공식 서버**: filesystem, github, postgres, sqlite, brave-search, puppeteer 등
- **커뮤니티 서버**: 2000+ 개 이상의 오픈소스 MCP 서버
- **기업 서버**: Notion, Linear, Sentry, Datadog 등 SaaS 서비스 공식 MCP 서버

**프로토콜 버전**:
- `2024-11-05`: 최초 공개 버전 (stdio, SSE)
- `2025-03-26`: Streamable HTTP Transport 추가, 인증 체계 강화

> 실전 팁: MCP 서버는 npm, pip, Docker 등 다양한 패키지 매니저로 배포된다. 새 서버를 찾을 때는 [MCP 서버 디렉토리](https://github.com/modelcontextprotocol/servers)를 먼저 확인하라.

---

## 2. 아키텍처 심층 분석

### Host → Client → Server 3계층 구조

MCP는 명확한 3계층 아키텍처를 따른다. 각 계층의 역할과 책임이 분리되어 있어 독립적으로 발전 가능하다.

```mermaid
graph TB
    subgraph Host["Host (호스트 애플리케이션)"]
        direction TB
        H[Claude Desktop / Claude Code / Cursor]

        subgraph Clients["MCP Clients"]
            C1[Client 1<br/>GitHub 서버 연결]
            C2[Client 2<br/>DB 서버 연결]
            C3[Client 3<br/>파일시스템 서버 연결]
        end

        H --> C1
        H --> C2
        H --> C3
    end

    C1 <-->|"JSON-RPC 2.0"| S1[MCP Server<br/>GitHub]
    C2 <-->|"JSON-RPC 2.0"| S2[MCP Server<br/>PostgreSQL]
    C3 <-->|"JSON-RPC 2.0"| S3[MCP Server<br/>Filesystem]

    S1 <--> R1[(GitHub API)]
    S2 <--> R2[(PostgreSQL DB)]
    S3 <--> R3[(Local Files)]
```

### 각 계층 역할과 책임

#### Host (호스트)

Host는 사용자와 직접 상호작용하는 최상위 애플리케이션이다.

| 책임 | 설명 |
|------|------|
| **LLM 관리** | AI 모델과의 대화 세션 관리 |
| **Client 생성** | 각 MCP 서버에 대응하는 Client 인스턴스 생성 |
| **보안 정책** | 사용자 동의 관리, 도구 실행 권한 제어 |
| **UI 제공** | 도구 호출 결과를 사용자에게 표시 |
| **라우팅** | LLM의 도구 호출 요청을 올바른 Client로 전달 |

```typescript
// Host의 핵심 책임 - 개념적 구조
interface MCPHost {
  // 연결된 모든 Client를 관리
  clients: Map<string, MCPClient>;

  // LLM이 도구 호출을 요청하면 적절한 Client로 라우팅
  routeToolCall(toolName: string, args: unknown): Promise<ToolResult>;

  // 사용자 동의 확인 후 도구 실행 허용
  requestUserApproval(tool: ToolDefinition): Promise<boolean>;

  // 모든 Client의 capability를 LLM에게 통합 제공
  aggregateCapabilities(): Capability[];
}
```

#### Client (클라이언트)

Client는 Host 내부에서 특정 MCP 서버와의 1:1 연결을 담당한다.

| 책임 | 설명 |
|------|------|
| **연결 관리** | 서버와의 Transport 연결 수립 및 유지 |
| **프로토콜 교환** | 초기화, capability 교환, 메시지 직렬화/역직렬화 |
| **상태 추적** | 서버 연결 상태, 가용 도구 목록 캐싱 |
| **오류 처리** | 서버 오류, 타임아웃, 재연결 처리 |

```typescript
// Client의 프로토콜 교환 구조
interface MCPClient {
  // 서버와 연결 수립
  connect(transport: Transport): Promise<void>;

  // 프로토콜 초기화 (capability 교환)
  initialize(): Promise<InitializeResult>;

  // 도구 호출
  callTool(name: string, args: Record<string, unknown>): Promise<CallToolResult>;

  // 리소스 읽기
  readResource(uri: string): Promise<ReadResourceResult>;

  // 프롬프트 가져오기
  getPrompt(name: string, args?: Record<string, string>): Promise<GetPromptResult>;
}
```

#### Server (서버)

Server는 외부 시스템과의 실제 통합을 수행하는 계층이다.

| 책임 | 설명 |
|------|------|
| **도구 제공** | 외부 시스템의 기능을 MCP 도구로 노출 |
| **리소스 제공** | 데이터를 MCP 리소스로 노출 |
| **프롬프트 제공** | 재사용 가능한 프롬프트 템플릿 노출 |
| **외부 통합** | API 호출, DB 쿼리, 파일 I/O 등 실제 작업 수행 |
| **보안 경계** | 접근 제어, 입력 검증, 감사 로깅 |

```typescript
// Server의 기본 구조
interface MCPServer {
  // 서버가 제공하는 capability 선언
  capabilities: ServerCapabilities;

  // 도구 목록 반환
  listTools(): Tool[];

  // 도구 실행
  executeTool(name: string, args: unknown): Promise<ToolResult>;

  // 리소스 목록 반환
  listResources(): Resource[];

  // 리소스 내용 읽기
  readResource(uri: string): Promise<ResourceContent>;
}
```

### 메시지 플로우

MCP 통신은 JSON-RPC 2.0 프로토콜을 기반으로 한다. 전체 라이프사이클은 초기화, 작업, 종료 3단계로 구성된다.

```mermaid
sequenceDiagram
    participant H as Host
    participant C as Client
    participant S as Server

    Note over H,S: Phase 1: 초기화
    H->>C: 서버 설정 전달
    C->>S: initialize 요청
    Note right of C: protocolVersion: "2025-03-26"<br/>capabilities: { tools: {} }
    S-->>C: initialize 응답
    Note left of S: protocolVersion: "2025-03-26"<br/>capabilities: { tools: {}, resources: {} }<br/>serverInfo: { name, version }
    C->>S: notifications/initialized

    Note over H,S: Phase 2: 도구 발견
    C->>S: tools/list 요청
    S-->>C: tools/list 응답
    Note left of S: tools: [<br/>  { name: "query_db", ... },<br/>  { name: "insert_record", ... }<br/>]
    C->>H: 가용 도구 목록 전달

    Note over H,S: Phase 3: 도구 실행
    H->>C: callTool("query_db", { sql: "SELECT..." })
    C->>S: tools/call 요청
    S-->>C: tools/call 응답
    Note left of S: content: [<br/>  { type: "text", text: "결과..." }<br/>]
    C->>H: 실행 결과 전달

    Note over H,S: Phase 4: 종료
    C->>S: close 또는 Transport 연결 해제
```

### JSON-RPC 2.0 메시지 형식

MCP의 모든 통신은 3가지 메시지 타입으로 이루어진다.

**Request (요청)**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "query_database",
    "arguments": {
      "sql": "SELECT * FROM users LIMIT 10"
    }
  }
}
```

**Response (응답)**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "id | name | email\n1 | Alice | alice@example.com\n2 | Bob | bob@example.com"
      }
    ]
  }
}
```

**Notification (알림)** — id가 없으며 응답을 기대하지 않는다:
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/config.json"
  }
}
```

**Error Response (오류 응답)**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Invalid params: missing required field 'sql'",
    "data": {
      "field": "sql",
      "reason": "required"
    }
  }
}
```

### 프로토콜 버전 관리

클라이언트와 서버는 초기화 단계에서 프로토콜 버전을 협상한다.

```mermaid
flowchart TD
    A[Client 요청: protocolVersion = '2025-03-26'] --> B{서버가 해당 버전 지원?}
    B -->|Yes| C[서버 응답: protocolVersion = '2025-03-26']
    B -->|No| D{서버가 더 낮은 버전 지원?}
    D -->|Yes| E[서버 응답: 지원하는 가장 높은 버전]
    D -->|No| F[서버 응답: 오류 반환]
    C --> G[정상 통신 시작]
    E --> H{Client가 해당 버전 수용?}
    H -->|Yes| G
    H -->|No| I[연결 종료]
    F --> I
```

| 버전 | 출시일 | 주요 변경사항 |
|------|--------|-------------|
| `2024-11-05` | 2024년 11월 | 최초 공개 버전. stdio, SSE Transport |
| `2025-03-26` | 2025년 3월 | Streamable HTTP 추가. OAuth 2.1 인증. 구조화된 도구 출력. 배치 메시지 |

> 실전 팁: `protocolVersion`은 날짜 형식(`YYYY-MM-DD`)을 사용한다. 서버 개발 시 최신 버전을 우선 지원하되, 하위 호환을 위해 이전 버전도 함께 지원하는 것이 좋다.

---

## 3. Transport 계층

Transport 계층은 Client와 Server 간 실제 메시지 전달을 담당한다. MCP는 3가지 표준 Transport를 정의한다.

### stdio (Standard I/O)

가장 일반적인 Transport로, 로컬 프로세스의 표준 입출력(stdin/stdout)을 통해 통신한다.

**작동 원리**:
```mermaid
sequenceDiagram
    participant C as Client Process
    participant S as Server Process

    Note over C,S: Client가 Server를 자식 프로세스로 실행
    C->>S: stdin으로 JSON-RPC 메시지 전송
    Note right of C: 각 메시지는 개행(\n)으로 구분
    S-->>C: stdout으로 JSON-RPC 응답 전송
    Note left of S: stderr는 로그/디버그용
```

**특징**:
- Client가 Server 프로세스를 직접 실행 (spawn)
- 메시지는 개행 문자(`\n`)로 구분된 JSON-RPC
- Server의 `stderr`는 로그 출력용으로 사용 (프로토콜 메시지가 아님)
- 네트워크 불필요, 로컬에서만 동작

**설정 예시**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/projects"
      ]
    }
  }
}
```

**장점**:
- 설정이 가장 간단하다
- 네트워크 레이턴시 없음
- 별도 포트/호스트 설정 불필요
- 프로세스 격리로 보안성 확보

**단점**:
- 로컬에서만 사용 가능 (원격 서버 불가)
- Client가 Server의 라이프사이클을 관리해야 한다
- 서버 프로세스 크래시 시 재시작 필요

### SSE (Server-Sent Events)

HTTP 기반의 원격 통신 Transport이다. 2024-11-05 버전에서 도입되었으며, 2025-03-26 버전에서 Streamable HTTP로 대체 권장된다.

**작동 원리**:
```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server (HTTP)

    C->>S: GET /sse (SSE 연결 수립)
    Note right of S: SSE 스트림으로<br/>서버→클라이언트 메시지
    S-->>C: event: endpoint<br/>data: /messages?sessionId=abc123

    C->>S: POST /messages?sessionId=abc123
    Note right of C: 클라이언트→서버 메시지<br/>(JSON-RPC Request)
    S-->>C: SSE event: message<br/>data: {"jsonrpc":"2.0",...}
```

**특징**:
- 서버가 HTTP 엔드포인트를 노출
- `GET /sse`로 SSE 스트림 수립 (서버→클라이언트)
- `POST /messages`로 요청 전송 (클라이언트→서버)
- Session ID로 연결 식별

**설정 예시**:
```json
{
  "mcpServers": {
    "remote-db": {
      "url": "https://mcp-server.example.com/sse",
      "headers": {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIs..."
      }
    }
  }
}
```

**장점**:
- 원격 서버 연결 가능
- 서버를 중앙 집중식으로 관리
- 여러 클라이언트가 동시 연결 가능

**단점**:
- SSE 연결 유지 필요 (long-lived connection)
- 프록시/로드밸런서와 호환 문제 가능
- Streamable HTTP로 대체 권장

### Streamable HTTP

2025-03-26 버전에서 도입된 최신 Transport이다. SSE의 한계를 극복하며 가장 유연한 통신 모델을 제공한다.

**작동 원리**:
```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server (HTTP)

    Note over C,S: 단일 HTTP 엔드포인트 사용

    C->>S: POST /mcp<br/>{"jsonrpc":"2.0","method":"initialize",...}
    Note right of S: Content-Type 결정:<br/>application/json 또는<br/>text/event-stream

    alt 단순 응답
        S-->>C: 200 OK<br/>Content-Type: application/json<br/>{"jsonrpc":"2.0","result":{...}}
    else 스트리밍 응답
        S-->>C: 200 OK<br/>Content-Type: text/event-stream<br/>event: message<br/>data: {"jsonrpc":"2.0",...}
        S-->>C: event: message<br/>data: {"jsonrpc":"2.0",...}
    end

    Note over C,S: 선택적 SSE 스트림 (서버 알림용)
    C->>S: GET /mcp (SSE 연결 수립)
    S-->>C: SSE 스트림으로 서버 알림 수신
```

**특징**:
- 단일 HTTP 엔드포인트(`POST /mcp`)로 모든 메시지 처리
- 응답이 JSON 또는 SSE 스트림 중 선택 가능
- 서버 알림을 위한 선택적 `GET /mcp` SSE 스트림
- `Mcp-Session-Id` 헤더로 세션 관리
- 상태 비저장(stateless) 모드도 지원

**설정 예시**:
```json
{
  "mcpServers": {
    "cloud-service": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIs..."
      }
    }
  }
}
```

**장점**:
- 기존 HTTP 인프라(로드밸런서, CDN, 프록시)와 완벽 호환
- 상태 비저장/저장 모드 모두 지원
- SSE 연결 유지 불필요 (선택적)
- 배치 메시지 지원으로 효율적 통신

**단점**:
- 최신 프로토콜이므로 모든 클라이언트가 아직 지원하지 않을 수 있다
- SSE보다 서버 구현이 약간 더 복잡

### Transport 비교표

| 항목 | stdio | SSE | Streamable HTTP |
|------|-------|-----|----------------|
| **통신 방식** | stdin/stdout | HTTP GET(SSE) + POST | HTTP POST + 선택적 GET(SSE) |
| **서버 위치** | 로컬 전용 | 로컬/원격 | 로컬/원격 |
| **연결 유지** | 프로세스 존속 | SSE 연결 유지 필수 | 연결 유지 선택적 |
| **프록시 호환** | N/A | 제한적 | 완벽 |
| **배치 메시지** | 미지원 | 미지원 | 지원 |
| **상태 관리** | 프로세스 단위 | Session ID | Mcp-Session-Id 헤더 |
| **프로토콜 버전** | 2024-11-05+ | 2024-11-05+ | 2025-03-26+ |
| **권장 용도** | 로컬 도구, CLI | 레거시 원격 서버 | 새로운 원격 서버 |
| **난이도** | 쉬움 | 보통 | 보통 |

> 실전 팁: 새 MCP 서버를 개발한다면 stdio를 기본으로 구현하고, 원격 배포가 필요하면 Streamable HTTP를 추가하라. SSE는 레거시 호환 목적으로만 유지하되, 신규 개발에는 권장하지 않는다.

---

## 4. MCP 서버 설정 (Claude Code 기준)

Claude Code는 MCP 서버를 프로젝트 스코프와 사용자 스코프 두 가지 레벨에서 관리한다.

### 설정 스코프 개요

```mermaid
graph TB
    subgraph "사용자 스코프 (전역)"
        U["~/.claude/settings.json"]
        U1["모든 프로젝트에서 사용 가능"]
        U2["개인 API 키, 범용 도구"]
    end

    subgraph "프로젝트 스코프 (로컬)"
        P[".mcp.json (프로젝트 루트)"]
        P1["해당 프로젝트에서만 사용"]
        P2["팀원과 Git으로 공유 가능"]
    end

    U --> U1
    U --> U2
    P --> P1
    P --> P2

    U1 -.->|"병합"| R[최종 MCP 서버 목록]
    P1 -.->|"병합"| R
```

### 프로젝트 스코프: `.mcp.json`

프로젝트 루트에 `.mcp.json` 파일을 생성하면 해당 프로젝트의 MCP 서버를 정의할 수 있다. Git으로 커밋하면 팀원 전체가 동일한 MCP 서버 설정을 공유한다.

**파일 구조**:
```json
{
  "mcpServers": {
    "server-name": {
      "command": "실행할 명령어",
      "args": ["인자1", "인자2"],
      "env": {
        "ENV_VAR": "값"
      },
      "cwd": "/작업/디렉토리"
    }
  }
}
```

**실전 예시 — 다양한 서버 유형**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/projects/my-app"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "${{env.DATABASE_URL}}"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${{env.BRAVE_API_KEY}}"
      }
    }
  }
}
```

### 사용자 스코프: `~/.claude/settings.json`

사용자의 모든 프로젝트에서 전역적으로 사용할 MCP 서버를 설정한다.

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

### `claude mcp add` CLI 명령어

Claude Code CLI로 MCP 서버를 대화형으로 추가할 수 있다.

**기본 문법**:
```bash
claude mcp add <서버이름> [옵션] -- <명령어> [인자...]
```

**스코프 옵션**:
```bash
# 프로젝트 스코프 (기본값) — .mcp.json에 저장
claude mcp add my-server -- npx -y @example/mcp-server

# 사용자 스코프 — ~/.claude/settings.json에 저장
claude mcp add my-server --scope user -- npx -y @example/mcp-server
```

**서버 유형별 추가**:
```bash
# stdio 서버 (기본)
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/dir

# SSE 서버
claude mcp add remote-server --transport sse --url https://mcp.example.com/sse

# Streamable HTTP 서버
claude mcp add cloud-server --transport http --url https://api.example.com/mcp

# 환경변수 포함
claude mcp add github \
  -e GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx \
  -- npx -y @modelcontextprotocol/server-github
```

**서버 관리 명령어**:
```bash
# 등록된 서버 목록 확인
claude mcp list

# 특정 서버 상세 정보
claude mcp get filesystem

# 서버 제거
claude mcp remove filesystem

# 서버 재시작 (설정 변경 후)
claude mcp restart filesystem
```

### stdio 서버 vs URL 기반 서버 설정 차이

**stdio 서버** — `command` + `args` 사용:
```json
{
  "mcpServers": {
    "local-tool": {
      "command": "node",
      "args": ["/path/to/server.js"],
      "env": {
        "LOG_LEVEL": "debug"
      },
      "cwd": "/path/to/working/dir"
    }
  }
}
```

**URL 기반 서버 (SSE / Streamable HTTP)** — `url` 사용:
```json
{
  "mcpServers": {
    "remote-tool": {
      "url": "https://mcp-server.example.com/sse",
      "headers": {
        "Authorization": "Bearer ${{env.API_TOKEN}}"
      }
    }
  }
}
```

### 설정 필드 레퍼런스

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `command` | string | stdio 서버 시 | 실행할 바이너리 (npx, node, python, uvx 등) |
| `args` | string[] | No | 명령어 인자 배열 |
| `env` | object | No | 환경변수 맵. `${{env.VAR}}` 템플릿 지원 |
| `cwd` | string | No | 서버 프로세스의 작업 디렉토리 |
| `url` | string | URL 서버 시 | SSE 또는 Streamable HTTP 엔드포인트 |
| `headers` | object | No | HTTP 요청에 포함할 헤더 |

> 실전 팁: `.mcp.json`에 API 키를 직접 넣지 마라. 반드시 `${{env.VARIABLE_NAME}}` 템플릿을 사용하고 실제 값은 `.env` 파일이나 시스템 환경변수로 관리하라. `.mcp.json`은 Git에 커밋하되, `.env`는 `.gitignore`에 추가한다.

---

## 5. MCP 프리미티브 상세

MCP는 4가지 핵심 프리미티브(Primitive)를 제공한다. 각 프리미티브는 서로 다른 역할을 담당하며, 서버는 필요한 프리미티브만 선택적으로 구현한다.

```mermaid
graph LR
    subgraph "MCP 프리미티브"
        T["Tools (도구)"]
        R["Resources (리소스)"]
        P["Prompts (프롬프트)"]
        S["Sampling (샘플링)"]
    end

    T -->|"모델이 호출"| T1["함수 실행, 부작용 가능"]
    R -->|"클라이언트가 요청"| R1["데이터 읽기, 읽기 전용"]
    P -->|"사용자가 선택"| P1["프롬프트 템플릿"]
    S -->|"서버가 요청"| S1["역방향 LLM 호출"]
```

### Tools (도구)

Tools는 **모델이 호출하는 함수**다. 외부 시스템에 대한 작업을 수행하며 부작용(side effect)을 가질 수 있다.

**핵심 특성**:
- 모델(LLM)이 자율적으로 호출 결정
- 입력 스키마(JSON Schema)로 파라미터 정의
- 결과로 텍스트, 이미지, 에러 등 반환
- 부작용 가능 (파일 생성, DB 수정, API 호출 등)

**Tool 정의 (서버 측)**:
```typescript
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "create_issue",
        description: "GitHub 리포지토리에 새 이슈를 생성합니다. " +
          "버그 리포트, 기능 요청, 작업 추적에 사용합니다.",
        inputSchema: {
          type: "object",
          properties: {
            owner: {
              type: "string",
              description: "리포지토리 소유자 (사용자 또는 조직)"
            },
            repo: {
              type: "string",
              description: "리포지토리 이름"
            },
            title: {
              type: "string",
              description: "이슈 제목"
            },
            body: {
              type: "string",
              description: "이슈 본문 (마크다운 지원)"
            },
            labels: {
              type: "array",
              items: { type: "string" },
              description: "이슈에 부여할 라벨 목록"
            }
          },
          required: ["owner", "repo", "title"]
        }
      },
      {
        name: "search_issues",
        description: "GitHub 이슈를 검색합니다. " +
          "키워드, 라벨, 상태 등으로 필터링 가능합니다.",
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "GitHub 이슈 검색 쿼리 (GitHub Search 문법)"
            },
            owner: {
              type: "string",
              description: "리포지토리 소유자로 필터링"
            },
            repo: {
              type: "string",
              description: "리포지토리 이름으로 필터링"
            },
            state: {
              type: "string",
              enum: ["open", "closed", "all"],
              description: "이슈 상태 필터 (기본: open)"
            }
          },
          required: ["query"]
        }
      }
    ]
  };
});
```

**Tool 실행 (서버 측)**:
```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "create_issue": {
      const { owner, repo, title, body, labels } = args;
      const response = await octokit.issues.create({
        owner,
        repo,
        title,
        body: body || "",
        labels: labels || []
      });

      return {
        content: [
          {
            type: "text",
            text: `이슈 생성 완료: #${response.data.number}\n` +
              `URL: ${response.data.html_url}\n` +
              `제목: ${response.data.title}`
          }
        ]
      };
    }

    case "search_issues": {
      const { query, owner, repo, state } = args;
      let q = query;
      if (owner && repo) q += ` repo:${owner}/${repo}`;
      if (state) q += ` state:${state}`;

      const response = await octokit.search.issuesAndPullRequests({ q });

      const results = response.data.items.map(issue =>
        `#${issue.number} [${issue.state}] ${issue.title}`
      ).join("\n");

      return {
        content: [
          {
            type: "text",
            text: `검색 결과 (${response.data.total_count}건):\n${results}`
          }
        ]
      };
    }

    default:
      return {
        content: [{ type: "text", text: `알 수 없는 도구: ${name}` }],
        isError: true
      };
  }
});
```

**Tool 호출 메시지 (JSON-RPC)**:
```json
{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "tools/call",
  "params": {
    "name": "create_issue",
    "arguments": {
      "owner": "my-org",
      "repo": "my-project",
      "title": "로그인 페이지 500 에러 발생",
      "body": "## 재현 단계\n1. /login 접속\n2. 이메일 입력 후 제출\n\n## 예상 동작\n로그인 성공\n\n## 실제 동작\n500 Internal Server Error",
      "labels": ["bug", "priority-high"]
    }
  }
}
```

**Tool 응답 메시지**:
```json
{
  "jsonrpc": "2.0",
  "id": 42,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "이슈 생성 완료: #157\nURL: https://github.com/my-org/my-project/issues/157\n제목: 로그인 페이지 500 에러 발생"
      }
    ]
  }
}
```

### Resources (리소스)

Resources는 **서버가 제공하는 읽기 전용 데이터**다. 모델에게 컨텍스트 정보를 제공하기 위해 사용된다.

**핵심 특성**:
- 클라이언트(또는 사용자)가 명시적으로 요청
- URI 기반 접근 (`file://`, `db://`, `api://` 등)
- 읽기 전용, 부작용 없음
- MIME 타입으로 콘텐츠 형식 명시

**Resource 정의 (서버 측)**:
```typescript
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [
      {
        uri: "db://myapp/schema",
        name: "데이터베이스 스키마",
        description: "myapp 데이터베이스의 전체 테이블 스키마 정보",
        mimeType: "application/json"
      },
      {
        uri: "config://myapp/settings",
        name: "애플리케이션 설정",
        description: "현재 배포 환경의 애플리케이션 설정값",
        mimeType: "application/json"
      }
    ]
  };
});
```

**Resource Template (동적 리소스)**:
```typescript
server.setRequestHandler(ListResourceTemplatesRequestSchema, async () => {
  return {
    resourceTemplates: [
      {
        uriTemplate: "db://myapp/table/{tableName}/schema",
        name: "테이블 스키마",
        description: "특정 테이블의 컬럼, 인덱스, 제약조건 정보",
        mimeType: "application/json"
      },
      {
        uriTemplate: "logs://myapp/{service}/{date}",
        name: "서비스 로그",
        description: "특정 서비스의 날짜별 로그",
        mimeType: "text/plain"
      }
    ]
  };
});
```

**Resource 읽기 (서버 측)**:
```typescript
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  if (uri === "db://myapp/schema") {
    const tables = await db.query(`
      SELECT table_name, column_name, data_type, is_nullable
      FROM information_schema.columns
      WHERE table_schema = 'public'
      ORDER BY table_name, ordinal_position
    `);

    return {
      contents: [
        {
          uri: "db://myapp/schema",
          mimeType: "application/json",
          text: JSON.stringify(tables.rows, null, 2)
        }
      ]
    };
  }

  // 동적 리소스 템플릿 매칭
  const tableMatch = uri.match(/^db:\/\/myapp\/table\/(\w+)\/schema$/);
  if (tableMatch) {
    const tableName = tableMatch[1];
    const schema = await db.query(`
      SELECT column_name, data_type, is_nullable, column_default
      FROM information_schema.columns
      WHERE table_name = $1
      ORDER BY ordinal_position
    `, [tableName]);

    return {
      contents: [
        {
          uri,
          mimeType: "application/json",
          text: JSON.stringify(schema.rows, null, 2)
        }
      ]
    };
  }

  throw new McpError(ErrorCode.InvalidRequest, `Unknown resource: ${uri}`);
});
```

**Resource 메시지 (JSON-RPC)**:
```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "method": "resources/read",
  "params": {
    "uri": "db://myapp/table/users/schema"
  }
}
```

**Resource 응답**:
```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": {
    "contents": [
      {
        "uri": "db://myapp/table/users/schema",
        "mimeType": "application/json",
        "text": "[{\"column_name\":\"id\",\"data_type\":\"uuid\",\"is_nullable\":\"NO\"},{\"column_name\":\"email\",\"data_type\":\"varchar\",\"is_nullable\":\"NO\"},{\"column_name\":\"name\",\"data_type\":\"varchar\",\"is_nullable\":\"YES\"}]"
      }
    ]
  }
}
```

### Prompts (프롬프트)

Prompts는 **재사용 가능한 프롬프트 템플릿**이다. 사용자가 명시적으로 선택하여 LLM에게 전달한다.

**핵심 특성**:
- 사용자가 명시적으로 선택 (슬래시 명령, 메뉴 등)
- 파라미터화된 템플릿 지원
- 역할(role)별 메시지 시퀀스 정의 가능
- 리소스 참조 포함 가능

**Prompt 정의 (서버 측)**:
```typescript
server.setRequestHandler(ListPromptsRequestSchema, async () => {
  return {
    prompts: [
      {
        name: "code_review",
        description: "코드 리뷰를 수행합니다. 보안, 성능, 가독성 관점에서 분석합니다.",
        arguments: [
          {
            name: "language",
            description: "프로그래밍 언어 (typescript, python, java 등)",
            required: true
          },
          {
            name: "focus",
            description: "리뷰 초점 (security, performance, readability, all)",
            required: false
          }
        ]
      },
      {
        name: "sql_optimizer",
        description: "SQL 쿼리를 분석하고 최적화 방안을 제안합니다.",
        arguments: [
          {
            name: "dialect",
            description: "SQL 방언 (postgresql, mysql, sqlite)",
            required: true
          }
        ]
      }
    ]
  };
});
```

**Prompt 반환 (서버 측)**:
```typescript
server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "code_review") {
    const focus = args?.focus || "all";

    return {
      description: `${args.language} 코드 리뷰 (초점: ${focus})`,
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `당신은 시니어 ${args.language} 개발자입니다. ` +
              `다음 관점에서 코드를 리뷰하세요:\n\n` +
              (focus === "all" || focus === "security"
                ? "- 보안: SQL 인젝션, XSS, 인증/인가 취약점\n" : "") +
              (focus === "all" || focus === "performance"
                ? "- 성능: N+1 쿼리, 불필요한 연산, 메모리 누수\n" : "") +
              (focus === "all" || focus === "readability"
                ? "- 가독성: 네이밍, 함수 분리, 주석 품질\n" : "") +
              "\n각 이슈에 대해 심각도(Critical/Major/Minor)와 개선 코드를 제시하세요."
          }
        }
      ]
    };
  }

  if (name === "sql_optimizer") {
    return {
      description: `${args.dialect} SQL 최적화`,
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `당신은 ${args.dialect} 데이터베이스 전문가입니다. ` +
              `제공되는 SQL 쿼리에 대해:\n\n` +
              "1. 실행 계획(EXPLAIN) 분석\n" +
              "2. 인덱스 활용 여부 확인\n" +
              "3. 쿼리 리라이팅 제안\n" +
              "4. 예상 성능 개선도\n\n" +
              "을 분석하세요."
          }
        }
      ]
    };
  }

  throw new McpError(ErrorCode.InvalidRequest, `Unknown prompt: ${name}`);
});
```

### Sampling (샘플링)

Sampling은 **서버가 LLM에게 요청하는 역방향 패턴**이다. 일반적으로 클라이언트가 서버에 요청하지만, Sampling은 서버가 클라이언트(Host)의 LLM에게 텍스트 생성을 요청한다.

**핵심 특성**:
- 서버 → 클라이언트(Host) 방향 요청
- Host의 보안 정책에 따라 실행 제어
- 에이전틱 루프 구현에 활용
- 사용자 동의 하에 실행

```mermaid
sequenceDiagram
    participant U as 사용자
    participant H as Host (LLM)
    participant S as MCP Server

    U->>H: "이 코드를 분석해줘"
    H->>S: tools/call (analyze_code)
    Note right of S: 서버가 분석 중<br/>추가 LLM 판단 필요
    S->>H: sampling/createMessage 요청
    Note left of H: Host가 사용자<br/>동의 확인
    H-->>S: sampling 응답 (LLM 생성 텍스트)
    S-->>H: tools/call 최종 응답
    H->>U: 분석 결과 표시
```

**Sampling 요청 (서버 → 클라이언트)**:
```json
{
  "jsonrpc": "2.0",
  "id": 100,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "다음 로그 패턴이 보안 위협인지 분석하세요:\n[2025-02-24 03:14:15] Multiple failed login attempts from IP 192.168.1.100"
        }
      }
    ],
    "maxTokens": 500,
    "temperature": 0.2,
    "systemPrompt": "당신은 보안 분석 전문가입니다. 로그 패턴을 분석하고 위협 수준을 평가하세요."
  }
}
```

### 프리미티브 선택 가이드

어떤 프리미티브를 사용해야 할지 결정하는 플로우차트:

```mermaid
flowchart TD
    A["외부 시스템과 상호작용 필요"] --> B{"부작용이 있는가?<br/>(데이터 수정, API 호출 등)"}
    B -->|"Yes"| C["Tools 사용"]
    B -->|"No"| D{"데이터를 읽기만 하는가?"}
    D -->|"Yes"| E{"URI로 식별 가능한가?"}
    E -->|"Yes"| F["Resources 사용"]
    E -->|"No"| C
    D -->|"No"| G{"사용자가 선택하는<br/>프롬프트 템플릿인가?"}
    G -->|"Yes"| H["Prompts 사용"]
    G -->|"No"| I{"서버가 LLM에게<br/>생성을 요청하는가?"}
    I -->|"Yes"| J["Sampling 사용"]
    I -->|"No"| C
```

**프리미티브 비교표**:

| 프리미티브 | 제어 주체 | 방향 | 부작용 | 용도 |
|-----------|---------|------|--------|------|
| **Tools** | 모델 (LLM) | Client → Server | O | 함수 호출, 데이터 수정, API 호출 |
| **Resources** | 클라이언트/사용자 | Client → Server | X | 데이터 읽기, 컨텍스트 제공 |
| **Prompts** | 사용자 | Client → Server | X | 프롬프트 템플릿, 워크플로우 |
| **Sampling** | 서버 | Server → Client | X | 역방향 LLM 호출, 에이전틱 루프 |

> 실전 팁: 대부분의 MCP 서버는 Tools만 구현해도 충분하다. Resources는 모델에게 풍부한 컨텍스트를 제공할 때, Prompts는 복잡한 워크플로우를 템플릿화할 때 추가 구현하라. Sampling은 고급 에이전틱 시나리오에서만 필요하다.

---

## 6. 도구 탐색 및 관리

Claude Code에서 MCP 서버와 도구를 관리하는 방법을 다룬다.

### `/mcp` 명령으로 서버 상태 확인

Claude Code 대화 중 `/mcp` 슬래시 명령을 입력하면 연결된 모든 MCP 서버의 상태를 확인할 수 있다.

```
> /mcp

MCP Servers:
  github        ✅ connected (5 tools)
  postgres      ✅ connected (3 tools)
  filesystem    ✅ connected (7 tools)
  brave-search  ❌ disconnected (BRAVE_API_KEY not set)
```

각 상태의 의미:

| 상태 | 설명 |
|------|------|
| `connected` | 서버 정상 연결, 도구 사용 가능 |
| `disconnected` | 연결 실패, 설정/환경 확인 필요 |
| `connecting` | 연결 시도 중 |
| `error` | 서버 실행 중 오류 발생 |

### 도구 목록 조회 및 검색

MCP 서버에 연결되면 해당 서버의 도구가 자동으로 사용 가능해진다. Claude Code에게 직접 물어보는 것이 가장 간편하다.

```
사용자: 현재 사용 가능한 MCP 도구 목록을 보여줘

Claude: 현재 연결된 MCP 서버와 사용 가능한 도구:

**github** (5 tools):
  - create_issue: GitHub 이슈 생성
  - search_issues: 이슈 검색
  - create_pull_request: PR 생성
  - get_file_contents: 파일 내용 조회
  - list_repos: 리포지토리 목록

**postgres** (3 tools):
  - query: SQL 쿼리 실행 (읽기 전용)
  - list_tables: 테이블 목록 조회
  - describe_table: 테이블 스키마 조회

**filesystem** (7 tools):
  - read_file: 파일 읽기
  - write_file: 파일 쓰기
  - list_directory: 디렉토리 목록
  - create_directory: 디렉토리 생성
  - move_file: 파일 이동
  - search_files: 파일 검색
  - get_file_info: 파일 메타데이터
```

### 서버 재시작 및 디버그

MCP 서버에 문제가 발생하면 다음 명령어로 진단하고 재시작한다.

```bash
# 특정 서버 재시작
claude mcp restart github

# 모든 서버 재시작
claude mcp restart

# 서버 상세 정보 확인 (연결 상태, 환경변수 등)
claude mcp get github
```

**대화 중 서버 재시작**:

Claude Code 대화 세션에서도 `/mcp` 명령 후 인터랙티브하게 서버를 재시작할 수 있다. 서버의 코드를 수정한 후 바로 반영할 때 유용하다.

### 연결 문제 진단

서버 연결이 실패할 때의 진단 절차:

```mermaid
flowchart TD
    A["서버 연결 실패"] --> B{"설정 파일 확인"}
    B --> C{".mcp.json 또는<br/>settings.json 존재?"}
    C -->|"No"| D["설정 파일 생성"]
    C -->|"Yes"| E{"문법 오류?"}
    E -->|"Yes"| F["JSON 문법 수정"]
    E -->|"No"| G{"command 경로 확인"}
    G --> H{"바이너리 존재?"}
    H -->|"No"| I["패키지 설치<br/>npm install / pip install"]
    H -->|"Yes"| J{"환경변수 설정?"}
    J -->|"No"| K["환경변수 설정"]
    J -->|"Yes"| L{"권한 문제?"}
    L -->|"Yes"| M["실행 권한 부여<br/>chmod +x"]
    L -->|"No"| N["서버 로그 확인<br/>stderr 출력"]
```

**수동 테스트 — 서버 직접 실행**:
```bash
# 서버를 직접 실행하여 오류 확인
npx -y @modelcontextprotocol/server-filesystem /tmp/test 2>&1

# Python 서버의 경우
uvx mcp-server-fetch 2>&1

# 환경변수가 필요한 서버
GITHUB_TOKEN=ghp_xxx npx -y @modelcontextprotocol/server-github 2>&1
```

**JSON-RPC 수동 테스트**:
```bash
# 서버에 초기화 메시지를 직접 보내 응답 확인
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}' | npx -y @modelcontextprotocol/server-filesystem /tmp/test
```

> 실전 팁: MCP 서버 연결 문제의 80%는 환경변수 미설정이다. `claude mcp get <서버명>`으로 설정을 확인하고, `${{env.VAR}}` 템플릿이 올바르게 치환되는지 확인하라.

---

## 7. 실전 설정 가이드

### 첫 MCP 서버 설정 (Step-by-Step)

가장 간단한 filesystem 서버를 설정하며 MCP의 기본 흐름을 익힌다.

**Step 1: 프로젝트 루트에 `.mcp.json` 생성**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/projects/my-app"
      ]
    }
  }
}
```

**Step 2: Claude Code 실행 및 확인**:
```bash
# 프로젝트 디렉토리에서 Claude Code 실행
cd /home/user/projects/my-app
claude

# 대화 중 MCP 상태 확인
> /mcp
# filesystem ✅ connected (7 tools) 확인
```

**Step 3: 도구 사용**:
```
사용자: src 디렉토리의 파일 목록을 보여줘

Claude: (MCP filesystem 서버의 list_directory 도구를 호출하여 결과 표시)
```

### 다중 서버 설정

실제 프로젝트에서는 여러 MCP 서버를 동시에 사용한다.

**웹 개발 프로젝트 예시**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/projects/web-app"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "${{env.DATABASE_URL}}"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${{env.BRAVE_API_KEY}}"
      }
    },
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

**데이터 분석 프로젝트 예시**:
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": [
        "mcp-server-sqlite",
        "--db-path",
        "/home/user/data/analytics.db"
      ]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/data"
      ]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

### 팀 공유 설정 (`.mcp.json` in Git)

`.mcp.json`을 Git에 커밋하면 팀원 모두가 동일한 MCP 서버 설정을 사용한다.

**`.mcp.json` (Git에 커밋)**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "${{env.DATABASE_URL}}"
      ]
    },
    "sentry": {
      "command": "npx",
      "args": ["-y", "@sentry/mcp-server"],
      "env": {
        "SENTRY_AUTH_TOKEN": "${{env.SENTRY_AUTH_TOKEN}}"
      }
    }
  }
}
```

**`.env.example` (Git에 커밋 — 템플릿)**:
```bash
# MCP 서버 환경변수
# 이 파일을 .env로 복사한 후 실제 값을 채우세요

# GitHub
GITHUB_TOKEN=ghp_your_token_here

# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# Sentry
SENTRY_AUTH_TOKEN=sntrys_your_token_here
```

**`.gitignore`**:
```
# 환경변수 (실제 시크릿)
.env
.env.local
.env.*.local

# .mcp.json은 커밋한다 (시크릿은 ${{env.VAR}}로 참조)
# !.mcp.json
```

**팀 온보딩 절차**:
```bash
# 1. 리포지토리 클론
git clone https://github.com/my-org/my-project.git
cd my-project

# 2. 환경변수 파일 생성
cp .env.example .env
# .env 파일을 열어 실제 토큰 값 입력

# 3. Claude Code 실행 — .mcp.json이 자동으로 읽힘
claude

# 4. MCP 서버 연결 확인
> /mcp
```

### CI/CD 환경 설정

CI/CD 파이프라인에서 MCP 서버를 사용하는 방법이다.

**GitHub Actions 예시**:
```yaml
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run AI Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # .mcp.json이 리포지토리에 있으므로 자동 로드
          claude -p "이 PR의 변경사항을 리뷰하고 코멘트를 작성해줘"
```

> 실전 팁: CI/CD에서 MCP 서버를 사용할 때는 stdio Transport만 사용하라. 원격 서버(SSE/HTTP)는 네트워크 설정이 복잡해진다. CI 환경에서는 `npx -y`로 패키지를 즉시 설치하여 사용하는 것이 가장 간편하다.

---

## 8. 환경변수 및 시크릿 관리

### `${{env.VAR}}` 템플릿 문법

MCP 설정에서 시크릿을 안전하게 참조하는 표준 방법이다.

**기본 문법**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}"
      }
    }
  }
}
```

`${{env.GITHUB_TOKEN}}`은 런타임에 시스템 환경변수 `GITHUB_TOKEN`의 값으로 치환된다.

**사용 가능한 위치**:
- `env` 객체의 값
- `args` 배열의 문자열 인자
- `url` 값
- `headers` 객체의 값

```json
{
  "mcpServers": {
    "custom-server": {
      "command": "node",
      "args": [
        "/path/to/server.js",
        "--db", "${{env.DATABASE_URL}}",
        "--port", "3000"
      ],
      "env": {
        "API_KEY": "${{env.SERVICE_API_KEY}}",
        "LOG_LEVEL": "info"
      }
    },
    "remote-server": {
      "url": "https://mcp.example.com/${{env.TENANT_ID}}/sse",
      "headers": {
        "Authorization": "Bearer ${{env.MCP_AUTH_TOKEN}}",
        "X-Tenant-ID": "${{env.TENANT_ID}}"
      }
    }
  }
}
```

### `.env` 파일 연동

프로젝트 루트의 `.env` 파일에 환경변수를 정의하면 Claude Code가 자동으로 로드한다.

**`.env` 파일**:
```bash
# MCP 서버 시크릿
GITHUB_TOKEN=ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ123456
DATABASE_URL=postgresql://admin:secretpass@localhost:5432/production
BRAVE_API_KEY=BSA_abcdef1234567890
SENTRY_AUTH_TOKEN=sntrys_ABCdef123456789

# 애플리케이션 설정
NODE_ENV=development
LOG_LEVEL=debug
```

**주의사항**:
```bash
# .env 파일은 절대 Git에 커밋하지 않는다
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
echo ".env.*.local" >> .gitignore
```

### 시크릿 관리 모범 사례

| 방법 | 보안 수준 | 적합한 환경 |
|------|---------|-----------|
| `.env` 파일 | 중간 | 로컬 개발 |
| 시스템 환경변수 | 중간 | 서버, CI/CD |
| 1Password / Vault | 높음 | 팀/프로덕션 |
| CI/CD Secrets | 높음 | CI/CD 파이프라인 |

**1Password CLI 연동 예시**:
```bash
# 1Password CLI로 시크릿을 환경변수에 로드
export GITHUB_TOKEN=$(op read "op://Development/GitHub Token/credential")
export DATABASE_URL=$(op read "op://Development/PostgreSQL/connection_string")

# Claude Code 실행
claude
```

**direnv 연동 (자동 환경변수 로드)**:
```bash
# .envrc 파일 (프로젝트 루트)
# direnv가 디렉토리 진입 시 자동으로 환경변수 로드
export GITHUB_TOKEN=$(op read "op://Development/GitHub Token/credential")
export DATABASE_URL="postgresql://localhost:5432/myapp_dev"
export BRAVE_API_KEY=$(op read "op://Development/Brave Search/api_key")
```

```bash
# direnv 설정
cd /home/user/projects/my-app
direnv allow .
# 이후 이 디렉토리에 진입하면 자동으로 환경변수 로드
```

### 환경별(dev/staging/prod) 설정

환경별로 다른 MCP 서버 설정을 적용하는 패턴이다.

**방법 1: 환경변수로 분기**:
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "${{env.DATABASE_URL}}"
      ]
    }
  }
}
```

```bash
# .env.development
DATABASE_URL=postgresql://localhost:5432/myapp_dev

# .env.staging
DATABASE_URL=postgresql://staging-db.example.com:5432/myapp_staging

# .env.production
DATABASE_URL=postgresql://prod-db.example.com:5432/myapp_prod
```

```bash
# 환경별 .env 파일 로드
cp .env.development .env  # 개발 환경
cp .env.staging .env      # 스테이징 환경
```

**방법 2: wrapper 스크립트**:
```bash
#!/bin/bash
# scripts/mcp-postgres.sh

ENV=${NODE_ENV:-development}

case $ENV in
  development)
    DB_URL="postgresql://localhost:5432/myapp_dev"
    ;;
  staging)
    DB_URL="postgresql://staging-db.internal:5432/myapp"
    ;;
  production)
    DB_URL="postgresql://prod-db.internal:5432/myapp"
    ;;
esac

exec npx -y @modelcontextprotocol/server-postgres "$DB_URL"
```

```json
{
  "mcpServers": {
    "postgres": {
      "command": "bash",
      "args": ["./scripts/mcp-postgres.sh"],
      "env": {
        "NODE_ENV": "${{env.NODE_ENV}}"
      }
    }
  }
}
```

> 실전 팁: 프로덕션 데이터베이스에 연결하는 MCP 서버는 반드시 읽기 전용 사용자를 사용하라. `query` 도구가 `DROP TABLE`이나 `DELETE`를 실행하는 것을 방지하기 위해 DB 레벨에서 권한을 제한해야 한다.

---

## 9. 트러블슈팅

### 일반적인 오류와 해결법

#### 1. 서버 연결 실패: "Failed to connect to MCP server"

**원인**: 서버 바이너리를 찾을 수 없거나 실행 실패
```
Error: Failed to connect to MCP server 'github': spawn npx ENOENT
```

**해결**:
```bash
# npx가 설치되어 있는지 확인
which npx
# 없으면 Node.js 설치
# macOS: brew install node
# Ubuntu: sudo apt install nodejs npm

# 패키지를 직접 설치하여 테스트
npx -y @modelcontextprotocol/server-github --help
```

#### 2. 환경변수 미설정: "Environment variable not found"

**원인**: `${{env.VAR}}` 템플릿이 치환되지 않음
```
Error: Environment variable GITHUB_TOKEN is not set
```

**해결**:
```bash
# 환경변수 확인
echo $GITHUB_TOKEN

# .env 파일에 설정
echo 'GITHUB_TOKEN=ghp_your_token_here' >> .env

# 또는 시스템 환경변수로 설정
export GITHUB_TOKEN=ghp_your_token_here
```

#### 3. JSON 파싱 오류: "Unexpected token in .mcp.json"

**원인**: `.mcp.json` 파일의 JSON 문법 오류
```
Error: Unexpected token ',' at position 245 in .mcp.json
```

**해결**:
```bash
# JSON 문법 검증
cat .mcp.json | python3 -m json.tool

# 흔한 실수: 마지막 항목 뒤의 쉼표 (trailing comma)
# 잘못된 예:
# { "mcpServers": { "github": { ... }, } }
#                                      ^ 이 쉼표 제거
```

#### 4. 권한 거부: "Permission denied"

**원인**: 서버 스크립트의 실행 권한 없음
```
Error: spawn /path/to/server.sh EACCES
```

**해결**:
```bash
# 실행 권한 부여
chmod +x /path/to/server.sh

# 또는 bash로 실행하도록 설정 변경
# "command": "bash", "args": ["/path/to/server.sh"]
```

#### 5. 포트 충돌: "Address already in use"

**원인**: SSE/HTTP 서버가 사용할 포트가 이미 점유됨
```
Error: listen EADDRINUSE: address already in use :::3000
```

**해결**:
```bash
# 포트 사용 중인 프로세스 확인
lsof -i :3000

# 프로세스 종료
kill -9 <PID>

# 또는 다른 포트 사용
# "args": ["--port", "3001"]
```

#### 6. 타임아웃: "Server initialization timed out"

**원인**: 서버 시작이 너무 오래 걸림 (npm 패키지 다운로드 등)
```
Error: Server 'heavy-server' initialization timed out after 30000ms
```

**해결**:
```bash
# 패키지를 미리 설치하여 npx 다운로드 시간 제거
npm install -g @example/mcp-heavy-server

# 설정에서 글로벌 설치된 바이너리 직접 사용
# "command": "mcp-heavy-server" (npx 대신)
```

#### 7. 프로토콜 버전 불일치: "Protocol version mismatch"

**원인**: 클라이언트와 서버의 프로토콜 버전이 호환되지 않음
```
Error: Server requires protocol version 2025-03-26, client supports 2024-11-05
```

**해결**:
```bash
# Claude Code 업데이트
npm update -g @anthropic-ai/claude-code

# 또는 MCP 서버 패키지 업데이트
npx -y @modelcontextprotocol/server-github@latest
```

#### 8. 메모리 부족: "JavaScript heap out of memory"

**원인**: 대량 데이터를 처리하는 MCP 서버가 메모리 제한 초과
```
FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
```

**해결**:
```json
{
  "mcpServers": {
    "heavy-server": {
      "command": "node",
      "args": ["--max-old-space-size=4096", "/path/to/server.js"],
      "env": {
        "NODE_OPTIONS": "--max-old-space-size=4096"
      }
    }
  }
}
```

#### 9. SSL/TLS 오류: "UNABLE_TO_VERIFY_LEAF_SIGNATURE"

**원인**: 원격 MCP 서버의 SSL 인증서 문제
```
Error: unable to verify the first certificate
```

**해결**:
```bash
# 인증서 체인 확인
openssl s_client -connect mcp.example.com:443 -showcerts

# 기업 프록시 환경의 경우 CA 인증서 설정
export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca.crt
```

#### 10. 도구 호출 실패: "Tool execution failed"

**원인**: MCP 서버의 도구 실행 중 내부 오류
```
Error: Tool 'query_database' failed: connection refused
```

**해결**:
```bash
# 서버가 의존하는 외부 서비스 확인
# PostgreSQL 서버의 경우: DB 연결 확인
psql $DATABASE_URL -c "SELECT 1"

# GitHub 서버의 경우: 토큰 유효성 확인
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user

# 서버 stderr 로그 확인 (수동 실행 시)
npx -y @modelcontextprotocol/server-postgres $DATABASE_URL 2>server.log
```

### 디버그 모드 활성화

MCP 서버의 상세한 로그를 확인하려면 환경변수로 디버그 모드를 활성화한다.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}",
        "DEBUG": "mcp:*",
        "LOG_LEVEL": "debug"
      }
    }
  }
}
```

### 로그 확인 방법

Claude Code의 MCP 관련 로그는 여러 위치에서 확인할 수 있다.

```bash
# Claude Code 로그 디렉토리
ls ~/.claude/logs/

# MCP 서버 stderr 출력 확인 (수동 실행 시)
npx -y @modelcontextprotocol/server-github 2>&1 | tee /tmp/mcp-github.log

# macOS에서 최근 로그 확인
log show --predicate 'process == "claude"' --last 1h
```

### 네트워크 문제 진단

원격 MCP 서버(SSE/HTTP) 연결 문제 진단이다.

```bash
# 서버 접근 가능 여부 확인
curl -v https://mcp.example.com/sse

# DNS 해상도 확인
nslookup mcp.example.com

# 포트 접근 확인
nc -zv mcp.example.com 443

# 프록시 환경에서의 연결 테스트
curl -v --proxy $HTTP_PROXY https://mcp.example.com/sse
```

### 버전 호환성 이슈

MCP 생태계가 빠르게 발전하므로 버전 호환성 문제가 발생할 수 있다.

```bash
# Claude Code 버전 확인
claude --version

# MCP 서버 패키지 버전 확인
npm list -g @modelcontextprotocol/server-github

# 최신 버전으로 업데이트
npm update -g @anthropic-ai/claude-code
npm update -g @modelcontextprotocol/server-github

# 특정 버전 고정 (팀 일관성을 위해)
# .mcp.json에서 버전 명시
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github@0.6.2"]
    }
  }
}
```

| Claude Code 버전 | 지원 MCP 프로토콜 | 비고 |
|-----------------|-----------------|------|
| 1.0.x | 2024-11-05 | stdio, SSE |
| 1.1.x+ | 2025-03-26 | + Streamable HTTP |

> 실전 팁: 트러블슈팅의 첫 단계는 항상 서버를 수동으로 실행하여 stderr 출력을 확인하는 것이다. `npx -y @server/package 2>&1`로 실행하면 대부분의 오류 원인을 즉시 파악할 수 있다.

---

## 10. 관련 문서 링크

### 이 지식 센터의 다른 문서

MCP 관련 심화 주제는 다음 문서에서 다룬다.

| 문서 | 내용 | 적합한 독자 |
|------|------|-----------|
| [01-MCP-서버-개발-가이드.md](./01-MCP-서버-개발-가이드.md) | TypeScript/Python SDK로 커스텀 MCP 서버 개발. 프로젝트 초기 설정, 도구/리소스/프롬프트 구현, 테스트, 배포까지. | 서버 개발자 |
| [02-MCP-보안-인증-가이드.md](./02-MCP-보안-인증-가이드.md) | OAuth 2.1 인증 플로우, 토큰 관리, 입력 검증, rate limiting, 감사 로깅. 프로덕션 보안 체크리스트. | 보안 엔지니어, 서버 운영자 |
| [03-MCP-실전-패턴-모음.md](./03-MCP-실전-패턴-모음.md) | DB 연동, GitHub 자동화, 모니터링, 슬랙 알림 등 실전 통합 패턴. 복사해서 바로 쓸 수 있는 완성된 서버 코드. | 실무 개발자 |
| [04-MCP-서버-카탈로그.md](./04-MCP-서버-카탈로그.md) | 인기 MCP 서버 100선. 카테고리별 분류, 설정 예시, 평점, 활용 시나리오. | 모든 사용자 |
| [Awesome-MCP-Servers-한국어-가이드.md](./Awesome-MCP-Servers-한국어-가이드.md) | **2596개+ MCP 서버** 한국어 종합 카탈로그. 32개 카테고리, 4개 출처 통합. | 모든 사용자 |

### 문서 간 관계

```mermaid
graph TB
    README["README.md<br/>(현재 문서)<br/>MCP 종합 가이드"]

    DEV["01-MCP-서버-개발-가이드.md<br/>커스텀 서버 개발"]
    SEC["02-MCP-보안-인증-가이드.md<br/>보안 & 인증"]
    PAT["03-MCP-실전-패턴-모음.md<br/>통합 패턴"]
    CAT["04-MCP-서버-카탈로그.md<br/>서버 카탈로그"]
    AWE["Awesome-MCP-Servers-한국어-가이드.md<br/>2596개+ 서버 종합"]

    README -->|"서버 개발하기"| DEV
    README -->|"보안 강화하기"| SEC
    README -->|"실전 활용하기"| PAT
    README -->|"서버 찾기"| CAT
    README -->|"전체 서버 탐색"| AWE

    DEV -->|"보안 적용"| SEC
    DEV -->|"패턴 참조"| PAT
    PAT -->|"서버 활용"| CAT
    SEC -->|"서버 보안 강화"| DEV
```

### 학습 경로

MCP를 처음 접하는 경우 다음 순서로 학습하는 것을 권장한다.

```mermaid
graph LR
    A["1. README.md<br/>(현재 문서)<br/>핵심 개념 이해"] --> B["2. 서버 카탈로그<br/>인기 서버 설치<br/>및 사용"]
    B --> C["3. 실전 패턴<br/>통합 시나리오<br/>구현"]
    C --> D["4. 서버 개발<br/>커스텀 서버<br/>직접 구현"]
    D --> E["5. 보안 가이드<br/>프로덕션<br/>보안 강화"]
```

### 외부 참조

**공식 문서**:
- [MCP 공식 사양](https://spec.modelcontextprotocol.io/) — 프로토콜 전체 스펙
- [MCP 공식 문서](https://modelcontextprotocol.io/docs) — 가이드 및 튜토리얼
- [MCP GitHub](https://github.com/modelcontextprotocol) — 소스 코드 및 이슈

**SDK**:
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — Node.js/TypeScript용 MCP SDK
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) — Python용 MCP SDK
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) — JVM/Kotlin용 MCP SDK

**서버 레지스트리**:
- [MCP 공식 서버](https://github.com/modelcontextprotocol/servers) — Anthropic 공식 서버 모음
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) — 커뮤니티 큐레이션 서버 목록
- [mcp.so](https://mcp.so/) — MCP 서버 검색 엔진
- [Smithery](https://smithery.ai/) — MCP 서버 레지스트리 및 설치 도구

**Claude Code 문서**:
- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code) — Claude Code 전체 가이드
- [Claude Code MCP 설정](https://docs.anthropic.com/en/docs/claude-code/mcp) — MCP 서버 설정 가이드

**관련 사양**:
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) — MCP의 기반 프로토콜
- [JSON Schema](https://json-schema.org/) — 도구 입력 스키마 정의
- [OAuth 2.1](https://oauth.net/2.1/) — MCP 인증 프레임워크

---

## 부록

### A. MCP 설정 치트시트

**최소 설정 (로컬 파일시스템 접근)**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

**일반적인 개발 환경 설정**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${{env.DATABASE_URL}}"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

**풀스택 프로젝트 설정**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{env.GITHUB_TOKEN}}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${{env.DATABASE_URL}}"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${{env.BRAVE_API_KEY}}"
      }
    },
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### B. CLI 명령어 레퍼런스

```bash
# 서버 추가
claude mcp add <name> [--scope user|project] [--transport stdio|sse|http] [-e KEY=VALUE] -- <command> [args...]

# 서버 목록
claude mcp list

# 서버 상세 정보
claude mcp get <name>

# 서버 제거
claude mcp remove <name>

# 서버 재시작
claude mcp restart [name]

# SSE/HTTP 서버 추가
claude mcp add <name> --transport sse --url <url>
claude mcp add <name> --transport http --url <url>

# 환경변수 포함 추가
claude mcp add <name> -e API_KEY=xxx -e SECRET=yyy -- npx -y @example/server
```

### C. JSON-RPC 메서드 레퍼런스

| 메서드 | 방향 | 설명 |
|--------|------|------|
| `initialize` | Client → Server | 연결 초기화, capability 교환 |
| `notifications/initialized` | Client → Server | 초기화 완료 알림 |
| `tools/list` | Client → Server | 사용 가능한 도구 목록 조회 |
| `tools/call` | Client → Server | 도구 실행 |
| `resources/list` | Client → Server | 리소스 목록 조회 |
| `resources/read` | Client → Server | 리소스 읽기 |
| `resources/templates/list` | Client → Server | 리소스 템플릿 목록 조회 |
| `resources/subscribe` | Client → Server | 리소스 변경 구독 |
| `prompts/list` | Client → Server | 프롬프트 목록 조회 |
| `prompts/get` | Client → Server | 프롬프트 가져오기 |
| `sampling/createMessage` | Server → Client | 역방향 LLM 호출 |
| `notifications/tools/list_changed` | Server → Client | 도구 목록 변경 알림 |
| `notifications/resources/updated` | Server → Client | 리소스 업데이트 알림 |
| `notifications/resources/list_changed` | Server → Client | 리소스 목록 변경 알림 |
| `ping` | 양방향 | 연결 상태 확인 |

### D. 오류 코드 레퍼런스

| 코드 | 이름 | 설명 |
|------|------|------|
| `-32700` | ParseError | JSON 파싱 실패 |
| `-32600` | InvalidRequest | 유효하지 않은 JSON-RPC 요청 |
| `-32601` | MethodNotFound | 메서드를 찾을 수 없음 |
| `-32602` | InvalidParams | 파라미터가 유효하지 않음 |
| `-32603` | InternalError | 서버 내부 오류 |

### E. 용어 사전

| 용어 | 설명 |
|------|------|
| **MCP** | Model Context Protocol. AI 모델과 외부 도구 연결 표준 프로토콜 |
| **Host** | MCP Client를 포함하는 최상위 애플리케이션 (Claude Desktop, Claude Code 등) |
| **Client** | Host 내부에서 특정 MCP Server와의 1:1 연결을 관리하는 모듈 |
| **Server** | 외부 시스템과의 실제 통합을 수행하며 도구/리소스/프롬프트를 제공하는 프로세스 |
| **Transport** | Client-Server 간 메시지 전달 방식 (stdio, SSE, Streamable HTTP) |
| **Tool** | 모델이 호출하는 함수. 부작용을 가질 수 있음 |
| **Resource** | 서버가 제공하는 읽기 전용 데이터. URI로 식별 |
| **Prompt** | 재사용 가능한 프롬프트 템플릿. 사용자가 명시적으로 선택 |
| **Sampling** | 서버가 Host의 LLM에게 역방향으로 텍스트 생성을 요청하는 패턴 |
| **Capability** | 클라이언트/서버가 지원하는 기능 집합. 초기화 시 교환 |
| **JSON-RPC 2.0** | MCP의 기반 통신 프로토콜. 요청/응답/알림 메시지 형식 |
| **Primitive** | MCP의 핵심 구성 요소 (Tool, Resource, Prompt, Sampling) |
| **stdio** | Standard I/O. 로컬 프로세스의 표준 입출력을 통한 통신 방식 |
| **SSE** | Server-Sent Events. HTTP 기반 단방향 스트리밍 통신 |
| **Streamable HTTP** | MCP 최신 Transport. 단일 HTTP 엔드포인트로 양방향 통신 |
| **inputSchema** | JSON Schema로 정의된 도구의 입력 파라미터 스키마 |
| **URI Template** | RFC 6570 기반의 동적 리소스 주소 템플릿 (`db://app/table/{name}`) |

---

> 이 문서는 MCP의 핵심 개념과 실전 설정을 다루는 종합 가이드이다. 커스텀 서버 개발, 보안 강화, 실전 패턴, 서버 카탈로그에 대한 심화 내용은 각각의 전용 문서를 참조하라.
