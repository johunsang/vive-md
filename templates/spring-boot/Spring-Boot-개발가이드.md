# CLAUDE.md - Spring Boot 프로젝트 가이드

## 1. 프로젝트 개요

### 기술 스택

| 구분 | 기술 | 버전 |
|------|------|------|
| Framework | Spring Boot | 3.3.x |
| Language | Java | 17+ (LTS) |
| Build Tool | Gradle | 8.x (Kotlin DSL) |
| ORM | Spring Data JPA + Hibernate | 6.x |
| Database | PostgreSQL (운영), H2 (테스트) | 16.x / 2.x |
| Security | Spring Security | 6.x |
| Validation | Jakarta Bean Validation | 3.x |
| Cache | Spring Cache + Redis | 7.x |
| API 문서 | SpringDoc OpenAPI (Swagger) | 2.x |
| 테스트 | JUnit 5 + Mockito + TestContainers | 5.x / 5.x / 1.x |
| 모니터링 | Actuator + Micrometer | - |

### 프로젝트 구조 상세 트리

```
project-root/
├── build.gradle.kts                    # 루트 빌드 스크립트
├── settings.gradle.kts                 # 멀티 모듈 설정
├── gradle/
│   └── libs.versions.toml              # 버전 카탈로그
├── docker/
│   ├── Dockerfile                      # 프로덕션 이미지
│   ├── Dockerfile.dev                  # 개발 이미지
│   └── docker-compose.yml              # 로컬 인프라 (DB, Redis, Kafka)
├── docs/
│   └── api/                            # API 문서
├── scripts/
│   ├── init-db.sql                     # DB 초기화 스크립트
│   └── deploy.sh                       # 배포 스크립트
├── src/
│   ├── main/
│   │   ├── java/com/example/app/
│   │   │   ├── AppApplication.java     # 메인 클래스
│   │   │   ├── domain/                 # 도메인 패키지
│   │   │   ├── global/                 # 전역 공통 모듈
│   │   │   └── infra/                  # 외부 인프라 연동
│   │   └── resources/
│   │       ├── application.yml         # 기본 설정
│   │       ├── application-local.yml   # 로컬 환경
│   │       ├── application-dev.yml     # 개발 환경
│   │       ├── application-staging.yml # 스테이징 환경
│   │       ├── application-prod.yml    # 운영 환경
│   │       ├── logback-spring.xml      # 로깅 설정
│   │       └── messages/
│   │           ├── errors.properties           # 에러 메시지
│   │           └── errors_ko.properties        # 한국어 에러 메시지
│   └── test/
│       ├── java/com/example/app/
│       │   ├── domain/                 # 도메인별 테스트
│       │   ├── global/                 # 공통 모듈 테스트
│       │   ├── integration/            # 통합 테스트
│       │   └── support/                # 테스트 지원 클래스
│       └── resources/
│           ├── application-test.yml    # 테스트 설정
│           └── data/                   # 테스트 데이터 (SQL, JSON)
└── CLAUDE.md
```

### 멀티 모듈 구성 예시

```
project-root/
├── settings.gradle.kts
├── build.gradle.kts
├── module-core/                # 도메인 엔티티, 공통 유틸
│   └── build.gradle.kts
├── module-api/                 # REST API 서버
│   └── build.gradle.kts
├── module-admin/               # 관리자 API
│   └── build.gradle.kts
├── module-batch/               # 배치 처리
│   └── build.gradle.kts
└── module-infra/               # 외부 인프라 연동
    └── build.gradle.kts
```

**settings.gradle.kts (멀티 모듈)**:
```kotlin
rootProject.name = "my-project"

include(
    "module-core",
    "module-api",
    "module-admin",
    "module-batch",
    "module-infra"
)
```

### build.gradle.kts 핵심 설정

```kotlin
plugins {
    java
    id("org.springframework.boot") version "3.3.5"
    id("io.spring.dependency-management") version "1.1.6"
}

group = "com.example"
version = "0.0.1-SNAPSHOT"

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}

repositories {
    mavenCentral()
}

dependencies {
    // Spring Boot Starters
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springframework.boot:spring-boot-starter-data-jpa")
    implementation("org.springframework.boot:spring-boot-starter-security")
    implementation("org.springframework.boot:spring-boot-starter-validation")
    implementation("org.springframework.boot:spring-boot-starter-cache")
    implementation("org.springframework.boot:spring-boot-starter-data-redis")
    implementation("org.springframework.boot:spring-boot-starter-actuator")

    // Database
    runtimeOnly("org.postgresql:postgresql")
    runtimeOnly("com.h2database:h2")

    // API Documentation
    implementation("org.springdoc:springdoc-openapi-starter-webmvc-ui:2.6.0")

    // JWT
    implementation("io.jsonwebtoken:jjwt-api:0.12.6")
    runtimeOnly("io.jsonwebtoken:jjwt-impl:0.12.6")
    runtimeOnly("io.jsonwebtoken:jjwt-jackson:0.12.6")

    // QueryDSL
    implementation("com.querydsl:querydsl-jpa:5.1.0:jakarta")
    annotationProcessor("com.querydsl:querydsl-apt:5.1.0:jakarta")
    annotationProcessor("jakarta.annotation:jakarta.annotation-api")
    annotationProcessor("jakarta.persistence:jakarta.persistence-api")

    // MapStruct
    implementation("org.mapstruct:mapstruct:1.6.3")
    annotationProcessor("org.mapstruct:mapstruct-processor:1.6.3")

    // Lombok
    compileOnly("org.projectlombok:lombok")
    annotationProcessor("org.projectlombok:lombok")
    annotationProcessor("org.projectlombok:lombok-mapstruct-binding:0.2.0")

    // Test
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.springframework.security:spring-security-test")
    testImplementation("org.testcontainers:junit-jupiter")
    testImplementation("org.testcontainers:postgresql")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

tasks.withType<Test> {
    useJUnitPlatform()
}
```

### 프로파일 전략

| 프로파일 | 용도 | DB | 로그 레벨 | 특이사항 |
|----------|------|-----|-----------|----------|
| `local` | 로컬 개발 | H2 / Docker PostgreSQL | DEBUG | ddl-auto: create-drop |
| `dev` | 개발 서버 | PostgreSQL (개발용) | DEBUG | ddl-auto: update |
| `staging` | 스테이징 | PostgreSQL (스테이징) | INFO | ddl-auto: validate |
| `prod` | 운영 | PostgreSQL (운영) | WARN | ddl-auto: none, Flyway 사용 |

---

## 2. 코딩 컨벤션

### 네이밍 규칙

#### 클래스 네이밍

| 레이어 | 패턴 | 예시 |
|--------|------|------|
| Entity | 단수 명사 | `User`, `Order`, `Product` |
| Repository | `{Entity}Repository` | `UserRepository`, `OrderRepository` |
| Service (인터페이스) | `{Entity}Service` | `UserService` |
| Service (구현체) | `{Entity}ServiceImpl` | `UserServiceImpl` (단일 구현이면 생략) |
| Controller | `{Entity}Controller` | `UserController` |
| Request DTO | `{Action}{Entity}Request` | `CreateUserRequest`, `UpdateOrderRequest` |
| Response DTO | `{Entity}{Detail}Response` | `UserResponse`, `UserDetailResponse` |
| Exception | `{도메인}{상황}Exception` | `UserNotFoundException`, `DuplicateEmailException` |
| Enum | 단수 명사 또는 형용사 | `UserStatus`, `OrderType`, `PaymentMethod` |
| Config | `{기능}Config` | `SecurityConfig`, `RedisConfig`, `JpaConfig` |
| Mapper | `{Entity}Mapper` | `UserMapper`, `OrderMapper` |
| Validator | `{규칙}Validator` | `PasswordValidator`, `PhoneNumberValidator` |
| Event | `{Entity}{Action}Event` | `UserCreatedEvent`, `OrderCompletedEvent` |
| Listener | `{Event}Listener` | `UserCreatedEventListener` |

#### 메서드 네이밍

```java
// Controller 메서드: HTTP 메서드 + 자원 표현
@GetMapping       -> getUser(), getUsers(), getUserOrders()
@PostMapping      -> createUser(), registerUser()
@PutMapping       -> updateUser(), modifyUserProfile()
@PatchMapping     -> updateUserStatus(), changePassword()
@DeleteMapping    -> deleteUser(), removeUser()

// Service 메서드: 비즈니스 의미 중심
findUserById()           // 단건 조회 (없으면 예외)
findUserByEmail()        // 조건 조회
getUsers()               // 목록 조회 (페이징 포함)
searchUsers()            // 검색
createUser()             // 생성
updateUser()             // 수정
deleteUser()             // 삭제 (soft delete 포함)
existsByEmail()          // 존재 여부 확인
validatePassword()       // 검증

// Repository 메서드: Spring Data JPA 쿼리 메서드 패턴
findByEmail()
findByStatusAndCreatedAtAfter()
findAllByOrderByCreatedAtDesc()
existsByEmail()
countByStatus()
deleteByIdAndUserId()

// Boolean 반환 메서드: is/has/can/should 접두사
isActive()
hasPermission()
canAccess()
shouldNotify()

// Private 헬퍼 메서드: 동사 + 목적어
validateDuplicateEmail()
buildUserResponse()
calculateTotalPrice()
sendNotification()
```

#### 변수 네이밍

```java
// 컬렉션: 복수형
List<User> users;
Set<String> permissions;
Map<Long, Order> orderMap;    // Map은 {key}{Value}Map 또는 {의미}Map

// Optional: 접두사 없이 의미 표현
Optional<User> user;          // optionalUser (X)

// Boolean: is/has/can/should 또는 형용사/과거분사
boolean active;               // isActive (getter에서 is 사용)
boolean deleted;
boolean emailVerified;

// 상수: 의미 단위로 UPPER_SNAKE_CASE
static final int MAX_RETRY_COUNT = 3;
static final long ACCESS_TOKEN_EXPIRY_MS = 3600000L;
static final String CACHE_KEY_PREFIX = "user:";
static final String BEARER_PREFIX = "Bearer ";
```

#### REST 엔드포인트 네이밍

```java
// 기본 CRUD
GET    /api/v1/users              // 목록 조회
GET    /api/v1/users/{id}         // 단건 조회
POST   /api/v1/users              // 생성
PUT    /api/v1/users/{id}         // 전체 수정
PATCH  /api/v1/users/{id}         // 부분 수정
DELETE /api/v1/users/{id}         // 삭제

// 중첩 리소스
GET    /api/v1/users/{userId}/orders           // 특정 사용자의 주문 목록
POST   /api/v1/users/{userId}/orders           // 특정 사용자의 주문 생성
GET    /api/v1/users/{userId}/orders/{orderId} // 특정 주문 조회

// 검색/필터
GET    /api/v1/users?status=ACTIVE&page=0&size=20&sort=createdAt,desc

// 특수 행위 (RPC 스타일이 불가피한 경우)
POST   /api/v1/users/{id}/activate
POST   /api/v1/users/{id}/deactivate
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh
POST   /api/v1/orders/{id}/cancel
```

#### DB 테이블/컬럼 네이밍

```sql
-- 테이블: snake_case, 복수형
users, orders, order_items, user_roles

-- 컬럼: snake_case
id, user_id, email, created_at, updated_at, is_deleted

-- 인덱스: idx_{테이블}_{컬럼}
idx_users_email, idx_orders_user_id_status

-- 외래 키: fk_{테이블}_{참조테이블}
fk_orders_users, fk_order_items_orders

-- 유니크 제약: uk_{테이블}_{컬럼}
uk_users_email
```

### 디렉토리 구조 상세

