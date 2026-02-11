# CLAUDE.md - Vue 3 프로젝트 상세 가이드

> 이 문서는 Claude Code가 Vue 3 프로젝트를 바이브코딩할 때 참조하는 종합 스펙입니다.
> 모든 코드 예시는 실무에서 바로 복사해서 사용할 수 있는 완성형입니다.

---

## 1. 프로젝트 개요

### 1.1 기술 스택

| 기술 | 버전 | 용도 |
|------|------|------|
| Vue | 3.4+ | UI 프레임워크 (Composition API + `<script setup>`) |
| TypeScript | 5.x | 정적 타입 시스템 |
| Vite | 5.x | 빌드 도구 및 개발 서버 |
| Pinia | 2.x | 상태 관리 |
| Vue Router | 4.x | 클라이언트 사이드 라우팅 |
| pnpm | 9.x | 패키지 매니저 |
| Node.js | 20 LTS+ | 런타임 환경 |
| Vitest | 1.x+ | 단위/통합 테스트 |
| Playwright | 1.x+ | E2E 테스트 |
| ESLint | 9.x (flat config) | 코드 린팅 |
| Prettier | 3.x | 코드 포매팅 |

### 1.2 프로젝트 구조 상세 트리

```
project-root/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                    # CI 파이프라인 (lint, test, build)
│   │   └── deploy.yml                # 배포 파이프라인
│   └── PULL_REQUEST_TEMPLATE.md
├── .vscode/
│   ├── extensions.json               # 추천 확장 (Volar, ESLint, Prettier)
│   └── settings.json                 # 프로젝트별 에디터 설정
├── public/
│   ├── favicon.ico
│   └── robots.txt
├── src/
│   ├── api/                          # API 클라이언트 및 엔드포인트
│   │   ├── client.ts                 # axios 인스턴스 + 인터셉터
│   │   ├── endpoints/                # 도메인별 API 함수
│   │   │   ├── auth.api.ts
│   │   │   ├── user.api.ts
│   │   │   └── product.api.ts
│   │   └── index.ts                  # API 모듈 재export
│   ├── assets/                       # 정적 에셋
│   │   ├── images/
│   │   ├── fonts/
│   │   └── styles/
│   │       ├── reset.css             # CSS 리셋
│   │       ├── variables.css         # CSS 커스텀 속성
│   │       ├── typography.css        # 타이포그래피 정의
│   │       └── main.css              # 글로벌 스타일 진입점
│   ├── components/                   # 재사용 UI 컴포넌트
│   │   ├── base/                     # 원자적 기본 컴포넌트
│   │   │   ├── BaseButton.vue
│   │   │   ├── BaseInput.vue
│   │   │   ├── BaseModal.vue
│   │   │   └── BaseToast.vue
│   │   ├── layout/                   # 레이아웃 컴포넌트
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppSidebar.vue
│   │   │   ├── AppFooter.vue
│   │   │   └── AppLayout.vue
│   │   └── domain/                   # 도메인별 컴포넌트
│   │       ├── user/
│   │       │   ├── UserAvatar.vue
│   │       │   ├── UserCard.vue
│   │       │   └── UserList.vue
│   │       └── product/
│   │           ├── ProductCard.vue
│   │           └── ProductGrid.vue
│   ├── composables/                  # 재사용 로직 (Composition Functions)
│   │   ├── useApi.ts                 # API 호출 래퍼
│   │   ├── useAuth.ts               # 인증 상태 관리
│   │   ├── useForm.ts               # 폼 관리
│   │   ├── usePagination.ts         # 페이지네이션
│   │   ├── useDebounce.ts           # 디바운스
│   │   ├── useThrottle.ts           # 스로틀
│   │   └── useIntersectionObserver.ts
│   ├── constants/                    # 상수 정의
│   │   ├── app.constants.ts
│   │   └── api.constants.ts
│   ├── plugins/                      # Vue 플러그인
│   │   └── index.ts
│   ├── router/                       # Vue Router 설정
│   │   ├── index.ts                  # 라우터 인스턴스
│   │   ├── guards.ts                # 네비게이션 가드
│   │   └── routes.ts                # 라우트 정의
│   ├── stores/                       # Pinia 스토어
│   │   ├── useAuthStore.ts
│   │   ├── useUserStore.ts
│   │   └── useUiStore.ts
│   ├── types/                        # 공유 TypeScript 타입
│   │   ├── api.types.ts             # API 응답/요청 타입
│   │   ├── user.types.ts
│   │   ├── product.types.ts
│   │   └── common.types.ts          # 공통 유틸리티 타입
│   ├── utils/                        # 순수 유틸리티 함수
│   │   ├── format.ts                # 날짜, 숫자, 문자열 포매팅
│   │   ├── validate.ts              # 검증 유틸리티
│   │   ├── sanitize.ts             # XSS 방지 sanitize
│   │   └── storage.ts              # localStorage/sessionStorage 래퍼
│   ├── views/                        # 라우트 매핑 페이지 컴포넌트
│   │   ├── HomePage.vue
│   │   ├── LoginPage.vue
│   │   ├── DashboardPage.vue
│   │   └── NotFoundPage.vue
│   ├── App.vue                       # 루트 컴포넌트
│   ├── main.ts                       # 앱 진입점
│   └── env.d.ts                      # 환경변수 타입 선언
├── tests/
│   ├── unit/                         # 단위 테스트
│   ├── integration/                  # 통합 테스트
│   └── e2e/                          # E2E 테스트
├── .env                              # 로컬 환경변수 (gitignore)
├── .env.example                      # 환경변수 템플릿
├── .env.development                  # 개발 환경변수
├── .env.production                   # 프로덕션 환경변수
├── .env.staging                      # 스테이징 환경변수
├── .gitignore
├── .prettierrc                       # Prettier 설정
├── eslint.config.js                  # ESLint flat config
├── index.html                        # HTML 진입점
├── package.json
├── pnpm-lock.yaml
├── tsconfig.json                     # 기본 TypeScript 설정
├── tsconfig.app.json                 # 앱 소스 TypeScript 설정
├── tsconfig.node.json                # Node 환경 TypeScript 설정
├── vite.config.ts                    # Vite 설정
└── vitest.config.ts                  # Vitest 설정
```

### 1.3 vite.config.ts 핵심 설정

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
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
          vendor: ['vue', 'vue-router', 'pinia'],
        },
      },
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/assets/styles/variables" as *;`,
      },
    },
  },
})
```

### 1.4 tsconfig.json 설정 포인트

```jsonc
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": false,
    "jsx": "preserve",
    "jsxImportSource": "vue",
    "paths": {
      "@/*": ["./src/*"]
    },
    "types": ["vite/client", "vitest/globals"]
  },
  "include": ["src/**/*.ts", "src/**/*.vue", "env.d.ts"]
}
```

### 1.5 빌드 타겟 및 브라우저 지원

- **빌드 타겟**: ES2022
- **지원 브라우저**: Chrome 90+, Firefox 90+, Safari 15+, Edge 90+
- **미지원**: IE11, 레거시 모바일 브라우저
- **Polyfill 전략**: 필요 시 `core-js`를 통한 선택적 polyfill, 기본적으로 모던 브라우저만 지원

---

## 2. 코딩 컨벤션

### 2.1 네이밍 규칙

#### 2.1.1 파일 네이밍

| 파일 종류 | 규칙 | 예시 | 비고 |
|-----------|------|------|------|
| Vue 컴포넌트 | PascalCase.vue | `UserProfile.vue` | 항상 2단어 이상 |
| composable | camelCase, `use` 접두사 | `useAuth.ts` | 반환값이 반응형 |
| Pinia store | camelCase, `use` + `Store` | `useUserStore.ts` | defineStore ID와 일치 |
| 유틸리티 | camelCase | `formatDate.ts` | 순수 함수만 포함 |
| 타입 정의 | camelCase + `.types.ts` | `user.types.ts` | interface/type만 포함 |
| API 엔드포인트 | camelCase + `.api.ts` | `user.api.ts` | API 호출 함수만 포함 |
| 상수 | camelCase + `.constants.ts` | `app.constants.ts` | export const만 포함 |
| 테스트 | 대상파일명 + `.spec.ts` | `UserCard.spec.ts` | 테스트 대상과 동일 위치 또는 tests/ |

#### 2.1.2 코드 네이밍

```ts
// 변수: camelCase
const userName = ref('')
const isLoading = ref(false)
const hasPermission = computed(() => /* ... */)

// 함수: camelCase, 동사로 시작
function fetchUserData() { /* ... */ }
function handleClick() { /* ... */ }
function validateEmail(email: string): boolean { /* ... */ }

// 상수: UPPER_SNAKE_CASE
const MAX_RETRY_COUNT = 3
const API_BASE_URL = import.meta.env.VITE_API_URL
const DEFAULT_PAGE_SIZE = 20

// 타입/인터페이스: PascalCase
interface UserProfile {
  id: number
  name: string
  email: string
}

type ApiResponse<T> = {
  data: T
  message: string
  status: number
}

// enum: PascalCase (멤버도 PascalCase)
enum UserRole {
  Admin = 'admin',
  Editor = 'editor',
  Viewer = 'viewer',
}

// emit 이벤트: camelCase
const emit = defineEmits<{
  'update:modelValue': [value: string]
  'submit': [data: FormData]
  'delete': [id: number]
}>()

// provide/inject 키: Symbol + PascalCase 설명
const ThemeKey: InjectionKey<Ref<string>> = Symbol('Theme')

// CSS 클래스 (template 내): kebab-case
// <div class="user-card__header">

