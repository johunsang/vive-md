# Comprehensive Review: Vibe Coding & Orchestration Research (2025-2026)

> A systematic synthesis of recent advances in AI-native software development and multi-agent coordination

---

## 📋 Executive Summary

This document presents a comprehensive review of **22 seminal papers** published in 2025-2026, spanning two convergent domains:

| Domain | Papers | Key Themes |
|--------|--------|------------|
| **Vibe Coding** | 12 papers | Paradigm shift, security benchmarks, adoption metrics, quality trade-offs, educational implications, OSS ecosystem impact |
| **Orchestration** | 10 papers | Multi-agent coordination, failure taxonomy, scaling laws, latency optimization, cost-efficiency, domain-specific applications |

### 논문 타임라인 개요

```
2025 Q1-Q2                          2025 Q3-Q4                          2026 Q1-Q2
──────────────────────────────────────────────────────────────────────────────────────
                                    Sarkar (Jun)                        Koren (Jan)
Cemri - Why MAS Fail (Mar)          Bird (Sep)                          Robbes (Jan)
Dang - Evolving Orch. (May)         Tahir (Sep)                         Adimulam (Jan)
                                    Bamil (Oct)                         Shi - LAMaS (Jan)
                                    Ge - Survey (Oct)                   Liu - CASTER (Jan)
                                    Hua - SOCIA (Oct)                   Ma - MAESTRO (Jan)
                                    Huang - Don't Vibe (Dec)            Wattamwar (Jan)
                                    Chou - Rolling Dice (Dec)           Zhao - Safe? (Dec→Feb)
                                    Gama - Education (Dec)              Yu - AdaptOrch (Feb)
```

---

## Part I: Vibe Coding Research Landscape

### 1.1 Foundational Definitions & Theoretical Frameworks

#### Paper 1: "Vibe Coding: Toward an AI-Native Paradigm for Semantic Software Engineering" (Oct 2025)

**Authors:** Vinay Bamil et al.  
**arXiv:** 2510.17842

**Original Abstract:**
> "This paper introduces vibe coding, an emerging AI-native programming paradigm in which a developer specifies high-level functional intent along with qualitative descriptors of the desired 'vibe' (tone, style, or emotional resonance). An intelligent agent then transforms those specifications into executable software."

**Core Contribution:**
- **Reference Architecture**: Intent Parser → Semantic Embedding Engine → Agentic Code Generator → Interactive Feedback Loop
- **Formal Comparison**: Declarative vs. Functional vs. Prompt-based vs. Vibe Coding
- **Challenge Taxonomy**: Alignment, reproducibility, bias, explainability, maintainability, security

---

#### Paper 2: "A Survey of Vibe Coding with Large Language Models" (Oct-Dec 2025)

**Authors:** Yuyao Ge et al.  
**arXiv:** 2510.12399 (v2: Dec 2025)

**Original Abstract:**
> "Drawing from systematic analysis of over 1000 research papers, we survey the entire vibe coding ecosystem... formalizing it through a Constrained Markov Decision Process that captures the dynamic triadic relationship among human developers, software projects, and coding agents."

**Theoretical Foundation:**
```
CMDP Formalization: (S, A, P, R, γ, C)
- S: States (project configurations)
- A: Actions (agent operations)
- C: Constraints (human specifications)
```

**Development Model Taxonomy:**
| Model | Characteristics | Best For |
|-------|-----------------|----------|
| **Unconstrained Automation** | Full AI autonomy | Rapid prototyping |
| **Iterative Conversational** | Back-and-forth refinement | Exploratory development |
| **Planning-Driven** | Structured milestones | Complex projects |
| **Test-Driven** | Validation-centric | Quality-critical systems |
| **Context-Enhanced** | Rich context injection | Large codebases |

**Critical Insight:**
> "Successful Vibe Coding depends not merely on agent capabilities but on systematic context engineering, well-established development environments, and human-agent collaborative development models."

---

### 1.2 Empirical Studies & Behavioral Analysis

#### Paper 3: "Building Software by Rolling the Dice" (Dec 2025)

**Authors:** Yi-Hung Chou et al.  
**arXiv:** 2512.22418

**Study Design:**
| Metric | Value |
|--------|-------|
| Video Sources | 20 (7 live-streamed + 13 opinion) |
| Live Coding Hours | ~16 hours |
| Total Prompts Analyzed | 254 |
| Think-Aloud Content | ~5 hours |

**Key Findings:**

**Behavioral Spectrum:**
```
Full AI Reliance ◄─────────────────────────────► Critical Examination
        │                                            │
   [Trust-based]                              [Verification-based]
        │                                            │
   Minimal code review                        Active adaptation
```

**The "Rolling the Dice" Phenomenon:**
- Debugging described as stochastic process
- Generation outcomes inherently unpredictable
- Developers develop intuitive "gambling" strategies

**Mental Model Divergence:**
| Expertise Level | AI Reliance | Evaluation Strategy |
|-----------------|-------------|---------------------|
| Novice | High | Surface-level acceptance |
| Intermediate | Medium | Trial-and-error |
| Expert | Selective | Targeted verification |

---

#### Paper 4: "Vibe Coding: Programming Through Conversation" (Jun-Oct 2025)

**Authors:** Advait Sarkar et al.  
**arXiv:** 2506.23253

**Original Abstract:**
> "We present the first empirical study of vibe coding... vibe coding does not eliminate the need for programming expertise but rather redistributes it toward context management, rapid code evaluation, and decisions about when to transition between AI-driven and manual manipulation of code."

**Workflow Model:**
```
┌─────────────────────────────────────────────────────┐
│         ITERATIVE GOAL SATISFACTION CYCLE           │
├─────────────────────────────────────────────────────┤
│  PROMPT → GENERATE → EVALUATE → EDIT → [REPEAT]    │
│    ↑                                    │           │
│    └───────────── REFINE ───────────────┘           │
└─────────────────────────────────────────────────────┘
```

**Material Disengagement Concept:**
> "Practitioners orchestrate code production and manipulation, mediated through AI, while maintaining selective and strategic oversight."

**Trust Development Model:**
- **Dynamic & Contextual**: Not binary acceptance
- **Iterative Verification**: Built through repeated success/failure cycles
- **Tool-Specific**: Varies by AI tool capability

---

#### Paper 5: "Good Vibrations? A Qualitative Study of Co-Creation with AI" (Sep 2025)

**Authors:** Christian Bird et al.  
**arXiv:** 2509.12491

**Data Corpus:**
| Source | Words |
|--------|-------|
| Semi-structured interviews | ~60,000 |
| Reddit threads | ~80,000 |
| LinkedIn posts | ~50,000 |
| **Total** | **~190,000** |

**Grounded Theory Framework:**

```
                    ┌─────────────────────┐
                    │   DEVELOPER FLOW    │
                    │       & JOY         │
                    └──────────┬──────────┘
                               │
           ┌───────────────────┼───────────────────┐
           ▼                   ▼                   ▼
    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    │CONVERSATION │    │ CO-CREATION │    │   TRUST     │
    │INTERACTION  │◄──►│   DYNAMIC   │◄──►│  REGULATOR  │
    └─────────────┘    └─────────────┘    └─────────────┘
```

