# 요구사항 추적 매트릭스 (RTM)

> Requirements Traceability Matrix

---

## 문서 정보

| 항목 | 내용 |
|------|------|
| 프로젝트명 | [placeholder: 프로젝트명] |
| 문서 번호 | RTM-[placeholder: 문서번호] |
| 버전 | [placeholder: 버전 (예: 1.0.0)] |
| 작성일 | [placeholder: YYYY-MM-DD] |
| 작성자 | [placeholder: 작성자명 / 소속] |

---

## 변경 이력

| 버전 | 날짜 | 변경 내용 | 작성자 |
|------|------|-----------|--------|
| 0.1 | [placeholder] | 초안 작성 | [placeholder] |
| [placeholder] | [placeholder] | [placeholder] | [placeholder] |

---

## 1. 목적

요구사항 추적 매트릭스(RTM)는 소프트웨어 개발 전 과정에서 각 요구사항이 설계, 구현, 테스트 단계에 올바르게 반영되었는지를 추적하기 위한 문서이다.

본 문서의 목적은 다음과 같다:

- **완전성 보장**: 모든 요구사항이 설계, 구현, 테스트에 빠짐없이 반영되었는지 확인한다.
- **일관성 유지**: 요구사항 변경 시 영향 받는 설계, 코드, 테스트를 신속히 파악한다.
- **진행률 관리**: 요구사항별 구현 및 테스트 진행 상태를 한눈에 파악한다.
- **품질 확인**: 테스트 커버리지를 통해 품질 수준을 정량적으로 측정한다.
- **변경 영향 분석**: 요구사항 변경 시 영향 범위를 파악하여 리스크를 관리한다.

---

## 2. 추적 범위

본 RTM에서 추적하는 항목과 단계는 다음과 같다:

```
요구사항 (SRS)  →  유스케이스 (UCS)  →  설계 문서  →  구현 (코드)  →  테스트케이스
   FR-ID            UC-ID           DD-ID       Module/Class      TC-ID
   NFR-ID
```

| 추적 대상 | 문서/산출물 | ID 체계 |
|-----------|------------|---------|
| 기능 요구사항 | 요구사항 명세서 (SRS) | FR-XXX |
| 비기능 요구사항 | 요구사항 명세서 (SRS) | NFR-XXX |
| 유스케이스 | 유스케이스 명세서 (UCS) | UC-XXX |
| 설계 문서 | 상세 설계서 | DD-XXX |
| 구현 모듈 | 소스 코드 | 모듈명/클래스명 |
| 테스트케이스 | 테스트 명세서 | TC-XXX |

---

## 3. 상태 정의

매트릭스에서 사용하는 상태 값의 정의는 다음과 같다:

### 3.1 요구사항 상태

| 상태 | 설명 |
|------|------|
| 초안 (Draft) | 최초 작성 상태, 검토 필요 |
| 승인 (Approved) | 이해관계자 검토 및 승인 완료 |
| 변경중 (Changing) | 승인 후 변경 요청 발생 |
| 보류 (On Hold) | 일시적으로 구현 보류 |
| 삭제 (Deleted) | 요구사항에서 제외됨 |

### 3.2 매핑 상태

| 상태 | 설명 |
|------|------|
| 미착수 (Not Started) | 해당 단계 작업이 시작되지 않음 |
| 진행중 (In Progress) | 해당 단계 작업이 진행 중 |
| 완료 (Completed) | 해당 단계 작업이 완료됨 |
| N/A | 해당 단계가 적용되지 않음 |

---

## 4. 기능 요구사항 추적 매트릭스