// composable 반환값: 명확한 이름, readonly 적용
function useCounter() {
  const count = ref(0)
  const increment = () => { count.value++ }
  return { count: readonly(count), increment }
}
```

#### 2.1.3 컴포넌트 네이밍 규칙

```
Base 컴포넌트:    Base + 목적     → BaseButton, BaseInput, BaseModal
레이아웃:         App + 위치      → AppHeader, AppSidebar, AppFooter
도메인:           도메인 + 역할   → UserCard, ProductGrid, OrderList
페이지:           이름 + Page     → HomePage, LoginPage, DashboardPage
```

### 2.2 import 순서와 정리 규칙

```ts
// 1. Vue 코어
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

// 2. 외부 라이브러리
import { storeToRefs } from 'pinia'
import { useQueryClient } from '@tanstack/vue-query'
import axios from 'axios'

// 3. 내부 stores
import { useAuthStore } from '@/stores/useAuthStore'
import { useUserStore } from '@/stores/useUserStore'

// 4. 내부 composables
import { useApi } from '@/composables/useApi'
import { useForm } from '@/composables/useForm'

// 5. 내부 components
import BaseButton from '@/components/base/BaseButton.vue'
import UserCard from '@/components/domain/user/UserCard.vue'

// 6. 유틸리티
import { formatDate } from '@/utils/format'
import { validateEmail } from '@/utils/validate'

// 7. 타입 (항상 import type 사용)
import type { UserProfile } from '@/types/user.types'
import type { ApiResponse } from '@/types/api.types'

// 8. 상수
import { MAX_RETRY_COUNT } from '@/constants/app.constants'
```

**규칙 요약:**
- 각 그룹 사이에 빈 줄 하나
- 타입 전용 import에는 반드시 `import type` 사용
- 동일 그룹 내 알파벳 순 정렬
- barrel export(`index.ts`)는 3개 이상의 export가 있을 때만 생성
- 사용하지 않는 import는 즉시 제거

### 2.3 에러 핸들링 패턴

#### 2.3.1 전역 에러 핸들러

```ts
// src/main.ts
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// 전역 Vue 에러 핸들러
app.config.errorHandler = (err, instance, info) => {
  console.error('[Global Error]', err)
  console.error('[Component]', instance?.$options?.name || 'Unknown')
  console.error('[Info]', info)

  // 에러 리포팅 서비스로 전송 (Sentry 등)
  // reportError({ error: err, component: info })
}

// 전역 경고 핸들러 (개발 환경 전용)
if (import.meta.env.DEV) {
  app.config.warnHandler = (msg, instance, trace) => {
    console.warn('[Vue Warn]', msg)
    console.warn('[Trace]', trace)
  }
}

app.mount('#app')
```

#### 2.3.2 API 에러 처리

```ts
// src/api/client.ts
import axios, { type AxiosError } from 'axios'

export interface ApiError {
  message: string
  code: string
  status: number
  details?: Record<string, string[]>
}

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

// 응답 인터셉터: 에러 정규화
apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError<ApiError>) => {
    if (error.response) {
      // 서버가 응답을 반환한 경우 (4xx, 5xx)
      const apiError: ApiError = {
        message: error.response.data?.message || '서버 오류가 발생했습니다.',
        code: error.response.data?.code || 'UNKNOWN_ERROR',
        status: error.response.status,
        details: error.response.data?.details,
      }
      return Promise.reject(apiError)
    }

    if (error.request) {
      // 요청은 보냈으나 응답 없음 (네트워크 에러)
      return Promise.reject({
        message: '네트워크 연결을 확인해주세요.',
        code: 'NETWORK_ERROR',
        status: 0,
      } satisfies ApiError)
    }

    // 요청 설정 중 에러
    return Promise.reject({
      message: '요청 처리 중 오류가 발생했습니다.',
      code: 'REQUEST_ERROR',
      status: 0,
    } satisfies ApiError)
  },
)

export { apiClient }
```

#### 2.3.3 컴포넌트 에러 바운더리

```vue
<!-- src/components/base/ErrorBoundary.vue -->
<script setup lang="ts">
import { ref, onErrorCaptured } from 'vue'

interface Props {
  fallbackMessage?: string
}

const props = withDefaults(defineProps<Props>(), {
  fallbackMessage: '오류가 발생했습니다. 다시 시도해주세요.',
})

const error = ref<Error | null>(null)

onErrorCaptured((err: Error) => {
  error.value = err
  return false // 에러 전파 중단
})

function retry() {
  error.value = null
}
</script>

<template>
  <slot v-if="!error" />
  <div v-else class="error-boundary">
    <p>{{ props.fallbackMessage }}</p>
    <button @click="retry">다시 시도</button>
  </div>
</template>
```

### 2.4 컴포넌트 코드 구조 (script setup 내 작성 순서)

```vue
<script setup lang="ts">
// ---- 1. 타입 import ----
import type { UserProfile } from '@/types/user.types'

// ---- 2. 외부 import ----
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

// ---- 3. 내부 import ----
import { useAuthStore } from '@/stores/useAuthStore'
import { useApi } from '@/composables/useApi'
import BaseButton from '@/components/base/BaseButton.vue'
import { formatDate } from '@/utils/format'

// ---- 4. Props 정의 ----
interface Props {
  userId: number
  showAvatar?: boolean
}
const props = withDefaults(defineProps<Props>(), {
  showAvatar: true,
})

// ---- 5. Emits 정의 ----
const emit = defineEmits<{
  'select': [user: UserProfile]
  'delete': [id: number]
}>()

// ---- 6. Composables 호출 ----
const router = useRouter()
const authStore = useAuthStore()
const { execute, isLoading, error } = useApi<UserProfile>()

// ---- 7. 반응형 상태 (ref, reactive) ----
const isExpanded = ref(false)
const searchQuery = ref('')

// ---- 8. Computed ----
const fullName = computed(() => `${user.value?.firstName} ${user.value?.lastName}`)
const isOwner = computed(() => authStore.userId === props.userId)

// ---- 9. Watch ----
watch(() => props.userId, (newId) => {
  fetchUser(newId)
})

// ---- 10. 메서드 ----
async function fetchUser(id: number) {
  await execute(() => userApi.getById(id))
}

function handleSelect() {
  if (user.value) emit('select', user.value)
}

// ---- 11. Lifecycle Hooks ----
onMounted(() => {
  fetchUser(props.userId)
})

onUnmounted(() => {
  // 클린업: 이벤트 리스너, 타이머 등 해제
})
</script>
```

### 2.5 SFC 구조 규칙

```vue
<!-- 순서: template > script > style -->

<template>
  <!-- 단일 루트 요소 권장 (Vue 3에서 필수는 아니지만 일관성) -->
  <div class="component-name">
    <!-- 내용 -->
  </div>
</template>

<script setup lang="ts">
// Composition API 코드
</script>

<style scoped>
/* scoped 스타일 */
</style>
```

**규칙:**
- `<template>` → `<script setup>` → `<style scoped>` 순서 고정
- `<script setup lang="ts">` 필수 사용
- `<style scoped>` 기본 사용, 전역 스타일이 필요하면 별도 CSS 파일
- 컴포넌트당 200줄 이하 유지. 초과 시 composable 또는 하위 컴포넌트로 분리

### 2.6 TypeScript 활용

#### 2.6.1 Props 타입 정의

```ts
// 인라인 타입 (간단한 경우)
const props = defineProps<{
  title: string
  count?: number
}>()

// withDefaults (기본값이 필요한 경우)
interface Props {
  title: string
  count?: number
  items?: string[]
}
const props = withDefaults(defineProps<Props>(), {
  count: 0,
  items: () => [],
})
```

#### 2.6.2 Emits 타입 정의

```ts
// 튜플 문법 (Vue 3.3+)
const emit = defineEmits<{
  'change': [id: number]
  'update:modelValue': [value: string]
  'submit': [data: { name: string; email: string }]
}>()
```

#### 2.6.3 제네릭 컴포넌트 (Vue 3.3+)

```vue
<script setup lang="ts" generic="T extends { id: number }">
interface Props {
  items: T[]
  selected?: T
}

defineProps<Props>()

const emit = defineEmits<{
  'select': [item: T]
}>()
</script>

<template>
  <ul>
    <li
      v-for="item in items"
      :key="item.id"
      @click="emit('select', item)"
    >
      <slot :item="item" />
    </li>
  </ul>
</template>
```

#### 2.6.4 defineModel (Vue 3.4+)

```vue
<script setup lang="ts">
// v-model 양방향 바인딩 간소화
const modelValue = defineModel<string>({ required: true })
const isOpen = defineModel<boolean>('open', { default: false })
</script>

<template>
  <input :value="modelValue" @input="modelValue = ($event.target as HTMLInputElement).value" />
</template>
```

#### 2.6.5 유틸리티 타입 패턴

```ts
// src/types/common.types.ts

/** API 페이지네이션 응답 */
export interface PaginatedResponse<T> {
  data: T[]
  meta: {
    currentPage: number
    lastPage: number
    perPage: number
    total: number
  }
}

/** API 표준 응답 */
export interface ApiResponse<T> {
  data: T
  message: string
  success: boolean
}

/** Nullable 타입 */
export type Nullable<T> = T | null

/** 선택적 프로퍼티를 필수로 변환 */
export type RequiredFields<T, K extends keyof T> = T & Required<Pick<T, K>>

/** 특정 키만 선택적으로 변환 */
export type OptionalFields<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>

/** 폼 데이터 타입 (id 제외) */
export type CreatePayload<T> = Omit<T, 'id' | 'createdAt' | 'updatedAt'>
export type UpdatePayload<T> = Partial<CreatePayload<T>>
```

### 2.7 CSS/스타일링 컨벤션

```vue
<style scoped>
/* 1. CSS 커스텀 속성 활용 */
.card {
  --card-padding: 1rem;
  --card-radius: 8px;
  padding: var(--card-padding);
  border-radius: var(--card-radius);
}

