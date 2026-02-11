# CLAUDE.md - React 프로젝트 종합 가이드

## 프로젝트 개요

### 기술 스택

- **프레임워크**: React 18.3+ (Concurrent Features 활성화)
- **언어**: TypeScript 5.4+, strict mode 필수
- **빌드 도구**: Vite 5.4+ (SWC 플러그인 사용)
- **패키지 매니저**: pnpm 9+ (workspace 프로토콜 지원)
- **Node.js**: 20 LTS 이상 (`.nvmrc` 파일로 버전 고정)
- **라우팅**: React Router v6.20+
- **서버 상태**: TanStack Query v5
- **클라이언트 상태**: Zustand v4
- **폼 관리**: React Hook Form v7 + Zod v3
- **테스트**: Vitest 1.x + React Testing Library 14+ + MSW 2.x + Playwright 1.40+
- **린팅**: ESLint 9 (Flat Config) + Prettier 3
- **CI**: GitHub Actions

### 프로젝트 구조 상세 트리

```
project-root/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD
│       ├── ci.yml           # PR 검증 (lint, type-check, test, build)
│       └── deploy.yml       # 배포 파이프라인
├── .husky/                  # Git hooks (pre-commit, commit-msg)
├── public/
│   ├── favicon.ico
│   └── robots.txt
├── src/
│   ├── app/                 # 앱 진입점 및 프로바이더
│   │   ├── App.tsx          # 루트 컴포넌트, 라우터 연결
│   │   ├── providers.tsx    # 전역 프로바이더 구성
│   │   └── router.tsx       # React Router 설정
│   ├── components/          # 공통 UI 컴포넌트
│   │   ├── ui/              # 기본 UI (Button, Input, Modal 등)
│   │   ├── layout/          # 레이아웃 (Header, Footer, Sidebar)
│   │   └── feedback/        # 피드백 (Toast, Spinner, ErrorFallback)
│   ├── features/            # 도메인별 기능 모듈
│   │   ├── auth/            # 인증 기능
│   │   ├── users/           # 사용자 관리
│   │   └── dashboard/       # 대시보드
│   ├── hooks/               # 공통 커스텀 훅
│   ├── services/            # API 클라이언트 및 외부 서비스
│   │   ├── api.ts           # axios 인스턴스 설정
│   │   └── queryClient.ts   # TanStack Query 클라이언트
│   ├── stores/              # Zustand 전역 스토어
│   ├── types/               # 공유 타입 정의
│   ├── utils/               # 유틸리티 함수
│   ├── constants/           # 전역 상수
│   ├── styles/              # 전역 스타일
│   └── main.tsx             # 앱 엔트리포인트
├── tests/                   # 테스트 설정 및 유틸리티
│   ├── setup.ts             # Vitest 글로벌 설정
│   ├── utils.tsx            # 테스트 유틸 (custom render 등)
│   └── mocks/               # MSW 핸들러
├── e2e/                     # Playwright E2E 테스트
├── .env.example             # 환경 변수 템플릿
├── .eslintrc.cjs            # ESLint 설정
├── .prettierrc              # Prettier 설정
├── index.html               # HTML 엔트리
├── tsconfig.json            # TypeScript 설정
├── tsconfig.node.json       # Node.js용 TS 설정
├── vite.config.ts           # Vite 설정
├── vitest.config.ts         # Vitest 설정
├── playwright.config.ts     # Playwright 설정
└── package.json
```

### vite.config.ts 핵심 설정

```ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  plugins: [react(), tsconfigPaths()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
  build: {
    target: 'es2022',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom'],
          query: ['@tanstack/react-query'],
        },
      },
    },
  },
});
```

### tsconfig.json 핵심 설정

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2023", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "exactOptionalPropertyTypes": false,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src", "tests"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

### 브라우저 지원 범위

- Chrome 90+, Firefox 90+, Safari 15+, Edge 90+
- IE 미지원, 모바일 브라우저 최신 2개 버전 지원
- `browserslist` 설정: `">0.2%, not dead, not op_mini all"`

---

## 코딩 컨벤션

### 네이밍 규칙

#### 파일 네이밍

| 대상 | 규칙 | 예시 |
|---|---|---|
| 컴포넌트 파일 | PascalCase | `UserProfile.tsx`, `LoginForm.tsx` |
| 훅 파일 | camelCase, `use` 접두사 | `useAuth.ts`, `usePagination.ts` |
| 유틸리티 파일 | camelCase | `formatDate.ts`, `parseQuery.ts` |
| 상수 파일 | camelCase | `apiEndpoints.ts`, `errorMessages.ts` |
| 타입 파일 | camelCase | `user.types.ts` 또는 `types.ts` |
| 테스트 파일 | 원본 파일명 + `.test` | `UserProfile.test.tsx` |
| 스토리 파일 | 원본 파일명 + `.stories` | `Button.stories.tsx` |
| 스타일 파일 | 원본 파일명 + `.module` | `UserProfile.module.css` |
| 배럴 파일 | `index.ts` | 각 feature 디렉토리의 `index.ts` |

#### 변수 및 함수 네이밍

```tsx
// 변수: camelCase
const userName = 'Kim';
const isAuthenticated = true;
const itemCount = 42;

// 함수: camelCase, 동사로 시작
function fetchUserData(id: string): Promise<User> { ... }
function calculateTotalPrice(items: CartItem[]): number { ... }
function formatCurrency(amount: number): string { ... }

// 컴포넌트: PascalCase, 명사 또는 명사구
function UserProfile({ userId }: UserProfileProps) { ... }
function SearchResultList({ results }: SearchResultListProps) { ... }

// 훅: camelCase, use 접두사 + 명사/동사
function useAuth(): AuthState { ... }
function useDebounce<T>(value: T, delay: number): T { ... }
function usePagination(options: PaginationOptions): PaginationResult { ... }

// 상수: UPPER_SNAKE_CASE
const API_BASE_URL = '/api/v1';
const MAX_RETRY_COUNT = 3;
const DEFAULT_PAGE_SIZE = 20;
const CACHE_DURATION_MS = 5 * 60 * 1000;

// 이벤트 핸들러: handle 접두사 + 이벤트 대상 + 동사
function handleSubmit(e: FormEvent<HTMLFormElement>) { ... }
function handleUserDelete(userId: string) { ... }
function handleSearchInputChange(value: string) { ... }
function handleModalClose() { ... }

// Props 콜백: on 접두사 + 이벤트
interface ModalProps {
  onClose: () => void;
  onConfirm: (data: FormData) => void;
  onChange?: (value: string) => void;
}

// boolean 변수: is/has/should/can/will 접두사
const isLoading = true;
const hasPermission = false;
const shouldRefetch = true;
const canEdit = user.role === 'admin';
const willRedirect = status === 'success';

// 타입/인터페이스: PascalCase, I 접두사 금지
type UserId = string;
interface User { id: UserId; name: string; }
interface CreateUserRequest { name: string; email: string; }
interface UserListResponse { users: User[]; total: number; }

// 제네릭 타입 파라미터: 설명적 이름 사용
type ApiResponse<TData> = { data: TData; status: number; };
type FormFieldProps<TValue> = { value: TValue; onChange: (v: TValue) => void; };

// enum: PascalCase (멤버도 PascalCase), 가능하면 const object 선호
const UserRole = {
  Admin: 'admin',
  Editor: 'editor',
  Viewer: 'viewer',
} as const;
type UserRole = (typeof UserRole)[keyof typeof UserRole];
```

### 디렉토리 구조 상세 (Feature 기반)

```
src/features/auth/
├── components/               # 인증 관련 UI 컴포넌트
│   ├── LoginForm.tsx          # 로그인 폼 컴포넌트
│   ├── LoginForm.test.tsx     # 로그인 폼 테스트
│   ├── RegisterForm.tsx       # 회원가입 폼
│   ├── ProtectedRoute.tsx     # 인증 라우트 가드
│   └── RoleGuard.tsx          # 역할 기반 접근 제어
├── hooks/                     # 인증 관련 커스텀 훅
│   ├── useAuth.ts             # 인증 상태 관리
│   ├── useLogin.ts            # 로그인 mutation
│   └── useLogout.ts           # 로그아웃 mutation
├── api.ts                     # 인증 API 호출 함수
├── types.ts                   # 인증 관련 타입 정의
├── constants.ts               # 인증 관련 상수
├── utils.ts                   # 인증 유틸 (토큰 파싱 등)
└── index.ts                   # barrel export (public API)
```

**index.ts 규칙**: 외부에서 접근해야 하는 것만 export한다.

```ts
// features/auth/index.ts
export { LoginForm } from './components/LoginForm';
export { ProtectedRoute } from './components/ProtectedRoute';
export { useAuth } from './hooks/useAuth';
export type { AuthUser, LoginCredentials } from './types';
```

### import 순서 및 정리 규칙

```tsx
// 1. React 및 React 관련 (react, react-dom)
import { useState, useEffect, useCallback } from 'react';

// 2. 외부 라이브러리 (알파벳순)
import { useQuery, useMutation } from '@tanstack/react-query';
import { useForm } from 'react-hook-form';
import { useNavigate, useParams } from 'react-router-dom';
import { z } from 'zod';

// 3. 내부 모듈 - 절대 경로 (@/ 사용)
import { Button, Input } from '@/components/ui';
import { useAuth } from '@/features/auth';
import { api } from '@/services/api';
import { formatDate } from '@/utils/formatDate';

// 4. 타입 import (import type 사용)
import type { User, CreateUserRequest } from '@/types/user';
import type { ApiResponse } from '@/types/api';

// 5. 상대 경로 import (같은 feature 내부)
import { UserAvatar } from './UserAvatar';
import { useUserActions } from '../hooks/useUserActions';

// 6. 스타일/에셋 (최하단)
import styles from './UserProfile.module.css';
import heroImage from '@/assets/hero.webp';
```

**규칙**:
- `import type`은 반드시 타입 전용 import에 사용 (verbatimModuleSyntax 준수)
- 사용하지 않는 import는 즉시 제거
- 와일드카드 import(`import * as`) 지양, 필요한 것만 named import
- 순환 의존성(circular dependency) 금지 - feature 간 의존은 barrel export를 통해서만

### 에러 핸들링 패턴

#### Error Boundary 계층 구조

```tsx
// 최상위 Error Boundary - 전체 앱 감싸기
function AppErrorFallback({ error, resetErrorBoundary }: FallbackProps) {
  return (
    <div role="alert">
      <h2>예기치 않은 오류가 발생했습니다</h2>
      <pre>{error.message}</pre>
      <button onClick={resetErrorBoundary}>다시 시도</button>
    </div>
  );
}

// app/providers.tsx
import { ErrorBoundary } from 'react-error-boundary';

function AppProviders({ children }: PropsWithChildren) {
  return (
    <ErrorBoundary FallbackComponent={AppErrorFallback}>
      <QueryClientProvider client={queryClient}>
        {children}
      </QueryClientProvider>
    </ErrorBoundary>
  );
}
```