```
src/main/java/com/example/app/
├── AppApplication.java                     # @SpringBootApplication 메인 클래스
│
├── domain/
│   ├── user/                               # [도메인: 사용자]
│   │   ├── controller/
│   │   │   ├── UserController.java         # 일반 사용자 API 엔드포인트
│   │   │   └── AdminUserController.java    # 관리자용 사용자 API
│   │   ├── service/
│   │   │   ├── UserService.java            # 사용자 비즈니스 로직
│   │   │   └── UserQueryService.java       # 읽기 전용 조회 로직 (CQRS 분리 시)
│   │   ├── repository/
│   │   │   ├── UserRepository.java         # JPA Repository 인터페이스
│   │   │   ├── UserRepositoryCustom.java   # 커스텀 쿼리 인터페이스
│   │   │   └── UserRepositoryImpl.java     # QueryDSL 구현체
│   │   ├── entity/
│   │   │   ├── User.java                   # JPA Entity
│   │   │   ├── UserRole.java               # 역할 Entity 또는 Enum
│   │   │   └── UserStatus.java             # 상태 Enum
│   │   ├── dto/
│   │   │   ├── request/
│   │   │   │   ├── CreateUserRequest.java  # 생성 요청 DTO
│   │   │   │   ├── UpdateUserRequest.java  # 수정 요청 DTO
│   │   │   │   └── UserSearchCondition.java # 검색 조건 DTO
│   │   │   └── response/
│   │   │       ├── UserResponse.java       # 목록용 간략 응답
│   │   │       └── UserDetailResponse.java # 상세 응답
│   │   ├── mapper/
│   │   │   └── UserMapper.java             # MapStruct 매퍼 인터페이스
│   │   ├── event/
│   │   │   ├── UserCreatedEvent.java       # 사용자 생성 이벤트
│   │   │   └── UserCreatedEventListener.java
│   │   └── exception/
│   │       ├── UserNotFoundException.java
│   │       └── DuplicateEmailException.java
│   │
│   ├── order/                              # [도메인: 주문]
│   │   ├── controller/
│   │   ├── service/
│   │   ├── repository/
│   │   ├── entity/
│   │   ├── dto/
│   │   └── exception/
│   │
│   └── payment/                            # [도메인: 결제]
│       ├── controller/
│       ├── service/
│       ├── repository/
│       ├── entity/
│       ├── dto/
│       └── exception/
│
├── global/                                 # [전역 공통]
│   ├── config/
│   │   ├── SecurityConfig.java             # Spring Security 설정
│   │   ├── JpaConfig.java                  # JPA Auditing 등 설정
│   │   ├── RedisConfig.java                # Redis 직렬화/커넥션 설정
│   │   ├── CacheConfig.java                # 캐시 매니저 설정
│   │   ├── AsyncConfig.java                # 비동기 처리 ThreadPool 설정
│   │   ├── WebConfig.java                  # CORS, Interceptor, Converter 설정
│   │   ├── SwaggerConfig.java              # SpringDoc OpenAPI 설정
│   │   └── QuerydslConfig.java             # JPAQueryFactory Bean 설정
│   ├── exception/
│   │   ├── BusinessException.java          # 비즈니스 예외 최상위 클래스
│   │   ├── ErrorCode.java                  # 에러 코드 Enum
│   │   ├── ErrorResponse.java              # 에러 응답 DTO
│   │   └── GlobalExceptionHandler.java     # @RestControllerAdvice 전역 예외 처리
│   ├── security/
│   │   ├── jwt/
│   │   │   ├── JwtTokenProvider.java       # JWT 토큰 생성/검증
│   │   │   ├── JwtAuthenticationFilter.java # JWT 인증 필터
│   │   │   └── JwtProperties.java          # JWT 관련 설정 프로퍼티
│   │   ├── CustomUserDetails.java          # UserDetails 구현체
│   │   ├── CustomUserDetailsService.java   # UserDetailsService 구현체
│   │   └── SecurityUtil.java               # SecurityContext 유틸 (현재 사용자 추출)
│   ├── common/
│   │   ├── dto/
│   │   │   ├── ApiResponse.java            # 공통 API 응답 래퍼
│   │   │   └── PageResponse.java           # 페이지네이션 응답 래퍼
│   │   ├── entity/
│   │   │   └── BaseEntity.java             # Auditing 기반 엔티티
│   │   └── util/
│   │       └── DateTimeUtil.java           # 날짜/시간 유틸
│   └── aop/
│       ├── LoggingAspect.java              # 메서드 실행 로깅 AOP
│       └── PerformanceAspect.java          # 성능 측정 AOP
│
└── infra/                                  # [외부 인프라 연동]
    ├── redis/
    │   └── RedisService.java               # Redis 직접 접근 서비스
    ├── s3/
    │   ├── S3Config.java                   # AWS S3 설정
    │   └── S3FileService.java              # S3 파일 업로드/다운로드
    ├── mail/
    │   └── MailService.java                # 이메일 발송 서비스
    └── external/
        └── PaymentGatewayClient.java       # 외부 결제 API 클라이언트
```

### import 순서와 정리 규칙

```java
// 1. java 표준 라이브러리
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

// 2. jakarta 패키지 (Spring Boot 3.x)
import jakarta.persistence.Entity;
import jakarta.validation.constraints.NotBlank;

// 3. Spring Framework
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

// 4. 서드파티 라이브러리
import com.querydsl.jpa.impl.JPAQueryFactory;
import io.jsonwebtoken.Claims;
import lombok.RequiredArgsConstructor;

// 5. 프로젝트 내부 패키지
import com.example.app.domain.user.entity.User;
import com.example.app.global.exception.BusinessException;
```

**규칙**:
- 와일드카드 import (`import java.util.*`) 절대 금지
- 사용하지 않는 import 제거 (IDE 자동 정리 활용)
- static import는 일반 import 아래에 분리하여 배치
- 각 그룹 사이에 빈 줄 1개

### 에러 핸들링 패턴

#### ErrorCode Enum

```java
@Getter
@RequiredArgsConstructor
public enum ErrorCode {

    // Common (C)
    INVALID_INPUT_VALUE(HttpStatus.BAD_REQUEST, "C001", "잘못된 입력값입니다."),
    METHOD_NOT_ALLOWED(HttpStatus.METHOD_NOT_ALLOWED, "C002", "허용되지 않은 HTTP 메서드입니다."),
    INTERNAL_SERVER_ERROR(HttpStatus.INTERNAL_SERVER_ERROR, "C003", "서버 내부 오류가 발생했습니다."),
    INVALID_TYPE_VALUE(HttpStatus.BAD_REQUEST, "C004", "잘못된 타입의 값입니다."),
    ACCESS_DENIED(HttpStatus.FORBIDDEN, "C005", "접근 권한이 없습니다."),
    RESOURCE_NOT_FOUND(HttpStatus.NOT_FOUND, "C006", "리소스를 찾을 수 없습니다."),

    // Auth (A)
    AUTHENTICATION_FAILED(HttpStatus.UNAUTHORIZED, "A001", "인증에 실패했습니다."),
    TOKEN_EXPIRED(HttpStatus.UNAUTHORIZED, "A002", "토큰이 만료되었습니다."),
    TOKEN_INVALID(HttpStatus.UNAUTHORIZED, "A003", "유효하지 않은 토큰입니다."),
    REFRESH_TOKEN_NOT_FOUND(HttpStatus.UNAUTHORIZED, "A004", "리프레시 토큰을 찾을 수 없습니다."),

    // User (U)
    USER_NOT_FOUND(HttpStatus.NOT_FOUND, "U001", "사용자를 찾을 수 없습니다."),
    DUPLICATE_EMAIL(HttpStatus.CONFLICT, "U002", "이미 존재하는 이메일입니다."),
    INVALID_PASSWORD(HttpStatus.BAD_REQUEST, "U003", "비밀번호가 올바르지 않습니다."),
    USER_DISABLED(HttpStatus.FORBIDDEN, "U004", "비활성화된 사용자입니다."),

    // Order (O)
    ORDER_NOT_FOUND(HttpStatus.NOT_FOUND, "O001", "주문을 찾을 수 없습니다."),
    ORDER_ALREADY_CANCELLED(HttpStatus.BAD_REQUEST, "O002", "이미 취소된 주문입니다."),
    INSUFFICIENT_STOCK(HttpStatus.BAD_REQUEST, "O003", "재고가 부족합니다.");

    private final HttpStatus httpStatus;
    private final String code;
    private final String message;
}
```

#### BusinessException 계층 구조

```java
@Getter
public class BusinessException extends RuntimeException {

    private final ErrorCode errorCode;

    public BusinessException(ErrorCode errorCode) {
        super(errorCode.getMessage());
        this.errorCode = errorCode;
    }

    public BusinessException(ErrorCode errorCode, String detailMessage) {
        super(detailMessage);
        this.errorCode = errorCode;
    }
}

// 도메인별 예외
public class EntityNotFoundException extends BusinessException {
    public EntityNotFoundException(ErrorCode errorCode) {
        super(errorCode);
    }
}

public class DuplicateResourceException extends BusinessException {
    public DuplicateResourceException(ErrorCode errorCode) {
        super(errorCode);
    }
}

public class InvalidValueException extends BusinessException {
    public InvalidValueException(ErrorCode errorCode) {
        super(errorCode);
    }
}

// 사용 예시
public class UserNotFoundException extends EntityNotFoundException {
    public UserNotFoundException() {
        super(ErrorCode.USER_NOT_FOUND);
    }
}

public class DuplicateEmailException extends DuplicateResourceException {
    public DuplicateEmailException() {
        super(ErrorCode.DUPLICATE_EMAIL);
    }
}
```

#### ErrorResponse DTO

```java
@Getter
public class ErrorResponse {

    private final String code;
    private final String message;
    private final List<FieldError> errors;
    private final LocalDateTime timestamp;

    private ErrorResponse(String code, String message, List<FieldError> errors) {
        this.code = code;
        this.message = message;
        this.errors = errors;
        this.timestamp = LocalDateTime.now();
    }

    public static ErrorResponse of(ErrorCode errorCode) {
        return new ErrorResponse(errorCode.getCode(), errorCode.getMessage(), List.of());
    }

    public static ErrorResponse of(ErrorCode errorCode, List<FieldError> errors) {
        return new ErrorResponse(errorCode.getCode(), errorCode.getMessage(), errors);
    }

    public static ErrorResponse of(ErrorCode errorCode,
                                    BindingResult bindingResult) {
        List<FieldError> fieldErrors = bindingResult.getFieldErrors().stream()
                .map(error -> new FieldError(
                        error.getField(),
                        error.getRejectedValue() == null ? "" :
                                error.getRejectedValue().toString(),
                        error.getDefaultMessage()))
                .toList();
        return new ErrorResponse(errorCode.getCode(), errorCode.getMessage(), fieldErrors);
    }

    public record FieldError(String field, String value, String reason) {}
}
```

#### GlobalExceptionHandler