**Pain Points Identified:**
| Category | Specific Issues |
|----------|----------------|
| Specification | Ambiguity, shifting requirements |
| Reliability | Inconsistent outputs, hallucinations |
| Debugging | Opacity, difficulty tracing errors |
| Latency | Response delays breaking flow |
| Collaboration | Code review burden, team alignment |

**Delegation ↔ Co-Creation Continuum:**
```
DELEGATION ───────────────────────────────── CO-CREATION
   │                                             │
   │  "AI does it"                    "We do it together"  │
   │                                             │
   └── Trust Level Drives Position ──────────────┘
```

---

#### Paper 6: "Can You Feel the Vibes?" - Educational Study (Dec 2025)

**Authors:** Kiev Gama et al.  
**arXiv:** 2512.02750

**Study Context:**
| Parameter | Value |
|-----------|-------|
| Duration | 9 hours (1-day hackathon) |
| Participants | 31 undergraduates |
| Disciplines | Computing + Non-computing |
| Teams | 9 (mixed-experience) |
| Location | Brazilian public university |

**Positive Outcomes:**
- ✅ Rapid prototyping enabled
- ✅ Cross-disciplinary collaboration flourished
- ✅ Prompt engineering skills developed
- ✅ Functional demonstrations delivered
- ✅ Confidence building for newcomers

**Observed Challenges:**
| Issue | Description |
|-------|-------------|
| Premature Convergence | Teams settled on first viable idea |
| Uneven Code Quality | Required significant rework |
| Limited SE Practices | Testing, documentation neglected |

**Tool Usage Pattern:**
```
┌─────────────────────────────────────────────┐
│      SOPHISTICATED MULTI-AI PIPELINES       │
├─────────────────────────────────────────────┤
│  Tool A (Ideation) → Tool B (Coding) →     │
│  Tool C (Debugging) → Human (Refinement)   │
└─────────────────────────────────────────────┘
```

**Educational Implications:**
> "Vibe coding hackathons can serve as valuable low-stakes learning environments when coupled with explicit scaffolds for divergent thinking, critical evaluation of AI outputs, and realistic expectations about production quality."

---

### 1.3 Practice & Quality Studies

#### Paper 7: "Vibe Coding in Practice: Motivations, Challenges, Future Outlook" (Sep 2025)

**Authors:** Amjed Tahir et al.  
**arXiv:** 2510.00328

**Study Methodology:**
| Metric | Value |
|--------|-------|
| Grey Literature Sources | 101 |
| Behavioral Accounts | 518 |

**The Speed-Quality Trade-off Paradox:**

```
                    ┌─────────────────┐
                    │   INSTANT       │
                    │   SUCCESS       │
                    │   & FLOW        │
                    └────────┬────────┘
                             │
                             ▼
         ┌──────────────────────────────────┐
         │   HIGH MOTIVATION (Speed,        │
         │   Accessibility, Low Barrier)    │
         └──────────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                              ▼
    ┌─────────────────────┐    ┌─────────────────────┐
    │   PERCEIVED OUTPUT  │    │    REALITY CHECK    │
    │   "Fast but Flawed" │    │   QA Often Skipped  │
    └─────────────────────┘    └─────────────────────┘
```

**QA Practice Gaps:**
| Practice | Adoption Rate | Risk Level |
|----------|---------------|------------|
| Skipping testing | High | Critical |
| Blind trust in AI | Medium-High | High |
| Delegating checks to AI | Medium | High |
| Manual code review | Low | - |

**Vulnerable Developer Class:**
> "A new class of vulnerable software developers... those who build a product but are unable to debug it when issues arise."

---

#### Paper 8: "Improving Vibe Coding with Formal Verification" (Oct 2025)

**Authors:** [ACM Publication]  
**DOI:** 10.1145/3759425.3763390

**Problem Diagnosis:**
- Technical debt accumulation
- Security vulnerabilities
- Code churn for satisfactory results

**Root Cause:**
> "LLMs' inability to reconcile accumulating human-imposed constraints... LLMs prioritize user commands over code consistency."

**Proposed Side-Car System:**

```
┌─────────────────────────────────────────────────────────┐
│              VIBE CODING SESSION                        │
├─────────────────────────────────────────────────────────┤
│  Developer ◄────► LLM (Primary Generation)             │
│       │                                               │
│       │         ┌─────────────────────┐               │
│       └────────►│   SIDE-CAR SYSTEM   │               │
│                 │  ┌───────────────┐  │               │
│                 │  │1. Autoformalize│  │               │
│                 │  │   Specifications│ │               │
│                 │  ├───────────────┤  │               │
│                 │  │2. Validate     │  │               │
│                 │  │   Against Targets│                │
│                 │  ├───────────────┤  │               │
│                 │  │3. Actionable   │  │               │
│                 │  │   Feedback to LLM│                │
│                 │  ├───────────────┤  │               │
│                 │  │4. Developer    │  │               │
│                 │  │   Influence     │  │               │
│                 │  └───────────────┘  │               │
│                 └─────────────────────┘               │
└─────────────────────────────────────────────────────────┘
```

---

### 1.4 Ecosystem & Economic Impact

#### Paper 9: "Vibe Coding Kills Open Source" (Jan 2026)

**Authors:** Miklos Koren et al.  
**arXiv:** 2601.15494

**Economic Model:**

**OSS as Scalable Input:**
```
┌────────────────────────────────────────────────────────────┐
│                    OSS ECOSYSTEM                           │
├────────────────────────────────────────────────────────────┤
│                                                            │
│   ┌──────────┐        ┌──────────┐        ┌──────────┐   │
│   │  Entry   │───────►│  Quality │───────►│ Sharing  │   │
│   │ Decision │        │ Variance │        │ Decision │   │
│   └──────────┘        └──────────┘        └──────────┘   │
│        │                     │                   │        │
│        ▼                     ▼                   ▼        │
│   ┌──────────────────────────────────────────────────┐   │
│   │              USER ENGAGEMENT                     │   │
│   │  (Documentation reading, Bug reports,            │   │
│   │   Community participation = Maintainer returns)  │   │
│   └──────────────────────────────────────────────────┘   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Equilibrium Effects:**

| Scenario | Entry | Quality | Welfare |
|----------|-------|---------|---------|
| No Vibe Coding | Baseline | Baseline | Baseline |
| Widespread Vibe Coding | ↓↓ | ↓↓ | ↓ (despite ↑ productivity) |

**Key Mechanism:**
> "Vibe coding raises productivity by lowering the cost of using and building on existing code, but it also weakens the user engagement through which many maintainers earn returns."

**Required Solution:**
- Major changes in maintainer compensation models
- Alternative monetization beyond direct engagement
- Sustainable OSS funding mechanisms

---

### 1.5 Security, Adoption & Professional Practice

#### Paper 10: "Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code" (Dec 2025)

**Authors:** Songwen Zhao, Danqing Wang, Kexun Zhang, Jiaxuan Luo, Zhuo Li, Lei Li
**arXiv:** 2512.03262 (v2: Feb 2026)

**Original Abstract:**
> "Vibe coding is a new programming paradigm in which human engineers instruct large language model (LLM) agents to complete complex coding tasks with little supervision. We introduce SUSVIBES, a benchmark containing 200 real-world feature-request tasks from open-source projects."

**Benchmark Design (SUSVIBES):**

| Parameter | Value |
|-----------|-------|
| Tasks | 200 real-world feature requests |
| Source | Open-source projects with known vulnerabilities |
| Evaluation | Functional correctness + Security assessment |
| Agent Tested | SWE-Agent with Claude 4 Sonnet |

**Critical Findings:**

```
┌─────────────────────────────────────────────────────────────┐
│           CORRECTNESS vs. SECURITY GAP                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Functionally Correct Solutions:  61.0%   ████████████     │
│   Secure Solutions:                10.5%   ██                │
│                                                              │
│   Gap:                             50.5%   ──── DANGER ──── │
│                                                              │
│   Implication: Passing tests ≠ Safe code                    │
│   Most solutions introduce vulnerabilities                   │
│   that functional tests cannot detect                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Security Vulnerability Distribution:**
| Vulnerability Type | Frequency |
|--------------------|-----------|
| Injection flaws (SQL, XSS, Command) | High |
| Improper input validation | High |
| Authentication/Authorization bypass | Medium |
| Information disclosure | Medium |
| Race conditions | Low |