#### 라우트 레벨 Error Boundary

```tsx
// 각 라우트에 개별 Error Boundary 배치
const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <RouteErrorFallback />,
    children: [
      {
        path: 'dashboard',
        element: <Dashboard />,
        errorElement: <DashboardErrorFallback />,
      },
    ],
  },
]);
```

#### API 에러 처리 (TanStack Query)

```tsx
// 전역 에러 핸들러 설정
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: (failureCount, error) => {
        if (error instanceof ApiError && error.status === 404) return false;
        return failureCount < 3;
      },
      throwOnError: (error) => {
        // 5xx 에러는 Error Boundary로 전파
        return error instanceof ApiError && error.status >= 500;
      },
    },
    mutations: {
      onError: (error) => {
        if (error instanceof ApiError && error.status !== 401) {
          toast.error(error.userMessage);
        }
      },
    },
  },
});
```

#### 에러 타입 정의

```tsx
class ApiError extends Error {
  constructor(
    public status: number,
    public userMessage: string,
    public code?: string,
    cause?: unknown,
  ) {
    super(userMessage, { cause });
    this.name = 'ApiError';
  }
}

// API 클라이언트에서 에러 변환
api.interceptors.response.use(
  (response) => response,
  (error: AxiosError<{ message: string; code?: string }>) => {
    const status = error.response?.status ?? 500;
    const message = error.response?.data?.message ?? '알 수 없는 오류가 발생했습니다';
    const code = error.response?.data?.code;
    throw new ApiError(status, message, code, error);
  },
);
```

### 컴포넌트 코드 구조 (함수 내부 작성 순서)

```tsx
function UserProfile({ userId, onUpdate }: UserProfileProps) {
  // 1. 외부 훅 (라우터, 스토어, 쿼리)
  const navigate = useNavigate();
  const { data: user, isLoading } = useUser(userId);
  const theme = useThemeStore((s) => s.theme);

  // 2. 로컬 상태 (useState, useReducer)
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState<UserFormData | null>(null);

  // 3. Ref
  const inputRef = useRef<HTMLInputElement>(null);

  // 4. 파생 값 (계산된 값, useMemo)
  const fullName = user ? `${user.firstName} ${user.lastName}` : '';
  const isAdmin = user?.role === 'admin';
  const sortedPosts = useMemo(
    () => user?.posts.toSorted((a, b) => b.createdAt - a.createdAt),
    [user?.posts],
  );

  // 5. 이벤트 핸들러 및 콜백
  const handleEdit = useCallback(() => {
    setIsEditing(true);
    setFormData({ name: user?.name ?? '', email: user?.email ?? '' });
  }, [user]);

  const handleSave = useCallback(async () => {
    if (!formData) return;
    await onUpdate(formData);
    setIsEditing(false);
  }, [formData, onUpdate]);

  // 6. 사이드 이펙트 (useEffect)
  useEffect(() => {
    if (isEditing) {
      inputRef.current?.focus();
    }
  }, [isEditing]);

  // 7. 조기 반환 (로딩, 에러 상태)
  if (isLoading) return <Spinner />;
  if (!user) return <NotFound message="사용자를 찾을 수 없습니다" />;

  // 8. JSX 렌더링
  return (
    <section className={styles.profile}>
      <h1>{fullName}</h1>
      {isEditing ? (
        <EditForm ref={inputRef} data={formData} onSave={handleSave} />
      ) : (
        <ProfileView user={user} onEdit={handleEdit} />
      )}
    </section>
  );
}
```

### TypeScript 활용 패턴

#### Props 타입 정의

```tsx
// 기본 Props - interface 사용
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  children: ReactNode;
  onClick?: () => void;
}

// HTML 속성 확장
interface InputProps extends Omit<ComponentPropsWithoutRef<'input'>, 'size'> {
  label: string;
  error?: string;
  size?: 'sm' | 'md' | 'lg';
}

// children 포함 패턴
interface LayoutProps {
  children: ReactNode;
  sidebar?: ReactNode;
  header?: ReactNode;
}

// React.FC 사용 금지 - 일반 함수 선언 사용
// BAD
const Button: React.FC<ButtonProps> = ({ children }) => { ... };

// GOOD
function Button({ variant = 'primary', size = 'md', children, ...rest }: ButtonProps) {
  return <button className={clsx(styles.btn, styles[variant], styles[size])} {...rest}>{children}</button>;
}
```

#### 제네릭 컴포넌트

```tsx
// 제네릭 Select 컴포넌트
interface SelectProps<TValue extends string | number> {
  options: Array<{ label: string; value: TValue }>;
  value: TValue;
  onChange: (value: TValue) => void;
  placeholder?: string;
}

function Select<TValue extends string | number>({
  options,
  value,
  onChange,
  placeholder,
}: SelectProps<TValue>) {
  return (
    <select
      value={value}
      onChange={(e) => onChange(e.target.value as TValue)}
    >
      {placeholder && <option value="">{placeholder}</option>}
      {options.map((opt) => (
        <option key={opt.value} value={opt.value}>
          {opt.label}
        </option>
      ))}
    </select>
  );
}

// 제네릭 List 컴포넌트
interface ListProps<TItem> {
  items: TItem[];
  renderItem: (item: TItem, index: number) => ReactNode;
  keyExtractor: (item: TItem) => string;
  emptyMessage?: string;
}

function List<TItem>({ items, renderItem, keyExtractor, emptyMessage }: ListProps<TItem>) {
  if (items.length === 0) return <p>{emptyMessage ?? '데이터가 없습니다'}</p>;
  return (
    <ul>
      {items.map((item, i) => (
        <li key={keyExtractor(item)}>{renderItem(item, i)}</li>
      ))}
    </ul>
  );
}
```

#### 유틸리티 타입 활용

```tsx
// Pick, Omit 활용
type UserSummary = Pick<User, 'id' | 'name' | 'avatar'>;
type CreateUserInput = Omit<User, 'id' | 'createdAt' | 'updatedAt'>;

// Partial을 활용한 업데이트 타입
type UpdateUserInput = Partial<Pick<User, 'name' | 'email' | 'avatar'>>;

// Record 활용
type UserStatusMap = Record<UserStatus, { label: string; color: string }>;

// Extract, Exclude 활용
type WritableRole = Exclude<UserRole, 'viewer'>;
type AdminRole = Extract<UserRole, 'admin' | 'superAdmin'>;

// 타입 가드
function isApiError(error: unknown): error is ApiError {
  return error instanceof ApiError;
}

function isUser(data: unknown): data is User {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data &&
    'name' in data &&
    typeof (data as User).id === 'string'
  );
}

// Discriminated Union
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };
```

### CSS / 스타일링 컨벤션

#### CSS Modules 우선 사용

```tsx
// UserProfile.module.css
.container {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-text-primary);
}

// UserProfile.tsx
import styles from './UserProfile.module.css';
import clsx from 'clsx';

function UserProfile({ isActive }: UserProfileProps) {
  return (
    <div className={clsx(styles.container, isActive && styles.active)}>
      <h1 className={styles.title}>프로필</h1>
    </div>
  );
}
```

#### Tailwind CSS 사용 시

```tsx
// clsx 또는 tailwind-merge 활용
import { twMerge } from 'tailwind-merge';
import clsx from 'clsx';

// 유틸리티 함수
function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// 컴포넌트에서 사용
function Button({ variant, className, children }: ButtonProps) {
  return (
    <button
      className={cn(
        'rounded-lg px-4 py-2 font-medium transition-colors',
        variant === 'primary' && 'bg-blue-600 text-white hover:bg-blue-700',
        variant === 'secondary' && 'bg-gray-200 text-gray-800 hover:bg-gray-300',
        className,
      )}
    >
      {children}
    </button>
  );
}
```

### JSX 패턴

#### 조건부 렌더링

```tsx
// 삼항 연산자: 두 가지 상태 모두 렌더링할 때
{isEditing ? <EditForm /> : <DisplayView />}

// && 연산자: 조건부로 하나만 렌더링할 때
// 주의: 0이나 '' 같은 falsy 값은 렌더링될 수 있음
{items.length > 0 && <ItemList items={items} />}  // GOOD
{count && <Badge count={count} />}                  // BAD: count=0일 때 0이 렌더링됨
{count > 0 && <Badge count={count} />}              // GOOD

// 복잡한 조건: 변수로 분리하거나 즉시 반환
const content = (() => {
  if (isLoading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  if (!data) return <EmptyState />;
  return <DataView data={data} />;
})();
```

#### 리스트 렌더링

```tsx
// key는 반드시 고유한 식별자 사용 (배열 인덱스 금지)
{users.map((user) => (
  <UserCard key={user.id} user={user} />
))}

// Fragment로 감싸야 할 때 key 전달
{items.map((item) => (
  <Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.definition}</dd>
  </Fragment>
))}
```

### 주석 / 문서화 규칙

```tsx
// 왜(why) 이 코드가 필요한지만 주석 작성 - 무엇(what)은 코드로 표현
// BAD: 사용자를 가져온다
const user = await fetchUser(id);

// GOOD: 프로필 수정 후 최신 데이터로 캐시를 갱신하기 위해 다시 조회
const user = await fetchUser(id);

// TODO 주석 형식
// TODO(담당자): 설명 - #이슈번호

// JSDoc은 공개 API(라이브러리, 공용 유틸)에만 작성
/**
 * 통화 금액을 한국 원화 형식으로 포맷팅
 * @example formatCurrency(15000) => "15,000원"
 */
function formatCurrency(amount: number): string { ... }
```

---

## 보안 필수사항

### XSS(Cross-Site Scripting) 방지

#### React의 기본 이스케이핑

React는 JSX에서 문자열을 렌더링할 때 자동으로 HTML 엔티티를 이스케이핑한다. 이 기본 보호를 우회하지 않도록 주의한다.

```tsx
// React가 자동으로 이스케이핑 - 안전
<p>{userInput}</p>
// userInput이 "<script>alert('xss')</script>"여도 텍스트로 렌더링됨

// 위험: 이스케이핑을 우회하는 패턴들
// 1. dangerouslySetInnerHTML - 절대 사용 금지 (아래 대체 방법 참고)
<div dangerouslySetInnerHTML={{ __html: userInput }} /> // NEVER

// 2. DOM API 직접 사용 금지
ref.current.innerHTML = userInput; // NEVER
document.getElementById('root').innerHTML = data; // NEVER
```

#### dangerouslySetInnerHTML 대체 방법

서버에서 HTML을 받아 렌더링해야 하는 경우 (블로그, CMS 등):