```java
@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    protected ResponseEntity<ErrorResponse> handleBusinessException(BusinessException e) {
        log.warn("BusinessException: {}", e.getMessage());
        ErrorCode errorCode = e.getErrorCode();
        return ResponseEntity
                .status(errorCode.getHttpStatus())
                .body(ErrorResponse.of(errorCode));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    protected ResponseEntity<ErrorResponse> handleMethodArgumentNotValid(
            MethodArgumentNotValidException e) {
        log.warn("Validation failed: {}", e.getMessage());
        return ResponseEntity
                .status(HttpStatus.BAD_REQUEST)
                .body(ErrorResponse.of(ErrorCode.INVALID_INPUT_VALUE,
                        e.getBindingResult()));
    }

    @ExceptionHandler(ConstraintViolationException.class)
    protected ResponseEntity<ErrorResponse> handleConstraintViolation(
            ConstraintViolationException e) {
        log.warn("Constraint violation: {}", e.getMessage());
        return ResponseEntity
                .status(HttpStatus.BAD_REQUEST)
                .body(ErrorResponse.of(ErrorCode.INVALID_INPUT_VALUE));
    }

    @ExceptionHandler(HttpRequestMethodNotSupportedException.class)
    protected ResponseEntity<ErrorResponse> handleHttpRequestMethodNotSupported(
            HttpRequestMethodNotSupportedException e) {
        return ResponseEntity
                .status(HttpStatus.METHOD_NOT_ALLOWED)
                .body(ErrorResponse.of(ErrorCode.METHOD_NOT_ALLOWED));
    }

    @ExceptionHandler(AccessDeniedException.class)
    protected ResponseEntity<ErrorResponse> handleAccessDeniedException(
            AccessDeniedException e) {
        return ResponseEntity
                .status(HttpStatus.FORBIDDEN)
                .body(ErrorResponse.of(ErrorCode.ACCESS_DENIED));
    }

    @ExceptionHandler(Exception.class)
    protected ResponseEntity<ErrorResponse> handleException(Exception e) {
        log.error("Unhandled exception: ", e);
        return ResponseEntity
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(ErrorResponse.of(ErrorCode.INTERNAL_SERVER_ERROR));
    }
}
```

### DTO 패턴

#### Record 기반 Request/Response

```java
// Request DTO - Bean Validation 적용
public record CreateUserRequest(
        @NotBlank(message = "이름은 필수입니다.")
        @Size(max = 50, message = "이름은 50자 이하여야 합니다.")
        String name,

        @NotBlank(message = "이메일은 필수입니다.")
        @Email(message = "올바른 이메일 형식이 아닙니다.")
        String email,

        @NotBlank(message = "비밀번호는 필수입니다.")
        @Size(min = 8, max = 100, message = "비밀번호는 8~100자여야 합니다.")
        @Pattern(regexp = "^(?=.*[a-zA-Z])(?=.*\\d)(?=.*[!@#$%^&*]).+$",
                 message = "비밀번호는 영문, 숫자, 특수문자를 포함해야 합니다.")
        String password,

        @Size(max = 20, message = "전화번호는 20자 이하여야 합니다.")
        String phoneNumber
) {}

// Response DTO
public record UserResponse(
        Long id,
        String name,
        String email,
        UserStatus status,
        LocalDateTime createdAt
) {
    public static UserResponse from(User user) {
        return new UserResponse(
                user.getId(),
                user.getName(),
                user.getEmail(),
                user.getStatus(),
                user.getCreatedAt()
        );
    }
}

// 상세 Response (필드가 많은 경우)
public record UserDetailResponse(
        Long id,
        String name,
        String email,
        String phoneNumber,
        UserStatus status,
        List<String> roles,
        LocalDateTime createdAt,
        LocalDateTime updatedAt
) {
    public static UserDetailResponse from(User user) {
        return new UserDetailResponse(
                user.getId(),
                user.getName(),
                user.getEmail(),
                user.getPhoneNumber(),
                user.getStatus(),
                user.getRoles().stream()
                        .map(UserRole::getName)
                        .toList(),
                user.getCreatedAt(),
                user.getUpdatedAt()
        );
    }
}
```

#### MapStruct 매퍼

```java
@Mapper(componentModel = "spring",
        unmappedTargetPolicy = ReportingPolicy.IGNORE)
public interface UserMapper {

    User toEntity(CreateUserRequest request);

    UserResponse toResponse(User user);

    UserDetailResponse toDetailResponse(User user);

    @BeanMapping(nullValuePropertyMappingStrategy =
            NullValuePropertyMappingStrategy.IGNORE)
    void updateFromDto(UpdateUserRequest request, @MappingTarget User user);
}
```

### Entity 설계

#### BaseEntity (Auditing)

```java
@Getter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class BaseEntity {

    @CreatedDate
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @LastModifiedDate
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @CreatedBy
    @Column(name = "created_by", updatable = false)
    private String createdBy;

    @LastModifiedBy
    @Column(name = "updated_by")
    private String updatedBy;
}
```

#### JpaConfig (Auditing 활성화)

```java
@Configuration
@EnableJpaAuditing
public class JpaConfig {

    @Bean
    public AuditorAware<String> auditorProvider() {
        return () -> Optional.ofNullable(SecurityContextHolder.getContext())
                .map(SecurityContext::getAuthentication)
                .filter(Authentication::isAuthenticated)
                .map(Authentication::getName)
                .or(() -> Optional.of("system"));
    }
}
```

#### Entity 작성 패턴

```java
@Entity
@Table(name = "users",
        uniqueConstraints = {
                @UniqueConstraint(name = "uk_users_email",
                        columnNames = "email")
        },
        indexes = {
                @Index(name = "idx_users_status", columnList = "status"),
                @Index(name = "idx_users_created_at", columnList = "created_at")
        })
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class User extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 50)
    private String name;

    @Column(nullable = false, unique = true, length = 100)
    private String email;

    @Column(nullable = false)
    private String password;

    @Column(length = 20)
    private String phoneNumber;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 20)
    private UserStatus status;

    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL,
               orphanRemoval = true)
    private List<UserRole> roles = new ArrayList<>();

    @Column(nullable = false)
    private boolean deleted;

    // -- 생성 팩토리 메서드 --
    public static User create(String name, String email,
                               String encodedPassword) {
        User user = new User();
        user.name = name;
        user.email = email;
        user.password = encodedPassword;
        user.status = UserStatus.ACTIVE;
        user.deleted = false;
        return user;
    }

    // -- 비즈니스 메서드 --
    public void updateProfile(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    public void changePassword(String encodedPassword) {
        this.password = encodedPassword;
    }

    public void deactivate() {
        this.status = UserStatus.INACTIVE;
    }

    public void softDelete() {
        this.deleted = true;
        this.status = UserStatus.DELETED;
    }

    public void addRole(UserRole role) {
        this.roles.add(role);
        role.setUser(this);
    }
}
```

**Entity 규칙**:
- `@Setter` 사용 금지 - 비즈니스 메서드로 상태 변경
- `@NoArgsConstructor(access = AccessLevel.PROTECTED)` - JPA 요구사항 충족하면서 외부 직접 생성 방지
- 정적 팩토리 메서드 `create()` 또는 `@Builder` 사용
- 연관관계 편의 메서드 제공
- `@Enumerated(EnumType.STRING)` - ordinal 사용 금지
- `@Column` 제약 조건 명시 (nullable, length)

### 서비스 레이어 패턴

```java
@Slf4j
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)   // 클래스 레벨: 읽기 전용 기본
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final ApplicationEventPublisher eventPublisher;

    // 단건 조회
    public UserDetailResponse findById(Long id) {
        User user = findUserOrThrow(id);
        return UserDetailResponse.from(user);
    }

    // 목록 조회 (페이징)
    public PageResponse<UserResponse> getUsers(Pageable pageable) {
        Page<User> page = userRepository.findAllByDeletedFalse(pageable);
        Page<UserResponse> responsePage = page.map(UserResponse::from);
        return PageResponse.from(responsePage);
    }

    // 검색 (QueryDSL)
    public PageResponse<UserResponse> searchUsers(
            UserSearchCondition condition, Pageable pageable) {
        Page<UserResponse> page =
                userRepository.search(condition, pageable);
        return PageResponse.from(page);
    }

    // 생성 (쓰기 트랜잭션)
    @Transactional
    public UserResponse createUser(CreateUserRequest request) {
        validateDuplicateEmail(request.email());

        User user = User.create(
                request.name(),
                request.email(),
                passwordEncoder.encode(request.password())
        );
        User savedUser = userRepository.save(user);

        eventPublisher.publishEvent(new UserCreatedEvent(savedUser.getId()));
        log.info("사용자 생성 완료: userId={}", savedUser.getId());

        return UserResponse.from(savedUser);
    }

    // 수정
    @Transactional
    public UserResponse updateUser(Long id, UpdateUserRequest request) {
        User user = findUserOrThrow(id);
        user.updateProfile(request.name(), request.phoneNumber());
        return UserResponse.from(user);   // 변경 감지로 자동 업데이트
    }

    // 삭제 (soft delete)
    @Transactional
    public void deleteUser(Long id) {
        User user = findUserOrThrow(id);
        user.softDelete();
        log.info("사용자 삭제 완료: userId={}", id);
    }

    // -- Private 헬퍼 메서드 --
    private User findUserOrThrow(Long id) {
        return userRepository.findByIdAndDeletedFalse(id)
                .orElseThrow(UserNotFoundException::new);
    }

    private void validateDuplicateEmail(String email) {
        if (userRepository.existsByEmail(email)) {
            throw new DuplicateEmailException();
        }
    }
}
```

### Repository 패턴

#### 기본 JPA Repository

```java
public interface UserRepository extends JpaRepository<User, Long>,
        UserRepositoryCustom {

    Optional<User> findByEmail(String email);

    Optional<User> findByIdAndDeletedFalse(Long id);

    Page<User> findAllByDeletedFalse(Pageable pageable);

    boolean existsByEmail(String email);

    @Query("SELECT u FROM User u JOIN FETCH u.roles WHERE u.id = :id")
    Optional<User> findWithRolesById(@Param("id") Long id);

    @Modifying(clearAutomatically = true)
    @Query("UPDATE User u SET u.status = :status WHERE u.id IN :ids")
    int bulkUpdateStatus(@Param("ids") List<Long> ids,
                         @Param("status") UserStatus status);
}
```

#### 커스텀 Repository (QueryDSL)

```java
// 커스텀 인터페이스
public interface UserRepositoryCustom {
    Page<UserResponse> search(UserSearchCondition condition,
                              Pageable pageable);
}

// QueryDSL 구현체
@RequiredArgsConstructor
public class UserRepositoryImpl implements UserRepositoryCustom {

    private final JPAQueryFactory queryFactory;

    @Override
    public Page<UserResponse> search(UserSearchCondition condition,
                                     Pageable pageable) {
        QUser user = QUser.user;

        List<UserResponse> content = queryFactory
                .select(Projections.constructor(UserResponse.class,
                        user.id,
                        user.name,
                        user.email,
                        user.status,
                        user.createdAt))
                .from(user)
                .where(
                        nameContains(condition.name()),
                        emailContains(condition.email()),
                        statusEq(condition.status()),
                        user.deleted.isFalse()
                )
                .offset(pageable.getOffset())
                .limit(pageable.getPageSize())
                .orderBy(getOrderSpecifiers(pageable, user))
                .fetch();

        JPAQuery<Long> countQuery = queryFactory
                .select(user.count())
                .from(user)
                .where(
                        nameContains(condition.name()),
                        emailContains(condition.email()),
                        statusEq(condition.status()),
                        user.deleted.isFalse()
                );

        return PageableExecutionUtils.getPage(content, pageable,
                countQuery::fetchOne);
    }

    // BooleanExpression 반환으로 null safety 보장 (조건 조합에 유리)
    private BooleanExpression nameContains(String name) {
        return StringUtils.hasText(name) ?
                QUser.user.name.containsIgnoreCase(name) : null;
    }

    private BooleanExpression emailContains(String email) {
        return StringUtils.hasText(email) ?
                QUser.user.email.containsIgnoreCase(email) : null;
    }

    private BooleanExpression statusEq(UserStatus status) {
        return status != null ? QUser.user.status.eq(status) : null;
    }
}
```

### Controller 패턴

