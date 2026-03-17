---
title: Next.js에서 react-hook-form과 URL을 우아하게 동기화하는 법 2 🚀
date: 2025-07-16T21:00:01+09:00
categories: [Web]
draft: true
tags:
  - next.js
  - react-hook-form
  - typescript
---

지난포스트에서는 Next.js 프로젝트를 진행하면서 유용하게 사용할 수 있는 자작 커스텀 훅, `useFormUrlSync`을 개선한 버전에 대해서 이야기 해 봅니다. 
<!--more-->

## 전체 소스 코드
```tsx
"use client";

import type { AliasAny } from "@/types/alias.types";
import { isNumber } from "es-toolkit/compat";
import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useEffect, useRef } from "react";
import { type DefaultValues, type FieldValues, type UseFormProps, type UseFormReturn, useForm } from "react-hook-form";

/**
 * useFormUrlSync 훅의 옵션 타입
 * @template T - 폼 필드 값들의 타입
 */
type UseFormUrlSyncOptions<T extends FieldValues> = Omit<UseFormProps<T>, "defaultValues"> & {
  /** URL 동기화에서 제외할 필드명들 */
  excludeFromUrl?: (keyof T)[];
  /** URL 변경 시 replace 사용 여부 (기본값: true) */
  replace?: boolean;
  /** 폼의 기본값들 */
  defaultValues: DefaultValues<T>;
  /** URL 실시간 동기화 여부 (기본값: true) */
  sync?: boolean;
};

/**
 * useFormUrlSync 훅의 반환 타입
 * @template T - 폼 필드 값들의 타입
 */
type UseFormUrlSyncReturn<T extends FieldValues> = UseFormReturn<T> & {
  /** URL을 수동으로 동기화하는 함수 */
  syncToUrl: () => void;
};

/**
 * URL 파라미터 값을 적절한 타입으로 파싱합니다.
 * @param value - 파싱할 문자열 값
 * @returns 파싱된 값 (string | number | boolean)
 */
function parseUrlValue(value: string): string | number | boolean {
  if (value === "") return value;
  if (value === "true") return true;
  if (value === "false") return false;
  const numValue = Number(value);
  if (isNumber(numValue) && !Number.isNaN(numValue)) {
    return numValue;
  }
  return value;
}

/**
 * URL 검색 파라미터에서 초기값을 추출합니다.
 * @template T - 폼 필드 값들의 타입
 * @param searchParams - URL 검색 파라미터
 * @param excludeFromUrl - URL 동기화에서 제외할 필드명들
 * @returns URL에서 추출한 초기값들
 */
function extractInitialValuesFromUrl<T extends FieldValues>(
  searchParams: URLSearchParams,
  excludeFromUrl: (keyof T)[],
): Partial<T> {
  const urlValues: Partial<T> = {};
  for (const [key, value] of searchParams.entries()) {
    if (!excludeFromUrl.includes(key as keyof T)) {
      (urlValues as AliasAny)[key] = parseUrlValue(value);
    }
  }
  return urlValues;
}

/**
 * 폼 값들로부터 URL 파라미터를 생성합니다.
 * @template T - 폼 필드 값들의 타입
 * @param values - 폼 값들
 * @param currentParams - 현재 URL 파라미터
 * @param excludeFromUrl - URL 동기화에서 제외할 필드명들
 * @returns 새로운 URLSearchParams 객체
 */
function createUrlParamsFromValues<T extends FieldValues>(
  values: T,
  currentParams: URLSearchParams,
  excludeFromUrl: (keyof T)[],
): URLSearchParams {
  const params = new URLSearchParams(currentParams);
  for (const [key, value] of Object.entries(values)) {
    if (excludeFromUrl.includes(key as keyof T)) {
      continue;
    }
    if (value !== undefined && value !== null && value !== "") {
      params.set(key, String(value));
    } else {
      params.delete(key);
    }
  }
  return params;
}

/**
 * 두 객체의 깊은 비교를 수행합니다.
 * @param obj1 - 비교할 첫 번째 객체
 * @param obj2 - 비교할 두 번째 객체
 * @returns 객체들이 동일한지 여부
 */
function deepEqual(obj1: AliasAny, obj2: AliasAny): boolean {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}

/**
 * React Hook Form과 URL 검색 파라미터를 양방향으로 동기화하는 커스텀 훅입니다.
 *
 * @template T - 폼 필드 값들의 타입, FieldValues를 확장해야 함
 * @param options - 훅 설정 옵션
 * @returns React Hook Form의 UseFormReturn 객체
 *
 * @remarks
 * URL 파라미터는 자동으로 적절한 타입(string, number, boolean)으로 파싱됩니다.
 * 빈 문자열, null, undefined 값은 URL에서 제거됩니다.
 * Next.js의 useRouter와 useSearchParams를 사용하므로 Next.js 환경에서만 동작합니다.
 */
export function useFormUrlSync<T extends FieldValues>(options: UseFormUrlSyncOptions<T>): UseFormUrlSyncReturn<T> {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { excludeFromUrl = [], replace = true, defaultValues, sync = true, ...formOptions } = options;

  const isUpdatingFromUrl = useRef(false);

  const getUrlValues = useCallback(() => {
    return extractInitialValuesFromUrl<T>(searchParams, excludeFromUrl as (keyof T)[]);
  }, [searchParams, excludeFromUrl]);

  const initialValues = {
    ...defaultValues,
    ...getUrlValues(),
  } as DefaultValues<T>;

  const form = useForm({
    ...formOptions,
    defaultValues: initialValues,
  });

  const { watch, reset, getValues } = form;

  const updateUrl = useCallback(
    (values: T) => {
      const params = createUrlParamsFromValues(values, searchParams, excludeFromUrl as (keyof T)[]);
      const newSearchString = params.toString();
      const currentSearchString = new URLSearchParams(window.location.search).toString();

      if (newSearchString !== currentSearchString) {
        const newUrl = `${window.location.pathname}?${newSearchString}`;
        if (replace) {
          router.replace(newUrl, { scroll: false });
        } else {
          router.push(newUrl, { scroll: false });
        }
      }
    },
    [router, searchParams, excludeFromUrl, replace],
  );

  const syncToUrl = useCallback(() => {
    const values = getValues();
    updateUrl(values);
  }, [getValues, updateUrl]);

  useEffect(() => {
    if (sync) {
      const subscription = watch(values => {
        if (isUpdatingFromUrl.current) {
          return;
        }
        updateUrl(values as T);
      });

      return () => subscription.unsubscribe();
    }
  }, [watch, updateUrl, sync]);

  useEffect(() => {
    const urlValues = getUrlValues();
    const currentFormValues = getValues();

    const relevantFormValues: Partial<T> = {};
    for (const key in urlValues) {
      if (Object.prototype.hasOwnProperty.call(urlValues, key)) {
        relevantFormValues[key as keyof T] = currentFormValues[key as keyof T];
      }
    }

    if (!deepEqual(urlValues, relevantFormValues)) {
      isUpdatingFromUrl.current = true;

      reset({
        ...currentFormValues,
        ...urlValues,
      } as DefaultValues<T>);

      setTimeout(() => {
        isUpdatingFromUrl.current = false;
      }, 0);
    }
  }, [getUrlValues, reset, getValues]);

  return {
    ...form,
    syncToUrl: syncToUrl,
  };
}
```