```tsx
// 방법 1: DOMPurify로 sanitize (불가피한 경우에만)
import DOMPurify from 'dompurify';

// DOMPurify 설정 - 허용할 태그와 속성을 최소한으로 제한
const SANITIZE_CONFIG: DOMPurify.Config = {
  ALLOWED_TAGS: ['p', 'br', 'strong', 'em', 'ul', 'ol', 'li', 'a', 'h1', 'h2', 'h3', 'blockquote', 'code', 'pre'],
  ALLOWED_ATTR: ['href', 'target', 'rel', 'class'],
  ALLOW_DATA_ATTR: false,
  ADD_ATTR: ['target'],
  FORBID_TAGS: ['script', 'style', 'iframe', 'form', 'input', 'object', 'embed'],
  FORBID_ATTR: ['onerror', 'onload', 'onclick', 'onmouseover', 'onfocus', 'onblur'],
};

// 안전한 HTML 렌더링 컴포넌트
function SafeHTML({ html, className }: { html: string; className?: string }) {
  const sanitized = DOMPurify.sanitize(html, SANITIZE_CONFIG);
  return <div className={className} dangerouslySetInnerHTML={{ __html: sanitized }} />;
}

// 모든 링크에 rel="noopener noreferrer" 자동 추가
DOMPurify.addHook('afterSanitizeAttributes', (node) => {
  if (node.tagName === 'A') {
    node.setAttribute('target', '_blank');
    node.setAttribute('rel', 'noopener noreferrer');
  }
});

// 방법 2: 마크다운 파서 사용 (더 안전)
import { marked } from 'marked';
import DOMPurify from 'dompurify';

function MarkdownContent({ markdown }: { markdown: string }) {
  const html = marked.parse(markdown, { breaks: true });
  const clean = DOMPurify.sanitize(html, SANITIZE_CONFIG);
  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}

// 방법 3: 구조화된 데이터로 변환 (가장 안전)
// 서버에서 HTML 대신 구조화된 JSON을 반환하도록 API 설계
interface ContentBlock {
  type: 'paragraph' | 'heading' | 'list' | 'code';
  content: string;
  level?: number;
  items?: string[];
}

function StructuredContent({ blocks }: { blocks: ContentBlock[] }) {
  return (
    <article>
      {blocks.map((block, i) => {
        switch (block.type) {
          case 'heading':
            const Tag = `h${block.level ?? 2}` as keyof JSX.IntrinsicElements;
            return <Tag key={i}>{block.content}</Tag>;
          case 'paragraph':
            return <p key={i}>{block.content}</p>;
          case 'list':
            return (
              <ul key={i}>
                {block.items?.map((item, j) => <li key={j}>{item}</li>)}
              </ul>
            );
          case 'code':
            return <pre key={i}><code>{block.content}</code></pre>;
          default:
            return null;
        }
      })}
    </article>
  );
}
```

#### URL 검증 - javascript: 프로토콜 차단

```tsx
// URL 안전성 검증 유틸리티
function isSafeUrl(url: string): boolean {
  if (!url) return false;
  try {
    const parsed = new URL(url, window.location.origin);
    return ['http:', 'https:', 'mailto:', 'tel:'].includes(parsed.protocol);
  } catch {
    return false;
  }
}

// 안전한 href 생성
function getSafeHref(url: string): string {
  return isSafeUrl(url) ? url : '#';
}

// 컴포넌트에서 사용
function SafeLink({ href, children, ...rest }: AnchorHTMLAttributes<HTMLAnchorElement>) {
  const safeHref = getSafeHref(href ?? '');
  const isExternal = safeHref.startsWith('http');

  return (
    <a
      href={safeHref}
      {...(isExternal ? { target: '_blank', rel: 'noopener noreferrer' } : {})}
      {...rest}
    >
      {children}
    </a>
  );
}

// BAD 패턴들 - 절대 금지
<a href={userProvidedUrl}>클릭</a>           // XSS 위험
<img src={userProvidedUrl} />                 // 악성 URL 가능
<iframe src={userProvidedUrl} />              // 절대 금지
```

#### Content Security Policy 설정

```html
<!-- index.html - 개발 환경 -->
<meta
  http-equiv="Content-Security-Policy"
  content="
    default-src 'self';
    script-src 'self';
    style-src 'self' 'unsafe-inline';
    img-src 'self' data: https:;
    font-src 'self';
    connect-src 'self' http://localhost:* ws://localhost:*;
    frame-src 'none';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
  "
/>
```

프로덕션에서는 서버 HTTP 헤더로 CSP를 설정하고, nonce 기반 인라인 스크립트를 사용한다.

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-{SERVER_GENERATED_NONCE}';
  style-src 'self' 'nonce-{SERVER_GENERATED_NONCE}';
  img-src 'self' data: https://cdn.example.com;
  connect-src 'self' https://api.example.com;
  frame-ancestors 'none';
  form-action 'self';
  upgrade-insecure-requests;
```

#### 서드파티 라이브러리 XSS 위험

```tsx
// 위험: 사용자 입력을 HTML로 렌더링하는 서드파티 컴포넌트
// 항상 sanitize 후 전달
import ReactMarkdown from 'react-markdown';
import rehypeSanitize from 'rehype-sanitize';

<ReactMarkdown rehypePlugins={[rehypeSanitize]}>
  {userContent}
</ReactMarkdown>

// 위험: 차트 라이브러리에 사용자 입력을 라벨로 전달
// 반드시 텍스트 전용 렌더러 사용 확인
```

### CSRF(Cross-Site Request Forgery) 방지

#### axios 인터셉터 전체 설정

```tsx
// services/api.ts
import axios, { type InternalAxiosRequestConfig } from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? '/api',
  timeout: 30_000,
  withCredentials: true, // 쿠키 전송 활성화
  headers: {
    'Content-Type': 'application/json',
  },
});

// CSRF 토큰 요청 인터셉터
api.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  // 상태 변경 요청에만 CSRF 토큰 추가
  const methodsRequiringCsrf = ['post', 'put', 'patch', 'delete'];
  if (methodsRequiringCsrf.includes(config.method ?? '')) {
    // 쿠키에서 CSRF 토큰 읽기 (서버가 Set-Cookie로 설정)
    const csrfToken = getCookie('XSRF-TOKEN');
    if (csrfToken) {
      config.headers.set('X-XSRF-TOKEN', csrfToken);
    }
  }
  return config;
});

function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp(`(^| )${name}=([^;]+)`));
  return match ? decodeURIComponent(match[2]) : null;
}

export { api };
```

#### SameSite 쿠키 설정

서버에서 설정하지만, 프론트엔드 개발자도 이해해야 하는 설정:

```
Set-Cookie: session=abc123; SameSite=Lax; Secure; HttpOnly; Path=/; Max-Age=86400
Set-Cookie: XSRF-TOKEN=xyz789; SameSite=Lax; Secure; Path=/
```

- `SameSite=Lax`: GET 이외의 크로스사이트 요청에서 쿠키 전송 차단
- `SameSite=Strict`: 모든 크로스사이트 요청에서 쿠키 전송 차단
- CSRF 토큰 쿠키는 `HttpOnly` 없이 설정 (JS에서 읽어야 하므로)
- 세션 쿠키는 반드시 `HttpOnly` 설정

### 인증/인가 상세

#### JWT 토큰 관리 전략

```
규칙: JWT는 반드시 httpOnly 쿠키에 저장한다.
- localStorage/sessionStorage 저장 금지 (XSS로 탈취 가능)
- 메모리(변수)에만 저장하면 새로고침 시 사라짐
- httpOnly 쿠키: XSS로 접근 불가, 자동 전송
```

#### 토큰 갱신 플로우 전체 구현

```tsx
// services/api.ts
import axios, { type AxiosError, type InternalAxiosRequestConfig } from 'axios';

interface FailedRequest {
  resolve: (token: string) => void;
  reject: (error: unknown) => void;
}

let isRefreshing = false;
let failedQueue: FailedRequest[] = [];

function processQueue(error: unknown) {
  failedQueue.forEach((promise) => {
    if (error) {
      promise.reject(error);
    } else {
      promise.resolve('');
    }
  });
  failedQueue = [];
}

api.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config as InternalAxiosRequestConfig & { _retry?: boolean };

    // 401이고 아직 재시도하지 않은 요청
    if (error.response?.status === 401 && !originalRequest._retry) {
      // 이미 갱신 중이면 큐에 추가하고 대기
      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject });
        }).then(() => api(originalRequest));
      }

      originalRequest._retry = true;
      isRefreshing = true;

      try {
        // 리프레시 토큰으로 새 액세스 토큰 요청
        await axios.post('/api/auth/refresh', null, { withCredentials: true });
        processQueue(null);
        return api(originalRequest);
      } catch (refreshError) {
        processQueue(refreshError);
        // 리프레시도 실패하면 로그아웃 처리
        window.dispatchEvent(new CustomEvent('auth:expired'));
        return Promise.reject(refreshError);
      } finally {
        isRefreshing = false;
      }
    }

    return Promise.reject(error);
  },
);
```

#### ProtectedRoute 컴포넌트

```tsx
// features/auth/components/ProtectedRoute.tsx
import { Navigate, Outlet, useLocation } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

interface ProtectedRouteProps {
  allowedRoles?: string[];
  redirectTo?: string;
}

function ProtectedRoute({ allowedRoles, redirectTo = '/login' }: ProtectedRouteProps) {
  const { user, isLoading, isAuthenticated } = useAuth();
  const location = useLocation();

  if (isLoading) {
    return <FullPageSpinner />;
  }

  if (!isAuthenticated) {
    return <Navigate to={redirectTo} state={{ from: location }} replace />;
  }

  if (allowedRoles && user && !allowedRoles.includes(user.role)) {
    return <Navigate to="/forbidden" replace />;
  }

  return <Outlet />;
}
```

#### 역할 기반 접근 제어

```tsx
// features/auth/components/RoleGuard.tsx
interface RoleGuardProps {
  roles: string[];
  children: ReactNode;
  fallback?: ReactNode;
}

function RoleGuard({ roles, children, fallback = null }: RoleGuardProps) {
  const { user } = useAuth();
  if (!user || !roles.includes(user.role)) return <>{fallback}</>;
  return <>{children}</>;
}

// 사용 예시
<RoleGuard roles={['admin', 'editor']}>
  <DeleteButton onClick={handleDelete} />
</RoleGuard>

// 라우트에서 사용
const router = createBrowserRouter([
  {
    element: <ProtectedRoute />,
    children: [
      { path: '/dashboard', element: <Dashboard /> },
      {
        element: <ProtectedRoute allowedRoles={['admin']} />,
        children: [
          { path: '/admin', element: <AdminPanel /> },
        ],
      },
    ],
  },
]);
```

#### 세션 만료 처리

```tsx
// app/providers.tsx
function AuthExpirationHandler() {
  const navigate = useNavigate();
  const queryClient = useQueryClient();

  useEffect(() => {
    function handleExpired() {
      queryClient.clear();
      navigate('/login', { state: { message: '세션이 만료되었습니다. 다시 로그인해 주세요.' } });
    }

    window.addEventListener('auth:expired', handleExpired);
    return () => window.removeEventListener('auth:expired', handleExpired);
  }, [navigate, queryClient]);

  return null;
}
```

### 입력 검증 상세

#### Zod 스키마 정의 패턴

```tsx
import { z } from 'zod';