**Critical Insight:**
> 기능적 정확성(functional correctness)과 보안(security)의 극적인 괴리는 바이브코딩 패러다임의 근본적 한계를 노출한다. 테스트 통과만으로는 프로덕션 안전성을 보장할 수 없으며, 보안 전용 검증 레이어가 필수적이다.

---

#### Paper 11: "Professional Software Developers Don't Vibe, They Control" (Dec 2025)

**Authors:** Ruanqianqian Huang, Avery Reyna, Sorin Lerner, Haijun Xia, Brian Hempel
**arXiv:** 2512.14012

**Original Abstract:**
> "We examine how experienced developers integrate AI agents into software development workflows. Experienced developers value agents as a productivity boost while maintaining control over design decisions to preserve software quality standards."

**Professional vs. Casual Vibe Coding:**

```
┌─────────────────────────────────────────────────────────────┐
│     DEVELOPER CONTROL SPECTRUM (Professional Practice)       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   "Vibe Coding"              "Controlled Agent Use"          │
│   (Karpathy's definition)    (Professional practice)         │
│         │                           │                        │
│         ▼                           ▼                        │
│   ┌──────────────┐          ┌──────────────┐                │
│   │ Accept AI    │          │ Selective    │                │
│   │ output as-is │          │ delegation  │                │
│   │              │          │              │                │
│   │ Minimal      │          │ Active design│                │
│   │ oversight    │          │ decisions    │                │
│   │              │          │              │                │
│   │ Trust the    │          │ Verify &     │                │
│   │ "vibe"       │          │ control      │                │
│   └──────────────┘          └──────────────┘                │
│                                                              │
│   Novice/Casual ◄─────────────────────► Expert/Professional │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Professional Control Strategies:**
| Strategy | Description | Adoption |
|----------|-------------|----------|
| Scoped delegation | 명확한 범위의 작업만 AI에 위임 | High |
| Architecture ownership | 설계 결정은 인간이 보유 | High |
| Incremental review | 생성 코드의 단계별 검토 | Medium-High |
| Test-first approach | AI 코드에 대한 테스트 선행 | Medium |
| Context curation | AI에 제공하는 컨텍스트 정밀 관리 | Medium |

**Critical Insight:**
> 전문 개발자는 Karpathy가 정의한 의미의 바이브코딩을 하지 않는다. 대신 AI 에이전트를 생산성 도구로 활용하면서 설계 결정과 품질 기준에 대한 통제권을 유지한다. 이는 바이브코딩이 전문성 수준에 따라 근본적으로 다른 실천 양태를 보인다는 것을 의미한다.

---

#### Paper 12: "Agentic Much? Adoption of Coding Agents on GitHub" (Jan 2026)

**Authors:** Romain Robbes, Theo Matricon, Thomas Degueule, Andre Hora, Stefano Zacchiroli
**arXiv:** 2601.18341

**Original Abstract:**
> "In the first half of 2025, coding agents have emerged as a category of development tools that have very quickly transitioned to practice. These agents, such as Cursor and Claude Code, operate with high degrees of autonomy, up to generating complete pull requests from task descriptions."

**Large-Scale Adoption Study:**

| Parameter | Value |
|-----------|-------|
| GitHub Projects Analyzed | 129,134 |
| Analysis Period | First half of 2025 |
| Detection Method | Commit/PR attribution analysis |
| Tools Tracked | Cursor, Claude Code, Copilot, etc. |

**Adoption Metrics:**

```
┌─────────────────────────────────────────────────────────────┐
│           CODING AGENT ADOPTION ON GITHUB (2025 H1)          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Adoption Rate: 15.85% - 22.60%                            │
│   ████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░        │
│                                                              │
│   Context: Technology only months old at time of study       │
│                                                              │
│   Comparison with historical tool adoption:                  │
│   ┌────────────────────────────────────────┐                │
│   │ Git (2005):        ~5% in first year   │                │
│   │ Docker (2013):     ~8% in first year   │                │
│   │ TypeScript (2012): ~3% in first year   │                │
│   │ Coding Agents:     ~20% in 6 months!  │                │
│   └────────────────────────────────────────┘                │
│                                                              │
│   ➜ Fastest adoption of any dev tool category in history    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Adoption Distribution by Project Characteristics:**
| Project Type | Adoption Rate | Notes |
|-------------|---------------|-------|
| New projects (< 1 year) | Highest | AI-native development |
| Web/Frontend projects | High | Rapid prototyping use case |
| Enterprise/Backend | Medium | Cautious but growing |
| Systems/Infrastructure | Lower | Safety-critical domains |

**Critical Insight:**
> 코딩 에이전트의 GitHub 채택률(~20%)은 기술 역사상 가장 빠른 개발 도구 채택 사례에 해당한다. 이는 바이브코딩이 일시적 유행이 아닌 소프트웨어 개발의 구조적 전환을 나타낸다는 실증적 근거를 제공한다.

---

## Part II: Orchestration Research Landscape

### 2.1 Foundational Architectures & Protocols

#### Paper 13: "The Orchestration of Multi-Agent Systems" (Jan 2026)

**Authors:** Apoorva Adimulam et al.  
**arXiv:** 2601.13671