/* 2. BEM 네이밍 (선택적, scoped에서는 간소화 가능) */
.user-card { }
.user-card__header { }
.user-card__body { }
.user-card--active { }

/* 3. 반응형 디자인: 모바일 퍼스트 */
.container {
  padding: 1rem;
}
@media (min-width: 768px) {
  .container {
    padding: 2rem;
  }
}

/* 4. :deep() 자식 컴포넌트 스타일 오버라이드 */
.parent :deep(.child-class) {
  color: red;
}

/* 5. v-bind() CSS 내 반응형 값 */
.dynamic {
  color: v-bind(themeColor);
}
</style>
```

### 2.8 주석/문서화 규칙

```ts
// 컴포넌트 상단에 간단한 설명만 (JSDoc 남용 금지)
// 복잡한 비즈니스 로직에만 주석 작성
// "왜(Why)"를 설명하는 주석만 작성, "무엇(What)"은 코드가 설명

// Bad: 무의미한 주석
// 유저를 가져온다
const user = await fetchUser(id)

// Good: 비즈니스 이유 설명
// 관리자 계정은 조회수에 포함하지 않음 (마케팅팀 요청)
if (!user.isAdmin) incrementViewCount()
```

---

## 3. 보안 필수사항

### 3.1 XSS 방지

#### 3.1.1 v-html 대체 및 DOMPurify 설정

```ts
// src/utils/sanitize.ts
import DOMPurify from 'dompurify'

// 허용할 태그와 속성을 최소한으로 제한
const SANITIZE_CONFIG: DOMPurify.Config = {
  ALLOWED_TAGS: [
    'b', 'i', 'em', 'strong', 'a', 'p', 'br', 'ul', 'ol', 'li',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'code', 'pre',
    'span', 'div', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
  ],
  ALLOWED_ATTR: [
    'href', 'target', 'rel', 'src', 'alt', 'class', 'id',
    'width', 'height', 'colspan', 'rowspan',
  ],
  ALLOW_DATA_ATTR: false,
  ADD_ATTR: ['target'], // 외부 링크에 target 허용
}

/**
 * HTML 문자열을 안전하게 sanitize.
 * v-html 바인딩 전에 반드시 이 함수를 거쳐야 함.
 */
export function sanitizeHtml(dirty: string): string {
  return DOMPurify.sanitize(dirty, SANITIZE_CONFIG)
}

/**
 * 순수 텍스트만 추출 (모든 HTML 제거)
 */
export function stripHtml(html: string): string {
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: [],
    ALLOWED_ATTR: [],
  })
}

// DOMPurify 훅: 모든 링크에 rel="noopener noreferrer" 추가
DOMPurify.addHook('afterSanitizeAttributes', (node) => {
  if (node.tagName === 'A') {
    node.setAttribute('target', '_blank')
    node.setAttribute('rel', 'noopener noreferrer')
  }
})
```

**사용 패턴:**

```vue
<script setup lang="ts">
import { computed } from 'vue'
import { sanitizeHtml } from '@/utils/sanitize'

const props = defineProps<{ rawContent: string }>()

// 반드시 computed로 sanitize 결과를 캐시
const safeContent = computed(() => sanitizeHtml(props.rawContent))
</script>

<template>
  <!-- 절대 원본 HTML을 직접 바인딩하지 않음 -->
  <!-- Bad: <div v-html="rawContent" /> -->

  <!-- Good: sanitize된 HTML만 바인딩 -->
  <div v-html="safeContent" />

  <!-- Best: 가능하면 텍스트 보간 사용 -->
  <p>{{ props.rawContent }}</p>
</template>
```

#### 3.1.2 사용자 입력 이스케이핑

```ts
// src/utils/sanitize.ts 에 추가

/**
 * HTML 특수 문자 이스케이프
 */
export function escapeHtml(str: string): string {
  const map: Record<string, string> = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#x27;',
    '/': '&#x2F;',
  }
  return str.replace(/[&<>"'/]/g, (char) => map[char] ?? char)
}

/**
 * 속성값 이스케이프 (동적 속성 바인딩 시)
 */
export function escapeAttr(str: string): string {
  return str.replace(/[&"'<>]/g, (char) => `&#${char.charCodeAt(0)};`)
}
```

#### 3.1.3 URL 검증

```ts
// src/utils/validate.ts

const ALLOWED_PROTOCOLS = ['http:', 'https:', 'mailto:', 'tel:']

/**
 * URL이 안전한지 검증 (javascript: 프로토콜 등 차단)
 */
export function isSafeUrl(url: string): boolean {
  try {
    const parsed = new URL(url, window.location.origin)
    return ALLOWED_PROTOCOLS.includes(parsed.protocol)
  } catch {
    return false
  }
}

/**
 * 외부 링크 여부 확인
 */
export function isExternalUrl(url: string): boolean {
  try {
    const parsed = new URL(url, window.location.origin)
    return parsed.origin !== window.location.origin
  } catch {
    return false
  }
}
```

```vue
<!-- 안전한 링크 컴포넌트 -->
<script setup lang="ts">
import { computed } from 'vue'
import { isSafeUrl, isExternalUrl } from '@/utils/validate'

const props = defineProps<{ href: string; label: string }>()

const safeHref = computed(() => isSafeUrl(props.href) ? props.href : '#')
const isExternal = computed(() => isExternalUrl(props.href))
</script>

<template>
  <a
    :href="safeHref"
    :target="isExternal ? '_blank' : undefined"
    :rel="isExternal ? 'noopener noreferrer' : undefined"
  >
    {{ label }}
  </a>
</template>
```

#### 3.1.4 Content Security Policy

```html
<!-- index.html 또는 서버 응답 헤더로 설정 -->
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  font-src 'self';
  connect-src 'self' https://api.example.com;
  frame-src 'none';
  object-src 'none';
  base-uri 'self';
">
```

### 3.2 CSRF 방지

#### 3.2.1 axios 인터셉터 전체 설정

```ts
// src/api/client.ts
import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
  withCredentials: true, // 쿠키 전송 필수
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest', // AJAX 요청 식별
  },
})

// CSRF 토큰 인터셉터
apiClient.interceptors.request.use((config) => {
  // 방법 1: meta 태그에서 읽기
  const metaToken = document
    .querySelector('meta[name="csrf-token"]')
    ?.getAttribute('content')

  // 방법 2: 쿠키에서 읽기 (Django, Laravel 등)
  const cookieToken = document.cookie
    .split('; ')
    .find((row) => row.startsWith('XSRF-TOKEN='))
    ?.split('=')[1]

  const token = metaToken || (cookieToken ? decodeURIComponent(cookieToken) : null)

  if (token) {
    config.headers['X-CSRF-Token'] = token
    config.headers['X-XSRF-TOKEN'] = token
  }

  return config
})
```

#### 3.2.2 SameSite 쿠키 활용

```
서버 응답 헤더 예시:
Set-Cookie: session=abc123; SameSite=Strict; Secure; HttpOnly; Path=/
Set-Cookie: XSRF-TOKEN=xyz789; SameSite=Strict; Secure; Path=/
```

- **SameSite=Strict**: 외부 사이트에서의 모든 쿠키 전송 차단 (가장 안전)
- **SameSite=Lax**: GET 요청에서는 허용, POST 등에서는 차단 (기본값)
- 프론트엔드에서는 `withCredentials: true`로 쿠키 전송 보장

### 3.3 인증/인가 상세

#### 3.3.1 JWT 토큰 관리

```
httpOnly 쿠키 방식 (권장):
✅ XSS로 탈취 불가
✅ 자동 전송 (withCredentials)
❌ CSRF 취약 → CSRF 토큰 필요
❌ 모바일 앱 연동 어려움

localStorage 방식 (비권장):
❌ XSS로 탈취 가능
✅ CSRF 공격 면역
✅ 모바일/API 호환성
❌ 수동으로 헤더에 추가 필요
```

**결론: httpOnly 쿠키 + CSRF 토큰 조합을 권장**

#### 3.3.2 토큰 갱신 플로우 전체 구현

```ts
// src/api/client.ts 에 추가

let isRefreshing = false
let failedQueue: Array<{
  resolve: (token: string) => void
  reject: (error: unknown) => void
}> = []

function processQueue(error: unknown, token: string | null) {
  failedQueue.forEach(({ resolve, reject }) => {
    if (error) {
      reject(error)
    } else if (token) {
      resolve(token)
    }
  })
  failedQueue = []
}

apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    // 401이고 재시도하지 않은 요청
    if (error.response?.status === 401 && !originalRequest._retry) {
      // 이미 갱신 중이면 큐에 추가
      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        }).then(() => {
          return apiClient(originalRequest)
        })
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        // 토큰 갱신 요청 (httpOnly 쿠키 방식이면 쿠키가 자동 갱신됨)
        await apiClient.post('/auth/refresh')
        processQueue(null, 'refreshed')
        return apiClient(originalRequest)
      } catch (refreshError) {
        processQueue(refreshError, null)
        // 갱신 실패 시 로그아웃 처리
        window.location.href = '/login'
        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(error)
  },
)
```

#### 3.3.3 라우트 가드 전체 구현

```ts
// src/router/guards.ts
import type { Router } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'

// 라우트 메타 타입 확장
declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
    roles?: string[]
    title?: string
  }
}