// 기본 검증 스키마
const loginSchema = z.object({
  email: z
    .string()
    .min(1, '이메일을 입력해 주세요')
    .email('올바른 이메일 형식이 아닙니다'),
  password: z
    .string()
    .min(8, '비밀번호는 8자 이상이어야 합니다')
    .regex(/[A-Z]/, '대문자를 포함해야 합니다')
    .regex(/[0-9]/, '숫자를 포함해야 합니다')
    .regex(/[^A-Za-z0-9]/, '특수문자를 포함해야 합니다'),
});

// 타입 추론
type LoginFormData = z.infer<typeof loginSchema>;

// 비밀번호 확인 등 cross-field 검증
const registerSchema = z
  .object({
    name: z.string().min(2, '이름은 2자 이상이어야 합니다').max(50),
    email: z.string().email('올바른 이메일 형식이 아닙니다'),
    password: z.string().min(8, '비밀번호는 8자 이상이어야 합니다'),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: '비밀번호가 일치하지 않습니다',
    path: ['confirmPassword'],
  });

// 서버 응답 검증
const userResponseSchema = z.object({
  id: z.string().uuid(),
  name: z.string(),
  email: z.string().email(),
  role: z.enum(['admin', 'editor', 'viewer']),
  createdAt: z.string().datetime(),
});

type User = z.infer<typeof userResponseSchema>;
```

#### React Hook Form + Zod 연동

```tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError,
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: '', password: '' },
  });

  const loginMutation = useLogin();

  const onSubmit = handleSubmit(async (data) => {
    try {
      await loginMutation.mutateAsync(data);
    } catch (error) {
      if (isApiError(error) && error.code === 'INVALID_CREDENTIALS') {
        setError('root', { message: '이메일 또는 비밀번호가 올바르지 않습니다' });
      }
    }
  });

  return (
    <form onSubmit={onSubmit} noValidate>
      <div>
        <label htmlFor="email">이메일</label>
        <input id="email" type="email" {...register('email')} aria-invalid={!!errors.email} />
        {errors.email && <p role="alert">{errors.email.message}</p>}
      </div>
      <div>
        <label htmlFor="password">비밀번호</label>
        <input id="password" type="password" {...register('password')} />
        {errors.password && <p role="alert">{errors.password.message}</p>}
      </div>
      {errors.root && <p role="alert">{errors.root.message}</p>}
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? '로그인 중...' : '로그인'}
      </button>
    </form>
  );
}
```

### 시크릿 관리

```
.env                  # 기본 값 (커밋 금지)
.env.local            # 로컬 오버라이드 (커밋 금지)
.env.development      # 개발 환경 (커밋 가능 - 비밀 정보 없이)
.env.production       # 프로덕션 환경 (커밋 가능 - 비밀 정보 없이)
.env.example          # 템플릿 (커밋 필수)

규칙:
- VITE_ 접두사가 있는 변수만 클라이언트에 노출됨
- API 키, 시크릿은 절대 VITE_ 접두사로 시작하면 안 됨
- VITE_API_BASE_URL 같은 공개 가능한 설정만 VITE_ 사용
- 민감한 API 키는 서버 사이드(BFF/프록시)에서 관리
```

```ts
// 환경 변수 타입 안전하게 접근
// src/env.d.ts
/// <reference types="vite/client" />
interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string;
  readonly VITE_APP_TITLE: string;
  readonly VITE_SENTRY_DSN?: string;
}
```

### 클라이언트 사이드 보안

```tsx
// eval() 사용 절대 금지
eval(userInput);                        // NEVER
new Function(userInput)();              // NEVER
setTimeout(userInput, 0);               // 문자열 전달 금지
setInterval(userInput, 1000);           // 문자열 전달 금지

// postMessage 검증
useEffect(() => {
  function handleMessage(event: MessageEvent) {
    // 반드시 origin 검증
    if (event.origin !== 'https://trusted-domain.com') return;
    // 데이터 구조 검증
    const result = messageSchema.safeParse(event.data);
    if (!result.success) return;
    // 안전하게 처리
    processMessage(result.data);
  }
  window.addEventListener('message', handleMessage);
  return () => window.removeEventListener('message', handleMessage);
}, []);

// iframe 보안
// 외부 iframe 삽입 방지 (서버 헤더)
// X-Frame-Options: DENY
// Content-Security-Policy: frame-ancestors 'none';

// iframe 사용이 필요한 경우
<iframe
  src="https://trusted-embed.com/widget"
  sandbox="allow-scripts allow-same-origin"
  referrerPolicy="no-referrer"
  loading="lazy"
  title="위젯 설명"
/>
```

### 의존성 보안

```bash
# 정기 취약점 검사
pnpm audit
pnpm audit --fix

# 프로덕션 의존성만 검사
pnpm audit --prod

# package.json에 허용 가능한 취약점 명시
# .npmrc에 audit-level=moderate 설정
```

Renovate 또는 Dependabot 설정으로 자동 업데이트 PR을 생성한다. 보안 패치는 자동 머지를 고려한다.

---

## 생산성 가이드

### 커스텀 훅 패턴 상세

#### useApi - API 호출 래퍼

```tsx
// hooks/useApi.ts
import { useMutation, useQuery, type UseMutationOptions, type UseQueryOptions } from '@tanstack/react-query';
import { api } from '@/services/api';
import type { ApiError } from '@/types/api';

function useApiQuery<TData>(
  queryKey: readonly unknown[],
  url: string,
  options?: Omit<UseQueryOptions<TData, ApiError>, 'queryKey' | 'queryFn'>,
) {
  return useQuery<TData, ApiError>({
    queryKey,
    queryFn: async ({ signal }) => {
      const { data } = await api.get<TData>(url, { signal });
      return data;
    },
    ...options,
  });
}

function useApiMutation<TData, TVariables>(
  method: 'post' | 'put' | 'patch' | 'delete',
  url: string | ((variables: TVariables) => string),
  options?: UseMutationOptions<TData, ApiError, TVariables>,
) {
  return useMutation<TData, ApiError, TVariables>({
    mutationFn: async (variables) => {
      const resolvedUrl = typeof url === 'function' ? url(variables) : url;
      const { data } = await api[method]<TData>(resolvedUrl, variables);
      return data;
    },
    ...options,
  });
}

export { useApiQuery, useApiMutation };
```

#### usePagination - 페이지네이션 전체 구현

```tsx
// hooks/usePagination.ts
import { useState, useMemo, useCallback } from 'react';

interface PaginationOptions {
  totalItems: number;
  initialPage?: number;
  pageSize?: number;
  siblingCount?: number;
}

interface PaginationResult {
  currentPage: number;
  pageSize: number;
  totalPages: number;
  startIndex: number;
  endIndex: number;
  hasPrevious: boolean;
  hasNext: boolean;
  pages: (number | 'ellipsis')[];
  goToPage: (page: number) => void;
  nextPage: () => void;
  previousPage: () => void;
  setPageSize: (size: number) => void;
}

function usePagination({
  totalItems,
  initialPage = 1,
  pageSize: initialPageSize = 20,
  siblingCount = 1,
}: PaginationOptions): PaginationResult {
  const [currentPage, setCurrentPage] = useState(initialPage);
  const [pageSize, setPageSizeState] = useState(initialPageSize);

  const totalPages = Math.max(1, Math.ceil(totalItems / pageSize));
  const safePage = Math.min(currentPage, totalPages);

  const startIndex = (safePage - 1) * pageSize;
  const endIndex = Math.min(startIndex + pageSize - 1, totalItems - 1);

  const pages = useMemo(() => {
    const range = (start: number, end: number) =>
      Array.from({ length: end - start + 1 }, (_, i) => start + i);

    const totalPageNumbers = siblingCount * 2 + 5;
    if (totalPageNumbers >= totalPages) return range(1, totalPages);

    const leftSibling = Math.max(safePage - siblingCount, 1);
    const rightSibling = Math.min(safePage + siblingCount, totalPages);
    const showLeftEllipsis = leftSibling > 2;
    const showRightEllipsis = rightSibling < totalPages - 1;

    const result: (number | 'ellipsis')[] = [];
    result.push(1);
    if (showLeftEllipsis) result.push('ellipsis');
    range(leftSibling, rightSibling).forEach((p) => { if (p !== 1 && p !== totalPages) result.push(p); });
    if (showRightEllipsis) result.push('ellipsis');
    if (totalPages > 1) result.push(totalPages);

    return result;
  }, [totalPages, safePage, siblingCount]);

  const goToPage = useCallback((page: number) => {
    setCurrentPage(Math.max(1, Math.min(page, totalPages)));
  }, [totalPages]);

  const nextPage = useCallback(() => goToPage(safePage + 1), [safePage, goToPage]);
  const previousPage = useCallback(() => goToPage(safePage - 1), [safePage, goToPage]);
  const setPageSize = useCallback((size: number) => {
    setPageSizeState(size);
    setCurrentPage(1);
  }, []);

  return {
    currentPage: safePage, pageSize, totalPages, startIndex, endIndex,
    hasPrevious: safePage > 1, hasNext: safePage < totalPages,
    pages, goToPage, nextPage, previousPage, setPageSize,
  };
}
```

#### useDebounce / useThrottle

```tsx
// hooks/useDebounce.ts
import { useState, useEffect } from 'react';

function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// hooks/useDebouncedCallback.ts
import { useCallback, useRef } from 'react';

function useDebouncedCallback<T extends (...args: never[]) => void>(
  callback: T,
  delay: number,
): T {
  const timeoutRef = useRef<ReturnType<typeof setTimeout>>();
  const callbackRef = useRef(callback);
  callbackRef.current = callback;

  return useCallback(
    ((...args: Parameters<T>) => {
      clearTimeout(timeoutRef.current);
      timeoutRef.current = setTimeout(() => callbackRef.current(...args), delay);
    }) as T,
    [delay],
  );
}
```

#### useIntersectionObserver

```tsx
// hooks/useIntersectionObserver.ts
import { useEffect, useRef, useState, type RefObject } from 'react';

interface UseIntersectionObserverOptions extends IntersectionObserverInit {
  freezeOnceVisible?: boolean;
}

function useIntersectionObserver<T extends HTMLElement = HTMLDivElement>(
  options: UseIntersectionObserverOptions = {},
): [RefObject<T | null>, IntersectionObserverEntry | null] {
  const { threshold = 0, root = null, rootMargin = '0px', freezeOnceVisible = false } = options;
  const ref = useRef<T | null>(null);
  const [entry, setEntry] = useState<IntersectionObserverEntry | null>(null);

  const frozen = entry?.isIntersecting && freezeOnceVisible;

  useEffect(() => {
    const node = ref.current;
    if (!node || frozen) return;

    const observer = new IntersectionObserver(
      ([observerEntry]) => setEntry(observerEntry),
      { threshold, root, rootMargin },
    );

    observer.observe(node);
    return () => observer.disconnect();
  }, [threshold, root, rootMargin, frozen]);

  return [ref, entry];
}
```

#### useLocalStorage

```tsx
// hooks/useLocalStorage.ts
import { useState, useCallback } from 'react';