웹 애플리케이션에서 필터나 검색 기능을 구현할 때, 사용자가 설정한 상태를 URL에 반영하고 싶은 경우가 많습니다. 예를 들어, 사용자가 상품 목록에서 카테고리를 선택하고 가격 범위를 설정했을 때, 이 정보가 URL에 반영되어 페이지를 새로고침하거나 다른 사람과 공유해도 동일한 필터 상태를 유지할 수 있어야 합니다.

이런 요구사항을 해결하기 위해 React Hook Form과 URL 검색 파라미터를 양방향으로 동기화하는 `useFormUrlSync` 커스텀 훅을 소개합니다.

## 주요 기능

### 1. 양방향 동기화
- **폼 → URL**: 폼 값이 변경되면 자동으로 URL이 업데이트됩니다
- **URL → 폼**: URL 파라미터가 변경되면 폼 상태도 자동으로 업데이트됩니다

### 2. 타입 안전성
URL 파라미터는 기본적으로 문자열이지만, 이 훅은 자동으로 적절한 타입으로 변환합니다:
- `"true"` → `true` (boolean)
- `"false"` → `false` (boolean)
- `"42"` → `42` (number)
- `"hello"` → `"hello"` (string)

### 3. 선택적 필드 제외
특정 필드를 URL 동기화에서 제외할 수 있습니다. 예를 들어, 비밀번호나 임시 상태 같은 민감한 정보는 URL에 노출되지 않도록 할 수 있습니다.