export function setupRouteGuards(router: Router) {
  router.beforeEach(async (to, from) => {
    const authStore = useAuthStore()

    // 페이지 타이틀 설정
    document.title = (to.meta.title as string) || '앱 이름'

    // 인증 불필요 페이지
    if (!to.meta.requiresAuth) return true

    // 인증 상태 확인
    if (!authStore.isAuthenticated) {
      // 토큰이 쿠키에 있을 수 있으니 사용자 정보 조회 시도
      try {
        await authStore.fetchCurrentUser()
      } catch {
        return {
          name: 'Login',
          query: { redirect: to.fullPath },
        }
      }
    }

    // 역할 기반 접근 제어
    if (to.meta.roles && to.meta.roles.length > 0) {
      const hasRole = to.meta.roles.some((role) =>
        authStore.userRoles.includes(role),
      )
      if (!hasRole) {
        return { name: 'Forbidden' }
      }
    }

    return true
  })
}
```

```ts
// src/router/routes.ts
import type { RouteRecordRaw } from 'vue-router'

export const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomePage.vue'),
    meta: { title: '홈' },
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginPage.vue'),
    meta: { title: '로그인' },
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/views/DashboardPage.vue'),
    meta: { requiresAuth: true, title: '대시보드' },
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('@/views/AdminPage.vue'),
    meta: { requiresAuth: true, roles: ['admin'], title: '관리자' },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFoundPage.vue'),
  },
]
```

#### 3.3.4 권한별 컴포넌트 렌더링

```vue
<!-- src/components/base/AuthorizedView.vue -->
<script setup lang="ts">
import { computed } from 'vue'
import { useAuthStore } from '@/stores/useAuthStore'

interface Props {
  roles?: string[]
  permissions?: string[]
  fallback?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  roles: () => [],
  permissions: () => [],
  fallback: false,
})

const authStore = useAuthStore()

const isAuthorized = computed(() => {
  if (props.roles.length > 0) {
    return props.roles.some((role) => authStore.userRoles.includes(role))
  }
  if (props.permissions.length > 0) {
    return props.permissions.some((perm) => authStore.hasPermission(perm))
  }
  return authStore.isAuthenticated
})
</script>

<template>
  <slot v-if="isAuthorized" />
  <slot v-else-if="fallback" name="fallback">
    <p>접근 권한이 없습니다.</p>
  </slot>
</template>
```

사용 예시:

```vue
<AuthorizedView :roles="['admin', 'editor']" fallback>
  <AdminPanel />
  <template #fallback>
    <p>관리자만 접근할 수 있습니다.</p>
  </template>
</AuthorizedView>
```

### 3.4 입력 검증 상세

#### 3.4.1 Zod 스키마 정의 패턴

```ts
// src/types/schemas/user.schema.ts
import { z } from 'zod'

export const loginSchema = z.object({
  email: z
    .string()
    .min(1, '이메일을 입력해주세요.')
    .email('올바른 이메일 형식이 아닙니다.'),
  password: z
    .string()
    .min(8, '비밀번호는 8자 이상이어야 합니다.')
    .regex(
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
      '영문 대소문자와 숫자를 포함해야 합니다.',
    ),
})

export const registerSchema = loginSchema
  .extend({
    name: z.string().min(2, '이름은 2자 이상이어야 합니다.').max(50),
    confirmPassword: z.string(),
    agreeTerms: z.literal(true, {
      errorMap: () => ({ message: '이용약관에 동의해주세요.' }),
    }),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: '비밀번호가 일치하지 않습니다.',
    path: ['confirmPassword'],
  })

// 타입 추출
export type LoginForm = z.infer<typeof loginSchema>
export type RegisterForm = z.infer<typeof registerSchema>
```

#### 3.4.2 폼 검증 composable 구현

```ts
// src/composables/useFormValidation.ts
import { ref, reactive, computed } from 'vue'
import type { ZodSchema, ZodError } from 'zod'

export function useFormValidation<T extends Record<string, unknown>>(
  schema: ZodSchema<T>,
  initialValues: T,
) {
  const formData = reactive({ ...initialValues }) as T
  const errors = ref<Record<string, string>>({})
  const touched = ref<Set<string>>(new Set())
  const isSubmitting = ref(false)

  const isValid = computed(() => {
    const result = schema.safeParse(formData)
    return result.success
  })

  function validateField(field: keyof T) {
    touched.value.add(field as string)
    const result = schema.safeParse(formData)
    if (!result.success) {
      const fieldError = result.error.errors.find(
        (e) => e.path[0] === field,
      )
      if (fieldError) {
        errors.value[field as string] = fieldError.message
      } else {
        delete errors.value[field as string]
      }
    } else {
      delete errors.value[field as string]
    }
  }

  function validateAll(): boolean {
    const result = schema.safeParse(formData)
    if (!result.success) {
      const zodError = result.error as ZodError
      errors.value = {}
      zodError.errors.forEach((err) => {
        const field = err.path[0] as string
        if (field) {
          touched.value.add(field)
          errors.value[field] = err.message
        }
      })
      return false
    }
    errors.value = {}
    return true
  }

  function resetForm() {
    Object.assign(formData, initialValues)
    errors.value = {}
    touched.value.clear()
    isSubmitting.value = false
  }

  function getFieldError(field: keyof T): string | undefined {
    return touched.value.has(field as string)
      ? errors.value[field as string]
      : undefined
  }

  return {
    formData,
    errors,
    touched,
    isValid,
    isSubmitting,
    validateField,
    validateAll,
    resetForm,
    getFieldError,
  }
}
```

### 3.5 시크릿 관리

```bash
# .env.example (git에 커밋, 실제 값은 비움)
VITE_API_URL=
VITE_APP_TITLE=

# .env.development (로컬 개발, gitignore)
VITE_API_URL=http://localhost:3000/api
VITE_APP_TITLE=My App (Dev)

# .env.production (프로덕션, gitignore)
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My App
```

```ts
// src/env.d.ts - 환경변수 타입 선언
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

**규칙:**
- `VITE_` 접두사가 있는 변수만 클라이언트 번들에 포함됨
- API 키, DB 비밀번호 등 민감한 시크릿은 절대 `VITE_` 접두사를 붙이지 않음
- 서버 사이드에서만 접근해야 하는 시크릿은 백엔드 서버에서 관리
- `.env` 파일은 반드시 `.gitignore`에 포함
- CI/CD에서는 환경변수로 주입

### 3.6 의존성 보안

```bash
# 취약점 검사 (CI에 포함)
pnpm audit

# 자동 수정 가능한 취약점 수정
pnpm audit --fix

# 특정 패키지 버전 강제 (override)
# package.json
{
  "pnpm": {
    "overrides": {
      "vulnerable-package": ">=2.0.0"
    }
  }
}
```

**규칙:**
- `pnpm-lock.yaml`은 반드시 git에 커밋
- `pnpm audit`를 CI 파이프라인에 포함
- Renovate 또는 Dependabot으로 자동 업데이트 PR 생성
- 심각도 high 이상 취약점은 즉시 수정

### 3.7 클라이언트 사이드 보안

```ts
// eval 사용 금지
// Bad: eval(userInput)
// Bad: new Function(userInput)
// Bad: setTimeout(userInput, 0) - 문자열 전달

// postMessage 수신 시 origin 검증 필수
window.addEventListener('message', (event) => {
  const ALLOWED_ORIGINS = ['https://trusted-domain.com']
  if (!ALLOWED_ORIGINS.includes(event.origin)) return

  // 메시지 처리
})

// iframe 보안: 서버 헤더로 제어
// X-Frame-Options: DENY
// 또는 CSP: frame-ancestors 'none'
```

### 3.8 API 통신 보안

```ts
// HTTPS 강제 (프로덕션에서)
if (import.meta.env.PROD && location.protocol !== 'https:') {
  location.replace(`https://${location.host}${location.pathname}`)
}

// 요청/응답 로깅 주의 (개발 환경에서만)
if (import.meta.env.DEV) {
  apiClient.interceptors.request.use((config) => {
    console.log(`[API] ${config.method?.toUpperCase()} ${config.url}`)
    return config
  })
}
// 프로덕션에서 민감 데이터가 콘솔에 출력되지 않도록 주의
```

---

## 4. 생산성 가이드

### 4.1 Composable 패턴 상세

#### 4.1.1 useApi: API 호출 래퍼

```ts
// src/composables/useApi.ts
import { ref, shallowRef } from 'vue'
import type { ApiError } from '@/api/client'

interface UseApiReturn<T> {
  data: Ref<T | null>
  error: Ref<ApiError | null>
  isLoading: Ref<boolean>
  execute: (request: () => Promise<T>) => Promise<T | null>
  reset: () => void
}

export function useApi<T>(): UseApiReturn<T> {
  const data = shallowRef<T | null>(null)
  const error = ref<ApiError | null>(null)
  const isLoading = ref(false)

  async function execute(request: () => Promise<T>): Promise<T | null> {
    isLoading.value = true
    error.value = null

    try {
      const response = await request()
      data.value = response
      return response
    } catch (err) {
      error.value = err as ApiError
      return null
    } finally {
      isLoading.value = false
    }
  }

  function reset() {
    data.value = null
    error.value = null
    isLoading.value = false
  }

  return { data, error, isLoading, execute, reset }
}
```

#### 4.1.2 usePagination: 페이지네이션

```ts
// src/composables/usePagination.ts
import { ref, computed, watch } from 'vue'
import type { PaginatedResponse } from '@/types/common.types'

interface UsePaginationOptions<T> {
  fetcher: (page: number, perPage: number) => Promise<PaginatedResponse<T>>
  perPage?: number
  immediate?: boolean
}