function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? (JSON.parse(item) as T) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = useCallback(
    (value: T | ((prev: T) => T)) => {
      setStoredValue((prev) => {
        const valueToStore = value instanceof Function ? value(prev) : value;
        try {
          window.localStorage.setItem(key, JSON.stringify(valueToStore));
        } catch (error) {
          console.warn(`localStorage에 "${key}" 저장 실패:`, error);
        }
        return valueToStore;
      });
    },
    [key],
  );

  const removeValue = useCallback(() => {
    try {
      window.localStorage.removeItem(key);
      setStoredValue(initialValue);
    } catch (error) {
      console.warn(`localStorage에서 "${key}" 삭제 실패:`, error);
    }
  }, [key, initialValue]);

  return [storedValue, setValue, removeValue] as const;
}
```

### 컴포넌트 설계 원칙 상세

#### Controlled vs Uncontrolled 패턴

```tsx
// Controlled: 부모가 상태를 완전히 제어
interface ControlledInputProps {
  value: string;
  onChange: (value: string) => void;
}

// Uncontrolled: 컴포넌트가 자체 상태 관리
interface UncontrolledInputProps {
  defaultValue?: string;
  onBlur?: (value: string) => void;
}

// 두 모드 모두 지원하는 패턴
interface FlexibleInputProps {
  value?: string;           // 제공되면 controlled
  defaultValue?: string;    // value 없으면 uncontrolled
  onChange?: (value: string) => void;
}

function FlexibleInput({ value, defaultValue = '', onChange }: FlexibleInputProps) {
  const [internalValue, setInternalValue] = useState(defaultValue);
  const isControlled = value !== undefined;
  const currentValue = isControlled ? value : internalValue;

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value;
    if (!isControlled) setInternalValue(newValue);
    onChange?.(newValue);
  };

  return <input value={currentValue} onChange={handleChange} />;
}
```

#### forwardRef + useImperativeHandle

```tsx
// 외부에서 컴포넌트 내부 메서드를 호출해야 할 때
interface ModalHandle {
  open: () => void;
  close: () => void;
}

const Modal = forwardRef<ModalHandle, ModalProps>(
  function Modal({ title, children }, ref) {
    const [isOpen, setIsOpen] = useState(false);

    useImperativeHandle(ref, () => ({
      open: () => setIsOpen(true),
      close: () => setIsOpen(false),
    }));

    if (!isOpen) return null;

    return (
      <dialog open>
        <h2>{title}</h2>
        {children}
        <button onClick={() => setIsOpen(false)}>닫기</button>
      </dialog>
    );
  },
);

// 사용
function Parent() {
  const modalRef = useRef<ModalHandle>(null);
  return (
    <>
      <button onClick={() => modalRef.current?.open()}>모달 열기</button>
      <Modal ref={modalRef} title="확인">내용</Modal>
    </>
  );
}
```

#### Compound Component 패턴

```tsx
// 관련 컴포넌트를 하나의 API로 묶는 패턴
interface TabsContextType {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

const TabsContext = createContext<TabsContextType | null>(null);

function useTabsContext() {
  const context = useContext(TabsContext);
  if (!context) throw new Error('Tabs 컴포넌트 내부에서 사용해야 합니다');
  return context;
}

function Tabs({ defaultTab, children }: { defaultTab: string; children: ReactNode }) {
  const [activeTab, setActiveTab] = useState(defaultTab);
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div role="tablist">{children}</div>
    </TabsContext.Provider>
  );
}

function TabTrigger({ value, children }: { value: string; children: ReactNode }) {
  const { activeTab, setActiveTab } = useTabsContext();
  return (
    <button role="tab" aria-selected={activeTab === value} onClick={() => setActiveTab(value)}>
      {children}
    </button>
  );
}

function TabContent({ value, children }: { value: string; children: ReactNode }) {
  const { activeTab } = useTabsContext();
  if (activeTab !== value) return null;
  return <div role="tabpanel">{children}</div>;
}

Tabs.Trigger = TabTrigger;
Tabs.Content = TabContent;

// 사용
<Tabs defaultTab="profile">
  <Tabs.Trigger value="profile">프로필</Tabs.Trigger>
  <Tabs.Trigger value="settings">설정</Tabs.Trigger>
  <Tabs.Content value="profile"><ProfileView /></Tabs.Content>
  <Tabs.Content value="settings"><SettingsView /></Tabs.Content>
</Tabs>
```

### 상태 관리 상세

#### TanStack Query 상세

```tsx
// queryKey 설계 - 계층적 키 구조
const queryKeys = {
  users: {
    all: ['users'] as const,
    lists: () => [...queryKeys.users.all, 'list'] as const,
    list: (filters: UserFilters) => [...queryKeys.users.lists(), filters] as const,
    details: () => [...queryKeys.users.all, 'detail'] as const,
    detail: (id: string) => [...queryKeys.users.details(), id] as const,
  },
  posts: {
    all: ['posts'] as const,
    byUser: (userId: string) => [...queryKeys.posts.all, 'byUser', userId] as const,
  },
} as const;

// 기본 Query 사용
function useUsers(filters: UserFilters) {
  return useQuery({
    queryKey: queryKeys.users.list(filters),
    queryFn: () => fetchUsers(filters),
    staleTime: 5 * 60 * 1000,        // 5분간 fresh
    gcTime: 30 * 60 * 1000,           // 30분간 캐시 유지
    placeholderData: keepPreviousData, // 페이지 전환 시 이전 데이터 유지
  });
}

// Mutation + Cache Invalidation
function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: CreateUserInput) => api.post<User>('/users', data),
    onSuccess: () => {
      // 사용자 목록 캐시 무효화
      queryClient.invalidateQueries({ queryKey: queryKeys.users.lists() });
    },
  });
}

// Optimistic Update
function useUpdateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: UpdateUserInput }) =>
      api.patch<User>(`/users/${id}`, data),
    onMutate: async ({ id, data }) => {
      await queryClient.cancelQueries({ queryKey: queryKeys.users.detail(id) });
      const previousUser = queryClient.getQueryData<User>(queryKeys.users.detail(id));
      queryClient.setQueryData<User>(queryKeys.users.detail(id), (old) =>
        old ? { ...old, ...data } : old,
      );
      return { previousUser };
    },
    onError: (_error, { id }, context) => {
      if (context?.previousUser) {
        queryClient.setQueryData(queryKeys.users.detail(id), context.previousUser);
      }
    },
    onSettled: (_data, _error, { id }) => {
      queryClient.invalidateQueries({ queryKey: queryKeys.users.detail(id) });
    },
  });
}

// Infinite Query (무한 스크롤)
function useInfinitePosts(userId: string) {
  return useInfiniteQuery({
    queryKey: queryKeys.posts.byUser(userId),
    queryFn: ({ pageParam }) =>
      api.get<PostsResponse>(`/users/${userId}/posts`, {
        params: { cursor: pageParam, limit: 20 },
      }),
    initialPageParam: undefined as string | undefined,
    getNextPageParam: (lastPage) => lastPage.data.nextCursor ?? undefined,
    select: (data) => data.pages.flatMap((page) => page.data.items),
  });
}
```

#### Zustand 상세

```tsx
// stores/uiStore.ts
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

interface UIState {
  theme: 'light' | 'dark' | 'system';
  sidebarOpen: boolean;
  locale: string;
}

interface UIActions {
  setTheme: (theme: UIState['theme']) => void;
  toggleSidebar: () => void;
  setLocale: (locale: string) => void;
}

const useUIStore = create<UIState & UIActions>()(
  devtools(
    persist(
      (set) => ({
        // 상태
        theme: 'system',
        sidebarOpen: true,
        locale: 'ko',

        // 액션
        setTheme: (theme) => set({ theme }, false, 'setTheme'),
        toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen }), false, 'toggleSidebar'),
        setLocale: (locale) => set({ locale }, false, 'setLocale'),
      }),
      {
        name: 'ui-store',
        partialize: (state) => ({ theme: state.theme, locale: state.locale }), // sidebarOpen은 persist 제외
      },
    ),
    { name: 'UIStore' },
  ),
);

// 셀렉터 패턴 - 필요한 상태만 구독하여 불필요한 리렌더링 방지
function ThemeToggle() {
  const theme = useUIStore((s) => s.theme);
  const setTheme = useUIStore((s) => s.setTheme);
  // theme이 변경될 때만 리렌더링됨
  return <button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}>{theme}</button>;
}

// 여러 값을 선택할 때는 shallow 비교 사용
import { useShallow } from 'zustand/react/shallow';

function Sidebar() {
  const { sidebarOpen, toggleSidebar } = useUIStore(
    useShallow((s) => ({ sidebarOpen: s.sidebarOpen, toggleSidebar: s.toggleSidebar })),
  );
  return sidebarOpen ? <nav>...</nav> : null;
}
```

#### Context API 성능 최적화

```tsx
// Context를 분리하여 불필요한 리렌더링 방지
// BAD: 하나의 큰 Context
const AppContext = createContext<{ user: User; theme: Theme; locale: string } | null>(null);

// GOOD: 관심사별로 분리
const UserContext = createContext<User | null>(null);
const ThemeContext = createContext<Theme>('light');

// 더 나은 패턴: 상태와 디스패치 분리
const CountStateContext = createContext<number>(0);
const CountDispatchContext = createContext<React.Dispatch<CountAction>>(() => {});

function CountProvider({ children }: PropsWithChildren) {
  const [count, dispatch] = useReducer(countReducer, 0);
  return (
    <CountStateContext.Provider value={count}>
      <CountDispatchContext.Provider value={dispatch}>
        {children}
      </CountDispatchContext.Provider>
    </CountStateContext.Provider>
  );
}

// 상태만 필요한 컴포넌트 - dispatch 변경 시 리렌더링 안됨
function CountDisplay() {
  const count = useContext(CountStateContext);
  return <span>{count}</span>;
}

// 디스패치만 필요한 컴포넌트 - 상태 변경 시 리렌더링 안됨
function CountButtons() {
  const dispatch = useContext(CountDispatchContext);
  return <button onClick={() => dispatch({ type: 'increment' })}>+</button>;
}
```

### React Router v6 상세

```tsx
// app/router.tsx
import { createBrowserRouter, type RouteObject } from 'react-router-dom';
import { lazy, Suspense } from 'react';