### 4. 실시간 동기화 제어
`sync` 옵션으로 실시간 동기화를 활성화/비활성화할 수 있으며, 수동으로 동기화할 수 있는 `syncToUrl` 함수도 제공됩니다.

## 사용 방법

### 기본 사용법

```typescript
import { useFormUrlSync } from './useFormUrlSync';

type FilterForm = {
  category: string;
  minPrice: number;
  maxPrice: number;
  inStock: boolean;
};

function ProductFilter() {
  const form = useFormUrlSync<FilterForm>({
    defaultValues: {
      category: '',
      minPrice: 0,
      maxPrice: 1000,
      inStock: false,
    },
  });

  const { register, watch } = form;
  const values = watch();

  return (
    <form>
      <select {...register('category')}>
        <option value="">전체 카테고리</option>
        <option value="electronics">전자제품</option>
        <option value="clothing">의류</option>
      </select>
      
      <input
        type="number"
        {...register('minPrice', { valueAsNumber: true })}
        placeholder="최소 가격"
      />
      
      <input
        type="number"
        {...register('maxPrice', { valueAsNumber: true })}
        placeholder="최대 가격"
      />
      
      <label>
        <input
          type="checkbox"
          {...register('inStock')}
        />
        재고 있는 상품만
      </label>
    </form>
  );
}
```

### 옵션 상세 설명

#### `excludeFromUrl`
특정 필드를 URL 동기화에서 제외합니다:

```typescript
const form = useFormUrlSync<FilterForm>({
  defaultValues: { /* ... */ },
  excludeFromUrl: ['password', 'temporaryState'],
});
```

#### `replace`
URL 변경 시 브라우저 히스토리 관리 방식을 결정합니다:

```typescript
const form = useFormUrlSync<FilterForm>({
  defaultValues: { /* ... */ },
  replace: false, // push 사용 (기본값: true)
});
```

#### `sync`
실시간 동기화 여부를 제어합니다:

```typescript
const form = useFormUrlSync<FilterForm>({
  defaultValues: { /* ... */ },
  sync: false, // 실시간 동기화 비활성화
});

// 수동으로 동기화
const { syncToUrl } = form;
const handleSubmit = () => {
  syncToUrl();
};
```

## 구현 상세 설명

### 1. URL 값 파싱 (`parseUrlValue`)

```typescript
function parseUrlValue(value: string): string | number | boolean {
  if (value === "") return value;
  if (value === "true") return true;
  if (value === "false") return false;
  const numValue = Number(value);
  if (isNumber(numValue) && !Number.isNaN(numValue)) {
    return numValue;
  }
  return value;
}
```

이 함수는 URL의 문자열 파라미터를 적절한 타입으로 변환합니다. 문자열이 boolean이나 number로 변환 가능한지 확인하고, 그렇지 않으면 원본 문자열을 반환합니다.

### 2. 초기값 추출 (`extractInitialValuesFromUrl`)

```typescript
function extractInitialValuesFromUrl<T extends FieldValues>(
  searchParams: URLSearchParams,
  excludeFromUrl: (keyof T)[],
): Partial<T> {
  const urlValues: Partial<T> = {};
  for (const [key, value] of searchParams.entries()) {
    if (!excludeFromUrl.includes(key as keyof T)) {
      (urlValues as AliasAny)[key] = parseUrlValue(value);
    }
  }
  return urlValues;
}
```

페이지 로드 시 URL에서 초기값을 추출하여 폼의 기본값과 병합합니다. `excludeFromUrl`에 포함된 필드는 제외됩니다.

### 3. URL 파라미터 생성 (`createUrlParamsFromValues`)

```typescript
function createUrlParamsFromValues<T extends FieldValues>(
  values: T,
  currentParams: URLSearchParams,
  excludeFromUrl: (keyof T)[],
): URLSearchParams {
  const params = new URLSearchParams(currentParams);
  for (const [key, value] of Object.entries(values)) {
    if (excludeFromUrl.includes(key as keyof T)) {
      continue;
    }
    if (value !== undefined && value !== null && value !== "") {
      params.set(key, String(value));
    } else {
      params.delete(key);
    }
  }
  return params;
}
```