export function usePagination<T>(options: UsePaginationOptions<T>) {
  const { fetcher, perPage = 20, immediate = true } = options

  const items = ref<T[]>([]) as Ref<T[]>
  const currentPage = ref(1)
  const lastPage = ref(1)
  const total = ref(0)
  const isLoading = ref(false)
  const error = ref<Error | null>(null)

  const hasNextPage = computed(() => currentPage.value < lastPage.value)
  const hasPrevPage = computed(() => currentPage.value > 1)

  async function fetchPage(page: number) {
    isLoading.value = true
    error.value = null

    try {
      const response = await fetcher(page, perPage)
      items.value = response.data
      currentPage.value = response.meta.currentPage
      lastPage.value = response.meta.lastPage
      total.value = response.meta.total
    } catch (err) {
      error.value = err as Error
    } finally {
      isLoading.value = false
    }
  }

  async function nextPage() {
    if (hasNextPage.value) await fetchPage(currentPage.value + 1)
  }

  async function prevPage() {
    if (hasPrevPage.value) await fetchPage(currentPage.value - 1)
  }

  async function goToPage(page: number) {
    if (page >= 1 && page <= lastPage.value) await fetchPage(page)
  }

  if (immediate) fetchPage(1)

  return {
    items,
    currentPage: computed(() => currentPage.value),
    lastPage: computed(() => lastPage.value),
    total: computed(() => total.value),
    hasNextPage,
    hasPrevPage,
    isLoading: computed(() => isLoading.value),
    error: computed(() => error.value),
    nextPage,
    prevPage,
    goToPage,
    refresh: () => fetchPage(currentPage.value),
  }
}
```

#### 4.1.3 useForm: 폼 관리

```ts
// src/composables/useForm.ts
import { reactive, ref, computed } from 'vue'

interface UseFormOptions<T extends Record<string, unknown>> {
  initialValues: T
  onSubmit: (values: T) => Promise<void>
}

export function useForm<T extends Record<string, unknown>>(
  options: UseFormOptions<T>,
) {
  const { initialValues, onSubmit } = options

  const values = reactive({ ...initialValues }) as T
  const isSubmitting = ref(false)
  const submitError = ref<string | null>(null)
  const isDirty = computed(() => {
    return Object.keys(initialValues).some(
      (key) => values[key as keyof T] !== initialValues[key as keyof T],
    )
  })

  async function handleSubmit() {
    if (isSubmitting.value) return

    isSubmitting.value = true
    submitError.value = null

    try {
      await onSubmit({ ...values })
    } catch (err) {
      submitError.value =
        err instanceof Error ? err.message : '제출 중 오류가 발생했습니다.'
    } finally {
      isSubmitting.value = false
    }
  }

  function resetForm() {
    Object.assign(values, initialValues)
    submitError.value = null
  }

  function setFieldValue<K extends keyof T>(field: K, value: T[K]) {
    values[field] = value
  }

  return {
    values,
    isSubmitting: computed(() => isSubmitting.value),
    submitError: computed(() => submitError.value),
    isDirty,
    handleSubmit,
    resetForm,
    setFieldValue,
  }
}
```

#### 4.1.4 useDebounce, useThrottle

```ts
// src/composables/useDebounce.ts
import { ref, watch, type Ref } from 'vue'
import { onUnmounted } from 'vue'

export function useDebounce<T>(source: Ref<T>, delay: number = 300): Ref<T> {
  const debounced = ref(source.value) as Ref<T>
  let timeoutId: ReturnType<typeof setTimeout>

  watch(source, (newValue) => {
    clearTimeout(timeoutId)
    timeoutId = setTimeout(() => {
      debounced.value = newValue
    }, delay)
  })

  onUnmounted(() => clearTimeout(timeoutId))

  return debounced
}

// src/composables/useThrottle.ts
export function useThrottle<T>(source: Ref<T>, interval: number = 300): Ref<T> {
  const throttled = ref(source.value) as Ref<T>
  let lastTime = 0

  watch(source, (newValue) => {
    const now = Date.now()
    if (now - lastTime >= interval) {
      throttled.value = newValue
      lastTime = now
    }
  })

  return throttled
}
```

#### 4.1.5 useIntersectionObserver

```ts
// src/composables/useIntersectionObserver.ts
import { ref, onUnmounted, watch, type Ref } from 'vue'

interface UseIntersectionObserverOptions {
  threshold?: number | number[]
  rootMargin?: string
}

export function useIntersectionObserver(
  target: Ref<HTMLElement | null>,
  callback: (isIntersecting: boolean) => void,
  options: UseIntersectionObserverOptions = {},
) {
  const { threshold = 0, rootMargin = '0px' } = options
  const isIntersecting = ref(false)
  let observer: IntersectionObserver | null = null

  function cleanup() {
    if (observer) {
      observer.disconnect()
      observer = null
    }
  }

  watch(target, (el) => {
    cleanup()
    if (!el) return

    observer = new IntersectionObserver(
      ([entry]) => {
        isIntersecting.value = entry.isIntersecting
        callback(entry.isIntersecting)
      },
      { threshold, rootMargin },
    )

    observer.observe(el)
  }, { immediate: true })

  onUnmounted(cleanup)

  return { isIntersecting }
}
```

### 4.2 컴포넌트 설계 원칙 상세

#### 4.2.1 Props/Emits 단방향 데이터 플로우

```vue
<!-- 부모: 데이터 소유, 자식에게 전달 -->
<template>
  <UserEditor
    :user="currentUser"
    @update="handleUpdate"
    @cancel="showEditor = false"
  />
</template>

<!-- 자식: Props를 읽기 전용으로 사용, emit으로 변경 요청 -->
<script setup lang="ts">
import type { User } from '@/types/user.types'

const props = defineProps<{ user: User }>()
const emit = defineEmits<{
  'update': [user: User]
  'cancel': []
}>()

// Props를 직접 수정하지 않고 로컬 복사본 사용
const localUser = ref({ ...props.user })

function handleSave() {
  emit('update', { ...localUser.value })
}
</script>
```

#### 4.2.2 Slot 패턴

```vue
<!-- Named Slot -->
<template>
  <div class="card">
    <header class="card__header">
      <slot name="header" />
    </header>
    <main class="card__body">
      <slot />  <!-- default slot -->
    </main>
    <footer class="card__footer">
      <slot name="footer" />
    </footer>
  </div>
</template>

<!-- Scoped Slot: 자식이 부모에게 데이터 전달 -->
<script setup lang="ts" generic="T extends { id: number }">
const props = defineProps<{ items: T[] }>()
</script>

<template>
  <ul>
    <li v-for="(item, index) in items" :key="item.id">
      <slot :item="item" :index="index" />
    </li>
  </ul>
</template>

<!-- 사용: -->
<GenericList :items="users">
  <template #default="{ item, index }">
    <span>{{ index + 1 }}. {{ item.name }}</span>
  </template>
</GenericList>
```

#### 4.2.3 Renderless Component 패턴

```vue
<!-- src/components/base/RenderlessToggle.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const isOpen = ref(false)

function toggle() { isOpen.value = !isOpen.value }
function open() { isOpen.value = true }
function close() { isOpen.value = false }
</script>

<template>
  <slot :is-open="isOpen" :toggle="toggle" :open="open" :close="close" />
</template>

<!-- 사용: UI를 완전히 자유롭게 구성 -->
<RenderlessToggle v-slot="{ isOpen, toggle }">
  <button @click="toggle">{{ isOpen ? '닫기' : '열기' }}</button>
  <div v-show="isOpen">토글 콘텐츠</div>
</RenderlessToggle>
```

#### 4.2.4 provide/inject 패턴

```ts
// src/composables/useTheme.ts
import { provide, inject, ref, type InjectionKey, type Ref } from 'vue'

type Theme = 'light' | 'dark'

interface ThemeContext {
  theme: Readonly<Ref<Theme>>
  toggleTheme: () => void
}

export const ThemeKey: InjectionKey<ThemeContext> = Symbol('Theme')

// Provider 측에서 호출
export function provideTheme() {
  const theme = ref<Theme>('light')
  const toggleTheme = () => {
    theme.value = theme.value === 'light' ? 'dark' : 'light'
  }
  provide(ThemeKey, { theme: readonly(theme), toggleTheme })
  return { theme, toggleTheme }
}

// Consumer 측에서 호출
export function useTheme(): ThemeContext {
  const context = inject(ThemeKey)
  if (!context) throw new Error('useTheme must be used within a ThemeProvider')
  return context
}
```

#### 4.2.5 동적 컴포넌트 및 Teleport

```vue
<!-- 동적 컴포넌트 -->
<script setup lang="ts">
import { shallowRef } from 'vue'
import TabHome from './TabHome.vue'
import TabProfile from './TabProfile.vue'
import TabSettings from './TabSettings.vue'

const tabs = { home: TabHome, profile: TabProfile, settings: TabSettings }
const activeTab = shallowRef<keyof typeof tabs>('home')
</script>

<template>
  <component :is="tabs[activeTab]" />
</template>

<!-- Teleport: DOM 트리 외부에 렌더링 -->
<Teleport to="body">
  <div v-if="showModal" class="modal-overlay">
    <div class="modal-content">
      <slot />
    </div>
  </div>
</Teleport>
```

### 4.3 Pinia 상태 관리 상세

#### 4.3.1 Setup Store 전체 패턴

```ts
// src/stores/useAuthStore.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/endpoints/auth.api'
import type { User } from '@/types/user.types'

export const useAuthStore = defineStore('auth', () => {
  // ---- State ----
  const user = ref<User | null>(null)
  const isLoading = ref(false)

  // ---- Getters (computed) ----
  const isAuthenticated = computed(() => user.value !== null)
  const userRoles = computed(() => user.value?.roles ?? [])
  const userId = computed(() => user.value?.id ?? null)

  function hasPermission(permission: string): boolean {
    return user.value?.permissions?.includes(permission) ?? false
  }

  // ---- Actions ----
  async function login(email: string, password: string) {
    isLoading.value = true
    try {
      const response = await authApi.login({ email, password })
      user.value = response.data.user
    } finally {
      isLoading.value = false
    }
  }

  async function logout() {
    await authApi.logout()
    user.value = null
  }

  async function fetchCurrentUser() {
    const response = await authApi.me()
    user.value = response.data
  }

  // ---- 반환: 외부에서 접근 가능한 것만 ----
  return {
    user: computed(() => user.value),
    isLoading: computed(() => isLoading.value),
    isAuthenticated,
    userRoles,
    userId,
    hasPermission,
    login,
    logout,
    fetchCurrentUser,
  }
})
```

#### 4.3.2 Store 사용 (storeToRefs)

```vue
<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/useAuthStore'