// 라우트별 코드 스플리팅
const Dashboard = lazy(() => import('@/features/dashboard/Dashboard'));
const UserList = lazy(() => import('@/features/users/UserList'));
const UserDetail = lazy(() => import('@/features/users/UserDetail'));
const Settings = lazy(() => import('@/features/settings/Settings'));

function SuspenseWrapper({ children }: PropsWithChildren) {
  return <Suspense fallback={<PageSkeleton />}>{children}</Suspense>;
}

const routes: RouteObject[] = [
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <RootErrorFallback />,
    children: [
      { index: true, element: <Navigate to="/dashboard" replace /> },
      {
        element: <ProtectedRoute />,
        children: [
          {
            path: 'dashboard',
            element: <SuspenseWrapper><Dashboard /></SuspenseWrapper>,
          },
          {
            path: 'users',
            children: [
              { index: true, element: <SuspenseWrapper><UserList /></SuspenseWrapper> },
              { path: ':userId', element: <SuspenseWrapper><UserDetail /></SuspenseWrapper> },
            ],
          },
          {
            path: 'admin',
            element: <ProtectedRoute allowedRoles={['admin']} />,
            children: [
              { path: 'settings', element: <SuspenseWrapper><Settings /></SuspenseWrapper> },
            ],
          },
        ],
      },
      { path: 'login', element: <LoginPage /> },
      { path: '*', element: <NotFoundPage /> },
    ],
  },
];

export const router = createBrowserRouter(routes);
```

### 테스트 전략 상세

#### Vitest 설정

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react-swc';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  plugins: [react(), tsconfigPaths()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./tests/setup.ts'],
    css: { modules: { classNameStrategy: 'non-scoped' } },
    coverage: {
      provider: 'v8',
      reporter: ['text', 'lcov'],
      include: ['src/**/*.{ts,tsx}'],
      exclude: ['src/**/*.d.ts', 'src/**/*.stories.tsx', 'src/**/index.ts', 'src/main.tsx'],
      thresholds: { branches: 80, functions: 80, lines: 80, statements: 80 },
    },
    include: ['src/**/*.test.{ts,tsx}', 'tests/**/*.test.{ts,tsx}'],
  },
});
```

```ts
// tests/setup.ts
import '@testing-library/jest-dom/vitest';
import { cleanup } from '@testing-library/react';
import { afterEach, beforeAll, afterAll } from 'vitest';
import { server } from './mocks/server';

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => { cleanup(); server.resetHandlers(); });
afterAll(() => server.close());
```

#### React Testing Library 패턴

```tsx
// tests/utils.tsx - Custom Render
import { render, type RenderOptions } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { MemoryRouter } from 'react-router-dom';

interface CustomRenderOptions extends Omit<RenderOptions, 'wrapper'> {
  initialEntries?: string[];
  queryClient?: QueryClient;
}

function createTestQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: { retry: false, gcTime: 0 },
      mutations: { retry: false },
    },
  });
}

function customRender(
  ui: ReactElement,
  { initialEntries = ['/'], queryClient, ...options }: CustomRenderOptions = {},
) {
  const testQueryClient = queryClient ?? createTestQueryClient();

  function Wrapper({ children }: PropsWithChildren) {
    return (
      <QueryClientProvider client={testQueryClient}>
        <MemoryRouter initialEntries={initialEntries}>
          {children}
        </MemoryRouter>
      </QueryClientProvider>
    );
  }

  return { ...render(ui, { wrapper: Wrapper, ...options }), queryClient: testQueryClient };
}

export { customRender as render };
```

```tsx
// 컴포넌트 테스트 예시
import { screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { render } from '@/tests/utils';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  const user = userEvent.setup();

  it('유효한 자격 증명으로 로그인에 성공한다', async () => {
    const onSuccess = vi.fn();
    render(<LoginForm onSuccess={onSuccess} />);

    await user.type(screen.getByLabelText('이메일'), 'test@example.com');
    await user.type(screen.getByLabelText('비밀번호'), 'Password123!');
    await user.click(screen.getByRole('button', { name: '로그인' }));

    await waitFor(() => {
      expect(onSuccess).toHaveBeenCalledOnce();
    });
  });

  it('이메일이 비어있으면 에러 메시지를 표시한다', async () => {
    render(<LoginForm onSuccess={vi.fn()} />);

    await user.click(screen.getByRole('button', { name: '로그인' }));

    expect(await screen.findByText('이메일을 입력해 주세요')).toBeInTheDocument();
  });

  it('로그인 중 버튼이 비활성화된다', async () => {
    render(<LoginForm onSuccess={vi.fn()} />);

    await user.type(screen.getByLabelText('이메일'), 'test@example.com');
    await user.type(screen.getByLabelText('비밀번호'), 'Password123!');
    await user.click(screen.getByRole('button', { name: '로그인' }));

    expect(screen.getByRole('button', { name: '로그인 중...' })).toBeDisabled();
  });
});
```

#### MSW(Mock Service Worker) 설정

```tsx
// tests/mocks/handlers.ts
import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/api/users', ({ request }) => {
    const url = new URL(request.url);
    const page = Number(url.searchParams.get('page') ?? '1');
    return HttpResponse.json({
      users: [{ id: '1', name: '김철수', email: 'kim@example.com' }],
      total: 1,
      page,
    });
  }),

  http.post('/api/auth/login', async ({ request }) => {
    const body = (await request.json()) as { email: string; password: string };
    if (body.email === 'test@example.com' && body.password === 'Password123!') {
      return HttpResponse.json({ user: { id: '1', name: '테스트 사용자' } });
    }
    return HttpResponse.json({ message: '인증 실패' }, { status: 401 });
  }),
];

// tests/mocks/server.ts
import { setupServer } from 'msw/node';
import { handlers } from './handlers';

export const server = setupServer(...handlers);
```

#### 커스텀 훅 테스트

```tsx
import { renderHook, waitFor } from '@testing-library/react';
import { useDebounce } from '@/hooks/useDebounce';

describe('useDebounce', () => {
  beforeEach(() => { vi.useFakeTimers(); });
  afterEach(() => { vi.restoreAllTimers(); });

  it('지정된 딜레이 후 값이 업데이트된다', () => {
    const { result, rerender } = renderHook(
      ({ value, delay }) => useDebounce(value, delay),
      { initialProps: { value: 'hello', delay: 500 } },
    );

    expect(result.current).toBe('hello');

    rerender({ value: 'world', delay: 500 });
    expect(result.current).toBe('hello'); // 아직 업데이트 안 됨

    vi.advanceTimersByTime(500);
    expect(result.current).toBe('world'); // 딜레이 후 업데이트
  });
});
```

### ESLint + Prettier 설정

```js
// eslint.config.js (Flat Config)
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import importPlugin from 'eslint-plugin-import';

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  {
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      'import': importPlugin,
    },
    rules: {
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',
      'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/consistent-type-imports': ['error', { prefer: 'type-imports' }],
      '@typescript-eslint/no-floating-promises': 'error',
      'import/order': ['error', {
        groups: ['builtin', 'external', 'internal', 'parent', 'sibling', 'index', 'type'],
        pathGroups: [{ pattern: '@/**', group: 'internal' }],
        'newlines-between': 'always',
        alphabetize: { order: 'asc' },
      }],
      'import/no-cycle': 'error',
      'no-console': ['warn', { allow: ['warn', 'error'] }],
    },
    languageOptions: {
      parserOptions: { project: ['./tsconfig.json', './tsconfig.node.json'] },
    },
  },
  { ignores: ['dist/', 'node_modules/', '*.config.*'] },
);
```

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "all",
  "tabWidth": 2,
  "printWidth": 100,
  "bracketSpacing": true,
  "arrowParens": "always",
  "endOfLine": "lf"
}
```

### CLI 명령어 전체 리스트

```bash
# 개발
pnpm dev                    # 개발 서버 시작 (port 3000)
pnpm dev --host              # 네트워크 접근 가능 모드
pnpm build                   # 프로덕션 빌드
pnpm preview                 # 빌드 결과 미리보기

# 코드 품질
pnpm lint                    # ESLint 실행
pnpm lint --fix              # ESLint 자동 수정
pnpm format                  # Prettier 포매팅
pnpm format --check          # Prettier 검사만
pnpm type-check              # TypeScript 타입 검사 (tsc --noEmit)

# 테스트
pnpm test                    # Vitest 실행 (watch 모드)
pnpm test --run              # Vitest 단일 실행
pnpm test --coverage         # 커버리지 리포트 생성
pnpm test --ui               # Vitest UI 실행
pnpm test:e2e                # Playwright E2E 테스트
pnpm test:e2e --ui           # Playwright UI 모드

# 분석
pnpm build -- --analyze      # 번들 분석 (rollup-plugin-visualizer)
pnpm audit                   # 보안 취약점 검사

# Git hooks (husky + lint-staged)
# pre-commit: lint-staged (변경 파일에 lint + format 적용)
# commit-msg: commitlint (Conventional Commits 검증)
```

---

## 성능 최적화

### 코드 스플리팅 상세

#### React.lazy + Suspense 패턴

```tsx
// 라우트 기반 스플리팅 (가장 기본)
const Dashboard = lazy(() => import('./features/dashboard/Dashboard'));
const Settings = lazy(() => import('./features/settings/Settings'));

function AppRouter() {
  return (
    <Suspense fallback={<PageSkeleton />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}

// 컴포넌트 기반 스플리팅 (무거운 컴포넌트)
const HeavyChart = lazy(() => import('./components/HeavyChart'));
const MarkdownEditor = lazy(() => import('./components/MarkdownEditor'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);
  return (
    <div>
      <button onClick={() => setShowChart(true)}>차트 보기</button>
      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <HeavyChart data={chartData} />
        </Suspense>
      )}
    </div>
  );
}

// Named export일 때 lazy 사용
const LazyUserProfile = lazy(() =>
  import('./UserProfile').then((module) => ({ default: module.UserProfile })),
);
```

#### Prefetching / Preloading 전략

```tsx
// 마우스 호버 시 프리페치
const UserDetail = lazy(() => import('./features/users/UserDetail'));

function UserListItem({ userId }: { userId: string }) {
  const prefetch = useCallback(() => {
    // 컴포넌트 코드 프리페치
    import('./features/users/UserDetail');
    // 데이터 프리페치
    queryClient.prefetchQuery({
      queryKey: queryKeys.users.detail(userId),
      queryFn: () => fetchUser(userId),
    });
  }, [userId]);

  return (
    <Link
      to={`/users/${userId}`}
      onMouseEnter={prefetch}
      onFocus={prefetch}
    >
      사용자 상세
    </Link>
  );
}