```java
@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
@Tag(name = "User", description = "사용자 API")
public class UserController {

    private final UserService userService;

    @GetMapping
    @Operation(summary = "사용자 목록 조회")
    public ResponseEntity<ApiResponse<PageResponse<UserResponse>>> getUsers(
            @PageableDefault(size = 20, sort = "createdAt",
                    direction = Sort.Direction.DESC) Pageable pageable) {
        return ResponseEntity.ok(
                ApiResponse.ok(userService.getUsers(pageable)));
    }

    @GetMapping("/{id}")
    @Operation(summary = "사용자 상세 조회")
    public ResponseEntity<ApiResponse<UserDetailResponse>> getUser(
            @PathVariable Long id) {
        return ResponseEntity.ok(
                ApiResponse.ok(userService.findById(id)));
    }

    @GetMapping("/search")
    @Operation(summary = "사용자 검색")
    public ResponseEntity<ApiResponse<PageResponse<UserResponse>>> searchUsers(
            @ModelAttribute UserSearchCondition condition,
            @PageableDefault(size = 20) Pageable pageable) {
        return ResponseEntity.ok(
                ApiResponse.ok(userService.searchUsers(condition, pageable)));
    }

    @PostMapping
    @Operation(summary = "사용자 생성")
    public ResponseEntity<ApiResponse<UserResponse>> createUser(
            @RequestBody @Valid CreateUserRequest request) {
        UserResponse response = userService.createUser(request);
        URI location = URI.create("/api/v1/users/" + response.id());
        return ResponseEntity.created(location)
                .body(ApiResponse.ok(response));
    }

    @PutMapping("/{id}")
    @Operation(summary = "사용자 정보 수정")
    public ResponseEntity<ApiResponse<UserResponse>> updateUser(
            @PathVariable Long id,
            @RequestBody @Valid UpdateUserRequest request) {
        return ResponseEntity.ok(
                ApiResponse.ok(userService.updateUser(id, request)));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "사용자 삭제")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}
```

### 로깅 컨벤션

```java
// SLF4J + Lombok @Slf4j 사용
@Slf4j
@Service
public class OrderService {

    // 로그 레벨 가이드
    // ERROR: 즉시 대응 필요, 시스템 장애, 데이터 정합성 문제
    // WARN:  잠재적 문제, 비정상 상황이지만 처리 가능
    // INFO:  비즈니스 의미 있는 이벤트 (생성, 수정, 삭제, 상태 변경)
    // DEBUG: 개발 중 디버깅 (메서드 진입/종료, 변수값)
    // TRACE: 매우 상세한 흐름 (루프 내부, 쿼리 파라미터)

    public void processOrder(Long orderId) {
        log.info("주문 처리 시작: orderId={}", orderId);

        try {
            // 비즈니스 로직
            log.debug("결제 검증 진행: orderId={}", orderId);

        } catch (BusinessException e) {
            log.warn("주문 처리 실패 - 비즈니스 예외: orderId={}, error={}",
                    orderId, e.getMessage());
            throw e;
        } catch (Exception e) {
            log.error("주문 처리 실패 - 시스템 오류: orderId={}", orderId, e);
            throw new BusinessException(ErrorCode.INTERNAL_SERVER_ERROR);
        }

        log.info("주문 처리 완료: orderId={}", orderId);
    }
}
```

**로깅 규칙**:
- 문자열 연결 금지 - SLF4J 플레이스홀더 `{}` 사용
- 민감 정보(비밀번호, 토큰, 카드번호) 로그 출력 금지
- 예외 로깅 시 스택 트레이스 포함: `log.error("msg", e)`
- 로그에 트랜잭션 식별 정보(id) 반드시 포함

---

## 3. 보안 필수사항

### OWASP Top 10 대응 전략

#### A01: Broken Access Control (접근 제어 실패)

```java
// 1. URL 기반 접근 제어
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests(auth -> auth
            .requestMatchers("/api/v1/auth/**").permitAll()
            .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
            .requestMatchers(HttpMethod.GET, "/api/v1/users/**").authenticated()
            .requestMatchers(HttpMethod.POST, "/api/v1/users/**").hasRole("ADMIN")
            .anyRequest().authenticated()
    );
    return http.build();
}

// 2. 메서드 레벨 접근 제어
@PreAuthorize("hasRole('ADMIN') or #id == authentication.principal.id")
public UserDetailResponse findById(Long id) { ... }

// 3. 소유자 검증 (가장 중요한 패턴)
public OrderResponse getOrder(Long orderId) {
    Order order = orderRepository.findById(orderId)
            .orElseThrow(OrderNotFoundException::new);

    Long currentUserId = SecurityUtil.getCurrentUserId();
    if (!order.getUserId().equals(currentUserId)) {
        throw new BusinessException(ErrorCode.ACCESS_DENIED);
    }
    return OrderResponse.from(order);
}
```

#### A02: Cryptographic Failures (암호화 실패)

```java
// 비밀번호 해싱: BCrypt (strength 10~12)
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder(12);
}

// 민감 데이터 암호화: AES-256
@Component
public class AesEncryptor {
    @Value("${app.encryption.key}")
    private String secretKey;

    public String encrypt(String plainText) {
        // AES-256-GCM 사용 권장
    }

    public String decrypt(String cipherText) {
        // 복호화
    }
}

// application.yml에서 민감 설정값은 환경 변수로
spring:
  datasource:
    password: ${DB_PASSWORD}
```

#### A03: Injection

```java
// SQL Injection 방지 - 반드시 파라미터 바인딩
// 안전한 패턴:
@Query("SELECT u FROM User u WHERE u.email = :email")
Optional<User> findByEmail(@Param("email") String email);

// 안전한 네이티브 쿼리:
@Query(value = "SELECT * FROM users WHERE status = :status",
       nativeQuery = true)
List<User> findByStatusNative(@Param("status") String status);

// 위험 - 절대 사용 금지:
@Query("SELECT u FROM User u WHERE u.name = '" + name + "'")  // SQL Injection!

// QueryDSL은 기본적으로 파라미터 바인딩 사용하므로 안전
queryFactory.selectFrom(user)
        .where(user.email.eq(email))   // 파라미터 바인딩 자동 적용
        .fetchOne();

// OS Command Injection 방지
// Runtime.exec(), ProcessBuilder 사용 시 입력값 직접 사용 금지
// 화이트리스트 검증 필수
```

#### A04: Insecure Design (안전하지 않은 설계)

```java
// Rate Limiting 적용
@Bean
public Bucket rateLimitBucket() {
    Bandwidth limit = Bandwidth.classic(100,
            Refill.intervally(100, Duration.ofMinutes(1)));
    return Bucket.builder().addLimit(limit).build();
}

// 비밀번호 재설정 - 예측 불가능한 토큰 사용
public String generateResetToken() {
    return UUID.randomUUID().toString();  // 또는 SecureRandom
}

// 민감한 작업 시 재인증 요구
@PostMapping("/users/me/delete-account")
public ResponseEntity<Void> deleteAccount(
        @RequestBody @Valid DeleteAccountRequest request) {
    // 비밀번호 재확인 후 계정 삭제
}
```

#### A05: Security Misconfiguration (보안 설정 오류)

```java
// 보안 헤더 설정
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http.headers(headers -> headers
            .contentTypeOptions(Customizer.withDefaults())          // X-Content-Type-Options: nosniff
            .frameOptions(frame -> frame.deny())                    // X-Frame-Options: DENY
            .httpStrictTransportSecurity(hsts -> hsts
                    .includeSubDomains(true)
                    .maxAgeInSeconds(31536000))                     // HSTS
            .referrerPolicy(referrer ->
                    referrer.policy(ReferrerPolicyHeaderWriter
                            .ReferrerPolicy.STRICT_ORIGIN_WHEN_CROSS_ORIGIN))
            .permissionsPolicyHeader(permissions -> permissions
                    .policy("camera=(), microphone=(), geolocation=()"))
    );

    // Content-Security-Policy (CSP)
    http.headers(headers -> headers
            .contentSecurityPolicy(csp -> csp
                    .policyDirectives("default-src 'self'; " +
                            "script-src 'self'; " +
                            "style-src 'self' 'unsafe-inline'; " +
                            "img-src 'self' data:; " +
                            "font-src 'self'; " +
                            "connect-src 'self'; " +
                            "frame-ancestors 'none'"))
    );

    return http.build();
}

// Actuator 엔드포인트 보안
management:
  endpoints:
    web:
      exposure:
        include: health, info, metrics
      base-path: /internal/actuator   # 기본 경로 변경
  endpoint:
    health:
      show-details: when_authorized   # 인증된 경우만 상세 표시
```

#### A07: Identification and Authentication Failures

##### Spring Security 전체 구성

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(prePostEnabled = true)
@RequiredArgsConstructor
public class SecurityConfig {

    private final JwtAuthenticationFilter jwtAuthenticationFilter;
    private final CustomAccessDeniedHandler accessDeniedHandler;
    private final CustomAuthenticationEntryPoint authenticationEntryPoint;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                // CSRF 비활성화 (JWT 기반 stateless)
                .csrf(AbstractHttpConfigurer::disable)

                // 세션 관리: STATELESS
                .sessionManagement(session -> session
                        .sessionCreationPolicy(SessionCreationPolicy.STATELESS))

                // CORS 설정
                .cors(cors -> cors.configurationSource(corsConfigurationSource()))

                // 예외 처리
                .exceptionHandling(exception -> exception
                        .authenticationEntryPoint(authenticationEntryPoint)
                        .accessDeniedHandler(accessDeniedHandler))

                // URL 권한 설정
                .authorizeHttpRequests(auth -> auth
                        .requestMatchers(
                                "/api/v1/auth/**",
                                "/swagger-ui/**",
                                "/v3/api-docs/**",
                                "/actuator/health"
                        ).permitAll()
                        .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
                        .anyRequest().authenticated()
                )

                // JWT 필터 등록
                .addFilterBefore(jwtAuthenticationFilter,
                        UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowedOrigins(List.of(
                "http://localhost:3000",
                "https://app.example.com"
        ));
        config.setAllowedMethods(List.of(
                "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"));
        config.setAllowedHeaders(List.of("*"));
        config.setExposedHeaders(List.of("Authorization", "X-Total-Count"));
        config.setAllowCredentials(true);
        config.setMaxAge(3600L);

        UrlBasedCorsConfigurationSource source =
                new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", config);
        return source;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(12);
    }

    @Bean
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }
}
```

##### JWT 인증 플로우

```java
@Slf4j
@Component
@RequiredArgsConstructor
public class JwtTokenProvider {

    @Value("${jwt.secret}")
    private String secretKey;

    @Value("${jwt.access-token-expiry:3600000}")   // 1시간
    private long accessTokenExpiry;

    @Value("${jwt.refresh-token-expiry:604800000}") // 7일
    private long refreshTokenExpiry;

    private SecretKey key;

    @PostConstruct
    public void init() {
        byte[] keyBytes = Decoders.BASE64.decode(secretKey);
        this.key = Keys.hmacShaKeyFor(keyBytes);
    }

    public String generateAccessToken(Authentication authentication) {
        CustomUserDetails userDetails =
                (CustomUserDetails) authentication.getPrincipal();

        return Jwts.builder()
                .subject(userDetails.getUsername())
                .claim("userId", userDetails.getUserId())
                .claim("roles", userDetails.getAuthorities().stream()
                        .map(GrantedAuthority::getAuthority)
                        .toList())
                .issuedAt(new Date())
                .expiration(new Date(System.currentTimeMillis()
                        + accessTokenExpiry))
                .signWith(key)
                .compact();
    }

    public String generateRefreshToken(String username) {
        return Jwts.builder()
                .subject(username)
                .issuedAt(new Date())
                .expiration(new Date(System.currentTimeMillis()
                        + refreshTokenExpiry))
                .signWith(key)
                .compact();
    }