const authStore = useAuthStore()

// 반응형 상태는 storeToRefs로 구조분해
const { user, isAuthenticated, isLoading } = storeToRefs(authStore)

// 액션은 직접 구조분해 (함수이므로 반응성 불필요)
const { login, logout } = authStore
</script>
```

#### 4.3.3 Pinia 플러그인: persistedstate

```ts
// src/main.ts
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

// store에서 persist 옵션 추가
export const useUiStore = defineStore('ui', () => {
  const sidebarOpen = ref(true)
  const theme = ref<'light' | 'dark'>('light')
  return { sidebarOpen, theme }
}, {
  persist: {
    pick: ['theme'], // theme만 localStorage에 저장
  },
})
```

### 4.4 Vue Router 상세

#### 4.4.1 네스티드 라우팅과 동적 라우팅

```ts
const routes: RouteRecordRaw[] = [
  {
    path: '/users',
    component: () => import('@/views/users/UsersLayout.vue'),
    children: [
      {
        path: '',
        name: 'UserList',
        component: () => import('@/views/users/UserListPage.vue'),
      },
      {
        path: ':id(\\d+)', // 숫자만 매칭
        name: 'UserDetail',
        component: () => import('@/views/users/UserDetailPage.vue'),
        props: (route) => ({ userId: Number(route.params.id) }),
      },
      {
        path: ':id(\\d+)/edit',
        name: 'UserEdit',
        component: () => import('@/views/users/UserEditPage.vue'),
        meta: { requiresAuth: true, roles: ['admin'] },
      },
    ],
  },
]
```

#### 4.4.2 스크롤 동작

```ts
// src/router/index.ts
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition // 뒤로가기: 이전 스크롤 위치
    if (to.hash) return { el: to.hash, behavior: 'smooth' } // 해시 앵커
    return { top: 0, behavior: 'smooth' } // 새 페이지: 최상단
  },
})
```

### 4.5 테스트 전략 상세

#### 4.5.1 Vitest 설정

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'jsdom',
    include: ['src/**/*.spec.ts', 'tests/**/*.spec.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      include: ['src/**/*.{ts,vue}'],
      exclude: ['src/**/*.spec.ts', 'src/types/**', 'src/main.ts'],
      thresholds: {
        statements: 80,
        branches: 75,
        functions: 80,
        lines: 80,
      },
    },
    setupFiles: ['./tests/setup.ts'],
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
```

#### 4.5.2 컴포넌트 테스트

```ts
// src/components/domain/user/UserCard.spec.ts
import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import UserCard from './UserCard.vue'

describe('UserCard', () => {
  const defaultProps = {
    user: { id: 1, name: '홍길동', email: 'hong@test.com' },
  }

  it('사용자 이름을 렌더링한다', () => {
    const wrapper = mount(UserCard, { props: defaultProps })
    expect(wrapper.text()).toContain('홍길동')
  })

  it('클릭 시 select 이벤트를 emit한다', async () => {
    const wrapper = mount(UserCard, { props: defaultProps })
    await wrapper.trigger('click')
    expect(wrapper.emitted('select')).toHaveLength(1)
    expect(wrapper.emitted('select')![0]).toEqual([defaultProps.user])
  })

  it('삭제 버튼 클릭 시 delete 이벤트를 emit한다', async () => {
    const wrapper = mount(UserCard, { props: defaultProps })
    await wrapper.find('[data-testid="delete-btn"]').trigger('click')
    expect(wrapper.emitted('delete')).toHaveLength(1)
  })
})
```

#### 4.5.3 Composable 테스트

```ts
// src/composables/useDebounce.spec.ts
import { describe, it, expect, vi } from 'vitest'
import { ref, nextTick } from 'vue'
import { useDebounce } from './useDebounce'

describe('useDebounce', () => {
  it('지정된 지연 후에 값을 업데이트한다', async () => {
    vi.useFakeTimers()

    const source = ref('initial')
    const debounced = useDebounce(source, 300)

    expect(debounced.value).toBe('initial')

    source.value = 'updated'
    await nextTick()
    expect(debounced.value).toBe('initial') // 아직 변경 안됨

    vi.advanceTimersByTime(300)
    await nextTick()
    expect(debounced.value).toBe('updated') // 300ms 후 변경

    vi.useRealTimers()
  })
})
```

#### 4.5.4 Store 테스트

```ts
// src/stores/useAuthStore.spec.ts
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useAuthStore } from './useAuthStore'

vi.mock('@/api/endpoints/auth.api', () => ({
  authApi: {
    login: vi.fn(),
    logout: vi.fn(),
    me: vi.fn(),
  },
}))

describe('useAuthStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('초기 상태는 미인증이다', () => {
    const store = useAuthStore()
    expect(store.isAuthenticated).toBe(false)
    expect(store.user).toBeNull()
  })

  it('로그인 성공 시 user가 설정된다', async () => {
    const { authApi } = await import('@/api/endpoints/auth.api')
    vi.mocked(authApi.login).mockResolvedValue({
      data: { user: { id: 1, name: 'Test' } },
    })

    const store = useAuthStore()
    await store.login('test@test.com', 'password')

    expect(store.isAuthenticated).toBe(true)
  })
})
```

#### 4.5.5 MSW로 API 모킹

```ts
// tests/mocks/handlers.ts
import { http, HttpResponse } from 'msw'

export const handlers = [
  http.get('/api/users', () => {
    return HttpResponse.json({
      data: [
        { id: 1, name: '홍길동' },
        { id: 2, name: '김영희' },
      ],
    })
  }),

  http.post('/api/auth/login', async ({ request }) => {
    const body = await request.json() as { email: string }
    if (body.email === 'test@test.com') {
      return HttpResponse.json({
        data: { user: { id: 1, name: 'Test User' } },
      })
    }
    return HttpResponse.json(
      { message: '인증 실패' },
      { status: 401 },
    )
  }),
]

// tests/setup.ts
import { setupServer } from 'msw/node'
import { handlers } from './mocks/handlers'

export const server = setupServer(...handlers)

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())
```

### 4.6 ESLint + Prettier 설정

```js
// eslint.config.js (ESLint 9 flat config)
import js from '@eslint/js'
import tseslint from 'typescript-eslint'
import pluginVue from 'eslint-plugin-vue'
import vueParser from 'vue-eslint-parser'

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs['flat/recommended'],
  {
    files: ['**/*.vue'],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        parser: tseslint.parser,
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
    },
  },
  {
    rules: {
      'vue/multi-word-component-names': 'error',
      'vue/no-v-html': 'warn',
      'vue/component-api-style': ['error', ['script-setup']],
      'vue/define-macros-order': ['error', {
        order: ['defineProps', 'defineEmits', 'defineModel'],
      }],
      '@typescript-eslint/no-unused-vars': ['error', {
        argsIgnorePattern: '^_',
      }],
      '@typescript-eslint/consistent-type-imports': ['error', {
        prefer: 'type-imports',
      }],
      'no-console': ['warn', { allow: ['warn', 'error'] }],
    },
  },
]
```

```json
// .prettierrc
{
  "semi": false,
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100,
  "tabWidth": 2,
  "arrowParens": "always",
  "endOfLine": "lf",
  "vueIndentScriptAndStyle": false
}
```

### 4.7 CLI 명령어 전체 리스트

```bash
# 개발
pnpm dev                    # 개발 서버 시작 (HMR, 기본 5173 포트)
pnpm dev --host             # 네트워크에 노출 (모바일 테스트)
pnpm dev --port 3000        # 포트 변경

# 빌드
pnpm build                  # 프로덕션 빌드
pnpm preview                # 빌드 결과 로컬 서버로 확인

# 테스트
pnpm test                   # Vitest 실행 (watch 모드)
pnpm test:run               # Vitest 단일 실행
pnpm test:coverage          # 커버리지 리포트 생성
pnpm test:e2e               # Playwright E2E 테스트
pnpm test:e2e --ui          # Playwright UI 모드

# 코드 품질
pnpm lint                   # ESLint 검사
pnpm lint --fix             # ESLint 자동 수정
pnpm format                 # Prettier 포매팅
pnpm type-check             # vue-tsc 타입 검사

# 의존성
pnpm install                # 의존성 설치
pnpm add <package>          # 패키지 추가
pnpm add -D <package>       # 개발 의존성 추가
pnpm audit                  # 보안 취약점 검사
pnpm outdated               # 업데이트 가능한 패키지 확인

# 분석
npx vite-bundle-visualizer  # 번들 크기 시각화
```

---

## 5. 성능 최적화

### 5.1 코드 스플리팅 / 레이지 로딩

#### 5.1.1 라우트 레이지 로딩

```ts
// 모든 라우트 컴포넌트는 동적 import 사용
const routes: RouteRecordRaw[] = [
  {
    path: '/dashboard',
    // Vite가 자동으로 별도 청크로 분리
    component: () => import('@/views/DashboardPage.vue'),
  },
  {
    path: '/admin',
    // webpackChunkName에 해당하는 Vite 매직 코멘트 (선택적)
    component: () => import(/* @vite-ignore */ '@/views/AdminPage.vue'),
  },
]
```

#### 5.1.2 defineAsyncComponent