// Viewport에 들어오면 프리페치 (IntersectionObserver)
function PrefetchOnVisible({ componentImport, children }: {
  componentImport: () => Promise<unknown>;
  children: ReactNode;
}) {
  const [ref, entry] = useIntersectionObserver({ rootMargin: '200px' });

  useEffect(() => {
    if (entry?.isIntersecting) {
      componentImport();
    }
  }, [entry?.isIntersecting, componentImport]);

  return <div ref={ref}>{children}</div>;
}
```

### 렌더링 최적화 상세

#### React.memo 사용 기준

```tsx
// React.memo 사용이 효과적인 경우:
// 1. 부모가 자주 리렌더링되지만 자식의 props는 변하지 않을 때
// 2. 렌더링 비용이 높은 컴포넌트 (복잡한 계산, 많은 자식)
// 3. 리스트의 개별 아이템 컴포넌트

const UserCard = memo(function UserCard({ user }: { user: User }) {
  return (
    <div className={styles.card}>
      <img src={user.avatar} alt={user.name} />
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
});

// React.memo 불필요한 경우:
// 1. props가 매번 바뀌는 컴포넌트
// 2. 렌더링이 빠른 단순 컴포넌트
// 3. children을 받는 대부분의 컴포넌트 (children은 매번 새 참조)

// 커스텀 비교 함수 (드물게 필요)
const ExpensiveList = memo(
  function ExpensiveList({ items, onSelect }: ExpensiveListProps) {
    return <ul>{items.map((item) => <li key={item.id}>{item.name}</li>)}</ul>;
  },
  (prev, next) => prev.items.length === next.items.length && prev.items.every((item, i) => item.id === next.items[i].id),
);
```

#### useMemo / useCallback 사용 기준

```tsx
// useMemo - 비용 큰 계산 결과를 메모이제이션
function ProductList({ products, filter }: ProductListProps) {
  // GOOD: 대량 데이터 필터링/정렬
  const filteredProducts = useMemo(
    () => products.filter((p) => p.category === filter).sort((a, b) => a.price - b.price),
    [products, filter],
  );

  // BAD: 단순한 계산에는 불필요
  const title = useMemo(() => `상품 ${products.length}개`, [products.length]); // 과도한 최적화

  return <List items={filteredProducts} />;
}

// useCallback - memo된 자식에 전달하는 콜백 함수
function Parent() {
  // GOOD: memo된 자식에 전달하는 콜백
  const handleSelect = useCallback((id: string) => {
    setSelectedId(id);
  }, []);

  return <MemoizedChild onSelect={handleSelect} />;
}

// BAD: memo되지 않은 자식에게는 useCallback 불필요
function Parent() {
  const handleClick = useCallback(() => { ... }, []); // 불필요
  return <button onClick={handleClick}>클릭</button>; // button은 memo 안됨
}
```

#### useTransition / useDeferredValue (React 18)

```tsx
// useTransition: 긴급하지 않은 상태 업데이트를 낮은 우선순위로 처리
function SearchPage() {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    // 입력 반영은 즉시 (urgent)
    setQuery(e.target.value);

    // 검색 결과 필터링은 낮은 우선순위 (transition)
    startTransition(() => {
      setSearchFilter(e.target.value);
    });
  };

  return (
    <div>
      <input value={query} onChange={handleChange} />
      {isPending && <Spinner />}
      <SearchResults filter={searchFilter} />
    </div>
  );
}

// useDeferredValue: 값의 업데이트를 지연시켜 UI 반응성 유지
function AutocompleteResults({ query }: { query: string }) {
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;

  const results = useMemo(() => filterItems(deferredQuery), [deferredQuery]);

  return (
    <div style={{ opacity: isStale ? 0.7 : 1 }}>
      {results.map((item) => <ResultItem key={item.id} item={item} />)}
    </div>
  );
}
```

#### key를 활용한 리셋 패턴

```tsx
// key 변경으로 컴포넌트 완전 초기화 (언마운트 후 재마운트)
function UserProfilePage() {
  const { userId } = useParams<{ userId: string }>();

  // userId가 바뀌면 EditForm의 모든 상태가 초기화됨
  return <EditForm key={userId} userId={userId} />;
}

// 리스트에서 key를 올바르게 사용
// BAD: 인덱스를 key로 사용하면 항목 추가/삭제/정렬 시 버그 발생
{items.map((item, index) => <Item key={index} item={item} />)} // NEVER

// GOOD: 고유한 식별자 사용
{items.map((item) => <Item key={item.id} item={item} />)}
```

#### 불필요한 리렌더링 감지

```tsx
// React DevTools Profiler 사용 (크롬 확장 프로그램)
// 1. React DevTools > Profiler 탭
// 2. Record 클릭 후 상호작용 수행
// 3. 불필요한 렌더링이 있는 컴포넌트 확인
// 4. "Why did this render?" 기능 활용

// 개발 중 디버깅용 (프로덕션에서 제거)
function useWhyDidYouRender(componentName: string, props: Record<string, unknown>) {
  const previousProps = useRef(props);

  useEffect(() => {
    const changedProps: Record<string, { from: unknown; to: unknown }> = {};
    for (const key of Object.keys(props)) {
      if (previousProps.current[key] !== props[key]) {
        changedProps[key] = { from: previousProps.current[key], to: props[key] };
      }
    }
    if (Object.keys(changedProps).length > 0) {
      console.debug(`[${componentName}] 리렌더링 원인:`, changedProps);
    }
    previousProps.current = props;
  });
}
```

### 가상화 상세

#### @tanstack/react-virtual 설정

```tsx
import { useVirtualizer } from '@tanstack/react-virtual';