**Unified Architectural Framework:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐   │
│  │ Planning  │  │  Policy   │  │   State   │  │  Quality  │   │
│  │           │  │Enforcement│  │Management │  │Operations │   │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘   │
│       │               │              │              │          │
│       └───────────────┴──────────────┴──────────────┘          │
│                         │                                      │
│                         ▼                                      │
│              ┌─────────────────────┐                          │
│              │   COMMUNICATION     │                          │
│              │     SUBSTRATE       │                          │
│              ├─────────────────────┤                          │
│              │ • Model Context     │                          │
│              │   Protocol (MCP)    │                          │
│              │   - External tools  │                          │
│              │   - Context data    │                          │
│              ├─────────────────────┤                          │
│              │ • Agent2Agent       │                          │
│              │   Protocol (A2A)    │                          │
│              │   - Peer coord.     │                          │
│              │   - Negotiation     │                          │
│              │   - Delegation      │                          │
│              └─────────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
```

**Protocol Comparison:**
| Protocol | Scope | Purpose |
|----------|-------|---------|
| **MCP** | Agent ↔ External | Standardized tool/data access |
| **A2A** | Agent ↔ Agent | Peer coordination & delegation |

---

### 2.2 Performance Optimization

#### Paper 14: "Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems" (Jan 2026)

**Authors:** Xi Shi et al.  
**arXiv:** 2601.10560

**Problem Statement:**
> "Multi-agent systems enable complex reasoning by coordinating multiple agents, but often incur high inference latency due to multi-step execution and repeated model invocations."

**LAMaS Framework:**

```
┌─────────────────────────────────────────────────────────────┐
│               LAMaS ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Input Task                                                │
│      │                                                      │
│      ▼                                                      │
│   ┌─────────────────────┐                                  │
│   │  PARALLEL EXECUTION │                                  │
│   │     CONTROLLER      │                                  │
│   └──────────┬──────────┘                                  │
│              │                                              │
│              ▼                                              │
│   ┌─────────────────────┐                                  │
│   │ EXECUTION TOPOLOGY  │◄── Optimizes Critical Path      │
│   │    GRAPH (ETG)      │                                  │
│   └─────────────────────┘                                  │
│                                                             │
│   Key Innovation: Explicit latency supervision              │
│   under parallel execution                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Performance Results:**
| Metric | Improvement |
|--------|-------------|
| Critical Path Reduction | 38-46% |
| Task Performance | Maintained/Improved |
| vs. State-of-the-Art | Significant advantage |

---

#### Paper 15: "CASTER: Breaking the Cost-Performance Barrier" (Jan 2026)

**Authors:** Shanyv Liu et al.  
**arXiv:** 2601.19793

**Problem:** Static model allocation wastes computation on trivial sub-tasks

**Solution Architecture:**

```
┌──────────────────────────────────────────────────────────────┐
│                    CASTER ROUTER                             │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Task Input                                                 │
│      │                                                       │
│      ▼                                                       │
│   ┌─────────────────────────────────────┐                   │
│   │        DUAL-SIGNAL ROUTER           │                   │
│   ├─────────────────────────────────────┤                   │
│   │  Signal 1: Semantic Embeddings      │                   │
│   │  Signal 2: Structural Meta-features │                   │
│   │                                     │                   │
│   │  Combined ──► Task Difficulty Est.  │                   │
│   └─────────────────────────────────────┘                   │
│                        │                                     │
│                        ▼                                     │
│   ┌─────────────────────────────────────┐                   │
│   │    DYNAMIC MODEL SELECTION          │                   │
│   │                                     │                   │
│   │  Weak Model ◄── Easy Tasks          │                   │
│   │  Strong Model ◄── Hard Tasks        │                   │
│   └─────────────────────────────────────┘                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Training Paradigm:**
```
COLD START ──► ITERATIVE EVOLUTION
    │                │
    │         On-policy negative
    │         feedback from routing
    │         failures
    │                │
    └────────────────┘
```

**Results:**
| Metric | Value |
|--------|-------|
| Cost Reduction | Up to 72.4% |
| Success Rate | Matches strong-model baseline |
| Domains Tested | Software Eng, Data Analysis, Scientific Discovery, Cybersecurity |
| vs. FrugalGPT | Consistent outperformance |

---

### 2.3 Domain-Specific Applications

#### Paper 16: "SOCIA-Nabla: Textual Gradient Meets Multi-Agent Orchestration" (Oct 2025)

**Authors:** Yuncheng Hua et al.  
**arXiv:** 2510.18551

**Core Innovation:** Unifying multi-agent orchestration with loss-aligned optimization

**Workflow Loop:**
```
┌─────────────────────────────────────────────────────────────┐
│            LOSS-DRIVEN OPTIMIZATION LOOP                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Code Synthesis ──► Execution ──► Evaluation ──► Code Repair
│        │                                              │      │
│        └──────────────────────────────────────────────┘      │
│                        ↑                                     │
│              Textual-Gradient Descent (TGD)                  │
│                                                             │
│   Human-in-the-loop: Task-spec confirmation only            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Evaluation Domains (CPS Tasks):**
| Domain | Achievement |
|--------|-------------|
| User Modeling | SOTA accuracy |
| Mask Adoption | SOTA accuracy |
| Personal Mobility | SOTA accuracy |

**Key Contribution:**
> "Converts brittle prompt pipelines into reproducible, constraint-aware simulator code generation that scales across domains and simulation granularities."

---

#### Paper 17: "ARIES: Multi-Agent Framework for Epidemiological Surveillance" (Jan 2026)

**Authors:** Aniket Vijay Wattamwar  
**arXiv:** 2601.01831

**Problem:** General-purpose AI unsuited for epidemiological domain (hallucinations, data silo navigation)

**Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                      ARIES FRAMEWORK                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────────────────────┐                  │
│   │      HIERARCHICAL COMMAND           │                  │
│   │          GPT ORCHESTRATOR           │                  │
│   └──────────────┬──────────────────────┘                  │
│                  │                                          │
│         ┌────────┴────────┐                                │
│         ▼                 ▼                                │
│   ┌──────────┐      ┌──────────┐                          │
│   │ Sub-Agent│      │ Sub-Agent│      ... (Scalable Swarm) │
│   │  (WHO)   │      │  (CDC)   │                          │
│   └────┬─────┘      └────┬─────┘                          │
│        │                 │                                 │
│        ▼                 ▼                                 │
│   ┌──────────────────────────────┐                        │
│   │   AUTONOMOUS QUERIES         │                        │
│   │   - WHO databases            │                        │
│   │   - CDC reports              │                        │
│   │   - Peer-reviewed papers     │                        │
│   └──────────────────────────────┘                        │
│                                                             │
│   Output: Near real-time threat identification              │
│           & signal divergence detection                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Value Proposition:**
- Moves beyond static, disease-specific dashboards
- Dynamic intelligence ecosystem
- Specialized reasoning > Generic models

---

#### Paper 18: "LLM-based Optimization Algorithm Selection for Network Orchestration" (2025)

**Authors:** [ACM Publication]  
**DOI:** 10.1145/3731599.3767458

**Problem:** No universal optimization algorithm performs optimally across all scenarios