```ts
import { defineAsyncComponent } from 'vue'

// 기본 사용
const HeavyChart = defineAsyncComponent(
  () => import('@/components/domain/chart/HeavyChart.vue'),
)

// 로딩/에러 상태 처리
const AsyncChart = defineAsyncComponent({
  loader: () => import('@/components/domain/chart/HeavyChart.vue'),
  loadingComponent: () => import('@/components/base/LoadingSpinner.vue'),
  errorComponent: () => import('@/components/base/ErrorFallback.vue'),
  delay: 200,    // 200ms 내 로드 완료 시 로딩 컴포넌트 미표시
  timeout: 10000, // 10초 초과 시 에러 컴포넌트 표시
})
```

#### 5.1.3 동적 import 패턴

```ts
// 무거운 라이브러리는 사용 시점에 동적 import
async function renderMarkdown(content: string) {
  const { marked } = await import('marked')
  return marked.parse(content)
}

// 조건부 모듈 로딩
async function initializeEditor(type: 'simple' | 'rich') {
  if (type === 'rich') {
    const { Editor } = await import('@tiptap/vue-3')
    return new Editor({ /* config */ })
  }
  return null
}
```

#### 5.1.4 Prefetching / Preloading 전략

```vue
<!-- 라우터 링크에 마우스 호버 시 프리페치 -->
<script setup lang="ts">
import { ref } from 'vue'

const prefetchedRoutes = new Set<string>()

function handleMouseEnter(routePath: string) {
  if (prefetchedRoutes.has(routePath)) return
  prefetchedRoutes.add(routePath)
  // 라우트 컴포넌트 미리 로딩
  import(`../views/${routePath}.vue`)
}
</script>
```

```ts
// Vite의 자동 프리페치/프리로드 활용
// vite.config.ts에서 별도 설정 불필요 - 기본적으로 동적 import 청크에 대해
// <link rel="modulepreload"> 자동 생성
```

### 5.2 렌더링 최적화

#### 5.2.1 v-once, v-memo

```vue
<template>
  <!-- v-once: 절대 변하지 않는 정적 콘텐츠 -->
  <header v-once>
    <h1>{{ appTitle }}</h1>
    <p>{{ appDescription }}</p>
  </header>

  <!-- v-memo: 특정 의존성이 변할 때만 재렌더링 (Vue 3.2+) -->
  <div v-for="item in list" :key="item.id" v-memo="[item.id === selected]">
    <p>{{ item.name }}</p>
    <span :class="{ active: item.id === selected }">
      {{ item.id === selected ? '선택됨' : '' }}
    </span>
  </div>
</template>
```

#### 5.2.2 shallowRef / shallowReactive

```ts
// 대량 데이터에 깊은 반응성이 불필요한 경우
import { shallowRef, triggerRef } from 'vue'

// Bad: 깊은 반응성 (수천 개 객체의 모든 프로퍼티를 추적)
const hugeList = ref<Item[]>([])

// Good: 얕은 반응성 (배열 자체의 교체만 추적)
const hugeList = shallowRef<Item[]>([])

// 갱신 시: 배열을 새로 할당
hugeList.value = [...hugeList.value, newItem]

// 또는 내부 변경 후 수동 트리거
hugeList.value.push(newItem)
triggerRef(hugeList)
```

#### 5.2.3 computed vs method vs watch 선택 기준

```ts
// computed: 의존 데이터로부터 파생된 값 (캐시됨, 의존값 변경 시만 재계산)
const fullName = computed(() => `${first.value} ${last.value}`)

// method: 이벤트 핸들러 또는 매번 실행해야 하는 로직
function handleSubmit() { /* ... */ }

// watch: 사이드 이펙트 (API 호출, DOM 조작, 로깅 등)
watch(userId, async (newId) => {
  await fetchUserDetails(newId)
})

// watchEffect: 의존성을 자동 추적하는 사이드 이펙트
watchEffect(() => {
  document.title = `${userName.value} - Dashboard`
})
```

#### 5.2.4 가상 스크롤

```vue
<!-- vue-virtual-scroller 사용 (1000개 이상 아이템) -->
<script setup lang="ts">
import { RecycleScroller } from 'vue-virtual-scroller'
import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'
</script>

<template>
  <RecycleScroller
    :items="hugeList"
    :item-size="50"
    key-field="id"
    v-slot="{ item }"
  >
    <div class="list-item">{{ item.name }}</div>
  </RecycleScroller>
</template>
```

#### 5.2.5 KeepAlive 활용

```vue
<!-- 탭 전환 시 컴포넌트 상태 보존 -->
<template>
  <KeepAlive :include="['DashboardPage', 'ProfilePage']" :max="5">
    <component :is="currentTab" />
  </KeepAlive>
</template>

<!-- KeepAlive 내부 컴포넌트에서 활성화/비활성화 훅 사용 -->
<script setup lang="ts">
import { onActivated, onDeactivated } from 'vue'

onActivated(() => {
  // 캐시에서 복원될 때 데이터 갱신
  refreshData()
})

onDeactivated(() => {
  // 캐시로 들어갈 때 정리
})
</script>
```

### 5.3 API / 데이터 최적화

#### 5.3.1 TanStack Query (vue-query)

```ts
// src/plugins/queryClient.ts
import { QueryClient, VueQueryPlugin } from '@tanstack/vue-query'

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000,      // 5분간 fresh 상태
      gcTime: 10 * 60 * 1000,         // 10분 후 가비지 컬렉션
      retry: 2,
      refetchOnWindowFocus: false,
    },
  },
})

// main.ts에서 등록
app.use(VueQueryPlugin, { queryClient })
```

```vue
<!-- 컴포넌트에서 사용 -->
<script setup lang="ts">
import { useQuery, useMutation, useQueryClient } from '@tanstack/vue-query'
import { userApi } from '@/api/endpoints/user.api'

// 데이터 조회 (자동 캐싱, 재시도, 갱신)
const { data: users, isLoading, error } = useQuery({
  queryKey: ['users'],
  queryFn: () => userApi.getAll(),
})

// 데이터 변경 + 옵티미스틱 업데이트
const queryClient = useQueryClient()

const { mutate: deleteUser } = useMutation({
  mutationFn: (id: number) => userApi.delete(id),
  onMutate: async (deletedId) => {
    await queryClient.cancelQueries({ queryKey: ['users'] })
    const previous = queryClient.getQueryData(['users'])

    queryClient.setQueryData(['users'], (old: User[]) =>
      old.filter((u) => u.id !== deletedId),
    )

    return { previous }
  },
  onError: (_err, _id, context) => {
    queryClient.setQueryData(['users'], context?.previous)
  },
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ['users'] })
  },
})
</script>
```

#### 5.3.2 Infinite Scroll 구현

```vue
<script setup lang="ts">
import { useInfiniteQuery } from '@tanstack/vue-query'
import { useIntersectionObserver } from '@/composables/useIntersectionObserver'
import { ref } from 'vue'

const loadMoreRef = ref<HTMLElement | null>(null)

const {
  data,
  fetchNextPage,
  hasNextPage,
  isFetchingNextPage,
} = useInfiniteQuery({
  queryKey: ['products'],
  queryFn: ({ pageParam = 1 }) => productApi.getAll(pageParam),
  getNextPageParam: (lastPage) =>
    lastPage.meta.currentPage < lastPage.meta.lastPage
      ? lastPage.meta.currentPage + 1
      : undefined,
  initialPageParam: 1,
})

useIntersectionObserver(loadMoreRef, (isIntersecting) => {
  if (isIntersecting && hasNextPage.value && !isFetchingNextPage.value) {
    fetchNextPage()
  }
})

const allItems = computed(() =>
  data.value?.pages.flatMap((page) => page.data) ?? [],
)
</script>

<template>
  <div v-for="item in allItems" :key="item.id">
    {{ item.name }}
  </div>
  <div ref="loadMoreRef">
    <span v-if="isFetchingNextPage">로딩 중...</span>
  </div>
</template>
```

#### 5.3.3 WebSocket / SSE 연동

```ts
// src/composables/useWebSocket.ts
import { ref, onUnmounted } from 'vue'

export function useWebSocket(url: string) {
  const data = ref<unknown>(null)
  const isConnected = ref(false)
  let ws: WebSocket | null = null
  let reconnectTimer: ReturnType<typeof setTimeout>

  function connect() {
    ws = new WebSocket(url)

    ws.onopen = () => { isConnected.value = true }

    ws.onmessage = (event) => {
      data.value = JSON.parse(event.data)
    }

    ws.onclose = () => {
      isConnected.value = false
      reconnectTimer = setTimeout(connect, 3000) // 자동 재연결
    }

    ws.onerror = () => { ws?.close() }
  }

  function send(payload: unknown) {
    if (ws?.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(payload))
    }
  }

  function disconnect() {
    clearTimeout(reconnectTimer)
    ws?.close()
  }

  connect()

  onUnmounted(disconnect)

  return { data, isConnected, send, disconnect }
}
```

### 5.4 이미지/에셋 최적화

```vue
<!-- 반응형 이미지 + lazy loading -->
<template>
  <img
    :src="imageUrl"
    :srcset="`
      ${imageUrl}?w=400 400w,
      ${imageUrl}?w=800 800w,
      ${imageUrl}?w=1200 1200w
    `"
    sizes="(max-width: 640px) 400px, (max-width: 1024px) 800px, 1200px"
    loading="lazy"
    decoding="async"
    :alt="altText"
    :width="width"
    :height="height"
  />
</template>
```

```ts
// vite.config.ts 에셋 처리
export default defineConfig({
  build: {
    assetsInlineLimit: 4096, // 4KB 이하 파일은 base64 인라인
  },
})
```

**폰트 최적화:**

