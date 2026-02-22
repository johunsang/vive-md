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
8. [멀티에이전트 벤치마크 비교](#8-멀티에이전트-벤치마크-비교)

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
| 15 | SEMAP (Protocol-Driven) | 2025 | SE 원칙 기반 프로토콜 레이어로 MAS 실패 69.6% 감소 | ★★★ 실패 방지 |
| 16 | SWE-bench Pro | 2025 | 장기 호라이즌 SE 벤치마크, 1865 문제, 41 저장소 | ★★ 벤치마크 |
| 17 | SWE-EVO | 2025/2026 | 소프트웨어 진화 시나리오 벤치마크, 멀티파일 수정 | ★★ 진화 벤치마크 |
| 18 | Multi-Agent Collaboration Mechanisms Survey | 2025 | 협업 메커니즘 분류 체계(유형, 구조, 전략, 프로토콜) | ★★★ 협업 설계 |
| 19 | Self-Organized Agents (SoA) | 2024 | 초대규모 코드 생성, 에이전트 자기 조직화 | ★★ 대규모 코드 |

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

### 5-3. Self-Organized Agents (SoA) — 초대규모 코드 생성

**논문**: [Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization](https://arxiv.org/abs/2404.02183) (2024)

**핵심 아이디어**:
```
복잡한 코드 생성 작업
    ↓ 자기 조직화
에이전트 그룹이 자율적으로:
  1. 작업 분해 (Task Decomposition)
  2. 역할 할당 (Role Assignment)
  3. 코드 생성 + 통합 (Code Generation + Integration)
  4. 반복 최적화 (Iterative Optimization)
```

- **자기 조직화**: 중앙 오케스트레이터 없이 에이전트들이 스스로 역할과 작업을 결정
- **대규모 코드 대응**: 수천 줄 이상의 복잡한 프로젝트 코드 생성 가능
- **반복 최적화**: 생성된 코드의 품질을 에이전트 간 피드백으로 개선

**Octo Orchestra 적용 포인트**:
- 현재 Octo Orchestra는 중앙집중(비서) 패턴 → SoA처럼 에이전트 자율성을 높이는 것은 장기 비전
- 단, 대규모 코드 생성 시 에이전트 간 코드 통합 전략은 참고할 가치가 있음

---

### 5-4. Agentless — 에이전트 없이도 가능

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

**MAST 14가지 실패 모드 상세 분류**:

| # | 실패 모드 | 카테고리 | 빈도 | 심각도 | 설명 |
|---|-----------|----------|------|--------|------|
| F1 | 작업 분배 오류 | 설계 | 높음 | 심각 | 에이전트 능력과 불일치하는 작업 할당 |
| F2 | 역할 중복 | 설계 | 중간 | 보통 | 여러 에이전트가 동일 작업 수행 |
| F3 | 오케스트레이션 결함 | 설계 | 중간 | 심각 | 조율 로직 자체의 버그/비효율 |
| F4 | 메시지 손실 | 불일치 | 높음 | 심각 | 에이전트 간 메시지가 전달되지 않음 |
| F5 | 컨텍스트 드리프트 | 불일치 | 높음 | 보통 | 대화가 진행될수록 맥락 이탈 |
| F6 | 상충 행동 | 불일치 | 낮음 | 심각 | 에이전트 간 모순되는 수정 |
| F7 | 무한 루프 | 불일치 | 중간 | 심각 | 에이전트가 끝없이 반복 수정 |
| F8 | 검증 누락 | 검증 | 높음 | 보통 | 결과물을 검증하지 않고 전달 |
| F9 | 완료 조건 불명확 | 검증 | 중간 | 보통 | 언제 작업이 끝났는지 불분명 |
| F10 | 환각 전파 | 불일치 | 높음 | 심각 | 한 에이전트의 환각이 다른 에이전트로 전파 |
| F11 | 도구 오용 | 설계 | 중간 | 보통 | 잘못된 도구를 잘못된 방식으로 사용 |
| F12 | 토큰 소진 | 설계 | 낮음 | 심각 | 컨텍스트 윈도우 초과로 정보 손실 |
| F13 | 부분 완료 | 검증 | 높음 | 보통 | 작업의 일부만 완료하고 완료로 보고 |
| F14 | 의존성 교착 | 설계 | 낮음 | 심각 | 에이전트 간 순환 의존성 |

**구체적 실패 사례와 해결 전략**:

#### 사례 1: 환각 전파 (Cascading Hallucination)
```
시나리오: Agent A가 존재하지 않는 API를 코드에 사용
        → Agent B가 해당 API를 기반으로 테스트 작성
        → Agent C가 테스트 통과시키려고 더 잘못된 코드 생성
        → 전체 시스템 실패

해결 전략:
1. 각 에이전트가 외부 API 사용 시 실제 존재 여부 검증 필수
2. 에이전트 간 산출물 전달 시 "검증 게이트" 삽입
3. Octo Orchestra 적용: [VERIFY]에 "import/API 존재 확인" 단계 추가
```

#### 사례 2: 무한 수정 루프 (Infinite Fix Loop)
```
시나리오: Agent A가 버그 수정 → 새 버그 발생
        → Agent B가 새 버그 수정 → 원래 버그 재발
        → 무한 반복 (토큰/시간 소진)

해결 전략:
1. 수정 시도 횟수에 명시적 상한 설정 (max 3 iterations)
2. 2회 이상 실패 시 다른 접근 방식 시도
3. Octo Orchestra 적용: [WARNINGS]에 "3회 이상 시도 시 중단" 명시
```

#### 사례 3: 파일 충돌 (Merge Conflict from Scope Violation)
```
시나리오: Agent A가 자신의 파일 외에 공용 config 수정
        → Agent B도 같은 config 수정
        → 머지 시 충돌 → 양쪽 작업 모두 손실 위험

해결 전략:
1. 파일 소유권을 명시적으로 할당 ([OWN FILES])
2. 공유 파일은 한 에이전트만 담당하거나, 머지 순서 지정
3. Octo Orchestra 적용: [DO NOT TOUCH] 목록으로 접근 금지 파일 명시
```

#### 사례 4: 컨텍스트 드리프트 (Context Drift)
```
시나리오: 에이전트가 긴 작업 수행 중 초기 지시를 잊음
        → 파일 중반부터 다른 스타일/패턴으로 코드 작성
        → 일관성 없는 결과물

해결 전략:
1. 프롬프트에 핵심 규칙을 반복 배치 (시작부 + 중간부)
2. 긴 작업은 여러 하위 작업으로 분리
3. Octo Orchestra 적용: [STEPS]를 세밀하게 분해, 각 단계에 핵심 규칙 재언급
```

**실패 예방 패턴 종합**:

| 예방 패턴 | 대상 실패 모드 | Octo Orchestra 구현 |
|-----------|---------------|-------------------|
| 파일 소유권 격리 | F1, F2, F6 | `[OWN FILES]` + `[DO NOT TOUCH]` |
| 수정 횟수 상한 | F7, F12 | `[WARNINGS]`: max 3 iterations |
| 검증 게이트 | F8, F10, F13 | `[VERIFY]` 섹션 필수화 |
| 명시적 완료 조건 | F9, F13 | PTY alive 체크 + 커밋 기반 판단 |
| 역할 정체성 강화 | F1, F2, F5 | `[ROLE]` 섹션으로 전문성 활성화 |
| 구조화된 산출물 | F4, F5, F10 | 파일 기반 소통 (대화 아닌 문서) |
| 의존성 명시 | F14 | 작업 간 의존성 그래프 사전 정의 |
| 도구 사용 가이드 | F11 | `[STEPS]`에 구체적 도구/명령어 명시 |

**Octo Orchestra에서의 대응 전략 요약**:

| 실패 유형 | 우리의 대응 |
|-----------|-------------|
| 작업 분배 문제 | 파일 소유권 명확 할당 (`[OWN FILES]` + `[DO NOT TOUCH]`) |
| 역할 중복 | 각 에이전트에 고유한 `[GOAL]`과 `[FILES]` |
| 소통 실패 | 현재: 독립 실행 (소통 불필요). 향후: 비서 모니터링 |
| 컨텍스트 손실 | 파일 기반 프롬프트로 완전한 컨텍스트 전달 |
| 검증 부재 | `[VERIFY]` 섹션에 검증 단계 필수 포함 |
| 완료 조건 모호 | PTY alive 체크 + 커밋 카운트로 객관적 완료 판단 |
| 환각 전파 | 검증 게이트 + API/import 존재 확인 |
| 무한 루프 | 최대 시도 횟수 3회 제한 |
| 파일 충돌 | 워크트리 격리 + 파일 소유권 배타적 할당 |

---

### 6-2. SEMAP — 프로토콜 기반 MAS 실패 방지

**논문**: [Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach](https://arxiv.org/abs/2510.12120) (2025)

**핵심 문제**: 기존 MAS가 실패하는 3가지 핵심 결함:
1. **Under-specification** — 에이전트 행동 사양이 불충분
2. **Coordination Misalignment** — 에이전트 간 조율 불일치
3. **Inappropriate Verification** — 부적절한 검증 절차

**SEMAP (Software Engineering Multi-Agent Protocol)**:
```
3대 SE 설계 원칙을 프로토콜 레이어로 구현:

1. Explicit Behavioral Contract Modeling
   → 각 에이전트의 행동 계약을 명시적으로 정의

2. Structured Messaging
   → JSON-RPC 2.0 기반 구조화된 메시지 포맷

3. Lifecycle-Guided Execution with Verification
   → 라이프사이클 단계별 검증 게이트 삽입
```

**성과**:
- MAST 프레임워크 기준 **총 실패 69.6% 감소** (함수 레벨 코드 개발)
- 배포 레벨 코드 개발에서 **56.7% 실패 감소**
- Google A2A (Agent-to-Agent) 인프라 위에 구현

**Octo Orchestra 적용 포인트**:
- 행동 계약 = 우리의 `[GOAL]`, `[STEPS]`, `[VERIFY]` 시스템
- 구조화된 메시지 = 파일 기반 산출물 교환
- 라이프사이클 검증 = preflight → running → verifying → merging
- **SEMAP이 69.6% 실패 감소를 달성한 것은 우리의 프롬프트 구조화 접근이 올바르다는 실증적 증거**

---

### 6-3. LLM Multi-Agent Systems: Challenges and Open Problems

**논문**: [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578) (2024, 2026 개정)

**4대 도전 과제**:

1. **작업 할당 최적화**: 다양한 능력의 에이전트에게 효율적 작업 분배
2. **추론 강화**: 반복적 토론으로 협력적 의사결정 강화
3. **컨텍스트 관리**: 다중 에이전트 간 복잡하고 계층적인 컨텍스트 정보 관리
4. **메모리 시스템**: 에이전트 상호작용을 지원하는 견고한 메모리 아키텍처

### 6-4. Multi-Agent Collaboration Mechanisms Survey — 협업 메커니즘 분류 체계

**논문**: [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322) (2025)

**분류 프레임워크 — 5가지 차원**:

| 차원 | 유형 | 설명 |
|------|------|------|
| **Actors** | 동질적 / 이질적 | 같은 모델 vs 다른 모델/역할의 에이전트 |
| **Types** | 협력 / 경쟁 / 혼합 | 에이전트 간 상호작용 유형 |
| **Structures** | P2P / 중앙집중 / 분산 | 조직 구조 토폴로지 |
| **Strategies** | 역할 기반 / 모델 기반 | 작업 분배 전략 |
| **Protocols** | 동기 / 비동기 / 이벤트 | 통신 프로토콜 유형 |

**Octo Orchestra 매핑**:
- **Actors**: 이질적 (각 에이전트가 다른 파일/역할 담당)
- **Types**: 협력 (경쟁 요소 없음, 모두 하나의 프로젝트에 기여)
- **Structures**: 중앙집중 (비서 에이전트가 조율)
- **Strategies**: 역할 기반 (파일 소유권 기반 역할 분배)
- **Protocols**: 비동기 (각 에이전트 독립 실행, 완료 후 머지)

---

## 7. Octo Orchestra에 착용할 핵심 아이디어

논문들에서 추출한 핵심 아이디어를 Octo Orchestra의 현재 구현과 대조하고,
즉시 적용 가능한 것과 향후 로드맵으로 분류한다.

> **관련 가이드**: 실전 적용 체크리스트와 도구별 매핑은 [멀티에이전트 오케스트레이션 논문 가이드](../../docs/multi-agent-orchestration-papers-guide.md)에서 확인할 수 있다.

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

**구체적 Octo Orchestra 설정 예시**:
```yaml
# octo-orchestra agent prompt template
=== YOUR TASK ===
[ROLE] 프론트엔드 UI 전문가. React/TypeScript에 능숙하며,
접근성(A11y)과 반응형 디자인을 항상 고려합니다.
코드 리뷰어 관점에서 자신의 코드를 먼저 검토합니다.

[GOAL] 대시보드 페이지의 차트 컴포넌트를 구현한다.
[OWN FILES] src/components/Dashboard/Chart.tsx, src/hooks/useChartData.ts
[DO NOT TOUCH] src/api/*, src/store/*
```

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

**구체적 Octo Orchestra 비서 프롬프트 예시**:
```
당신은 Octo Orchestra 비서입니다. 사용자 요청을 다음 단계로 처리합니다:

1단계 - PRD 작성:
   - 무엇을 만드는가? (What)
   - 왜 필요한가? (Why)
   - 주요 제약 조건은? (Constraints)
   - 성공 기준은? (Success Criteria)

2단계 - 아키텍처 설계:
   - 영향받는 파일/모듈 목록
   - 데이터 흐름도 (A → B → C)
   - 의존성 그래프

3단계 - 에이전트 분해:
   - 에이전트별 [OWN FILES] 할당 (겹침 없이)
   - 에이전트별 [GOAL] + [STEPS] 작성
   - 의존성 순서 정의 (A 완료 후 B 시작 필요?)

4단계 - JSON 출력:
   {
     "agents": [
       { "nickname": "꼬물이", "role": "...", "files": [...], "depends_on": [] },
       { "nickname": "먹물이", "role": "...", "files": [...], "depends_on": ["꼬물이"] }
     ]
   }
```

---

#### C. `[VERIFY]` 섹션을 AgentCoder식 테스트 루프로 강화
> 출처: AgentCoder, MapCoder

현재 `[VERIFY]`는 "확인하라" 수준이지만, AgentCoder가 입증한 것처럼
**구체적인 테스트 절차**를 명시하면 품질이 크게 향상된다.

**적용 — 기술 스택별 [VERIFY] 템플릿**:

```
# Rust/Tauri 프로젝트
[VERIFY]
1. cargo check (컴파일 확인)
2. cargo clippy -- -D warnings (린트 확인)
3. cargo test (기존 테스트 실행)
4. 변경사항에 대한 수동 테스트
5. 실패 시 수정 후 재테스트 (최대 3회)
6. 모든 테스트 통과 후에만 커밋
```

```
# React/TypeScript 프로젝트
[VERIFY]
1. npx tsc --noEmit (타입 체크)
2. npx eslint src/ --ext .ts,.tsx (린트 확인)
3. npx vitest run (테스트 실행)
4. 변경된 컴포넌트가 import/export 올바른지 확인
5. 실패 시 수정 후 재테스트 (최대 3회)
6. 모든 테스트 통과 후에만 커밋
```

```
# Python 프로젝트
[VERIFY]
1. python -m py_compile <changed_files> (구문 확인)
2. python -m pytest (테스트 실행)
3. 변경된 모듈의 import 체인 확인
4. 실패 시 수정 후 재테스트 (최대 3회)
5. 모든 테스트 통과 후에만 커밋
```

---

#### D. MAST 실패 모드 기반 방어적 프롬프트
> 출처: MAST (실패 분석 논문), SEMAP (프로토콜 기반 접근)

가장 흔한 실패 유형에 대한 방어를 프롬프트에 명시.
SEMAP이 이 접근으로 **69.6% 실패 감소**를 달성했다.

**적용**: 에이전트 프롬프트에 추가
```
[WARNINGS]
- DO NOT modify files not listed in [OWN FILES] — this causes merge conflicts
- DO NOT install new dependencies without explicit instruction
- If you are stuck for more than 3 attempts, STOP and commit what you have
- Write a clear commit message explaining what you did and what remains
- DO NOT delete existing code unless your task explicitly says to remove it
- Always read the full file before modifying — understand ALL existing code first
```

**강화된 방어적 프롬프트 (SEMAP 원칙 반영)**:
```
=== CODE MODIFICATION RULES (CRITICAL) ===
- NEVER rewrite or replace entire files. Make SURGICAL, MINIMAL edits only.
- ALWAYS read the full file first, understand ALL existing code, then ADD or MODIFY.
- Preserve ALL existing functionality. Your changes must be ADDITIVE.
- Before committing, run git diff and verify you haven't deleted existing code.
- If a file has 400 lines, your modified version should have ~400+ lines.
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

**보고서 활용 워크플로우**:
```
1. 각 에이전트가 /tmp/octo-report-{nickname}.md 생성
2. 비서 에이전트가 모든 보고서를 읽고:
   a. 파일 충돌 가능성 분석
   b. 머지 순서 결정 (의존성 그래프 기반)
   c. 후속 작업 필요 여부 판단
3. 머지 결과를 최종 보고서로 통합
```

---

### 중기 로드맵 (Medium-term)

#### F. 교차 검증 단계 (Cross-Team Validation)
> 출처: Croto (Cross-Team Orchestration)

에이전트 작업 완료 후, 머지 전에 **다른 에이전트가 코드 리뷰**.

```
Agent A 완료 → Agent B가 A의 diff 리뷰 → 문제 없으면 머지
```

**구체적 구현 방안**:
```
# 교차 검증 에이전트 프롬프트 템플릿
[ROLE] QA 리뷰어. 다른 에이전트의 코드를 검증합니다.
[GOAL] Agent A의 변경사항을 리뷰하고 문제를 보고합니다.
[STEPS]
1. git diff main..agent-a-branch 로 변경 내용 확인
2. 추가된 코드의 타입/구문 오류 확인
3. 기존 코드 삭제 여부 확인 (삭제되면 안됨)
4. 테스트 실행하여 기존 테스트 통과 여부 확인
5. 결과를 /tmp/octo-review-{agent-nickname}.md에 기록
```

#### G. 비서의 동적 작업 재할당
> 출처: TDAG, Evolving Orchestration

비서 에이전트가 진행 중에 상황을 모니터링하고:
- 에이전트가 막히면 힌트 제공
- 예상치 못한 추가 작업 발견 시 새 에이전트 생성
- 에이전트 완료 순서에 따라 다음 작업 동적 조정

**동적 재할당 시나리오**:
```
시나리오 1: Agent A가 10분째 커밋 없음
  → 비서가 Agent A의 로그 확인
  → 힌트 제공하거나, 작업을 더 작은 단위로 재분해

시나리오 2: Agent B가 예상보다 빨리 완료
  → Agent C의 작업 일부를 Agent B에게 재할당
  → 또는 추가 테스트/문서 작업 부여

시나리오 3: Agent A 완료 → 새로운 의존 작업 발견
  → 비서가 Agent D를 동적으로 생성
  → Agent A의 결과를 컨텍스트로 전달
```

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

**진화 메트릭 예시**:
```json
{
  "session_id": "2026-02-23-001",
  "agents": [
    {
      "nickname": "꼬물이",
      "task_complexity": "high",
      "completion_time_min": 12,
      "commits": 3,
      "merge_conflicts": 0,
      "test_pass_rate": 1.0
    }
  ],
  "overall": {
    "total_agents": 3,
    "total_time_min": 18,
    "merge_success_rate": 1.0,
    "files_modified": 8
  }
}
```

#### J. 모델별 최적 역할 할당
> 출처: AgentOrchestra, MAS Challenges

모든 에이전트에 같은 모델 불필요. 작업 복잡도에 맞는 모델 선택:
- 간단한 파일 수정: 경량 모델 (Haiku 등)
- 복잡한 아키텍처 설계: 고성능 모델 (Opus 등)
- 테스트 생성: 중간 모델 (Sonnet 등)

**모델-작업 매핑 가이드**:

| 작업 유형 | 추천 모델 | 근거 |
|-----------|----------|------|
| 단순 파일 수정/이동 | Haiku | 빠르고 저비용, 간단한 패턴 인식 충분 |
| 코드 생성 (함수/클래스) | Sonnet | 비용 대비 코드 품질 균형 |
| 아키텍처 설계/리팩토링 | Opus | 복잡한 의존성 이해, 전체 조감 필요 |
| 테스트 작성 | Sonnet | 테스트 패턴은 정형화되어 있음 |
| 코드 리뷰/QA | Opus | 미묘한 버그/설계 결함 포착 필요 |
| 문서 작성 | Sonnet | 구조화된 글쓰기 |
| 디버깅 | Opus | 복잡한 원인 분석, 스택 트레이스 해석 |

---

## 8. 멀티에이전트 벤치마크 비교

멀티에이전트 소프트웨어 개발 시스템의 성능을 평가하는 주요 벤치마크를 비교하고,
각 벤치마크가 측정하는 능력과 현재 SOTA 결과를 정리한다.

### 8-1. 주요 벤치마크 개요

| 벤치마크 | 측정 영역 | 규모 | 난이도 | 특징 |
|----------|----------|------|--------|------|
| **HumanEval** | 함수 레벨 코드 생성 | 164 문제 | 중간 | Python 함수 완성, pass@k 측정 |
| **MBPP** | 함수 레벨 코드 생성 | 974 문제 | 쉬움~중간 | 초보자용 프로그래밍 문제 |
| **SWE-bench** | 실전 버그 수정 | 2,294 이슈 | 높음 | 실제 GitHub 이슈 기반 |
| **SWE-bench Verified** | 실전 버그 수정 (검증됨) | 500 이슈 | 높음 | 전문가 검증된 서브셋 |
| **SWE-bench Pro** | 장기 호라이즌 SE | 1,865 문제 | 매우 높음 | 41 저장소, 123 언어, 멀티파일 |
| **SWE-EVO** | 소프트웨어 진화 | 48 작업 | 극도로 높음 | 평균 21 파일 수정, 874 테스트/인스턴스 |
| **GAIA** | 범용 AI 어시스턴트 | 466 질문 | 다양 | 추론, 도구 사용, 웹 브라우징 |
| **CodeContests** | 경쟁 프로그래밍 | 10K+ 문제 | 높음 | 알고리즘 설계 + 구현 |

### 8-2. 벤치마크별 멀티에이전트 시스템 성과 비교

#### HumanEval (pass@1)

| 시스템 | 점수 | 에이전트 수 | 접근 방식 |
|--------|------|------------|-----------|
| AgentCoder | **96.3%** | 3 | Programmer-Tester-Executor 반복 |
| MapCoder | 93.9% | 4 | Retrieval-Planning-Coding-Debugging |
| Self-Organized Agents | ~92% | 동적 | 자기 조직화 |
| 단일 에이전트 (GPT-4) | ~90% | 1 | 단일 프롬프트 |

**핵심 인사이트**: 멀티에이전트가 단일 에이전트 대비 **3~6%p 향상**, 토큰 비용은 **~60% 절감**.

#### MBPP (pass@1)

| 시스템 | 점수 | 에이전트 수 | 접근 방식 |
|--------|------|------------|-----------|
| AgentCoder | **91.8%** | 3 | Programmer-Tester-Executor 반복 |
| MapCoder | 83.1% | 4 | 4단계 파이프라인 |
| 단일 에이전트 (GPT-4) | ~78% | 1 | 단일 프롬프트 |

#### SWE-bench Verified

| 시스템 | 점수 | 유형 | 특징 |
|--------|------|------|------|
| Live-SWE-agent | **77.4%** | 자기 진화 | bash만으로 시작, 런타임 학습 |
| OpenHands + GPT-5 | ~65% | 프레임워크 | 다중 도구 활용 |
| SWE-agent | 12.5% | 단일 에이전트 | ACI 기반 (2024 초기) |

#### SWE-bench Pro (pass@1)

| 시스템 | 점수 | 특징 |
|--------|------|------|
| GPT-5 | **23.3%** | 최고 단일 모델 성과 |
| Opus 4.1 | ~20% | 강력한 추론 능력 |
| 오픈소스 모델 | <10% | 구문/도구 오류 빈번 |

**핵심 인사이트**: SWE-bench Pro는 SWE-bench Verified보다 **3배 어려움**. 멀티파일 수정(평균 4.1파일, 107.4줄)이 요구되며, 현재 최고 성과도 23.3%에 불과.

#### SWE-EVO

| 시스템 | 점수 | SWE-bench Verified 대비 |
|--------|------|------------------------|
| OpenHands + GPT-5 | **21%** | 65% → 21% (3배 하락) |
| 기타 에이전트 | <15% | 대부분 크게 하락 |

**핵심 인사이트**: 소프트웨어 진화(장기 멀티파일 수정)는 현재 에이전트의 가장 큰 약점. 강한 모델도 instruction following(릴리스 노트 해석) 실패, 약한 모델은 도구 사용/구문 오류.

#### GAIA

| 시스템 | 점수 | 특징 |
|--------|------|------|
| AgentOrchestra (TEA) | **89.04%** | Tool-Environment-Agent 라이프사이클 |
| 이전 SOTA | ~85% | - |

### 8-3. 벤치마크 난이도별 실패 패턴

| 난이도 | 대표 벤치마크 | 주요 실패 원인 | Octo Orchestra 시사점 |
|--------|-------------|---------------|---------------------|
| 낮음 | HumanEval, MBPP | 단순 로직 오류 | 단일 에이전트로 충분 |
| 중간 | SWE-bench | 코드 위치 찾기 실패 | 탐색 에이전트 필요 (Navigator) |
| 높음 | SWE-bench Pro | 멀티파일 조율 실패 | 파일 소유권 + 의존성 관리 |
| 극도로 높음 | SWE-EVO | 장기 추론/진화 실패 | 단계별 체크포인트 + 중간 검증 |

### 8-4. Octo Orchestra에 대한 벤치마크 시사점

1. **단순 작업은 단일 에이전트가 효율적**: HumanEval 수준 작업에 멀티에이전트는 과도함
2. **멀티파일 작업에서 멀티에이전트 가치 극대화**: SWE-bench Pro 수준에서 파일 소유권 기반 분할이 빛남
3. **장기 진화 작업은 아직 미해결**: SWE-EVO 수준은 단계별 체크포인트와 중간 검증이 필수
4. **모델 선택이 중요**: 같은 아키텍처라도 모델에 따라 성과 3~5배 차이
5. **실패 패턴은 예측 가능**: MAST + SWE-bench Pro 분석을 결합하면 실패를 사전 방어 가능

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

### 프로토콜 & 협업 메커니즘
- [Towards Engineering Multi-Agent LLMs: A Protocol-Driven Approach (SEMAP)](https://arxiv.org/abs/2510.12120) — 2025
- [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322) — 2025
- [Self-Organized Agents: Ultra Large-Scale Code Generation](https://arxiv.org/abs/2404.02183) — 2024

### 벤치마크
- [SWE-bench Pro: Long-Horizon Software Engineering Tasks](https://arxiv.org/abs/2509.16941) — 2025
- [SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution](https://arxiv.org/abs/2512.18470) — 2025/2026

### 서베이 & 분석
- [LLM-Based Multi-Agent Systems for SE: Literature Review](https://arxiv.org/abs/2404.04834) — ACM TOSEM
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — 2025
- [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578) — 2024
- [Large Language Model based Multi-Agents: A Survey](https://arxiv.org/abs/2402.01680) — 2024
- [The Orchestration of Multi-Agent Systems](https://arxiv.org/abs/2601.13671) — 2025
- [AI Agent Orchestration Patterns — Microsoft Azure](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) — 2026