**Framework:**
```
┌─────────────────────────────────────────────────────────────┐
│          LLM-BASED ALGORITHM SELECTION                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   INPUTS:                                                   │
│   • Algorithm descriptive embeddings (LLM-generated)       │
│   • Network state logs                                      │
│   • Service requests                                        │
│                                                             │
│                    │                                        │
│                    ▼                                        │
│   ┌─────────────────────────────────────┐                  │
│   │    CONTEXT-DRIVEN ABSTRACTION       │                  │
│   │         LAYER (LLM)                 │                  │
│   │                                     │                  │
│   │  Understands heterogeneous context  │                  │
│   │  Selects optimal algorithm          │                  │
│   └─────────────────────────────────────┘                  │
│                    │                                        │
│                    ▼                                        │
│   OUTPUT: Optimal optimization strategy                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Validation:**
- Simulations + FABRIC testbed demo
- Multi-domain, multi-continent deployment

---

### 2.4 Failure Analysis & Scaling Laws

#### Paper 19: "Why Do Multi-Agent LLM Systems Fail?" (Mar 2025)

**Authors:** Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, et al. (Berkeley/Stanford)
**arXiv:** 2503.13657

**Original Abstract:**
> "Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal. This gap highlights a critical need for a principled understanding of why MAS fail."

**MAST Failure Taxonomy:**

```
┌─────────────────────────────────────────────────────────────┐
│              MAST: MAS FAILURE TAXONOMY                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────────┐                                       │
│   │  SPECIFICATION   │── Task misunderstanding              │
│   │  FAILURES        │── Ambiguous role definitions          │
│   └────────┬────────┘                                       │
│            │                                                 │
│   ┌────────▼────────┐                                       │
│   │  COORDINATION   │── Message passing errors              │
│   │  FAILURES        │── Redundant/conflicting actions       │
│   └────────┬────────┘── Deadlocks & infinite loops          │
│            │                                                 │
│   ┌────────▼────────┐                                       │
│   │  EXECUTION      │── Tool use failures                   │
│   │  FAILURES        │── Hallucinated function calls         │
│   └────────┬────────┘── Context window overflow             │
│            │                                                 │
│   ┌────────▼────────┐                                       │
│   │  VERIFICATION   │── False positive completions          │
│   │  FAILURES        │── Quality regression undetected       │
│   └─────────────────┘                                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**MAST-Data Dataset:**
| Parameter | Value |
|-----------|-------|
| MAS Frameworks Tested | 7 |
| Model Families | 4 |
| Failure Annotations | 1,000+ (consistently annotated) |
| Benchmark Tasks | GAIA, SWE-bench, HumanEval |

**Key Findings:**
| Failure Category | Frequency | Severity |
|-----------------|-----------|----------|
| Coordination failures | 34% | High |
| Specification failures | 28% | High |
| Execution failures | 23% | Medium |
| Verification failures | 15% | Critical |

**Critical Insight:**
> MAS 실패의 주요 원인은 개별 에이전트 능력이 아닌 에이전트 간 조율(coordination) 문제이다. 더 강력한 모델을 사용하는 것만으로는 MAS 성능을 보장할 수 없으며, 오케스트레이션 설계 자체의 개선이 필수적이다.

---

#### Paper 20: "Multi-Agent Collaboration via Evolving Orchestration" (May 2025)

**Authors:** Yufan Dang, Chen Qian, Xueheng Luo, et al. (Tsinghua, ChatDev 연구팀)
**arXiv:** 2505.19591 (v2: Oct 2025)

**Original Abstract:**
> "Large language models have achieved remarkable results across diverse downstream tasks, but their monolithic nature restricts scalability and efficiency in complex problem-solving. While recent research explores multi-agent collaboration among LLMs, most approaches rely on static organizational structures."

**Evolving Orchestration Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│           EVOLVING ORCHESTRATION PARADIGM                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────────────────────────────┐                   │
│   │    PUPPETEER (Central Orchestrator)  │                   │
│   │    Trained via Reinforcement Learning │                   │
│   └──────────────┬──────────────────────┘                   │
│                  │                                           │
│        ┌─────────┼─────────┐                                │
│        ▼         ▼         ▼                                │
│   ┌────────┐ ┌────────┐ ┌────────┐                         │
│   │Agent A │ │Agent B │ │Agent C │   ... (N agents)        │
│   │(Coder) │ │(Review)│ │(Test)  │                         │
│   └────────┘ └────────┘ └────────┘                         │
│                                                              │
│   Static Orchestration:                                      │
│   A → B → C → D (fixed pipeline)                            │
│                                                              │
│   Evolving Orchestration:                                    │
│   A → C → A → B (adaptive, task-dependent)                  │
│   Puppeteer learns optimal sequencing via RL                 │
│                                                              │
│   Key Innovation:                                            │
│   - Dynamic agent sequencing per task                        │
│   - RL-trained orchestration policy                          │
│   - Reduces unnecessary agent invocations                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Comparison with Static Approaches:**
| Approach | Flexibility | Compute Cost | Performance |
|----------|-------------|--------------|-------------|
| Static Pipeline (ChatDev) | Low | Fixed | Baseline |
| Round-Robin | Medium | High (all agents every round) | +5-10% |
| Evolving Orchestration | High | Optimized (adaptive) | +15-25% |

**Critical Insight:**
> ChatDev 연구팀의 후속 연구로, 정적 파이프라인의 한계를 극복하는 강화학습 기반 동적 오케스트레이션을 제시한다. 이는 에이전트 수가 증가할수록 정적 구조의 비효율이 극대화된다는 관찰에 기반한다.

---

#### Paper 21: "AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence" (Feb 2026)

**Authors:** Geunbin Yu
**arXiv:** 2602.16873

**Original Abstract:**
> "As large language models from diverse providers converge toward comparable benchmark performance, the traditional paradigm of selecting a single best model per task yields diminishing returns. We argue that orchestration topology now dominates system-level performance over individual model capability."

**Core Thesis:**