폼 값들을 URL 파라미터로 변환합니다. 빈 값(`undefined`, `null`, `""`)은 URL에서 제거되어 깔끔한 URL을 유지합니다.

### 4. 무한 루프 방지

```typescript
const isUpdatingFromUrl = useRef(false);

useEffect(() => {
  if (sync) {
    const subscription = watch(values => {
      if (isUpdatingFromUrl.current) {
        return;
      }
      updateUrl(values as T);
    });

    return () => subscription.unsubscribe();
  }
}, [watch, updateUrl, sync]);
```

`useRef`를 사용하여 URL 업데이트로 인한 폼 변경과 폼 변경으로 인한 URL 업데이트를 구분합니다. 이를 통해 무한 루프를 방지합니다.

### 5. 깊은 비교 (`deepEqual`)

```typescript
function deepEqual(obj1: AliasAny, obj2: AliasAny): boolean {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}
```

객체의 깊은 비교를 통해 실제로 값이 변경되었을 때만 폼을 업데이트하여 불필요한 렌더링을 방지합니다.

## 실제 활용 예시

### 검색 필터 페이지

```typescript
type SearchFilters = {
  query: string;
  category: string;
  sortBy: 'price' | 'name' | 'date';
  priceRange: [number, number];
  isAvailable: boolean;
};

function SearchPage() {
  const form = useFormUrlSync<SearchFilters>({
    defaultValues: {
      query: '',
      category: '',
      sortBy: 'name',
      priceRange: [0, 1000],
      isAvailable: false,
    },
    excludeFromUrl: ['priceRange'], // 복잡한 객체는 URL에서 제외
  });

  const { register, watch } = form;
  const filters = watch();

  // 필터 변경 시 자동으로 URL 업데이트되고
  // 검색 결과도 자동으로 업데이트됨
  const { data: products } = useQuery({
    queryKey: ['products', filters],
    queryFn: () => fetchProducts(filters),
  });

  return (
    <div>
      <form>
        <input
          {...register('query')}
          placeholder="검색어 입력"
        />
        <select {...register('category')}>
          <option value="">전체</option>
          <option value="electronics">전자제품</option>
          <option value="books">도서</option>
        </select>
        <select {...register('sortBy')}>
          <option value="name">이름순</option>
          <option value="price">가격순</option>
          <option value="date">날짜순</option>
        </select>
        <label>
          <input
            type="checkbox"
            {...register('isAvailable')}
          />
          구매 가능한 상품만
        </label>
      </form>
      
      <ProductList products={products} />
    </div>
  );
}
```

## 주의사항 및 한계

### 1. Next.js 클라이언트 컴포넌트 전용
이 훅은 Next.js의 `useRouter`와 `useSearchParams`를 사용하므로:
- 클라이언트 컴포넌트에서만 동작합니다
- 컴포넌트 상단에 `"use client"` 지시어가 필요합니다

### 2. 복잡한 객체 타입 제한
URL 파라미터의 특성상 복잡한 객체나 배열은 직접 지원하지 않습니다. 이런 경우 `excludeFromUrl` 옵션을 사용하거나 별도의 직렬화 로직을 구현해야 합니다.

### 3. 히스토리 관리
기본적으로 `replace: true`로 설정되어 있어 뒤로 가기 버튼으로 필터 변경 이력을 탐색할 수 없습니다. 필요에 따라 `replace: false`로 설정할 수 있습니다.

### 4. 성능 고려사항
실시간 동기화가 활성화되어 있으면 모든 폼 변경이 URL 업데이트를 트리거합니다. 성능이 중요한 경우 `sync: false`로 설정하고 수동으로 동기화하는 것을 고려해보세요.

## 마무리

`useFormUrlSync` 훅은 React Hook Form과 URL 상태를 간편하게 동기화할 수 있는 강력한 도구입니다. 특히 검색이나 필터 기능이 있는 페이지에서 사용자 경험을 크게 향상시킬 수 있습니다.

주요 장점:
- **공유 가능한 URL**: 사용자가 설정한 필터 상태를 URL로 공유 가능
- **새로고침 안정성**: 페이지 새로고침 후에도 설정 유지
- **타입 안전성**: TypeScript를 통한 완전한 타입 지원
- **유연한 설정**: 다양한 옵션으로 프로젝트 요구사항에 맞게 조정 가능

이 훅을 활용하여 더 나은 사용자 경험을 제공하는 웹 애플리케이션을 만들어보세요!