    public boolean validateToken(String token) {
        try {
            Jwts.parser().verifyWith(key).build().parseSignedClaims(token);
            return true;
        } catch (ExpiredJwtException e) {
            log.warn("만료된 JWT 토큰: {}", e.getMessage());
        } catch (JwtException e) {
            log.warn("유효하지 않은 JWT 토큰: {}", e.getMessage());
        }
        return false;
    }

    public Claims getClaims(String token) {
        return Jwts.parser()
                .verifyWith(key)
                .build()
                .parseSignedClaims(token)
                .getPayload();
    }

    public String getUsernameFromToken(String token) {
        return getClaims(token).getSubject();
    }
}
```

```java
@Slf4j
@Component
@RequiredArgsConstructor
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private static final String AUTHORIZATION_HEADER = "Authorization";
    private static final String BEARER_PREFIX = "Bearer ";

    private final JwtTokenProvider jwtTokenProvider;
    private final CustomUserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain)
            throws ServletException, IOException {

        String token = resolveToken(request);

        if (token != null && jwtTokenProvider.validateToken(token)) {
            String username = jwtTokenProvider.getUsernameFromToken(token);
            UserDetails userDetails =
                    userDetailsService.loadUserByUsername(username);

            UsernamePasswordAuthenticationToken authentication =
                    new UsernamePasswordAuthenticationToken(
                            userDetails, null,
                            userDetails.getAuthorities());
            authentication.setDetails(
                    new WebAuthenticationDetailsSource()
                            .buildDetails(request));

            SecurityContextHolder.getContext()
                    .setAuthentication(authentication);
        }

        filterChain.doFilter(request, response);
    }

    private String resolveToken(HttpServletRequest request) {
        String bearerToken = request.getHeader(AUTHORIZATION_HEADER);
        if (StringUtils.hasText(bearerToken) &&
                bearerToken.startsWith(BEARER_PREFIX)) {
            return bearerToken.substring(BEARER_PREFIX.length());
        }
        return null;
    }

    @Override
    protected boolean shouldNotFilter(HttpServletRequest request) {
        String path = request.getRequestURI();
        return path.startsWith("/api/v1/auth/") ||
               path.startsWith("/swagger-ui/") ||
               path.startsWith("/v3/api-docs/");
    }
}
```

```java
@Getter
@RequiredArgsConstructor
public class CustomUserDetails implements UserDetails {

    private final Long userId;
    private final String username;
    private final String password;
    private final Collection<? extends GrantedAuthority> authorities;
    private final boolean enabled;

    public static CustomUserDetails from(User user) {
        List<SimpleGrantedAuthority> authorities = user.getRoles().stream()
                .map(role -> new SimpleGrantedAuthority("ROLE_" + role.getName()))
                .toList();
        return new CustomUserDetails(
                user.getId(),
                user.getEmail(),
                user.getPassword(),
                authorities,
                user.getStatus() == UserStatus.ACTIVE
        );
    }

    @Override
    public boolean isAccountNonExpired() { return true; }
    @Override
    public boolean isAccountNonLocked() { return true; }
    @Override
    public boolean isCredentialsNonExpired() { return true; }
}
```

##### @PreAuthorize 사용 패턴

```java
// 역할 기반
@PreAuthorize("hasRole('ADMIN')")
public void adminOnly() { ... }

// 복합 조건
@PreAuthorize("hasRole('ADMIN') or hasRole('MANAGER')")
public void adminOrManager() { ... }

// 소유자 검증 (SpEL)
@PreAuthorize("#userId == authentication.principal.userId")
public UserResponse getUserProfile(@PathVariable Long userId) { ... }

// 커스텀 표현식
@PreAuthorize("@authorizationChecker.isOwner(#orderId)")
public OrderResponse getOrder(@PathVariable Long orderId) { ... }

// 커스텀 검증 Bean
@Component("authorizationChecker")
@RequiredArgsConstructor
public class AuthorizationChecker {

    private final OrderRepository orderRepository;

    public boolean isOwner(Long orderId) {
        Long currentUserId = SecurityUtil.getCurrentUserId();
        return orderRepository.existsByIdAndUserId(orderId, currentUserId);
    }
}
```

### Bean Validation 상세

#### 커스텀 Validator 구현

```java
// 1. 어노테이션 정의
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = PhoneNumberValidator.class)
@Documented
public @interface ValidPhoneNumber {
    String message() default "올바른 전화번호 형식이 아닙니다.";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

// 2. Validator 구현
public class PhoneNumberValidator
        implements ConstraintValidator<ValidPhoneNumber, String> {

    private static final Pattern PHONE_PATTERN =
            Pattern.compile("^01[016789]-?\\d{3,4}-?\\d{4}$");

    @Override
    public boolean isValid(String value, ConstraintValidatorContext ctx) {
        if (value == null || value.isBlank()) {
            return true;   // @NotBlank와 조합하여 사용
        }
        return PHONE_PATTERN.matcher(value).matches();
    }
}

// 3. 사용
public record CreateUserRequest(
        @NotBlank String name,
        @NotBlank @Email String email,
        @ValidPhoneNumber String phoneNumber
) {}
```

#### 그룹 검증

```java
// 검증 그룹 정의
public interface OnCreate {}
public interface OnUpdate {}

// DTO에 그룹 적용
public record UserRequest(
        @Null(groups = OnCreate.class)
        @NotNull(groups = OnUpdate.class)
        Long id,

        @NotBlank(groups = {OnCreate.class, OnUpdate.class})
        String name,

        @NotBlank(groups = OnCreate.class)
        @Email
        String email
) {}

// Controller에서 그룹 지정
@PostMapping
public ResponseEntity<ApiResponse<UserResponse>> create(
        @RequestBody @Validated(OnCreate.class) UserRequest request) { ... }

@PutMapping("/{id}")
public ResponseEntity<ApiResponse<UserResponse>> update(
        @PathVariable Long id,
        @RequestBody @Validated(OnUpdate.class) UserRequest request) { ... }
```

### 파일 업로드 보안

```java
@RestController
@RequestMapping("/api/v1/files")
@RequiredArgsConstructor
public class FileController {

    private static final Set<String> ALLOWED_EXTENSIONS =
            Set.of("jpg", "jpeg", "png", "gif", "pdf", "docx", "xlsx");
    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

    private final FileService fileService;

    @PostMapping("/upload")
    public ResponseEntity<ApiResponse<FileResponse>> upload(
            @RequestParam("file") MultipartFile file) {

        // 1. 빈 파일 검증
        if (file.isEmpty()) {
            throw new InvalidValueException(ErrorCode.INVALID_INPUT_VALUE);
        }

        // 2. 파일 크기 검증
        if (file.getSize() > MAX_FILE_SIZE) {
            throw new InvalidValueException(ErrorCode.INVALID_INPUT_VALUE);
        }

        // 3. 확장자 검증 (화이트리스트)
        String extension = getExtension(file.getOriginalFilename());
        if (!ALLOWED_EXTENSIONS.contains(extension.toLowerCase())) {
            throw new InvalidValueException(ErrorCode.INVALID_INPUT_VALUE);
        }

        // 4. Content-Type 검증 (확장자와 일치 여부)
        String contentType = file.getContentType();
        if (!isValidContentType(extension, contentType)) {
            throw new InvalidValueException(ErrorCode.INVALID_INPUT_VALUE);
        }

        // 5. 파일명 sanitize (경로 순회 공격 방지)
        String safeFileName = UUID.randomUUID() + "." + extension;

        return ResponseEntity.ok(
                ApiResponse.ok(fileService.upload(file, safeFileName)));
    }
}
```

### Rate Limiting

```java
@Component
@RequiredArgsConstructor
public class RateLimitFilter extends OncePerRequestFilter {

    private final Map<String, Bucket> buckets =
            new ConcurrentHashMap<>();

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain)
            throws ServletException, IOException {

        String clientIp = getClientIp(request);
        Bucket bucket = buckets.computeIfAbsent(clientIp,
                k -> createBucket());

        if (bucket.tryConsume(1)) {
            filterChain.doFilter(request, response);
        } else {
            response.setStatus(HttpStatus.TOO_MANY_REQUESTS.value());
            response.setContentType(MediaType.APPLICATION_JSON_VALUE);
            response.getWriter().write(
                    "{\"code\":\"C007\",\"message\":\"요청이 너무 많습니다.\"}");
        }
    }

    private Bucket createBucket() {
        return Bucket.builder()
                .addLimit(Bandwidth.classic(100,
                        Refill.intervally(100, Duration.ofMinutes(1))))
                .build();
    }

    private String getClientIp(HttpServletRequest request) {
        String xff = request.getHeader("X-Forwarded-For");
        return xff != null ? xff.split(",")[0].trim() :
                request.getRemoteAddr();
    }
}
```

---

## 4. 생산성 가이드

### 공통 응답 래퍼 전체 구현

```java
@Getter
public class ApiResponse<T> {

    private final boolean success;
    private final T data;
    private final String message;

    private ApiResponse(boolean success, T data, String message) {
        this.success = success;
        this.data = data;
        this.message = message;
    }

    public static <T> ApiResponse<T> ok(T data) {
        return new ApiResponse<>(true, data, null);
    }

    public static <T> ApiResponse<T> ok(T data, String message) {
        return new ApiResponse<>(true, data, message);
    }

    public static ApiResponse<Void> ok() {
        return new ApiResponse<>(true, null, null);
    }

    public static ApiResponse<Void> error(String message) {
        return new ApiResponse<>(false, null, message);
    }

    public static <T> ApiResponse<T> error(String message, T data) {
        return new ApiResponse<>(false, data, message);
    }
}
```

```java
@Getter
public class PageResponse<T> {

    private final List<T> content;
    private final int page;
    private final int size;
    private final long totalElements;
    private final int totalPages;
    private final boolean first;
    private final boolean last;

    private PageResponse(Page<T> page) {
        this.content = page.getContent();
        this.page = page.getNumber();
        this.size = page.getSize();
        this.totalElements = page.getTotalElements();
        this.totalPages = page.getTotalPages();
        this.first = page.isFirst();
        this.last = page.isLast();
    }

    public static <T> PageResponse<T> from(Page<T> page) {
        return new PageResponse<>(page);
    }
}
```

### AOP 패턴

#### 실행 시간 로깅

```java
@Slf4j
@Aspect
@Component
public class PerformanceAspect {

    @Around("@annotation(com.example.app.global.aop.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint)
            throws Throwable {
        long start = System.currentTimeMillis();
        String methodName = joinPoint.getSignature().toShortString();

        try {
            Object result = joinPoint.proceed();
            long elapsed = System.currentTimeMillis() - start;
            log.info("[Performance] {} 실행 시간: {}ms", methodName, elapsed);

            if (elapsed > 3000) {
                log.warn("[Performance] 느린 메서드 감지: {} ({}ms)",
                        methodName, elapsed);
            }
            return result;
        } catch (Throwable e) {
            long elapsed = System.currentTimeMillis() - start;
            log.error("[Performance] {} 실행 실패 ({}ms): {}",
                    methodName, elapsed, e.getMessage());
            throw e;
        }
    }
}

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {}
```

#### API 요청/응답 로깅

```java
@Slf4j
@Aspect
@Component
public class LoggingAspect {

    @Around("within(com.example.app.domain..controller..*)")
    public Object logApiCall(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().toShortString();
        Object[] args = joinPoint.getArgs();

        log.info("[API 요청] {} args={}", methodName,
                filterSensitiveArgs(args));

        Object result = joinPoint.proceed();

        log.info("[API 응답] {} result={}", methodName,
                truncateResult(result));

        return result;
    }