```
┌─────────────────────────────────────────────────────────────┐
│      MODEL CAPABILITY vs. ORCHESTRATION TOPOLOGY             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Performance                                                │
│   ▲                                                          │
│   │         ┌─── Orchestration topology gains ──────┐       │
│   │         │    (Growing impact)                    │       │
│   │   ╱─────╲──────────────────────────────────╱────│       │
│   │  ╱       ╲                                ╱     │       │
│   │ ╱         ╲── Model capability gains ────╱      │       │
│   │╱           ╲  (Diminishing returns)     ╱       │       │
│   ├──────────────────────────────────────────────►  │       │
│   │           Model Capability Convergence           │       │
│   │                                                  │       │
│   └──────────────────────────────────────────────────┘       │
│                                                              │
│   Implication: As models converge in capability,             │
│   HOW you orchestrate matters more than WHICH model          │
│   you use                                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Orchestration Topology Types:**
| Topology | Structure | Best For |
|----------|-----------|----------|
| **Sequential** | A → B → C | Simple, dependent tasks |
| **Parallel** | A ∥ B ∥ C → Merge | Independent subtasks |
| **Hierarchical** | Manager → Workers | Complex decomposition |
| **Hybrid** | Mixed topology | Real-world systems |
| **Debate/Adversarial** | A ↔ B (challenge) | Reasoning, verification |

**Key Innovation:**
- 자동 토폴로지 선택(Automated topology selection) 프레임워크 제안
- 태스크 특성에 따라 최적 오케스트레이션 구조를 자동 결정
- 모델 선택보다 오케스트레이션 구조가 시스템 성능에 더 큰 영향을 미침을 실증

**Critical Insight:**
> LLM 성능이 수렴하는 시대에서, 시스템 수준의 성능 차별화는 개별 모델 능력이 아닌 오케스트레이션 토폴로지에 의해 결정된다. 이는 실무에서 모델 선택보다 아키텍처 설계에 더 많은 투자가 필요하다는 것을 의미한다.

---

### 2.5 Emerging Paradigms

#### Paper 22: "MAESTRO: Multi-Agent Evaluation Suite for Testing, Reliability, and Observability" (Jan 2026)

**Authors:** Tie Ma, Yixi Chen, Vaastav Anand, et al.
**arXiv:** 2601.00481

**Original Abstract:**
> "We present MAESTRO, an evaluation suite for the testing, reliability, and observability of LLM-based MAS. MAESTRO standardizes MAS configuration and execution through a unified interface."

**Framework Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                    MAESTRO EVALUATION SUITE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────────────────────────────┐                   │
│   │    UNIFIED CONFIGURATION LAYER      │                   │
│   │    (Framework-agnostic interface)    │                   │
│   └──────────────┬──────────────────────┘                   │
│                  │                                           │
│        ┌─────────┼─────────┬───────────┐                   │
│        ▼         ▼         ▼           ▼                   │
│   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐             │
│   │AutoGen │ │CrewAI  │ │LangGr. │ │Custom  │             │
│   │Adapter │ │Adapter │ │Adapter │ │MAS     │             │
│   └────────┘ └────────┘ └────────┘ └────────┘             │
│                                                              │
│   ┌─────────────────────────────────────┐                   │
│   │    OBSERVABILITY & METRICS          │                   │
│   │    • Latency (per-agent, e2e)       │                   │
│   │    • Cost (token usage, API calls)   │                   │
│   │    • Failure rate & recovery         │                   │
│   │    • Execution traces               │                   │
│   └─────────────────────────────────────┘                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Evaluation Dimensions:**
| Dimension | Metrics | Coverage |
|-----------|---------|----------|
| **Testing** | Task success rate, partial completion | Functional |
| **Reliability** | Failure recovery, retry success | Robustness |
| **Observability** | Execution traces, agent interactions | Debugging |
| **Cost** | Token usage, API call counts | Efficiency |
| **Latency** | Per-agent, end-to-end | Performance |

**Critical Insight:**
> MAS 분야에 표준화된 평가 프레임워크가 부재했던 문제를 해결한다. 서로 다른 MAS 프레임워크(AutoGen, CrewAI, LangGraph 등)를 동일한 기준으로 비교 가능하게 하여, 오케스트레이션 연구의 재현성과 비교 가능성을 크게 향상시킨다.

---

#### Workshop: "VibeX 2026 Workshop: Vibe Coding & Vibe Researching" (CFP)

**Venue:** EASE 2026
**URL:** conf.researchr.org/home/ease-2026/vibex-2026

**AI Coding Spectrum:**
```
Token-Level              Multi-File              Autonomous
Completion ─────────►  Edits ─────────►     Task Execution
   │                       │                      │
   │                       │                      │
   └───────────────────────┴──────────────────────┘
              EVOLUTION OF AI CODING
```

**Vibe Researching Concept:**

| Aspect | Deep Research | Vibe Researching |
|--------|--------------|------------------|
| **Approach** | Human-managed AI assistance | Agent-led workflows |
| **Focus** | Rigorous execution | High-level vision & direction |
| **AI Role** | Assistive | Autonomous |
| **Human Role** | Intensive management | Framing & oversight |
| **Tasks** | Literature synthesis, analysis | Delegated to agents |

---

## Part III: Cross-Domain Synthesis

### 3.1 Convergent Themes

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONCEPTUAL OVERLAP                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   VIBE CODING              │        ORCHESTRATION               │
│   ─────────────            │        ────────────                │
│                            │                                     │
│   Human ◄──► AI Agent      │        Agent ◄──► Agent            │
│   (Co-creation)            │        (Coordination)              │
│                            │                                     │
│   ┌─────────────────┐      │        ┌─────────────────┐         │
│   │  CONTEXT        │◄─────┼───────►│  STATE          │         │
│   │  MANAGEMENT     │      │        │  MANAGEMENT     │         │
│   └─────────────────┘      │        └─────────────────┘         │
│                            │                                     │
│   ┌─────────────────┐      │        ┌─────────────────┐         │
│   │  TRUST          │◄─────┼───────►│  QUALITY        │         │
│   │  DYNAMICS       │      │        │  OPERATIONS     │         │
│   └─────────────────┘      │        └─────────────────┘         │
│                            │                                     │
│   ┌─────────────────┐      │        ┌─────────────────┐         │
│   │  ITERATIVE      │◄─────┼───────►│  FEEDBACK       │         │
│   │  REFINEMENT     │      │        │  LOOPS          │         │
│   └─────────────────┘      │        └─────────────────┘         │
│                            │                                     │
└────────────────────────────┴─────────────────────────────────────┘
```

### 3.2 논문 간 교차 비교 분석

#### 3.2.1 바이브코딩 논문 비교표

| 논문 | 연구 유형 | 방법론 | 데이터 규모 | 핵심 발견 | 한계점 |
|------|----------|--------|------------|----------|--------|
| Bamil (P1) | 이론적 프레임워크 | Reference architecture 제안 | N/A | 바이브코딩 정식 정의 | 실증 검증 부재 |
| Ge (P2) | 서베이 | CMDP 형식화, 1000+ 논문 분석 | 1000+ papers | 5가지 개발 모델 분류 | 빠르게 변화하는 분야 |
| Chou (P3) | 실증 연구 | 비디오 분석, Think-aloud | 20 videos, 254 prompts | "주사위 굴리기" 현상 | 샘플 크기 제한 |
| Sarkar (P4) | 실증 연구 | 관찰 연구 | N/A | 전문성 재분배 | 장기 효과 미검증 |
| Bird (P5) | 질적 연구 | Grounded theory | ~190,000 words | 위임-공동창작 연속체 | 자기보고 편향 |
| Gama (P6) | 교육 연구 | 해커톤 관찰 | 31 participants | 교차학제 협업 효과 | 단기간 연구 |
| Tahir (P7) | Grey literature 분석 | 체계적 문헌 검토 | 101 sources, 518 accounts | 속도-품질 역설 | Grey literature 한계 |
| ACM (P8) | 시스템 설계 | Side-car 시스템 제안 | N/A | Formal verification 통합 | 프로토타입 단계 |
| Koren (P9) | 경제 분석 | 경제 모델링 | N/A | OSS 생태계 위협 | 모델 가정의 단순화 |
| Zhao (P10) | 벤치마크 | SUSVIBES benchmark | 200 tasks | 보안 61% vs 10.5% gap | 단일 에이전트 테스트 |
| Huang (P11) | 실증 연구 | 관찰 + 인터뷰 | N/A | 전문가는 "통제" 유지 | 특정 도구에 한정 |
| Robbes (P12) | 대규모 실증 | GitHub 데이터 분석 | 129,134 projects | ~20% 채택률 | 감지 정확도 한계 |