| 요구사항 ID | 요구사항명 | 우선순위 | 유스케이스 | 설계 문서 참조 | 구현 참조 (모듈/클래스) | 테스트케이스 ID | 요구사항 상태 | 설계 상태 | 구현 상태 | 테스트 상태 | 비고 |
|------------|-----------|----------|-----------|---------------|----------------------|---------------|-------------|-----------|-----------|-----------|------|
| FR-001 | 회원가입 | P1 | UC-001 | DD-001, DD-002 | auth/SignupService, auth/EmailVerification | TC-001-01 ~ TC-001-06, TC-SEC-001 | 승인 | 완료 | 진행중 | 미착수 | 이메일 인증 포함 |
| FR-002 | 로그인/로그아웃 | P1 | UC-002 | DD-001, DD-003 | auth/LoginService, auth/TokenService | TC-002-01 ~ TC-002-10, TC-SEC-003 | 승인 | 완료 | 진행중 | 미착수 | 소셜 로그인 포함 |
| FR-003 | 프로필 관리 | P2 | UC-003, UC-004, UC-005 | DD-004 | user/ProfileService, user/UserController | TC-003-01 ~ TC-003-05 | 승인 | 진행중 | 미착수 | 미착수 | |
| FR-004 | 역할/권한 관리 | P1 | UC-012, UC-013 | DD-005 | auth/RoleService, auth/PermissionGuard | TC-004-01 ~ TC-004-08, TC-AUTH-001 ~ TC-AUTH-005 | 승인 | 진행중 | 미착수 | 미착수 | RBAC |
| FR-005 | 게시글 관리 | P1 | UC-006 ~ UC-009 | DD-006, DD-007 | post/PostService, post/PostController, storage/FileService | TC-006-01 ~ TC-006-15 | 승인 | 완료 | 미착수 | 미착수 | CRUD + 파일 첨부 |
| FR-006 | 통합 검색 | P2 | UC-010 | DD-008 | search/SearchService, search/SearchIndex | TC-010-01 ~ TC-010-06 | 승인 | 미착수 | 미착수 | 미착수 | |
| FR-007 | 알림 | P2 | UC-011 | DD-009, DD-010 | notification/NotificationService, notification/EmailSender | TC-011-01 ~ TC-011-08 | 초안 | 미착수 | 미착수 | 미착수 | In-App + Email + Push |
| [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] |

---

## 5. 비기능 요구사항 추적 매트릭스

| 요구사항 ID | 요구사항명 | 분류 | 우선순위 | 설계 문서 참조 | 구현 참조 (모듈/설정) | 테스트케이스 ID | 요구사항 상태 | 구현 상태 | 테스트 상태 | 비고 |
|------------|-----------|------|----------|---------------|---------------------|---------------|-------------|-----------|-----------|------|
| NFR-001 | API 응답시간 | 성능 | P1 | DD-PERF-001 | infra/LoadBalancer, cache/CacheConfig | TC-PERF-001 ~ TC-PERF-003 | 승인 | 미착수 | 미착수 | 부하 테스트 필요 |
| NFR-002 | 동시 사용자 | 성능 | P1 | DD-PERF-001 | infra/AutoScaling | TC-PERF-004 ~ TC-PERF-005 | 승인 | 미착수 | 미착수 | |
| NFR-003 | 처리량 | 성능 | P1 | DD-PERF-001 | infra/QueueConfig | TC-PERF-006 | 승인 | 미착수 | 미착수 | |
| NFR-004 | 인증/인가 | 보안 | P1 | DD-SEC-001 | auth/JwtService, auth/RbacGuard | TC-SEC-001 ~ TC-SEC-010 | 승인 | 진행중 | 미착수 | |
| NFR-005 | 데이터 암호화 | 보안 | P1 | DD-SEC-002 | infra/TlsConfig, crypto/EncryptionService | TC-SEC-011 ~ TC-SEC-015 | 승인 | 미착수 | 미착수 | TLS + AES-256 |
| NFR-006 | 감사 로깅 | 보안 | P1 | DD-SEC-003 | logging/AuditLogger, logging/AuditInterceptor | TC-LOG-001 ~ TC-LOG-005 | 승인 | 미착수 | 미착수 | |
| NFR-007 | 업타임 목표 | 가용성 | P1 | DD-INFRA-001 | infra/HealthCheck, infra/MonitoringConfig | TC-HA-001 ~ TC-HA-003 | 승인 | 미착수 | 미착수 | 99.9% 목표 |
| NFR-008 | 장애 복구 | 가용성 | P1 | DD-INFRA-002 | infra/BackupConfig, infra/FailoverConfig | TC-HA-004 ~ TC-HA-006 | 승인 | 미착수 | 미착수 | RTO/RPO |
| NFR-009 | 확장 전략 | 확장성 | P2 | DD-INFRA-003 | infra/ScalingPolicy | TC-SCALE-001 ~ TC-SCALE-003 | 초안 | 미착수 | 미착수 | |
| NFR-010 | 브라우저 호환 | 호환성 | P1 | DD-UI-001 | frontend/BrowserPolyfills | TC-COMPAT-001 ~ TC-COMPAT-010 | 승인 | 미착수 | 미착수 | |
| NFR-011 | 코드 품질 | 유지보수성 | P2 | DD-DEV-001 | ci/QualityGate, ci/LintConfig | TC-QUAL-001 ~ TC-QUAL-003 | 초안 | 진행중 | 미착수 | |
| [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] |