    private String filterSensitiveArgs(Object[] args) {
        // password, token 등 민감 정보 마스킹
        return Arrays.stream(args)
                .map(arg -> arg != null ? arg.toString() : "null")
                .collect(Collectors.joining(", "));
    }

    private String truncateResult(Object result) {
        String str = result != null ? result.toString() : "null";
        return str.length() > 200 ? str.substring(0, 200) + "..." : str;
    }
}
```

### 테스트 전략 상세

#### 테스트 네이밍과 구조

```java
// 테스트 네이밍: 한글 사용 가능, DisplayName 활용
@DisplayName("UserService 단위 테스트")
class UserServiceTest {

    @Nested
    @DisplayName("createUser 메서드")
    class CreateUser {

        @Test
        @DisplayName("정상적인 요청으로 사용자를 생성한다")
        void createUser_validRequest_success() { ... }

        @Test
        @DisplayName("중복 이메일이면 DuplicateEmailException을 던진다")
        void createUser_duplicateEmail_throwsException() { ... }
    }

    @Nested
    @DisplayName("findById 메서드")
    class FindById {

        @Test
        @DisplayName("존재하는 ID로 사용자를 조회한다")
        void findById_existingId_returnsUser() { ... }

        @Test
        @DisplayName("존재하지 않는 ID이면 UserNotFoundException을 던진다")
        void findById_nonExistingId_throwsException() { ... }
    }
}
```

#### JUnit 5 + Mockito 단위 테스트

```java
@ExtendWith(MockitoExtension.class)
@DisplayName("UserService 단위 테스트")
class UserServiceTest {

    @InjectMocks
    private UserService userService;

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private ApplicationEventPublisher eventPublisher;

    @Nested
    @DisplayName("createUser")
    class CreateUser {

        @Test
        @DisplayName("정상 요청 - 사용자를 생성하고 응답을 반환한다")
        void success() {
            // given
            CreateUserRequest request = new CreateUserRequest(
                    "홍길동", "hong@example.com", "Password1!", "010-1234-5678");

            given(userRepository.existsByEmail(request.email()))
                    .willReturn(false);
            given(passwordEncoder.encode(request.password()))
                    .willReturn("encodedPassword");
            given(userRepository.save(any(User.class)))
                    .willAnswer(invocation -> {
                        User user = invocation.getArgument(0);
                        // Reflection으로 id 설정 또는 TestFixture 사용
                        return user;
                    });

            // when
            UserResponse response = userService.createUser(request);

            // then
            assertThat(response.name()).isEqualTo("홍길동");
            assertThat(response.email()).isEqualTo("hong@example.com");

            then(userRepository).should().save(any(User.class));
            then(eventPublisher).should()
                    .publishEvent(any(UserCreatedEvent.class));
        }

        @Test
        @DisplayName("중복 이메일 - DuplicateEmailException 발생")
        void duplicateEmail_throwsException() {
            // given
            CreateUserRequest request = new CreateUserRequest(
                    "홍길동", "existing@example.com", "Password1!", null);

            given(userRepository.existsByEmail(request.email()))
                    .willReturn(true);

            // when & then
            assertThatThrownBy(() -> userService.createUser(request))
                    .isInstanceOf(DuplicateEmailException.class);

            then(userRepository).should(never()).save(any());
        }
    }

    @Nested
    @DisplayName("findById")
    class FindById {

        @Test
        @DisplayName("존재하는 사용자 조회")
        void existingUser_returnsDetail() {
            // given
            User user = UserFixture.createUser(1L, "홍길동",
                    "hong@example.com");
            given(userRepository.findByIdAndDeletedFalse(1L))
                    .willReturn(Optional.of(user));

            // when
            UserDetailResponse response = userService.findById(1L);

            // then
            assertThat(response.id()).isEqualTo(1L);
            assertThat(response.name()).isEqualTo("홍길동");
        }
    }

    // ParameterizedTest 예시
    @ParameterizedTest
    @ValueSource(strings = {"", " ", "   "})
    @DisplayName("빈 이메일로 검색하면 빈 결과를 반환한다")
    void searchWithBlankEmail_returnsEmpty(String email) {
        // ...
    }

    @ParameterizedTest
    @CsvSource({
            "ACTIVE, true",
            "INACTIVE, false",
            "DELETED, false"
    })
    @DisplayName("사용자 상태에 따라 활성 여부를 반환한다")
    void isActive_byStatus(UserStatus status, boolean expected) {
        User user = UserFixture.createUserWithStatus(status);
        assertThat(user.isActive()).isEqualTo(expected);
    }
}
```

#### @WebMvcTest (Controller 테스트)

```java
@WebMvcTest(UserController.class)
@MockBean(JpaMetamodelMappingContext.class)  // JPA Auditing 관련
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private UserService userService;

    @Test
    @WithMockUser
    @DisplayName("POST /api/v1/users - 사용자 생성 성공")
    void createUser_success() throws Exception {
        // given
        CreateUserRequest request = new CreateUserRequest(
                "홍길동", "hong@example.com", "Password1!", null);
        UserResponse response = new UserResponse(
                1L, "홍길동", "hong@example.com",
                UserStatus.ACTIVE, LocalDateTime.now());

        given(userService.createUser(any())).willReturn(response);

        // when & then
        mockMvc.perform(post("/api/v1/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.success").value(true))
                .andExpect(jsonPath("$.data.name").value("홍길동"))
                .andExpect(jsonPath("$.data.email").value("hong@example.com"))
                .andDo(print());
    }

    @Test
    @WithMockUser
    @DisplayName("POST /api/v1/users - 유효하지 않은 이메일이면 400")
    void createUser_invalidEmail_returns400() throws Exception {
        CreateUserRequest request = new CreateUserRequest(
                "홍길동", "invalid-email", "Password1!", null);

        mockMvc.perform(post("/api/v1/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.code").value("C001"));
    }

    @Test
    @WithMockUser
    @DisplayName("GET /api/v1/users - 페이지네이션 목록 조회")
    void getUsers_withPagination() throws Exception {
        // given
        PageResponse<UserResponse> pageResponse = // ... mock setup

        given(userService.getUsers(any(Pageable.class)))
                .willReturn(pageResponse);

        // when & then
        mockMvc.perform(get("/api/v1/users")
                        .param("page", "0")
                        .param("size", "10")
                        .param("sort", "createdAt,desc"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.data.content").isArray())
                .andExpect(jsonPath("$.data.totalElements").isNumber());
    }
}
```

#### @DataJpaTest (Repository 테스트)

```java
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Import(QuerydslConfig.class)
class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private TestEntityManager entityManager;

    @Test
    @DisplayName("이메일로 사용자를 조회한다")
    void findByEmail_existingEmail_returnsUser() {
        // given
        User user = User.create("홍길동", "hong@example.com", "encoded");
        entityManager.persistAndFlush(user);

        // when
        Optional<User> found = userRepository.findByEmail("hong@example.com");

        // then
        assertThat(found).isPresent();
        assertThat(found.get().getName()).isEqualTo("홍길동");
    }

    @Test
    @DisplayName("삭제되지 않은 사용자만 조회한다")
    void findByIdAndDeletedFalse_deletedUser_returnsEmpty() {
        // given
        User user = User.create("홍길동", "hong@example.com", "encoded");
        user.softDelete();
        entityManager.persistAndFlush(user);

        // when
        Optional<User> found =
                userRepository.findByIdAndDeletedFalse(user.getId());

        // then
        assertThat(found).isEmpty();
    }
}
```

#### TestContainers 설정

```java
// 공통 TestContainers 설정 (상속용)
@Testcontainers
@SpringBootTest
@ActiveProfiles("test")
public abstract class IntegrationTestSupport {

    @Container
    static PostgreSQLContainer<?> postgres =
            new PostgreSQLContainer<>("postgres:16-alpine")
                    .withDatabaseName("testdb")
                    .withUsername("test")
                    .withPassword("test");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }
}

// Redis 컨테이너 추가 시
@Container
static GenericContainer<?> redis =
        new GenericContainer<>("redis:7-alpine")
                .withExposedPorts(6379);

@DynamicPropertySource
static void redisProperties(DynamicPropertyRegistry registry) {
    registry.add("spring.data.redis.host", redis::getHost);
    registry.add("spring.data.redis.port",
            () -> redis.getMappedPort(6379));
}
```

#### 테스트 픽스처

```java
public class UserFixture {

    public static User createUser(Long id, String name, String email) {
        User user = User.create(name, email, "encodedPassword");
        ReflectionTestUtils.setField(user, "id", id);
        ReflectionTestUtils.setField(user, "createdAt", LocalDateTime.now());
        return user;
    }

    public static User createActiveUser() {
        return createUser(1L, "홍길동", "hong@example.com");
    }

    public static User createUserWithStatus(UserStatus status) {
        User user = createActiveUser();
        ReflectionTestUtils.setField(user, "status", status);
        return user;
    }

    public static CreateUserRequest createUserRequest() {
        return new CreateUserRequest(
                "홍길동", "hong@example.com", "Password1!", "010-1234-5678");
    }
}
```

### API 문서화 (SpringDoc/Swagger)

```java
@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI openAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("My App API")
                        .description("Spring Boot REST API 문서")
                        .version("v1.0.0")
                        .contact(new Contact()
                                .name("Dev Team")
                                .email("dev@example.com")))
                .addSecurityItem(new SecurityRequirement()
                        .addList("bearerAuth"))
                .components(new Components()
                        .addSecuritySchemes("bearerAuth",
                                new SecurityScheme()
                                        .type(SecurityScheme.Type.HTTP)
                                        .scheme("bearer")
                                        .bearerFormat("JWT")));
    }
}
```

```yaml
# application.yml
springdoc:
  swagger-ui:
    path: /swagger-ui.html
    tags-sorter: alpha
    operations-sorter: alpha
  api-docs:
    path: /v3/api-docs
  show-actuator: false
  default-consumes-media-type: application/json
  default-produces-media-type: application/json
```

### Docker 설정

#### Dockerfile

```dockerfile
# 멀티스테이지 빌드
FROM eclipse-temurin:17-jdk-alpine AS builder
WORKDIR /app
COPY gradlew .
COPY gradle gradle
COPY build.gradle.kts .
COPY settings.gradle.kts .
COPY src src

RUN chmod +x gradlew && ./gradlew bootJar -x test

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", \
    "-XX:+UseContainerSupport", \
    "-XX:MaxRAMPercentage=75.0", \
    "-Djava.security.egd=file:/dev/./urandom", \
    "-jar", "app.jar"]
```

#### docker-compose.yml

```yaml
services:
  app:
    build:
      context: .
      dockerfile: docker/Dockerfile
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=local
      - DB_HOST=postgres
      - DB_PORT=5432
      - DB_NAME=myapp
      - DB_USERNAME=myapp
      - DB_PASSWORD=myapp
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started

  postgres:
    image: postgres:16-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: myapp
      POSTGRES_PASSWORD: myapp
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./scripts/init-db.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myapp"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

volumes:
  postgres-data:
  redis-data:
```

### CLI 명령어 전체 리스트

```bash
# === Gradle ===
./gradlew bootRun                            # 개발 서버 실행
./gradlew bootRun --args='--spring.profiles.active=local'  # 프로파일 지정 실행
./gradlew test                               # 전체 테스트 실행
./gradlew test --tests "*.UserServiceTest"   # 특정 테스트 클래스
./gradlew test --tests "*UserServiceTest.createUser*"  # 특정 메서드
./gradlew test -Dtest.profile=integration    # 프로파일 지정 테스트
./gradlew bootJar                            # 실행 가능 JAR 빌드
./gradlew clean build                        # 클린 빌드
./gradlew clean build -x test               # 테스트 제외 빌드
./gradlew dependencies                       # 의존성 트리 확인
./gradlew dependencyUpdates                  # 업데이트 가능 의존성 확인
./gradlew jacocoTestReport                   # 테스트 커버리지 리포트
./gradlew compileJava                        # 컴파일만 수행
./gradlew dependencyCheckAnalyze             # OWASP 의존성 보안 검사
./gradlew spotlessApply                      # 코드 포맷팅 적용