```css
/* 폰트 preload (index.html) */
/* <link rel="preload" href="/fonts/NotoSansKR.woff2" as="font" type="font/woff2" crossorigin> */

@font-face {
  font-family: 'Noto Sans KR';
  font-weight: 400;
  font-display: swap; /* FOUT 허용으로 LCP 개선 */
  src: url('/fonts/NotoSansKR-Regular.woff2') format('woff2');
  unicode-range: U+AC00-D7A3; /* 한글만 서브셋 */
}
```

### 5.5 번들 최적화

#### 5.5.1 Vite 빌드 설정

```ts
// vite.config.ts
export default defineConfig({
  build: {
    target: 'es2022',
    sourcemap: true,
    cssCodeSplit: true,
    rollupOptions: {
      output: {
        manualChunks(id) {
          // node_modules를 vendor 청크로 분리
          if (id.includes('node_modules')) {
            if (id.includes('vue') || id.includes('pinia') || id.includes('vue-router')) {
              return 'vendor-vue'
            }
            if (id.includes('@tanstack')) {
              return 'vendor-query'
            }
            return 'vendor'
          }
        },
      },
    },
    chunkSizeWarningLimit: 500, // 500KB 이상 청크 경고
  },
})
```

#### 5.5.2 Tree Shaking 보장

```ts
// package.json에서 sideEffects 설정
{
  "sideEffects": ["*.css", "*.vue"]
}

// import 시 named import 사용 (tree-shaking 가능)
// Good:
import { debounce } from 'lodash-es'

// Bad (전체 번들 포함):
import _ from 'lodash'
```

#### 5.5.3 번들 분석

```bash
# 번들 크기 시각화
npx vite-bundle-visualizer

# 초기 로딩 성능 목표치:
# - 초기 JS: 200KB (gzip) 이하
# - 초기 CSS: 50KB (gzip) 이하
# - LCP: 2.5초 이내
# - FID: 100ms 이내
# - CLS: 0.1 이하
```

### 5.6 Core Web Vitals 최적화

```
LCP (Largest Contentful Paint) - 2.5초 이내:
- 이미지 preload, 적절한 sizes/srcset
- 서버 응답 시간 최소화
- CSS/JS 렌더 블로킹 최소화
- font-display: swap

FID (First Input Delay) / INP - 100ms 이내:
- 메인 스레드 블로킹 최소화
- 무거운 연산은 Web Worker로 분리
- 코드 스플리팅으로 초기 JS 최소화
- 긴 작업(Long Task)은 requestIdleCallback으로 분할

CLS (Cumulative Layout Shift) - 0.1 이하:
- 이미지/비디오에 width/height 명시
- 동적 콘텐츠 삽입 시 공간 미리 확보
- 폰트 로딩으로 인한 레이아웃 시프트 방지 (font-display: optional)
- transform 애니메이션 사용 (top/left 대신)
```

```ts
// 성능 측정: web-vitals 라이브러리 활용
import { onCLS, onFID, onLCP, onFCP, onTTFB } from 'web-vitals'

function reportMetric(metric: { name: string; value: number }) {
  // 분석 서비스로 전송
  console.log(`[Perf] ${metric.name}: ${metric.value}`)
}

onCLS(reportMetric)
onFID(reportMetric)
onLCP(reportMetric)
onFCP(reportMetric)
onTTFB(reportMetric)
```

---

## 6. 주의사항 / Gotchas

### 6.1 reactive() 구조분해 시 반응성 소실

```ts
// Bad: 반응성 소실
const state = reactive({ count: 0, name: 'Vue' })
const { count, name } = state // count, name은 일반 값
count++ // 반응성 없음

// Good: toRefs() 사용
const { count, name } = toRefs(state) // count, name은 Ref
count.value++ // 반응성 유지

// Good: ref 사용 (권장)
const count = ref(0) // 처음부터 ref 사용
```

### 6.2 watch 소스 실수

```ts
const count = ref(0)

// Bad: .value를 전달하면 watch 시점의 값(숫자)이 됨
watch(count.value, (newVal) => { /* ... */ }) // 동작 안함

// Good: ref 자체를 전달
watch(count, (newVal) => { /* ... */ })

// Good: getter 함수로 전달
watch(() => count.value, (newVal) => { /* ... */ })

// reactive 객체의 특정 프로퍼티 감시
const state = reactive({ nested: { count: 0 } })

// Bad: 값을 직접 전달
watch(state.nested.count, () => {}) // 동작 안함

// Good: getter 함수
watch(() => state.nested.count, (newVal) => { /* ... */ })

// 깊은 감시가 필요한 경우
watch(() => state.nested, (newVal) => { /* ... */ }, { deep: true })
```

### 6.3 v-for + v-if 충돌

```vue
<!-- Bad: 같은 요소에 v-for + v-if (Vue 3에서 v-if가 우선, item 미정의 에러) -->
<li v-for="item in items" v-if="item.isActive" :key="item.id">
  {{ item.name }}
</li>

<!-- Good: computed로 필터링 -->
<script setup>
const activeItems = computed(() => items.value.filter(i => i.isActive))
</script>
<template>
  <li v-for="item in activeItems" :key="item.id">
    {{ item.name }}
  </li>
</template>

<!-- Good: template 태그로 분리 -->
<template v-for="item in items" :key="item.id">
  <li v-if="item.isActive">{{ item.name }}</li>
</template>
```

### 6.4 Props 읽기 전용 위반

```ts
const props = defineProps<{ user: User }>()

// Bad: Props 직접 수정 (런타임 경고)
props.user.name = 'New Name'

// Good: 로컬 복사본 사용
const localUser = ref({ ...props.user })

// Good: emit으로 부모에게 변경 요청
emit('update:user', { ...props.user, name: 'New Name' })
```

### 6.5 ref vs reactive 선택 기준

```ts
// ref 권장 (기본 선택):
// - 원시값 (string, number, boolean)
// - 값을 완전히 교체해야 하는 경우 (배열, 객체 재할당)
// - composable에서 반환할 때
const count = ref(0)
const items = ref<Item[]>([])
items.value = newItems // 전체 교체 가능

// reactive 사용 시점:
// - 구조가 고정된 객체 (폼 데이터 등)
// - 절대 재할당하지 않는 경우
const formData = reactive({
  name: '',
  email: '',
  password: '',
})
```

### 6.6 nextTick 필요 상황

```ts
import { nextTick } from 'vue'

// DOM 업데이트 후 접근이 필요한 경우
const message = ref('Hello')
message.value = 'Updated'

// Bad: DOM이 아직 업데이트되지 않음
console.log(document.getElementById('msg')?.textContent) // 'Hello'

// Good: DOM 업데이트 완료 후 실행
await nextTick()
console.log(document.getElementById('msg')?.textContent) // 'Updated'

// 주의: nextTick 남용 금지. 대부분 computed나 watch로 해결 가능
// nextTick이 필요한 경우: 서드파티 DOM 라이브러리 연동, 포커스 설정 등
```

### 6.7 Composition API에서의 this

```ts
// script setup에서는 this가 존재하지 않음
// Bad (에러):
onMounted(() => {
  // this.fetchData() // TypeError: this is undefined
})

// Good:
onMounted(() => {
  fetchData()
})
```

### 6.8 Template Refs 타이핑

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

// HTML 요소 ref
const inputRef = ref<HTMLInputElement | null>(null)

// 컴포넌트 ref
const childRef = ref<InstanceType<typeof ChildComponent> | null>(null)

onMounted(() => {
  inputRef.value?.focus()
  childRef.value?.someMethod()
})
</script>

<template>
  <input ref="inputRef" />
  <ChildComponent ref="childRef" />
</template>
```

### 6.9 비동기 컴포넌트 에러 처리

```vue
<script setup lang="ts">
import { defineAsyncComponent } from 'vue'

const AsyncComp = defineAsyncComponent({
  loader: () => import('./HeavyComponent.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorFallback,
  delay: 200,
  timeout: 10000,
  onError(error, retry, fail, attempts) {
    // 네트워크 에러이고 3회 미만 시도면 재시도
    if (error.message.includes('fetch') && attempts <= 3) {
      retry()
    } else {
      fail()
    }
  },
})
</script>
```

### 6.10 메모리 누수 방지

```ts
// 이벤트 리스너: 반드시 onUnmounted에서 해제
onMounted(() => {
  window.addEventListener('resize', handleResize)
})
onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

// setInterval / setTimeout: 반드시 정리
const intervalId = ref<ReturnType<typeof setInterval>>()
onMounted(() => {
  intervalId.value = setInterval(pollData, 5000)
})
onUnmounted(() => {
  if (intervalId.value) clearInterval(intervalId.value)
})

// AbortController: 진행 중인 API 호출 취소
const controller = new AbortController()
onUnmounted(() => {
  controller.abort()
})
```

### 6.11 Vue 3.4+ 주요 변경사항

```ts
// defineModel (3.4+): v-model 매크로 간소화
// 이전:
const props = defineProps<{ modelValue: string }>()
const emit = defineEmits<{ 'update:modelValue': [value: string] }>()
// computed + emit 조합 필요

// 3.4+:
const model = defineModel<string>()
// model.value로 직접 읽기/쓰기, 양방향 바인딩 자동 처리

// Generic 컴포넌트 (3.3+):
// <script setup lang="ts" generic="T extends Record<string, unknown>">

// Improved hydration mismatch 경고 (3.4+):
// 서버/클라이언트 불일치 시 더 자세한 경고 메시지 제공

// v-bind 축약 (3.4+):
// <img :id="id"> 와 동일: <img :id>
```

---

> 이 가이드는 Vue 3.4+ / TypeScript 5.x / Vite 5.x / Pinia 2.x 기준으로 작성되었습니다.
> 프로젝트에 맞게 조정하여 사용하세요.
