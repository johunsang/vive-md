# vive-md

바이브코딩용 개발 가이드 & 워터폴 산출물 템플릿 모음.

프로젝트에 해당 가이드를 복사하면 Claude Code가 보안 / 생산성 / 성능 모범 사례를 자동으로 적용합니다. 워터폴 산출물 템플릿으로 SRS, 설계서, 테스트 계획서 등을 바로 생성할 수 있습니다.

## 기술 스택 가이드

| 스택 | 파일 | 핵심 기술 | 분량 |
|------|------|-----------|------|
| Spring Boot | `templates/spring-boot/Spring-Boot-개발가이드.md` | Spring Boot 3.x, Java 17+, Gradle | ~3200줄 |
| Vue.js | `templates/vue/Vue3-개발가이드.md` | Vue 3, Composition API, TypeScript, Vite, Pinia | ~3000줄 |
| React | `templates/react/React-개발가이드.md` | React 18+, TypeScript, Vite | ~3000줄 |
| Next.js | `templates/nextjs/NextJS-개발가이드.md` | Next.js 14+, App Router, TypeScript, RSC | ~2700줄 |

## 크로스커팅 가이드

| 분야 | 파일 | 설명 | 분량 |
|------|------|------|------|
| 디자인 시스템 | `templates/design-system/디자인시스템-가이드.md` | 디자인 토큰, 컴포넌트, 접근성, 다크모드 | ~2500줄 |
| 보안 | `templates/security/보안-가이드.md` | OWASP Top 10, 인증/인가, 데이터 보호, API 보안 | ~2900줄 |

## 워터폴 방법론 산출물 템플릿

### Phase 0: 기획
| 산출물 | 파일 |
|--------|------|
| 서비스 기획서 | `templates/waterfall/00-기획/서비스기획서.md` |
| 비즈니스 정책서 | `templates/waterfall/00-기획/비즈니스정책서.md` |

### Phase 1: 요구사항 분석
| 산출물 | 파일 |
|--------|------|
| 요구사항 명세서 (SRS) | `templates/waterfall/01-요구사항분석/요구사항명세서-SRS.md` |
| 유스케이스 명세서 | `templates/waterfall/01-요구사항분석/유스케이스명세서.md` |
| 요구사항 추적 매트릭스 | `templates/waterfall/01-요구사항분석/요구사항추적매트릭스-RTM.md` |

### Phase 2: 시스템 설계
| 산출물 | 파일 |
|--------|------|
| 시스템 아키텍처 설계서 (SAD) | `templates/waterfall/02-시스템설계/시스템아키텍처설계서-SAD.md` |
| 데이터베이스 설계서 | `templates/waterfall/02-시스템설계/데이터베이스설계서.md` |
| API 설계서 | `templates/waterfall/02-시스템설계/API설계서.md` |
| 화면 설계서 | `templates/waterfall/02-시스템설계/화면설계서.md` |

### Phase 3: 상세 설계
| 산출물 | 파일 |
|--------|------|
| 상세 설계서 | `templates/waterfall/03-상세설계/상세설계서.md` |

### Phase 5: 테스트
| 산출물 | 파일 |
|--------|------|
| 테스트 계획서 | `templates/waterfall/05-테스트/테스트계획서.md` |
| 테스트 케이스 | `templates/waterfall/05-테스트/테스트케이스.md` |
| 테스트 결과 보고서 | `templates/waterfall/05-테스트/테스트결과보고서.md` |

### Phase 6: 배포
| 산출물 | 파일 |
|--------|------|
| 배포 계획서 | `templates/waterfall/06-배포/배포계획서.md` |
| 운영 가이드 | `templates/waterfall/06-배포/운영가이드.md` |

### Phase 7: 유지보수
| 산출물 | 파일 |
|--------|------|
| 유지보수 계획서 | `templates/waterfall/07-유지보수/유지보수계획서.md` |

### 검토 & 프로젝트 관리
| 산출물 | 파일 |
|--------|------|
| 단계별 검토 체크리스트 | `templates/waterfall/08-검토/단계별검토-체크리스트.md` |
| UX 검토서 | `templates/waterfall/08-검토/UX검토서.md` |
| 프로젝트 관리 산출물 | `templates/waterfall/08-검토/프로젝트관리-산출물.md` |

## 사용법

### 기술 스택 가이드 사용

```bash
# 예: React 프로젝트에 개발 가이드 적용
cp "templates/react/React-개발가이드.md" /path/to/your-project/CLAUDE.md

# 보안 가이드 추가
cp "templates/security/보안-가이드.md" /path/to/your-project/보안-가이드.md
```

### 워터폴 산출물 생성

```bash
# 프로젝트 산출물 디렉토리에 템플릿 복사
cp -r templates/waterfall/ /path/to/your-project/docs/

# Claude Code에게 요청:
# "요구사항명세서-SRS.md를 참고해서 우리 프로젝트의 SRS를 작성해줘"
# "테스트계획서.md 템플릿을 기반으로 테스트 계획서를 만들어줘"
# "단계별검토-체크리스트.md로 현재 설계를 검토해줘"
```

### 조합 사용 예시

```bash
# 풀스택 프로젝트: Spring Boot + React + 보안 + 디자인
cp "templates/spring-boot/Spring-Boot-개발가이드.md" my-project/CLAUDE.md
cp "templates/react/React-개발가이드.md" my-project/frontend/CLAUDE.md

# 워터폴 SI 프로젝트: 전체 산출물 세트
cp -r templates/waterfall/ my-project/docs/
cp "templates/security/보안-가이드.md" my-project/docs/
```

## 예시 프롬프트

```
# 개발 가이드 활용
"이 프로젝트에 로그인 기능을 추가해줘" → 가이드의 인증/인가 패턴 자동 적용
"사용자 목록 API를 만들어줘" → 가이드의 API 패턴, 보안, 성능 최적화 적용

# 워터폴 산출물 생성
"요구사항명세서-SRS.md를 기반으로 우리 쇼핑몰 프로젝트의 SRS를 작성해줘"
"시스템아키텍처설계서-SAD.md 템플릿으로 마이크로서비스 아키텍처를 설계해줘"
"API설계서.md를 참고해서 주문 관련 API를 설계해줘"
"테스트계획서.md 기반으로 테스트 계획을 수립해줘"
"단계별검토-체크리스트.md로 현재 요구사항 문서를 검토해줘"
"UX검토서.md를 기준으로 로그인 화면의 UX를 검토해줘"
```

## 기여

PR 환영합니다. 새로운 스택 가이드나 산출물 템플릿을 추가해 주세요.

## 라이선스

MIT