# === Docker ===
docker compose up -d                         # 인프라 컨테이너 실행
docker compose down                          # 컨테이너 중지 및 제거
docker compose down -v                       # 볼륨 포함 제거
docker compose logs -f app                   # 앱 로그 스트리밍
docker compose ps                            # 컨테이너 상태 확인
docker build -t myapp:latest -f docker/Dockerfile .  # 이미지 빌드
docker run -p 8080:8080 myapp:latest         # 컨테이너 실행

# === 데이터베이스 ===
docker compose exec postgres psql -U myapp   # PostgreSQL 접속
docker compose exec redis redis-cli          # Redis CLI 접속

# === JAR 실행 ===
java -jar build/libs/app-0.0.1-SNAPSHOT.jar --spring.profiles.active=prod
```

---

## 5. 성능 최적화

### JPA 최적화

#### N+1 문제 해결

```java
// 1. JOIN FETCH - JPQL에서 연관 엔티티를 한 번에 로딩
@Query("SELECT u FROM User u JOIN FETCH u.roles WHERE u.id = :id")
Optional<User> findWithRolesById(@Param("id") Long id);

// 주의: 컬렉션 JOIN FETCH는 페이징과 함께 사용 불가
// 아래 쿼리는 메모리에서 페이징 처리 (위험)
@Query("SELECT u FROM User u JOIN FETCH u.roles")
Page<User> findAllWithRoles(Pageable pageable);  // 경고 발생

// 2. @EntityGraph - 선언적 페치 전략
@EntityGraph(attributePaths = {"roles"})
@Query("SELECT u FROM User u WHERE u.id = :id")
Optional<User> findWithRolesByIdGraph(@Param("id") Long id);

// 여러 연관관계를 동시에 로딩
@EntityGraph(attributePaths = {"roles", "orders"})
Optional<User> findWithRolesAndOrdersById(Long id);

// 3. @BatchSize - 지연 로딩 시 IN 절로 일괄 조회
@Entity
public class User {
    @BatchSize(size = 100)
    @OneToMany(mappedBy = "user")
    private List<Order> orders = new ArrayList<>();
}

// 또는 글로벌 설정 (application.yml)
// spring.jpa.properties.hibernate.default_batch_fetch_size: 100

// 4. QueryDSL에서 fetchJoin
queryFactory.selectFrom(user)
        .leftJoin(user.roles, role).fetchJoin()
        .where(user.id.eq(userId))
        .fetchOne();
```

#### 읽기 전용 조회 최적화

```java
// 1. @Transactional(readOnly = true) - 영속성 컨텍스트 스냅샷 생략
@Transactional(readOnly = true)
public UserResponse findById(Long id) {
    // 변경 감지(dirty checking) 비활성화 -> 성능 향상
    User user = userRepository.findById(id)
            .orElseThrow(UserNotFoundException::new);
    return UserResponse.from(user);
}

// 2. DTO Projection - Entity 로딩 없이 필요한 필드만 조회

// Interface Projection (간단한 경우)
public interface UserSummary {
    Long getId();
    String getName();
    String getEmail();
}
List<UserSummary> findAllBy();

// Class (Record) Projection (타입 안전)
@Query("SELECT new com.example.app.domain.user.dto.response.UserResponse(" +
       "u.id, u.name, u.email, u.status, u.createdAt) " +
       "FROM User u WHERE u.deleted = false")
Page<UserResponse> findAllProjected(Pageable pageable);

// QueryDSL Projection
queryFactory
        .select(Projections.constructor(UserResponse.class,
                user.id, user.name, user.email,
                user.status, user.createdAt))
        .from(user)
        .where(user.deleted.isFalse())
        .fetch();
```

#### 벌크 연산

```java
// JPQL 벌크 업데이트 (영속성 컨텍스트 우회)
@Modifying(clearAutomatically = true, flushAutomatically = true)
@Query("UPDATE User u SET u.status = :status " +
       "WHERE u.id IN :ids")
int bulkUpdateStatus(@Param("ids") List<Long> ids,
                     @Param("status") UserStatus status);

// 벌크 삭제
@Modifying(clearAutomatically = true)
@Query("DELETE FROM User u WHERE u.status = 'DELETED' " +
       "AND u.updatedAt < :before")
int bulkDeleteOldUsers(@Param("before") LocalDateTime before);

// JPA saveAll vs JDBC batch insert
// saveAll은 여전히 건별 INSERT -> 대량 삽입 시 JDBC 직접 사용 권장
@RequiredArgsConstructor
public class UserBulkRepository {
    private final JdbcTemplate jdbcTemplate;

    public void bulkInsert(List<User> users) {
        jdbcTemplate.batchUpdate(
                "INSERT INTO users (name, email, status, created_at) " +
                "VALUES (?, ?, ?, ?)",
                new BatchPreparedStatementSetter() {
                    @Override
                    public void setValues(PreparedStatement ps, int i)
                            throws SQLException {
                        User user = users.get(i);
                        ps.setString(1, user.getName());
                        ps.setString(2, user.getEmail());
                        ps.setString(3, user.getStatus().name());
                        ps.setTimestamp(4,
                                Timestamp.valueOf(LocalDateTime.now()));
                    }
                    @Override
                    public int getBatchSize() { return users.size(); }
                });
    }
}
```

### 캐싱 전략

#### Spring Cache 설정

```java
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public RedisCacheManager cacheManager(
            RedisConnectionFactory connectionFactory) {

        // 기본 캐시 설정
        RedisCacheConfiguration defaultConfig =
                RedisCacheConfiguration.defaultCacheConfig()
                        .entryTtl(Duration.ofMinutes(30))
                        .serializeKeysWith(
                                RedisSerializationContext.SerializationPair
                                        .fromSerializer(
                                                new StringRedisSerializer()))
                        .serializeValuesWith(
                                RedisSerializationContext.SerializationPair
                                        .fromSerializer(
                                                new GenericJackson2JsonRedisSerializer()))
                        .disableCachingNullValues();

        // 캐시별 TTL 설정
        Map<String, RedisCacheConfiguration> cacheConfigs = Map.of(
                "users", defaultConfig.entryTtl(Duration.ofHours(1)),
                "userDetail", defaultConfig.entryTtl(Duration.ofMinutes(30)),
                "codes", defaultConfig.entryTtl(Duration.ofHours(24)),
                "settings", defaultConfig.entryTtl(Duration.ofHours(12))
        );

        return RedisCacheManager.builder(connectionFactory)
                .cacheDefaults(defaultConfig)
                .withInitialCacheConfigurations(cacheConfigs)
                .transactionAware()
                .build();
    }
}
```

#### 캐시 사용 패턴

```java
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class UserQueryService {

    private final UserRepository userRepository;

    // 캐시 조회 (캐시에 없으면 DB 조회 후 캐시 저장)
    @Cacheable(value = "userDetail", key = "#id",
               unless = "#result == null")
    public UserDetailResponse findById(Long id) {
        User user = userRepository.findById(id)
                .orElseThrow(UserNotFoundException::new);
        return UserDetailResponse.from(user);
    }

    // 캐시 갱신 (메서드 실행 후 결과를 캐시에 저장)
    @CachePut(value = "userDetail", key = "#id")
    @Transactional
    public UserDetailResponse updateAndCache(Long id,
                                              UpdateUserRequest request) {
        User user = userRepository.findById(id)
                .orElseThrow(UserNotFoundException::new);
        user.updateProfile(request.name(), request.phoneNumber());
        return UserDetailResponse.from(user);
    }

    // 캐시 삭제
    @CacheEvict(value = "userDetail", key = "#id")
    @Transactional
    public void deleteUser(Long id) {
        // ...
    }

    // 여러 캐시 동시 삭제
    @Caching(evict = {
            @CacheEvict(value = "userDetail", key = "#id"),
            @CacheEvict(value = "users", allEntries = true)
    })
    @Transactional
    public void updateUserStatus(Long id, UserStatus status) {
        // ...
    }
}
```

#### Redis 캐시 키 설계 규칙

```
# 키 패턴: {서비스}:{엔티티}:{식별자}
user:detail:123
user:list:page:0:size:20
order:detail:456
code:common:STATUS

# TTL 가이드라인
자주 변경되는 데이터: 5~15분
사용자 정보: 30분 ~ 1시간
코드성 데이터: 12~24시간
설정 데이터: 24시간
```

### 커넥션 풀 (HikariCP)

```yaml
spring:
  datasource:
    hikari:
      # 풀 크기 설정
      maximum-pool-size: 20          # 최대 커넥션 수 (CPU 코어 x 2 + 디스크 수)
      minimum-idle: 5                # 최소 유휴 커넥션 수
      # 타임아웃 설정
      connection-timeout: 3000       # 커넥션 대기 최대 시간 (ms) - 3초
      idle-timeout: 600000           # 유휴 커넥션 유지 시간 (ms) - 10분
      max-lifetime: 1800000          # 커넥션 최대 수명 (ms) - 30분
      # 검증
      validation-timeout: 5000       # 커넥션 검증 타임아웃 (ms)
      # 누수 감지 (개발/스테이징 환경)
      leak-detection-threshold: 30000  # 30초 이상 미반환 커넥션 경고
      # 풀 이름
      pool-name: MyAppHikariPool
```

### 비동기 처리

#### @Async 설정

```java
@Configuration
@EnableAsync
public class AsyncConfig implements AsyncConfigurer {

    @Override
    @Bean(name = "taskExecutor")
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);          // 기본 스레드 수
        executor.setMaxPoolSize(20);          // 최대 스레드 수
        executor.setQueueCapacity(100);       // 큐 크기
        executor.setThreadNamePrefix("async-");
        executor.setRejectedExecutionHandler(
                new ThreadPoolExecutor.CallerRunsPolicy());
        executor.setWaitForTasksToCompleteOnShutdown(true);
        executor.setAwaitTerminationSeconds(30);
        executor.initialize();
        return executor;
    }

    @Override
    public AsyncUncaughtExceptionHandler getAsyncUncaughtExceptionHandler() {
        return (throwable, method, params) -> {
            log.error("비동기 실행 오류 - 메서드: {}, 오류: {}",
                    method.getName(), throwable.getMessage(), throwable);
        };
    }
}
```

#### 이벤트 기반 처리

```java
// 이벤트 정의
public record OrderCompletedEvent(
        Long orderId,
        Long userId,
        BigDecimal totalAmount,
        LocalDateTime completedAt
) {}

// 이벤트 발행
@Service
@RequiredArgsConstructor
public class OrderService {
    private final ApplicationEventPublisher eventPublisher;

    @Transactional
    public void completeOrder(Long orderId) {
        Order order = findOrderOrThrow(orderId);
        order.complete();

        // 트랜잭션 커밋 후 이벤트 처리를 보장하려면
        // @TransactionalEventListener 사용
        eventPublisher.publishEvent(new OrderCompletedEvent(
                order.getId(), order.getUserId(),
                order.getTotalAmount(), LocalDateTime.now()));
    }
}

// 이벤트 리스너
@Slf4j
@Component
@RequiredArgsConstructor
public class OrderEventListener {

    private final NotificationService notificationService;
    private final PointService pointService;