---

## 6. 커버리지 요약

### 6.1 기능 요구사항 커버리지

| 지표 | 수치 | 비율 | 목표 |
|------|------|------|------|
| 총 기능 요구사항 수 | [placeholder: e.g., 7] | - | - |
| 승인된 요구사항 | [placeholder: e.g., 6] | [placeholder: e.g., 85.7%] | 100% |
| 유스케이스 매핑 완료 | [placeholder: e.g., 7] | [placeholder: e.g., 100%] | 100% |
| 설계 매핑 완료 | [placeholder: e.g., 4] | [placeholder: e.g., 57.1%] | 100% |
| 구현 완료 | [placeholder: e.g., 0] | [placeholder: e.g., 0%] | 100% |
| 테스트 매핑 완료 | [placeholder: e.g., 7] | [placeholder: e.g., 100%] | 100% |
| 테스트 실행 완료 | [placeholder: e.g., 0] | [placeholder: e.g., 0%] | 100% |

### 6.2 비기능 요구사항 커버리지

| 지표 | 수치 | 비율 | 목표 |
|------|------|------|------|
| 총 비기능 요구사항 수 | [placeholder: e.g., 11] | - | - |
| 승인된 요구사항 | [placeholder: e.g., 9] | [placeholder: e.g., 81.8%] | 100% |
| 설계 매핑 완료 | [placeholder: e.g., 3] | [placeholder: e.g., 27.3%] | 100% |
| 구현 완료 | [placeholder: e.g., 1] | [placeholder: e.g., 9.1%] | 100% |
| 테스트 매핑 완료 | [placeholder: e.g., 11] | [placeholder: e.g., 100%] | 100% |
| 테스트 실행 완료 | [placeholder: e.g., 0] | [placeholder: e.g., 0%] | 100% |

### 6.3 우선순위별 커버리지

| 우선순위 | 총 요구사항 | 설계 완료 | 구현 완료 | 테스트 완료 |
|----------|-----------|-----------|-----------|-----------|
| P1 필수 | [placeholder: e.g., 12] | [placeholder: e.g., 5 (41.7%)] | [placeholder: e.g., 0 (0%)] | [placeholder: e.g., 0 (0%)] |
| P2 권장 | [placeholder: e.g., 5] | [placeholder: e.g., 1 (20.0%)] | [placeholder: e.g., 0 (0%)] | [placeholder: e.g., 0 (0%)] |
| P3 선택 | [placeholder: e.g., 1] | [placeholder: e.g., 0 (0%)] | [placeholder: e.g., 0 (0%)] | [placeholder: e.g., 0 (0%)] |

### 6.4 전체 진행률 차트

```
설계 매핑률:  [=========>                    ] [placeholder]%
구현 매핑률:  [====>                         ] [placeholder]%
테스트 매핑률: [==========================>   ] [placeholder]%
테스트 통과률: [>                             ] [placeholder]%
```

---

## 7. 미매핑 항목 관리

### 7.1 미매핑 항목 목록

| 요구사항 ID | 요구사항명 | 미매핑 단계 | 사유 | 담당자 | 목표 해결일 |
|------------|-----------|-----------|------|--------|-----------|
| [placeholder] | [placeholder] | [placeholder: 설계 / 구현 / 테스트] | [placeholder] | [placeholder] | [placeholder] |