function VirtualList({ items }: { items: Item[] }) {
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 64, // 예상 아이템 높이
    overscan: 5,            // 뷰포트 밖에 미리 렌더링할 아이템 수
  });

  return (
    <div ref={parentRef} style={{ height: '600px', overflow: 'auto' }}>
      <div style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
        {virtualizer.getVirtualItems().map((virtualItem) => (
          <div
            key={virtualItem.key}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${virtualItem.size}px`,
              transform: `translateY(${virtualItem.start}px)`,
            }}
          >
            <ItemRow item={items[virtualItem.index]} />
          </div>
        ))}
      </div>
    </div>
  );
}
```

#### 무한 스크롤 + 가상화 조합

```tsx
function InfiniteVirtualList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
  } = useInfinitePosts();

  const allItems = data ?? [];
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: hasNextPage ? allItems.length + 1 : allItems.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 120,
    overscan: 5,
  });

  useEffect(() => {
    const lastItem = virtualizer.getVirtualItems().at(-1);
    if (!lastItem) return;
    if (lastItem.index >= allItems.length - 1 && hasNextPage && !isFetchingNextPage) {
      void fetchNextPage();
    }
  }, [virtualizer.getVirtualItems(), allItems.length, hasNextPage, isFetchingNextPage, fetchNextPage]);

  return (
    <div ref={parentRef} style={{ height: '80vh', overflow: 'auto' }}>
      <div style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
        {virtualizer.getVirtualItems().map((virtualItem) => {
          const isLoader = virtualItem.index >= allItems.length;
          return (
            <div
              key={virtualItem.key}
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                transform: `translateY(${virtualItem.start}px)`,
              }}
            >
              {isLoader ? <LoadMoreSpinner /> : <PostCard post={allItems[virtualItem.index]} />}
            </div>
          );
        })}
      </div>
    </div>
  );
}
```

### API / 데이터 최적화

#### WebSocket / SSE 연동

```tsx
// TanStack Query와 WebSocket 연동
function useRealtimeNotifications() {
  const queryClient = useQueryClient();

  useEffect(() => {
    const ws = new WebSocket(import.meta.env.VITE_WS_URL);

    ws.onmessage = (event) => {
      const message = JSON.parse(event.data) as WebSocketMessage;

      switch (message.type) {
        case 'notification':
          queryClient.invalidateQueries({ queryKey: ['notifications'] });
          break;
        case 'user_update':
          queryClient.setQueryData(
            queryKeys.users.detail(message.userId),
            (old: User | undefined) => old ? { ...old, ...message.data } : old,
          );
          break;
      }
    };

    ws.onerror = () => {
      // 재연결 로직
      setTimeout(() => ws.close(), 1000);
    };

    return () => ws.close();
  }, [queryClient]);
}
```

### 이미지 / 에셋 최적화

```tsx
// 반응형 이미지 + lazy loading
function OptimizedImage({ src, alt, width, height }: ImageProps) {
  return (
    <picture>
      <source srcSet={`${src}.avif`} type="image/avif" />
      <source srcSet={`${src}.webp`} type="image/webp" />
      <img
        src={`${src}.jpg`}
        alt={alt}
        width={width}
        height={height}       // CLS 방지를 위해 반드시 명시
        loading="lazy"        // 뷰포트 밖 이미지 지연 로딩
        decoding="async"      // 메인 스레드 블로킹 방지
        style={{ aspectRatio: `${width}/${height}` }}
      />
    </picture>
  );
}

// SVG 최적화: SVGR로 React 컴포넌트 변환
// vite.config.ts에 svgr 플러그인 추가
import Logo from '@/assets/logo.svg?react';
<Logo className="w-8 h-8" aria-label="로고" />

// 폰트 최적화
// index.html에 preload
// <link rel="preload" href="/fonts/pretendard.woff2" as="font" type="font/woff2" crossorigin />
// CSS: font-display: swap 사용
```

### 번들 최적화

```ts
// vite.config.ts - 프로덕션 빌드 최적화
export default defineConfig({
  build: {
    target: 'es2022',
    minify: 'esbuild',
    sourcemap: true,
    cssMinify: 'lightningcss',
    rollupOptions: {
      output: {
        manualChunks: {
          // React 코어 (변경 빈도 낮음 - 장기 캐시 유리)
          'react-vendor': ['react', 'react-dom'],
          // 라우팅
          'router': ['react-router-dom'],
          // 데이터 페칭
          'query': ['@tanstack/react-query'],
          // UI 라이브러리 (사용하는 경우)
          // 'ui': ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
        },
      },
    },
    chunkSizeWarningLimit: 500, // 500kB 초과 시 경고
  },
});

// Tree shaking 보장
// 1. package.json에 "sideEffects": false (또는 CSS 파일만 명시)
// 2. barrel export(index.ts)에서 re-export만 사용
// 3. lodash 대신 lodash-es 또는 개별 함수 import

// 번들 분석
// pnpm add -D rollup-plugin-visualizer
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(),
    visualizer({ open: true, gzipSize: true }),
  ],
});
```

### Core Web Vitals 최적화

```
LCP (Largest Contentful Paint) - 2.5초 이내:
- 주요 이미지에 fetchpriority="high" 사용
- 서버 사이드 렌더링 또는 정적 생성 고려
- CSS/JS 크기 최소화, 크리티컬 CSS 인라인
- CDN 사용, 리소스 프리로드

INP (Interaction to Next Paint) - 200ms 이내:
- 무거운 연산은 Web Worker로 오프로드
- useTransition으로 비긴급 업데이트 지연
- 이벤트 핸들러에서 동기적 DOM 조작 최소화
- requestIdleCallback 활용

CLS (Cumulative Layout Shift) - 0.1 이내:
- 이미지/비디오에 width/height 또는 aspect-ratio 명시
- 동적 콘텐츠 삽입 시 미리 공간 확보 (min-height)
- 웹 폰트에 font-display: swap + size-adjust
- 광고/임베드에 고정 크기 컨테이너 사용
```

---

## 주의사항 / Gotchas

### useEffect 의존성 배열 실수

```tsx
// BAD: 의존성 누락 - 무한 루프
function SearchResults({ query }: { query: string }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    // 매 렌더링마다 새 객체를 생성하여 무한 루프 발생 가능
    const params = { q: query, limit: 10 }; // 매번 새 참조
    fetchResults(params).then(setResults);
  }, [params]); // params는 매 렌더링마다 새 객체 -> 무한 루프

  // GOOD: 원시 값을 의존성으로 사용
  useEffect(() => {
    fetchResults({ q: query, limit: 10 }).then(setResults);
  }, [query]);
}

// BAD: 빈 의존성 배열로 업데이트 누락
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // count는 항상 0 (closure 트랩)
    }, 1000);
    return () => clearInterval(id);
  }, []); // count가 의존성에 없음

  // GOOD: 함수형 업데이트 사용
  useEffect(() => {
    const id = setInterval(() => {
      setCount((prev) => prev + 1); // 항상 최신 값 사용
    }, 1000);
    return () => clearInterval(id);
  }, []);
}
```

### useState closure 트랩 (stale closure)

```tsx
function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    // BAD: 3번 클릭해도 1만 증가 (각 호출이 같은 count=0을 참조)
    setCount(count + 1);
    setCount(count + 1);
    setCount(count + 1);

    // GOOD: 함수형 업데이트로 최신 값 기반 업데이트
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
  };
}

// 비동기 콜백에서의 stale closure
function AsyncExample() {
  const [value, setValue] = useState('');

  const handleSubmit = async () => {
    await submitData();
    console.log(value); // 제출 시점의 value가 아닌 클로저 생성 시점의 value

    // GOOD: ref로 최신 값 참조
  };

  const valueRef = useRef(value);
  valueRef.current = value;

  const handleSubmitFixed = async () => {
    await submitData();
    console.log(valueRef.current); // 항상 최신 값
  };
}
```

### key prop 오용

```tsx
// BAD: 배열 인덱스를 key로 사용
// 항목 추가/삭제/재정렬 시 React가 올바른 DOM 업데이트를 못함
{items.map((item, index) => (
  <TodoItem key={index} item={item} />
))}

// GOOD: 고유한 식별자 사용
{items.map((item) => (
  <TodoItem key={item.id} item={item} />
))}

// 고유 ID가 없는 경우: 데이터 생성 시 ID 부여
const addItem = (text: string) => {
  setItems((prev) => [...prev, { id: crypto.randomUUID(), text }]);
};
```

### StrictMode 더블 실행

```tsx
// StrictMode에서는 의도적으로 이펙트를 2번 실행 (mount -> unmount -> mount)
// 이는 cleanup이 올바르게 동작하는지 검증하기 위함

// BAD: StrictMode 제거로 "해결"하지 말 것
// const root = createRoot(document.getElementById('root')!);
// root.render(<App />); // StrictMode 없이 - 금지

// GOOD: cleanup 함수를 올바르게 작성
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then((res) => res.json())
    .then(setData)
    .catch((error) => {
      if (error.name !== 'AbortError') throw error;
    });

  return () => controller.abort(); // cleanup
}, []);
```

### async useEffect 패턴

```tsx
// BAD: useEffect에 async 함수 직접 전달
useEffect(async () => {  // 반환값이 Promise가 되어 cleanup으로 사용 불가
  const data = await fetchData();
  setData(data);
}, []);

// GOOD: 내부에서 async 함수 정의 후 호출
useEffect(() => {
  const controller = new AbortController();

  async function loadData() {
    try {
      const data = await fetchData({ signal: controller.signal });
      setData(data);
    } catch (error) {
      if (error instanceof DOMException && error.name === 'AbortError') return;
      setError(error);
    }
  }

  void loadData();
  return () => controller.abort();
}, []);
```

### 조건부 훅 호출 금지

```tsx
// BAD: 조건부로 훅 호출 - React 규칙 위반
function UserProfile({ userId }: { userId?: string }) {
  if (!userId) return <p>사용자를 선택하세요</p>;
  const { data } = useUser(userId); // 조건부 호출 금지!
  return <div>{data?.name}</div>;
}

// GOOD: 훅은 항상 호출하고, 결과를 조건부로 사용
function UserProfile({ userId }: { userId?: string }) {
  const { data } = useUser(userId ?? '', { enabled: !!userId });

  if (!userId) return <p>사용자를 선택하세요</p>;
  return <div>{data?.name}</div>;
}

// GOOD: 컴포넌트 분리
function UserProfileWrapper({ userId }: { userId?: string }) {
  if (!userId) return <p>사용자를 선택하세요</p>;
  return <UserProfileContent userId={userId} />;
}

function UserProfileContent({ userId }: { userId: string }) {
  const { data } = useUser(userId);
  return <div>{data?.name}</div>;
}
```

### useRef vs useState 선택 기준

```tsx
// useState: 값 변경 시 리렌더링이 필요한 경우
const [count, setCount] = useState(0);
// count가 변하면 UI에 반영되어야 함

// useRef: 값 변경 시 리렌더링이 불필요한 경우
const renderCount = useRef(0);     // 렌더링 횟수 추적 (디버깅)
const timerRef = useRef<number>(); // setInterval/setTimeout ID
const prevValueRef = useRef(value); // 이전 값 추적
const isMountedRef = useRef(true);  // 마운트 상태 추적

// useRef로 DOM 요소 참조
const inputRef = useRef<HTMLInputElement>(null);
const handleFocus = () => inputRef.current?.focus();
```

### e.target vs e.currentTarget

```tsx
// e.target: 실제로 이벤트가 발생한 요소 (자식 요소일 수 있음)
// e.currentTarget: 이벤트 핸들러가 등록된 요소 (항상 일관됨)

function Form() {
  // BAD: e.target은 클릭된 자식 요소일 수 있음
  const handleClick = (e: MouseEvent<HTMLDivElement>) => {
    console.log(e.target);        // <span>, <p> 등 자식 요소
    console.log(e.currentTarget); // 항상 <div> (핸들러가 등록된 요소)
  };

  // 폼에서 주의: form의 submit 이벤트
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget); // e.currentTarget 사용
    // e.target은 submit 트리거한 요소 (버튼 등)일 수 있음
  };
}
```

### 메모리 누수 방지

```tsx
// 1. useEffect cleanup에서 구독 해제
useEffect(() => {
  const subscription = eventBus.subscribe('event', handler);
  return () => subscription.unsubscribe();
}, []);

// 2. AbortController로 비동기 작업 취소
useEffect(() => {
  const controller = new AbortController();
  fetchData({ signal: controller.signal }).then(setData);
  return () => controller.abort();
}, []);

// 3. 타이머 정리
useEffect(() => {
  const timerId = setInterval(tick, 1000);
  return () => clearInterval(timerId);
}, []);

// 4. DOM 이벤트 리스너 정리
useEffect(() => {
  const handler = (e: KeyboardEvent) => { ... };
  window.addEventListener('keydown', handler);
  return () => window.removeEventListener('keydown', handler);
}, []);

// 5. WebSocket 연결 정리
useEffect(() => {
  const ws = new WebSocket(url);
  ws.onmessage = handleMessage;
  return () => ws.close();
}, [url]);
```

### React 18 자동 배칭 변경사항

```tsx
// React 18 이전: setTimeout, Promise 등에서는 배칭이 안 됨
// React 18: 모든 상태 업데이트가 자동으로 배칭됨

function Example() {
  const handleClick = async () => {
    // React 18: 이 두 업데이트가 하나의 리렌더링으로 배칭됨
    setCount((c) => c + 1);
    setFlag((f) => !f);
    // 리렌더링 1회만 발생
  };

  // 배칭을 원하지 않는 경우 (드물게 필요)
  const handleUrgent = () => {
    flushSync(() => setCount((c) => c + 1)); // 즉시 리렌더링
    // 여기서 DOM은 이미 업데이트된 상태
    flushSync(() => setFlag((f) => !f));      // 다시 즉시 리렌더링
  };
}
```

### Suspense와 Error Boundary 조합

```tsx
// Suspense: 로딩 상태 처리
// Error Boundary: 에러 상태 처리
// 함께 사용하여 완전한 비동기 상태 처리

function UserPage({ userId }: { userId: string }) {
  return (
    <ErrorBoundary FallbackComponent={ErrorFallback} onReset={() => window.location.reload()}>
      <Suspense fallback={<UserSkeleton />}>
        <UserProfile userId={userId} />
      </Suspense>
    </ErrorBoundary>
  );
}

// Error Boundary가 Suspense를 감싸야 함
// Suspense 내부에서 throw된 에러는 가장 가까운 Error Boundary에서 포착

// TanStack Query의 throwOnError와 함께 사용
function UserProfile({ userId }: { userId: string }) {
  // throwOnError: true이면 Error Boundary로 전파
  const { data } = useSuspenseQuery({
    queryKey: queryKeys.users.detail(userId),
    queryFn: () => fetchUser(userId),
  });

  // data는 항상 존재 (Suspense가 로딩 처리)
  return <div>{data.name}</div>;
}
```

### forwardRef 관련 참고사항

```tsx
// React 19에서 ref는 일반 props로 전달 가능하게 될 예정
// 현재(React 18)에서는 forwardRef 사용 필수

// React 18 (현재)
const Input = forwardRef<HTMLInputElement, InputProps>(
  function Input(props, ref) {
    return <input ref={ref} {...props} />;
  },
);

// React 19 (미래) - forwardRef 없이 직접 ref 전달 가능
// function Input({ ref, ...props }: InputProps & { ref?: Ref<HTMLInputElement> }) {
//   return <input ref={ref} {...props} />;
// }

// 마이그레이션 대비: forwardRef를 사용하되, 컴포넌트에 displayName 또는 named function 사용
```

### 서버 컴포넌트 vs 클라이언트 컴포넌트 경계

```tsx
// 현재 Vite + React는 순수 CSR (Client-Side Rendering)
// Next.js 등 풀스택 프레임워크로 마이그레이션 시 주의할 점:

// 서버 컴포넌트에서 사용 불가:
// - useState, useEffect 등 React hooks
// - 브라우저 API (window, document, localStorage)
// - 이벤트 핸들러 (onClick, onChange 등)

// 클라이언트 컴포넌트 필요 시: 'use client' 디렉티브 추가
// 서버/클라이언트 경계를 최대한 아래로 내려야 성능에 유리

// 현재 프로젝트가 CSR이더라도 hooks와 이벤트 핸들러를
// 별도 컴포넌트로 분리하는 습관은 향후 마이그레이션에 도움이 됨
```