    // 트랜잭션 커밋 후 실행 (기본값: AFTER_COMMIT)
    @TransactionalEventListener
    public void handleOrderCompleted(OrderCompletedEvent event) {
        log.info("주문 완료 이벤트 처리: orderId={}", event.orderId());
        notificationService.sendOrderCompletionNotice(event.userId());
    }

    // 비동기 + 트랜잭션 후 실행
    @Async
    @TransactionalEventListener
    public void handlePointAccumulation(OrderCompletedEvent event) {
        pointService.accumulate(event.userId(), event.totalAmount());
    }
}
```

### 모니터링

#### Actuator 설정

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health, info, metrics, prometheus, loggers, env
      base-path: /internal/actuator
  endpoint:
    health:
      show-details: when_authorized
      show-components: when_authorized
      probes:
        enabled: true    # Kubernetes liveness/readiness probes
    loggers:
      enabled: true      # 런타임 로그 레벨 변경 가능
  metrics:
    tags:
      application: ${spring.application.name}
    distribution:
      percentiles-histogram:
        http.server.requests: true
      sla:
        http.server.requests: 100ms, 500ms, 1s, 5s
  health:
    redis:
      enabled: true
    db:
      enabled: true
```

#### 커스텀 메트릭

```java
@Component
@RequiredArgsConstructor
public class OrderMetrics {

    private final MeterRegistry meterRegistry;

    // 카운터 - 주문 생성 수
    public void incrementOrderCount(String status) {
        meterRegistry.counter("orders.created",
                "status", status).increment();
    }

    // 게이지 - 현재 처리 중인 주문 수
    private final AtomicInteger processingOrders = new AtomicInteger(0);

    @PostConstruct
    public void registerGauges() {
        meterRegistry.gauge("orders.processing",
                processingOrders);
    }

    // 타이머 - 주문 처리 시간 측정
    public void recordProcessingTime(long durationMs) {
        meterRegistry.timer("orders.processing.duration")
                .record(Duration.ofMillis(durationMs));
    }

    // 히스토그램 - 주문 금액 분포
    public void recordOrderAmount(double amount) {
        meterRegistry.summary("orders.amount").record(amount);
    }
}
```

### 데이터베이스 최적화

#### 인덱스 전략

```sql
-- 자주 검색되는 단일 컬럼 인덱스
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);

-- 복합 인덱스 (조건 순서: 카디널리티 높은 컬럼 우선)
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- 부분 인덱스 (조건부)
CREATE INDEX idx_users_active ON users(email)
    WHERE status = 'ACTIVE' AND deleted = false;

-- 커버링 인덱스 (SELECT 절 컬럼 포함)
CREATE INDEX idx_users_cover ON users(email, name, status);
```

#### Entity 인덱스 선언

```java
@Entity
@Table(name = "orders",
        indexes = {
                @Index(name = "idx_orders_user_id", columnList = "user_id"),
                @Index(name = "idx_orders_status_created",
                        columnList = "status, created_at DESC"),
                @Index(name = "idx_orders_order_number",
                        columnList = "order_number", unique = true)
        })
public class Order extends BaseEntity { ... }
```

---

## 6. 주의사항 / Gotchas

### 순환 참조

```java
// 문제: 두 서비스가 서로 의존
@Service
@RequiredArgsConstructor
public class UserService {
    private final OrderService orderService;  // UserService -> OrderService
}

@Service
@RequiredArgsConstructor
public class OrderService {
    private final UserService userService;    // OrderService -> UserService
}
// 결과: BeanCurrentlyInCreationException

// 해결 1: 설계 개선 - 공통 로직을 별도 서비스로 분리
// 해결 2: 이벤트 기반으로 의존성 제거
// 해결 3 (임시): @Lazy 사용 (근본 해결 아님)
```

### 트랜잭션 전파 주의사항

```java
@Service
public class UserService {

    @Transactional
    public void createUser(CreateUserRequest request) {
        saveUser(request);            // 같은 클래스 내부 호출
        sendWelcomeEmail(request);    // @Transactional이 적용되지 않음!
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void sendWelcomeEmail(CreateUserRequest request) {
        // 이 메서드의 @Transactional은 무시됨
        // 이유: Spring AOP 프록시는 외부 호출에만 적용
    }
}

// 해결: 별도 서비스로 분리하거나 self-injection 사용
@Service
@RequiredArgsConstructor
public class UserService {
    private final EmailService emailService;  // 별도 서비스

    @Transactional
    public void createUser(CreateUserRequest request) {
        saveUser(request);
        emailService.sendWelcomeEmail(request);  // 프록시를 통한 외부 호출
    }
}
```

### Entity 직접 반환 금지

```java
// 위험: 양방향 연관관계에서 무한 재귀 (StackOverflowError)
@GetMapping("/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).orElseThrow();  // Entity 직접 반환!
}

// 해결: 반드시 DTO 변환 후 반환
@GetMapping("/{id}")
public ApiResponse<UserResponse> getUser(@PathVariable Long id) {
    return ApiResponse.ok(userService.findById(id));   // DTO 반환
}

// 추가 위험: Entity 직접 반환 시 민감 정보(password) 노출
// 추가 위험: LazyInitializationException 발생 가능
```

### LocalDateTime vs ZonedDateTime

```java
// LocalDateTime: 타임존 정보 없음 - 서버 타임존에 의존
// ZonedDateTime: 타임존 정보 포함 - 글로벌 서비스에 적합

// 권장: 서버/DB는 UTC 기준, 클라이언트 응답 시 타임존 변환
// application.yml
spring:
  jackson:
    time-zone: UTC
    date-format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'

// JVM 타임존 설정 (main 메서드 또는 @PostConstruct)
@PostConstruct
public void init() {
    TimeZone.setDefault(TimeZone.getTimeZone("UTC"));
}
```

### LazyInitializationException

```java
// 문제: 트랜잭션 종료 후 지연 로딩 컬렉션 접근
User user = userRepository.findById(1L).orElseThrow();
// 트랜잭션 종료
user.getRoles().size();  // LazyInitializationException!

// 해결 1: JOIN FETCH 또는 @EntityGraph 사용
// 해결 2: DTO 변환을 트랜잭션 내에서 수행
// 해결 3: spring.jpa.open-in-view=false 설정 (권장)

// Open Session in View (OSIV) 비활성화 권장
spring:
  jpa:
    open-in-view: false  # 컨트롤러까지 영속성 컨텍스트 확장 방지
```

### Hibernate ddl-auto 위험

```yaml
spring:
  jpa:
    hibernate:
      ddl-auto: none  # 운영 환경 필수!

# 각 옵션의 위험도:
# none:          스키마 변경 없음 (운영 환경 필수)
# validate:      스키마 검증만 수행 (운영 환경 가능)
# update:        스키마 변경 반영 (개발만, 컬럼 삭제 안 됨)
# create:        매번 새로 생성 (데이터 유실!)
# create-drop:   종료 시 삭제 (테스트용)

# 운영 환경에서는 Flyway 또는 Liquibase로 스키마 마이그레이션 관리
```

### N+1 감지 방법

```yaml
# 1. Hibernate 쿼리 로그 활성화 (개발 환경)
spring:
  jpa:
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        # 쿼리 통계 (개발 환경만)
        generate_statistics: true

# 2. p6spy 사용 (쿼리 파라미터 포함 로깅)
# 3. 로그에서 동일 쿼리 반복 패턴 확인

logging:
  level:
    org.hibernate.SQL: DEBUG               # 쿼리 출력
    org.hibernate.orm.jdbc.bind: TRACE     # 바인딩 파라미터
```

### @Transactional readOnly 오용

```java
// 잘못된 사용: readOnly 트랜잭션에서 데이터 변경 시도
@Transactional(readOnly = true)  // 클래스 레벨
public class UserService {

    // 이 메서드는 readOnly=true가 적용되어
    // 변경 감지가 동작하지 않을 수 있음!
    public void updateUser(Long id, UpdateUserRequest request) {
        User user = userRepository.findById(id).orElseThrow();
        user.updateProfile(request.name(), request.phoneNumber());
        // 변경이 DB에 반영되지 않을 수 있음
    }
}

// 올바른 사용: 쓰기 메서드에 @Transactional 명시
@Transactional(readOnly = true)  // 클래스 레벨: 읽기 기본
public class UserService {

    @Transactional   // 메서드 레벨: 쓰기 트랜잭션으로 오버라이드
    public void updateUser(Long id, UpdateUserRequest request) {
        // ...
    }
}
```

### Spring Boot 3.x 마이그레이션 (javax -> jakarta)

```java
// Spring Boot 2.x (javax)
import javax.persistence.Entity;
import javax.validation.constraints.NotBlank;
import javax.servlet.http.HttpServletRequest;

// Spring Boot 3.x (jakarta) - 전체 변경 필요
import jakarta.persistence.Entity;
import jakarta.validation.constraints.NotBlank;
import jakarta.servlet.http.HttpServletRequest;

// WebSecurityConfigurerAdapter 제거됨
// Before (2.x):
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter { }

// After (3.x): SecurityFilterChain Bean 등록 방식
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http.build();
    }
}
```

### Jackson 직렬화 이슈

```java
// LocalDateTime 직렬화 설정
@Configuration
public class JacksonConfig {

    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
        mapper.setTimeZone(TimeZone.getTimeZone("UTC"));
        // Hibernate 프록시 직렬화 지원
        mapper.registerModule(new Hibernate6Module());
        return mapper;
    }
}

// Enum 직렬화: @JsonValue / @JsonCreator
public enum UserStatus {
    ACTIVE("active"),
    INACTIVE("inactive");

    private final String value;

    @JsonValue
    public String getValue() { return value; }

    @JsonCreator
    public static UserStatus from(String value) {
        return Arrays.stream(values())
                .filter(s -> s.value.equals(value))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException(
                        "Unknown status: " + value));
    }
}

// 순환 참조 방지: @JsonIgnore 또는 DTO 사용
@Entity
public class Order {
    @ManyToOne(fetch = FetchType.LAZY)
    @JsonIgnore  // Entity 직접 반환 시 (비권장이지만 필요한 경우)
    private User user;
}
```

### Bean 등록 충돌

```java
// 같은 타입 Bean이 여럿인 경우
@Bean
public RestTemplate internalRestTemplate() { ... }

@Bean
public RestTemplate externalRestTemplate() { ... }
// 결과: NoUniqueBeanDefinitionException

// 해결 1: @Primary
@Bean
@Primary
public RestTemplate internalRestTemplate() { ... }

// 해결 2: @Qualifier
@Bean("externalRestTemplate")
public RestTemplate externalRestTemplate() { ... }

@Service
public class ExternalApiClient {
    private final RestTemplate restTemplate;

    public ExternalApiClient(
            @Qualifier("externalRestTemplate") RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }
}
```

### 파일 업로드 설정

```yaml
spring:
  servlet:
    multipart:
      max-file-size: 10MB       # 단일 파일 최대 크기
      max-request-size: 50MB    # 전체 요청 최대 크기
      enabled: true

# Tomcat 설정 (Spring Boot 내장 Tomcat)
server:
  tomcat:
    max-http-form-post-size: 50MB
    max-swallow-size: 50MB
```

### CORS 문제 해결

```java
// SecurityFilterChain에서 CORS 설정이 WebConfig보다 우선
// Spring Security 사용 시 반드시 SecurityConfig에서 CORS 설정

// 흔한 실수: WebConfig에서만 CORS 설정 -> Spring Security에 의해 차단
// 올바른 방법: SecurityConfig에서 .cors() 설정 (위 SecurityConfig 참고)

// Preflight 요청 (OPTIONS) 허용 확인
// Spring Security에서 .cors() 설정 시 자동으로 OPTIONS 허용
```