### 7.2 미매핑 항목 관리 규칙

1. **주간 점검**: 매주 프로젝트 회의에서 미매핑 항목을 검토하고, 해결 계획을 수립한다.
2. **자동 알림**: 미매핑 항목이 목표 해결일을 초과한 경우, 프로젝트 관리자에게 자동 알림을 발송한다.
3. **에스컬레이션**: 2주 이상 미해결 상태인 미매핑 항목은 프로젝트 관리자에게 에스컬레이션한다.
4. **P1 요구사항 우선**: P1(필수) 요구사항의 미매핑 항목은 최우선으로 해결한다.
5. **변경 연동**: 요구사항 변경(추가/수정/삭제) 시 RTM을 동시에 갱신하며, 영향 받는 설계/구현/테스트를 식별한다.
6. **품질 게이트**: 설계 완료율 100%, 구현 완료율 100%, 테스트 매핑률 100%가 되어야 해당 단계를 통과할 수 있다.

### 7.3 매핑률 목표 기준

| 단계 전환 | 설계 매핑률 | 구현 매핑률 | 테스트 매핑률 |
|-----------|-----------|-----------|-------------|
| 요구사항 → 설계 단계 진입 | 100% (P1) | - | - |
| 설계 → 구현 단계 진입 | 100% | - | 100% (TC ID 부여) |
| 구현 → 테스트 단계 진입 | 100% | 100% (P1) | 100% |
| 테스트 → 배포 승인 | 100% | 100% | 100% (통과) |

---

## 8. RTM 갱신 절차

### 8.1 갱신 주기

| 이벤트 | 갱신 항목 | 담당자 |
|--------|----------|--------|
| 요구사항 추가/변경/삭제 | 요구사항 ID, 상태 열 갱신 | PM / BA |
| 유스케이스 작성/변경 | UC 매핑 열 갱신 | BA |
| 설계 문서 작성/변경 | 설계 문서 참조 열 갱신 | 설계자 |
| 코드 구현 완료 | 구현 참조 열, 구현 상태 갱신 | 개발자 |
| 테스트케이스 작성 | 테스트케이스 ID 열 갱신 | QA |
| 테스트 실행 완료 | 테스트 상태 갱신 | QA |
| 정기 점검 (주간) | 전체 커버리지 요약 갱신 | PM |

### 8.2 변경 영향 분석 체크리스트

요구사항 변경 시 다음 항목을 점검한다:

- [ ] 변경된 요구사항의 RTM 상태 업데이트
- [ ] 관련 유스케이스 영향 확인 및 갱신 여부 판단
- [ ] 관련 설계 문서 영향 확인 및 갱신 여부 판단
- [ ] 관련 구현 모듈 영향 확인 및 수정 범위 산정
- [ ] 관련 테스트케이스 영향 확인 및 추가/수정 여부 판단
- [ ] 연관 요구사항(의존성)에 대한 파급 효과 확인
- [ ] 커버리지 요약 재계산

---

## 부록: RTM ID 체계

| 산출물 | ID 형식 | 예시 | 설명 |
|--------|---------|------|------|
| 기능 요구사항 | FR-XXX | FR-001 | 기능 요구사항 순번 |
| 비기능 요구사항 | NFR-XXX | NFR-001 | 비기능 요구사항 순번 |
| 유스케이스 | UC-XXX | UC-001 | 유스케이스 순번 |
| 설계 문서 | DD-XXX | DD-001 | 상세 설계 문서 순번 |
| 설계 문서 (분류별) | DD-{분류}-XXX | DD-SEC-001 | 분류: SEC(보안), PERF(성능), INFRA(인프라), UI, DEV |
| 테스트케이스 | TC-XXX-YY | TC-001-01 | 관련 FR/UC 번호-순번 |
| 테스트케이스 (분류별) | TC-{분류}-XXX | TC-SEC-001 | 분류: SEC, PERF, HA, SCALE, COMPAT, QUAL, AUTH, LOG |

---

> **본 문서는 프로젝트 전 생명주기에 걸쳐 유지되며, 요구사항 또는 산출물 변경 시 반드시 동시에 갱신한다.**