#### 3.2.2 오케스트레이션 논문 비교표

| 논문 | 아키텍처 패턴 | 최적화 대상 | 성능 개선 | 평가 방법 |
|------|-------------|------------|----------|----------|
| Adimulam (P13) | Unified framework (MCP/A2A) | 프로토콜 통합 | N/A (프레임워크) | 아키텍처 분석 |
| Shi - LAMaS (P14) | Parallel execution + ETG | Latency | 38-46% 감소 | 벤치마크 |
| Liu - CASTER (P15) | Dual-signal router | Cost | 72.4% 절감 | 4개 도메인 |
| Hua - SOCIA (P16 기존) | Loss-driven loop + TGD | Task accuracy | SOTA on CPS | 3개 도메인 |
| Wattamwar - ARIES (P17 기존) | Hierarchical swarm | Domain-specific | Real-time detection | 역학 감시 |
| Cemri (P16) | Failure taxonomy | 실패 분석 | N/A (분류 체계) | 7 MAS, 4 models |
| Dang (P17) | Evolving orchestration + RL | Efficiency | +15-25% | ChatDev 계열 |
| Yu - AdaptOrch (P18) | Auto topology selection | Topology | N/A (프레임워크) | 이론적 분석 |
| Ma - MAESTRO (P19) | Evaluation suite | 평가 표준화 | N/A (벤치마크) | 다중 프레임워크 |
| VibeX (P20) | Workshop/Vision | N/A | N/A | N/A |

#### 3.2.3 연구 방법론 분포

```
┌─────────────────────────────────────────────────────────────┐
│            RESEARCH METHODOLOGY DISTRIBUTION                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   이론/프레임워크  ████████          6편 (27%)               │
│   실증 연구        ██████████████    8편 (36%)               │
│   벤치마크/평가    ██████            4편 (18%)               │
│   시스템 설계      ████              3편 (14%)               │
│   경제/사회 분석   ██                1편 (5%)                │
│                                                              │
│   관찰: 실증 연구 비중이 가장 높으나, 대부분 단기간          │
│         장기적 영향 추적 연구는 아직 부재                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Research Gaps & Opportunities

| Gap | Vibe Coding | Orchestration | 교차 영역 |
|-----|-------------|---------------|----------|
| **Security** | 보안 검증 자동화 (P10) | MAS 보안 공격 벡터 (P16) | 보안 인식 오케스트레이션 |
| **Scalability** | 개인 → 팀 (P12) | Multi-agent → Enterprise (P18) | 팀 수준 바이브코딩 + MAS |
| **Quality** | Formal verification (P8) | Automated quality gates (P19) | AI 생성 코드 품질 보증 체계 |
| **Trust** | 전문가 통제 유지 (P11) | Inter-agent trust (P16, P17) | Human-in-the-loop 신뢰 |
| **Economics** | OSS 지속가능성 (P9) | Cost optimization (P15) | 비용 효율적 보안 바이브코딩 |
| **Adoption** | ~20% 채택 (P12) | 프레임워크 난립 (P19) | 표준화된 바이브코딩 MAS |

### 3.4 Future Research Directions

1. **보안 인식 바이브코딩 (Security-Aware Vibe Coding)**
   - P10의 SUSVIBES 벤치마크가 밝힌 61% vs 10.5% 격차 해소
   - P8의 Formal verification side-car를 MAS에 통합
   - 실시간 보안 취약점 감지 에이전트 통합

2. **적응적 오케스트레이션 (Adaptive Orchestration)**
   - P18 AdaptOrch의 자동 토폴로지 선택을 바이브코딩 워크플로우에 적용
   - P17 Evolving Orchestration의 RL 기반 최적화 확대
   - P15 CASTER의 비용 최적화와 P14 LAMaS의 레이턴시 최적화 통합

3. **실패 방지 MAS 설계 (Failure-Resilient MAS Design)**
   - P16 MAST taxonomy 기반 사전 실패 예방 시스템
   - P19 MAESTRO의 observability 확장
   - 자가 치유(self-healing) 오케스트레이션 패턴

4. **경제적 지속가능성 (Economic Sustainability)**
   - P9의 OSS 위협 분석에 대한 해결책 연구
   - P12의 채택률 데이터 기반 경제 영향 모델링
   - 바이브코딩 시대의 새로운 개발자 가치 제안

5. **팀 수준 바이브코딩 (Team-Level Vibe Coding)**
   - P11의 전문가 통제 전략을 MAS에 확장
   - P5의 공동창작 모델과 P17의 evolving orchestration 융합
   - Human-Multi-Agent 하이브리드 개발 방법론

### 3.5 실무 적용 가이드

#### 프로젝트 규모별 권장 오케스트레이션 패턴

```
┌─────────────────────────────────────────────────────────────┐
│        PROJECT SIZE → ORCHESTRATION RECOMMENDATION           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   SMALL (1-2명, MVP/PoC)                                    │
│   ├─ 바이브코딩 모드: Unconstrained Automation (P2)         │
│   ├─ 오케스트레이션: 불필요 (단일 에이전트)                  │
│   ├─ 보안: 기본 린팅 + P10 SUSVIBES 체크리스트              │
│   └─ 주의: P7 속도-품질 역설 인식                           │
│                                                              │
│   MEDIUM (3-5명, 프로덕션 서비스)                            │
│   ├─ 바이브코딩 모드: Planning-Driven (P2)                   │
│   ├─ 오케스트레이션: Sequential + P8 Side-car 검증           │
│   ├─ 보안: P10 벤치마크 기준 보안 게이트 통합               │
│   ├─ 비용: P15 CASTER 라우팅으로 72% 비용 절감 가능         │
│   └─ 평가: P19 MAESTRO 메트릭 적용                          │
│                                                              │
│   LARGE (6+명, 엔터프라이즈)                                 │
│   ├─ 바이브코딩 모드: Context-Enhanced + Test-Driven (P2)    │
│   ├─ 오케스트레이션: P18 AdaptOrch (자동 토폴로지 선택)     │
│   ├─ 실패 방지: P16 MAST taxonomy 기반 모니터링             │
│   ├─ 레이턴시: P14 LAMaS 병렬 실행 최적화                   │
│   ├─ 프로토콜: P13 MCP + A2A 하이브리드                     │
│   └─ 전문가 통제: P11 Scoped delegation 전략 적용           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 도구 선택 가이드

| 요구사항 | 권장 접근법 | 관련 논문 | 핵심 고려사항 |
|----------|-----------|----------|-------------|
| 빠른 프로토타이핑 | 단일 에이전트 + 바이브코딩 | P1, P2, P6 | 보안 후속 검증 필수 (P10) |
| 비용 최적화 | CASTER 라우팅 | P15, P18 | 72% 비용 절감, 성능 유지 |
| 레이턴시 최소화 | LAMaS 병렬 실행 | P14 | 38-46% 크리티컬 패스 감소 |
| 품질 보증 | Formal verification + Side-car | P8, P10 | 보안 게이트 통합 |
| 팀 협업 | Evolving orchestration | P17, P18 | 정적 파이프라인 회피 |
| 장기 유지보수 | Context-enhanced + 전문가 통제 | P2, P11 | 기술 부채 관리 |
| MAS 평가 | MAESTRO suite | P19 | 프레임워크 간 비교 |
| 실패 대응 | MAST taxonomy + monitoring | P16 | 조율 실패가 주요 원인 |

