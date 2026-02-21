# 멀티에이전트 & 오케스트레이션 논문 종합 조사

> 2023~2026년 멀티에이전트 소프트웨어 개발 관련 핵심 논문을 조사하고,
> Octo Orchestra에 적용할 수 있는 아이디어를 추출한 문서.
> 2026-02-17 작성.
---

## 목차

1. [논문 목록 요약표](#1-논문-목록-요약표)
2. [역할 기반 에이전트 시스템](#2-역할-기반-에이전트-시스템)
3. [오케스트레이션 아키텍처](#3-오케스트레이션-아키텍처)
4. [코드 생성 특화 멀티에이전트](#4-코드-생성-특화-멀티에이전트)
5. [실전 소프트웨어 엔지니어링 에이전트](#5-실전-소프트웨어-엔지니어링-에이전트)
6. [실패 분석 & 도전 과제](#6-실패-분석--도전-과제)
7. [Octo Orchestra에 착용할 핵심 아이디어](#7-octo-orchestra에-착용할-핵심-아이디어)

---

## 1. 논문 목록 요약표

| # | 논문명 | 발표 | 핵심 기여 | 적용 가능성 |
|---|--------|------|-----------|-------------|
| 1 | ChatDev | ACL 2024 | Chat Chain + 역할 기반 소프트웨어 개발 가상 회사 | ★★★ 역할 정의 |
| 2 | MetaGPT | ICLR 2024 | SOP 기반 문서 소통, 조립 라인 패러다임 | ★★★ 구조화된 산출물 |
| 3 | Evolving Orchestration | NeurIPS 2025 | RL 기반 동적 오케스트레이터 (Puppeteer) | ★★ 적응형 순서 |
| 4 | Cross-Team (Croto) | 2024 | 독립 팀 병렬 → 교차 협업 | ★★★ 병렬 팀 패턴 |
| 5 | AgentOrchestra (TEA) | 2025 | Tool-Environment-Agent 라이프사이클 | ★★ 라이프사이클 |
| 6 | MapCoder | ACL 2024 | 4단계 코드 생성 파이프라인 | ★★ 계획→코드→디버그 |
| 7 | AgentCoder | 2023 | Programmer-Tester-Executor 반복 | ★★★ Maker-Checker |
| 8 | SWE-agent | 2024 | Agent-Computer Interface (ACI) 설계 | ★★ 인터페이스 |
| 9 | Live-SWE-agent | 2025 | 런타임 자기 진화, 77.4% SWE-bench | ★ 자기 개선 |
| 10 | TDAG | Neural Networks | 동적 작업 분해 + 하위 에이전트 자동 생성 | ★★ 동적 분해 |
| 11 | MAS 실패 분석 (MAST) | 2025 | 14가지 실패 모드 분류, 1600+ 트레이스 | ★★★ 실패 예방 |
| 12 | MAS Challenges | 2024 | 작업 할당, 추론, 컨텍스트, 메모리 도전 | ★★ 설계 참고 |
| 13 | HyperAgent | 2024 | Planner-Navigator-Editor-Executor 범용 | ★★ 역할 모델 |
| 14 | MAS for SE Survey | ACM TOSEM | SDLC 전 단계에서의 MAS 종합 분석 | ★★★ 전체 조감 |

---

## 2. 역할 기반 에이전트 시스템

### 2-1. ChatDev — 대화 기반 가상 소프트웨어 회사

**논문**: [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) (ACL 2024)

**아키텍처**:
```
CEO → CTO → Programmer → Code Reviewer → Tester → Designer
         ↓
    4단계 순차 파이프라인
    설계(Design) → 코딩(Coding) → 테스팅(Testing) → 문서화(Documenting)
```

**핵심 메커니즘**:
- **Chat Chain**: 전체 프로세스를 원자적 채팅 세션으로 분해. 각 세션에서 두 역할이 대화로 하위 작업 해결
- **역할 플레이**: 각 에이전트에 시스템 프롬프트로 구체적 역할 부여 (CEO, CTO, 프로그래머, 아트 디자이너 등)
- **Communicative Dehallucination**: 에이전트 간 대화로 환각 감소. 자연어 + 프로그래밍 언어 혼합 사용

**핵심 발견**:
- 자연어는 시스템 설계에, 프로그래밍 언어는 디버깅에 효과적
- 언어가 멀티에이전트 협업의 통합 브릿지 역할
- 단일 에이전트(GPT-Engineer) 대비 완성도, 실행성, 일관성, 품질 모두 우수

**Octo Orchestra 적용 포인트**:
- 에이전트별 명확한 역할 시스템 프롬프트 → 우리의 `[GOAL]`, `[STEPS]` 형식과 일치
- Chat Chain처럼 작업을 원자적으로 분해하는 것이 핵심

---

### 2-2. MetaGPT — SOP 기반 문서 소통

**논문**: [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) (ICLR 2024)

**아키텍처**:
```
Product Manager → Architect → Project Manager → Engineer → QA Engineer
         ↓
    SOP로 연결된 조립 라인 (Assembly Line)
    PRD → System Design → Task List → Code → Test Report
```

**핵심 메커니즘**:
- **구조화된 SOP**: 사람 조직의 표준 운영 절차를 프롬프트 시퀀스로 인코딩
- **문서 기반 소통**: ChatDev의 대화 기반과 달리, 에이전트 간 **구조화된 문서**(PRD, 시스템 설계서, 태스크 목록)로 소통
- **중간 결과 검증**: 전문 도메인 지식을 가진 에이전트가 중간 산출물 검증

**ChatDev vs MetaGPT 핵심 차이**:

| 특성 | ChatDev | MetaGPT |
|------|---------|---------|
| 소통 방식 | 에이전트 간 **대화** | 에이전트 간 **구조화된 문서** |
| 구조 | Chat Chain (순차 채팅) | Assembly Line (조립 라인) |
| 환각 방지 | 대화 중 상호 검증 | 문서화된 SOP + 중간 검증 |
| 장점 | 유연한 협업 | 정보 누락/무관한 내용 방지 |

**핵심 발견**:
- 구조화된 산출물이 대화보다 정보 전달에 효과적
- SOP를 프롬프트에 인코딩하면 cascading hallucination 방지
- 더 복잡한 작업에서 일관성 높은 솔루션 생성

**Octo Orchestra 적용 포인트**:
- 비서 모드의 계획 수립 시 **구조화된 문서 형식**(PRD → 태스크 분해 → 파일 할당) 채택 → 이미 적용 중
- 에이전트 간 소통이 필요할 때 대화보다 **파일 기반 산출물**이 더 신뢰성 높음
- SOP를 프롬프트에 인코딩 → 우리의 `[STEPS]`, `[VERIFY]` 섹션과 일맥상통

---

### 2-3. HyperAgent — 범용 4역할 시스템

**논문**: [HyperAgent: Generalist Software Engineering Agents](https://openreview.net/forum?id=PZf4RsPMBG) (2024)

**4 에이전트 역할**:
```
Planner → Navigator → Code Editor → Executor
(계획)    (탐색)      (편집)         (실행/테스트)
```

- **Planner**: 자연어 요구사항을 실행 가능한 계획으로 변환
- **Navigator**: 코드베이스를 탐색하여 관련 파일/함수 식별
- **Code Editor**: 실제 코드 수정 수행
- **Executor**: 테스트 실행 및 결과 검증

다양한 프로그래밍 언어에서 SE 작업의 전체 라이프사이클 관리.

**Octo Orchestra 적용 포인트**:
- 계획(Plan) → 탐색(Navigate) → 편집(Code) → 검증(Test)의 명확한 4단계
- 이 단계를 각 에이전트의 `[STEPS]`에 반영 가능

---

## 3. 오케스트레이션 아키텍처

### 3-1. Evolving Orchestration — RL 기반 Puppeteer

**논문**: [Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591) (NeurIPS 2025)

**핵심 아이디어**:
```
Puppeteer (오케스트레이터, RL로 학습)
    ↓ 동적 활성화/순서 결정
Puppet 1, Puppet 2, ... Puppet N (전문 에이전트)
```

- **정적 구조의 한계**: 기존 멀티에이전트 시스템은 고정된 조직 구조 → 작업 복잡도와 에이전트 수 증가 시 조율 오버헤드 급증
- **Puppeteer 패러다임**: 중앙 오케스트레이터가 **강화학습**으로 최적 에이전트 순서/우선순위 학습
- **진화하는 구조**: 작업 상태에 따라 동적으로 에이전트 활성화/비활성화

**핵심 발견**:
- 핵심 개선은 오케스트레이터 진화에 의한 **더 간결하고 순환적인 추론 구조**에서 발생
- 정적 접근 대비 **성능 향상 + 계산 비용 감소** 동시 달성

**Octo Orchestra 적용 포인트**:
- 현재 우리의 에이전트 실행은 "모두 동시 시작" 고정 패턴
- 향후: 에이전트 완료 순서에 따라 다음 에이전트 작업 동적 조정 가능
- 예: A 에이전트가 API 모듈 완성 → B 에이전트에게 알려서 해당 API 사용하도록 컨텍스트 갱신

---

### 3-2. Cross-Team Orchestration (Croto) — 병렬 팀 + 교차 협업

**논문**: [Multi-Agent Collaboration via Cross-Team Orchestration](https://arxiv.org/abs/2406.08979) (2024)

**핵심 아이디어**:
```
Team A ─→ Solution A ──┐
Team B ─→ Solution B ──┼→ Cross-Team Insight Exchange → Best Solution
Team C ─→ Solution C ──┘
```

- **단일 팀의 한계**: 한 팀 = 한 번에 한 결과물 → 해결 경로 탐색 부족
- **Croto 해법**: 여러 독립 팀이 **동시에 다른 솔루션 경로 탐색**
- **교차 협업**: 각 팀의 독립성 유지 + 인사이트 교환으로 최적 솔루션 도출

**핵심 발견**:
- 단일 팀 시스템 대비 **소프트웨어 품질 유의미하게 향상**
- 스토리 생성에도 적용 가능한 **일반화 능력** 입증

**Octo Orchestra 적용 포인트**:
- 이것이 바로 우리의 **git worktree 기반 병렬 에이전트** 패턴!
- 각 에이전트가 독립적으로 자기 파일에서 작업 = 팀 독립성
- 머지 단계에서 최적 결과 통합 = 교차 협업
- **개선 아이디어**: 에이전트 완료 후 서로의 결과를 리뷰하는 "교차 검증" 단계 추가

---

### 3-3. AgentOrchestra — TEA 프로토콜 라이프사이클

**논문**: [AgentOrchestra: Orchestrating Multi-Agent Intelligence with TEA Protocol](https://arxiv.org/abs/2506.12508) (2025)

**TEA 프로토콜**:
```
Tool ←→ Environment ←→ Agent
  각각 일급 자원(first-class resource)
  명시적 라이프사이클 + 버전 관리 인터페이스
```

- **계층적 오케스트레이션**: 중앙 플래너 → 전문 서브에이전트 → 동적 도구 인스턴스화
- **자기 진화**: 피드백 루프를 통한 컴포넌트 자기 개선 + 버전 롤백 지원
- **GAIA 벤치마크 89.04%** (SOTA)

**핵심 혁신**:
- 라이프사이클과 버전 관리를 원칙적으로 추상화
- 실행 중 동적 도구 정제
- 폐쇄 루프 컴포넌트 진화

**Octo Orchestra 적용 포인트**:
- 에이전트/도구/환경의 **라이프사이클 관리** 개념 → 우리의 워크트리 라이프사이클(preflight → running → merging → cleanup)과 일치
- **버전 관리**: 에이전트 작업 결과를 git 커밋으로 자동 버전 관리 → 이미 적용 중
- **롤백**: 머지 실패 시 브랜치 보존 → 이미 설계 중

---

### 3-4. TDAG — 동적 작업 분해 + 하위 에이전트 자동 생성

**논문**: [TDAG: A Multi-Agent Framework based on Dynamic Task Decomposition and Agent Generation](https://arxiv.org/abs/2402.10178) (Neural Networks, 2024)

**핵심 아이디어**:
```
Complex Task
    ↓ 동적 분해
Subtask 1 → Generated Subagent 1
Subtask 2 → Generated Subagent 2
Subtask N → Generated Subagent N
```

- **동적 분해**: 미리 정해진 분해가 아닌, 작업 진행 중 점진적으로 하위 작업 발견
- **에이전트 자동 생성**: 각 하위 작업에 맞춤형 에이전트 생성 (범용 에이전트가 아님)
- **적응성**: 다양하고 예측 불가능한 실세계 작업에 적응

**Octo Orchestra 적용 포인트**:
- 현재: 비서가 사전에 모든 에이전트를 계획 → **정적** 분해
- TDAG 방식: 에이전트 실행 중 새로운 하위 작업 발견 시 **동적으로 추가 에이전트** 생성
- 향후 고려: 비서 에이전트가 진행 상황을 모니터링하다가 필요한 추가 작업을 감지하여 새 에이전트 자동 생성

---

## 4. 코드 생성 특화 멀티에이전트

### 4-1. MapCoder — 4단계 인간 개발자 모방

**논문**: [MapCoder: Multi-Agent Code Generation for Competitive Problem Solving](https://arxiv.org/abs/2405.11403) (ACL 2024)

**4단계 파이프라인**:
```
Retrieval Agent → Planning Agent → Coding Agent → Debugging Agent
  (유사 예제 검색)   (알고리즘 설계)    (코드 생성)     (에러 수정)
```

- 인간 개발자의 전체 프로그램 합성 사이클을 그대로 모방
- 각 에이전트의 출력이 다음 에이전트의 in-context learning 신호가 됨

**벤치마크 성과** (pass@1):

| 벤치마크 | MapCoder | 이전 SOTA |
|----------|----------|----------|
| HumanEval | **93.9%** | - |
| MBPP | **83.1%** | - |
| CodeContests | **28.5%** | - |

**Octo Orchestra 적용 포인트**:
- Retrieval(검색) 단계의 중요성 → 계획 수립 시 **코드베이스 탐색**을 필수 1단계로 포함 (이미 적용: Explore → Map → Partition → Save)
- Planning → Coding → Debugging 순서 → 각 에이전트의 `[STEPS]`에 "먼저 계획 → 코드 → 테스트" 순서 명시

---

### 4-2. AgentCoder — Programmer-Tester-Executor 반복

**논문**: [AgentCoder: Multi-Agent Code Generation with Iterative Testing and Optimisation](https://arxiv.org/abs/2312.13010) (2023)

**3역할 반복 루프**:
```
Programmer Agent ──→ Test Designer Agent ──→ Test Executor Agent
       ↑                                           │
       └───────── 피드백 (실패한 테스트 결과) ←──────┘
```

- **Programmer**: 코드 생성/수정
- **Test Designer**: 테스트 케이스 생성
- **Test Executor**: 테스트 실행 → 결과를 Programmer에게 피드백

**벤치마크 성과**:

| 벤치마크 | AgentCoder | 이전 SOTA | 토큰 사용량 |
|----------|-----------|----------|------------|
| HumanEval | **96.3%** | 90.2% | 56.9K (vs 138.2K) |
| MBPP | **91.8%** | 78.9% | 66.3K (vs 206.5K) |

**핵심 발견**: 전문 에이전트의 반복 피드백이 단일 에이전트 + 복잡한 프롬프트보다 **정확도 높고 토큰 비용 낮음**.

**Octo Orchestra 적용 포인트**:
- **Maker-Checker 패턴**의 실증적 유효성 입증
- 각 에이전트의 프롬프트에 "코드 작성 후 반드시 테스트" 지시 → 이미 `[VERIFY]` 섹션에 포함
- **향후**: 별도의 테스트 에이전트를 두어 다른 에이전트의 코드를 자동 검증

---

## 5. 실전 소프트웨어 엔지니어링 에이전트

### 5-1. SWE-agent — Agent-Computer Interface

**논문**: [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) (2024)

**핵심 통찰**: LLM 에이전트는 **새로운 종류의 사용자**이며, 인간 UI와 다른 **전용 인터페이스**(ACI)가 필요하다.

- 파일 생성/편집, 저장소 탐색, 프로그램 실행에 최적화된 커스텀 인터페이스
- SWE-bench 12.5% pass@1 (당시 SOTA)
- 인터페이스 설계가 에이전트 성능에 직접 영향

**Octo Orchestra 적용 포인트**:
- 에이전트에게 제공하는 **도구/인터페이스의 품질**이 결과에 직결
- CLI 에이전트(Claude, Codex, Kimi)는 이미 자체 ACI를 갖고 있으므로, 우리는 **프롬프트 품질**과 **환경 설정**(worktree, 파일 구조)에 집중

---

### 5-2. Live-SWE-agent — 런타임 자기 진화

**논문**: [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646) (2025)

**혁신**: 가장 기본적인 bash 도구만 가진 에이전트에서 시작 → **실행 중에 자기 스캐폴드를 자율적으로 진화**

- 별도의 오프라인 학습 없이 문제 풀면서 동시에 자기 개선
- SWE-bench Verified **77.4%** (전체 에이전트 중 최고, 독점 솔루션 포함)
- SWE-bench Pro **45.8%** (수작업 설계 에이전트 초과)

**Octo Orchestra 적용 포인트**:
- 장기적 비전: 오케스트라 비서가 반복 사용하면서 **더 나은 계획 수립/에이전트 할당 전략을 학습**
- 단기적: 오케스트레이션 결과(성공/실패)를 로그로 저장 → 다음 계획 수립 시 참고

---

### 5-3. Agentless — 에이전트 없이도 가능

**참고**: Agentless는 LLM에게 미래 행동 결정이나 복잡한 도구 사용 없이 3단계로 문제 해결:

```
Localization → Repair → Patch Validation
(문제 위치 찾기) (수정 생성) (패치 검증)
```

**Octo Orchestra 시사점**:
- 모든 작업에 복잡한 에이전트 오케스트레이션이 필요한 것은 아님
- 단순한 버그 수정은 단일 에이전트가 더 효율적일 수 있음
- **적절한 복잡도 선택**이 중요 (Microsoft의 "가장 낮은 복잡도" 원칙과 일치)

---

## 6. 실패 분석 & 도전 과제

### 6-1. MAST — 멀티에이전트 시스템 실패 분류 체계

**논문**: [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (2025)

**데이터**: 7개 프레임워크에서 1,600+ 트레이스 수집, 14가지 실패 모드 분류

**3대 실패 카테고리**:

#### 카테고리 1: 시스템 설계 문제
- 부적절한 작업 분배
- 에이전트 역할 중복/충돌
- 오케스트레이션 로직 결함

#### 카테고리 2: 에이전트 간 불일치
- 에이전트 간 소통 실패
- 컨텍스트 손실/왜곡
- 상충되는 행동

#### 카테고리 3: 작업 검증 문제
- 결과물 검증 부재
- 요구사항과 결과 불일치
- 완료 조건 모호

**높은 일치도**: inter-annotator agreement κ = 0.88 (매우 높음)

**Octo Orchestra에서의 대응 전략**:

| 실패 유형 | 우리의 대응 |
|-----------|-------------|
| 작업 분배 문제 | 파일 소유권 명확 할당 (`[OWN FILES]` + `[DO NOT TOUCH]`) |
| 역할 중복 | 각 에이전트에 고유한 `[GOAL]`과 `[FILES]` |
| 소통 실패 | 현재: 독립 실행 (소통 불필요). 향후: 비서 모니터링 |
| 컨텍스트 손실 | 파일 기반 프롬프트로 완전한 컨텍스트 전달 |
| 검증 부재 | `[VERIFY]` 섹션에 검증 단계 필수 포함 |
| 완료 조건 모호 | PTY alive 체크 + 커밋 카운트로 객관적 완료 판단 |

---

### 6-2. LLM Multi-Agent Systems: Challenges and Open Problems

**논문**: [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578) (2024, 2026 개정)

**4대 도전 과제**:

1. **작업 할당 최적화**: 다양한 능력의 에이전트에게 효율적 작업 분배
2. **추론 강화**: 반복적 토론으로 협력적 의사결정 강화
3. **컨텍스트 관리**: 다중 에이전트 간 복잡하고 계층적인 컨텍스트 정보 관리
4. **메모리 시스템**: 에이전트 상호작용을 지원하는 견고한 메모리 아키텍처

---

## 7. Octo Orchestra에 착용할 핵심 아이디어

논문들에서 추출한 핵심 아이디어를 Octo Orchestra의 현재 구현과 대조하고,
즉시 적용 가능한 것과 향후 로드맵으로 분류한다.

### 즉시 적용 가능 (Short-term)

#### A. 에이전트 프롬프트에 "역할 시스템" 강화
> 출처: ChatDev, MetaGPT, HyperAgent

현재 우리의 에이전트 프롬프트에 `[GOAL]`, `[STEPS]`, `[VERIFY]`가 있지만,
**명시적 역할 정체성**이 부족하다.

**적용**: 각 에이전트 프롬프트 시작에 역할 선언 추가
```
[ROLE] You are a senior backend developer specializing in Rust and Tauri.
You are methodical, write tests first, and never modify files outside your scope.
```

이것이 ChatDev에서 입증된 "역할 플레이"의 핵심 — 역할을 부여하면 해당 분야의 전문성이 활성화된다.

---

#### B. 계획 산출물을 구조화된 문서로
> 출처: MetaGPT

현재 비서의 계획은 JSON 형태의 에이전트 할당이지만,
MetaGPT처럼 **PRD → System Design → Task List** 계층 구조를 도입하면 더 나은 계획이 나온다.

**적용**: 비서 계획 프롬프트에 단계 추가
```
Phase 1: Write a brief PRD (what we're building, why, key constraints)
Phase 2: Design the approach (architecture, data flow)
Phase 3: Decompose into agent tasks with file assignments
Phase 4: Write JSON output
```

---

#### C. `[VERIFY]` 섹션을 AgentCoder식 테스트 루프로 강화
> 출처: AgentCoder, MapCoder

현재 `[VERIFY]`는 "확인하라" 수준이지만, AgentCoder가 입증한 것처럼
**구체적인 테스트 절차**를 명시하면 품질이 크게 향상된다.

**적용**:
```
[VERIFY]
1. cargo check (컴파일 확인)
2. Run existing tests: cargo test
3. Test your specific changes manually
4. If tests fail, fix and re-test (max 3 iterations)
5. Only commit when all tests pass
```

---

#### D. MAST 실패 모드 기반 방어적 프롬프트
> 출처: MAST (실패 분석 논문)

가장 흔한 실패 유형에 대한 방어를 프롬프트에 명시.

**적용**: 에이전트 프롬프트에 추가
```
[WARNINGS]
- DO NOT modify files not listed in [OWN FILES] — this causes merge conflicts
- DO NOT install new dependencies without explicit instruction
- If you are stuck for more than 3 attempts, STOP and commit what you have
- Write a clear commit message explaining what you did and what remains
```

---

#### E. 에이전트 완료 후 결과 보고서 자동 생성
> 출처: MetaGPT (문서 기반 소통), HyperAgent

각 에이전트가 완료 시 간단한 결과 보고를 남기면, 비서 에이전트가 이를 종합하여
머지 순서와 충돌 예측에 활용할 수 있다.

**적용**: 에이전트 프롬프트 마지막에 추가
```
[ON COMPLETION]
When you finish, create a file: /tmp/octo-report-{your-nickname}.md
Contents:
- Files modified: (list)
- What was done: (1-2 sentences)
- Known issues: (if any)
- Dependencies on other agents: (if any)
```

---

### 중기 로드맵 (Medium-term)

#### F. 교차 검증 단계 (Cross-Team Validation)
> 출처: Croto (Cross-Team Orchestration)

에이전트 작업 완료 후, 머지 전에 **다른 에이전트가 코드 리뷰**.

```
Agent A 완료 → Agent B가 A의 diff 리뷰 → 문제 없으면 머지
```

#### G. 비서의 동적 작업 재할당
> 출처: TDAG, Evolving Orchestration

비서 에이전트가 진행 중에 상황을 모니터링하고:
- 에이전트가 막히면 힌트 제공
- 예상치 못한 추가 작업 발견 시 새 에이전트 생성
- 에이전트 완료 순서에 따라 다음 작업 동적 조정

#### H. Maker-Checker 분리
> 출처: AgentCoder, Microsoft Group Chat

코드 생성 에이전트와 별도의 QA 에이전트를 두어:
```
Developer Agent → 코드 작성/커밋
QA Agent → 워크트리에서 테스트 실행, 코드 리뷰
```

---

### 장기 비전 (Long-term)

#### I. 자기 진화하는 비서
> 출처: Live-SWE-agent, Evolving Orchestration

오케스트레이션 결과(성공률, 머지 충돌 빈도, 에이전트별 생산성)를 로그로 누적하고,
비서가 이 데이터를 기반으로 **더 나은 작업 분해와 에이전트 할당을 학습**.

#### J. 모델별 최적 역할 할당
> 출처: AgentOrchestra, MAS Challenges

모든 에이전트에 같은 모델 불필요. 작업 복잡도에 맞는 모델 선택:
- 간단한 파일 수정: 경량 모델 (Haiku 등)
- 복잡한 아키텍처 설계: 고성능 모델 (Opus 등)
- 테스트 생성: 중간 모델 (Sonnet 등)

---

## 참고 문헌

### 역할 기반 시스템
- [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) — ACL 2024
- [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — ICLR 2024
- [HyperAgent: Generalist Software Engineering Agents](https://openreview.net/forum?id=PZf4RsPMBG) — 2024

### 오케스트레이션 아키텍처
- [Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591) — NeurIPS 2025
- [Multi-Agent Collaboration via Cross-Team Orchestration](https://arxiv.org/abs/2406.08979) — 2024
- [AgentOrchestra: TEA Protocol](https://arxiv.org/abs/2506.12508) — 2025
- [TDAG: Dynamic Task Decomposition and Agent Generation](https://arxiv.org/abs/2402.10178) — Neural Networks 2024

### 코드 생성
- [MapCoder: Multi-Agent Code Generation](https://arxiv.org/abs/2405.11403) — ACL 2024
- [AgentCoder: Multi-Agent Code Generation with Iterative Testing](https://arxiv.org/abs/2312.13010) — 2023

### 소프트웨어 엔지니어링 에이전트
- [SWE-agent: Agent-Computer Interfaces](https://arxiv.org/abs/2405.15793) — 2024
- [Live-SWE-agent: Self-Evolve on the Fly](https://arxiv.org/abs/2511.13646) — 2025

### 서베이 & 분석
- [LLM-Based Multi-Agent Systems for SE: Literature Review](https://arxiv.org/abs/2404.04834) — ACM TOSEM
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — 2025
- [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578) — 2024
- [Large Language Model based Multi-Agents: A Survey](https://arxiv.org/abs/2402.01680) — 2024
- [The Orchestration of Multi-Agent Systems](https://arxiv.org/abs/2601.13671) — 2025
- [AI Agent Orchestration Patterns — Microsoft Azure](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) — 2026
