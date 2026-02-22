# 바이브코딩 도구 가이드

AI 코딩 도구별 실전 사용법 및 팁 모음

---

## 가이드 목록

| 가이드 | 설명 | 도구 |
|--------|------|------|
| [AI 코딩 도구 실전 사용법](./AI-코딩-도구-실전-사용법.md) | Claude Code, Kimi CLI, Codex CLI 모델별 상세 명령어 및 설정 | 전체 |
| [Claude Code 바이브코딩 가이드](./Claude-Code-바이브코딩-가이드.md) | Claude Code 실전 팁 및 워크플로우 | Claude Code |
| [Kimi 바이브코딩 가이드](./Kimi-바이브코딩-가이드.md) | Kimi CLI 실전 팁 및 워크플로우 | Kimi CLI |

---

## 도구별 빠른 시작

### Claude Code

```bash
# 설치
curl -fsSL https://claude.ai/install.sh | bash

# 실행
claude

# 모델 선택
claude --model opus    # 복잡한 작업
claude --model sonnet  # 일반 작업 (기본)
claude --model haiku   # 빠른 작업
```

### Kimi CLI

```bash
# 설치
curl -LsSf https://code.kimi.com/install.sh | bash

# 실행
kimi

# 로그인
/login
```

### Codex CLI

```bash
# 설치
npm install -g @openai/codex

# 실행
codex

# 비대화형
codex exec "task"
```

---

## 도구 선택 가이드

| 상황 | 추천 도구 | 이유 |
|------|-----------|------|
| 비용 우선 | Kimi CLI | 가장 저렴한 가격 |
| 성능 우선 | Claude Code (Opus) | 최고의 추론 능력 |
| 오픈소스 필요 | Codex CLI | Apache 2.0 라이선스 |
| 멀티모달 작업 | Kimi CLI | 뛰어난 비전 기능 |
| CI/CD 통합 | Codex CLI | exec 모드 지원 |

---

> 💡 **팁**: 각 도구의 상세한 명령어와 설정은 [AI 코딩 도구 실전 사용법](./AI-코딩-도구-실전-사용법.md) 문서를 참고하세요.