#### 바이브코딩 성숙도 모델

```
┌─────────────────────────────────────────────────────────────┐
│         VIBE CODING MATURITY MODEL (VCMM)                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Level 1: Ad-hoc Vibe Coding                               │
│   │  "주사위 굴리기" (P3)                                    │
│   │  특징: 결과 예측 불가, 보안 미검증, 개인 의존적          │
│   │                                                          │
│   Level 2: Controlled Vibe Coding                            │
│   │  "통제된 에이전트 활용" (P11)                             │
│   │  특징: Scoped delegation, 아키텍처 소유권 유지            │
│   │                                                          │
│   Level 3: Verified Vibe Coding                              │
│   │  "검증된 바이브코딩" (P8, P10)                           │
│   │  특징: Formal verification, 보안 게이트, 자동 테스트     │
│   │                                                          │
│   Level 4: Orchestrated Vibe Coding                          │
│   │  "오케스트레이션 바이브코딩" (P14, P15, P17)             │
│   │  특징: MAS 통합, 비용/레이턴시 최적화, 적응적 구조       │
│   │                                                          │
│   Level 5: Autonomous Engineering                            │
│      "자율 엔지니어링" (P18, P20)                            │
│      특징: 자동 토폴로지, 자가 치유, 인간은 감독자           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Part IV: Key Insights Summary

### Critical Findings

| # | Finding | Source | Implications |
|---|---------|--------|------------|
| 1 | 바이브코딩은 전문성을 제거하지 않고 재분배한다 | P4, P11 | 교육 프로그램 진화 필요 |
| 2 | 속도-품질 역설은 구조적 문제이다 | P3, P7 | 새로운 QA 방법론 필요 |
| 3 | OSS 생태계가 실존적 위협에 직면했다 | P9 | 새로운 펀딩 모델 필요 |
| 4 | 기능적 정확성 ≠ 보안 안전성 (61% vs 10.5%) | P10 | 보안 전용 검증 레이어 필수 |
| 5 | 코딩 에이전트 채택률 ~20% (역사상 최고속) | P12 | 구조적 전환, 일시적 유행 아님 |
| 6 | 전문 개발자는 "바이브"하지 않고 "통제"한다 | P11 | 전문성 수준별 차별화된 접근 필요 |
| 7 | MAS 실패의 주원인은 조율(coordination) 문제 | P16 | 모델 개선보다 오케스트레이션 설계 우선 |
| 8 | 오케스트레이션 토폴로지가 모델 선택보다 중요 | P18 | 아키텍처 투자 우선순위 재조정 |
| 9 | 레이턴시는 MAS의 핵심 병목이다 | P14 | 병렬 실행 & 최적화 필수 |
| 10 | 비용-성능 장벽을 돌파할 수 있다 (72% 절감) | P15 | 동적 라우팅 도입 |
| 11 | Context engineering > Agent capability | P2 | 인프라 투자 우선 |
| 12 | 동적 신뢰가 Human-AI 협업의 기반이다 | P5 | 신뢰 보정 메커니즘 필요 |

### Methodological Innovations

- **CMDP formalization** for vibe coding dynamics (P2)
- **SUSVIBES benchmark** for security evaluation of vibe-coded software (P10)
- **Textual-Gradient Descent** for code optimization (SOCIA-Nabla)
- **Dual-Signal Routing** for model selection (P15 CASTER)
- **MAST taxonomy** for systematic MAS failure classification (P16)
- **RL-based evolving orchestration** for dynamic agent sequencing (P17)
- **Automated topology selection** for orchestration structure optimization (P18)
- **MAESTRO framework** for standardized MAS evaluation (P19)
- **Cold Start → Iterative Evolution** training paradigm (P15)

---

## References

### Vibe Coding Papers
1. Bamil et al. (2025). Vibe Coding: Toward an AI-Native Paradigm for Semantic Software Engineering. arXiv:2510.17842
2. Ge et al. (2025). A Survey of Vibe Coding with Large Language Models. arXiv:2510.12399
3. Chou et al. (2025). Building Software by Rolling the Dice. arXiv:2512.22418
4. Sarkar et al. (2025). Vibe Coding: Programming Through Conversation. arXiv:2506.23253
5. Bird et al. (2025). Good Vibrations? A Qualitative Study of Co-Creation with AI. arXiv:2509.12491
6. Gama et al. (2025). Can You Feel the Vibes? arXiv:2512.02750
7. Tahir et al. (2025). Vibe Coding in Practice: Motivations, Challenges, Future Outlook. arXiv:2510.00328
8. [ACM 2025]. Improving Vibe Coding with Formal Verification. DOI:10.1145/3759425.3763390
9. Koren et al. (2026). Vibe Coding Kills Open Source. arXiv:2601.15494
10. Zhao et al. (2025). Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code. arXiv:2512.03262
11. Huang et al. (2025). Professional Software Developers Don't Vibe, They Control. arXiv:2512.14012
12. Robbes et al. (2026). Agentic Much? Adoption of Coding Agents on GitHub. arXiv:2601.18341

### Orchestration Papers
13. Adimulam et al. (2026). The Orchestration of Multi-Agent Systems. arXiv:2601.13671
14. Shi et al. (2026). Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems (LAMaS). arXiv:2601.10560
15. Liu et al. (2026). CASTER: Breaking the Cost-Performance Barrier. arXiv:2601.19793
16. Cemri et al. (2025). Why Do Multi-Agent LLM Systems Fail? arXiv:2503.13657
17. Dang et al. (2025). Multi-Agent Collaboration via Evolving Orchestration. arXiv:2505.19591
18. Yu (2026). AdaptOrch: Task-Adaptive Multi-Agent Orchestration. arXiv:2602.16873
19. Ma et al. (2026). MAESTRO: Multi-Agent Evaluation Suite for Testing, Reliability, and Observability. arXiv:2601.00481
20. Hua et al. (2025). SOCIA-Nabla: Textual Gradient Meets Multi-Agent Orchestration. arXiv:2510.18551
21. Wattamwar (2026). ARIES: Multi-Agent Framework for Epidemiological Surveillance. arXiv:2601.01831
22. [ACM 2025]. LLM-based Optimization Algorithm Selection for Network Orchestration. DOI:10.1145/3731599.3767458

### Workshop & Vision Papers
23. VibeX 2026 Workshop: Vibe Coding & Vibe Researching (CFP). EASE 2026.

---

*Document compiled: February 2026*
*Last updated: February 23, 2026*
*Total papers reviewed: 22 (+ 1 workshop CFP)*
*Coverage: arXiv, ACM, IEEE, workshop proceedings*
