# 글목록 콤팩트 리스트 UI 개선

**날짜:** 2026-05-14  
**상태:** 승인됨

## 목표

홈페이지 및 카테고리/태그 목록 페이지에서 페이지당 표시되는 글 수를 7개에서 30개로 늘리고, 요약 없이 제목만 표시하는 콤팩트 리스트 스타일로 전환한다.

## 변경 범위

영향받는 페이지:
- 홈페이지 (`/`)
- 카테고리 목록 (`/categories/…`)
- 태그 목록 (`/tags/…`)

## 접근 방법

접근법 1 채택: `summary.html` 직접 수정 + `config.toml` pagerSize 변경 + SCSS 추가.

`list.html`, `index.html`은 수정하지 않는다.

## 변경 파일 목록

### 1. `config.toml`

```toml
[pagination]
  pagerSize = 30
```

기존값 `7`을 `30`으로 변경.

### 2. `themes/hago/layouts/_default/summary.html`

기존 전체 내용을 아래로 교체:

```html
<div class="post-list-item">
  <span class="post-list-date">{{ .Date.Format "2006.01.02" }}</span>
  <a href="{{ .Permalink }}" class="post-list-title" title="{{ .Title }}">{{ .Title }}</a>
</div>
```

제거 항목:
- `<article class="post">` 래퍼
- `<h2>` 제목 태그
- 날짜/카테고리 아이콘 블록
- `.post-summary` 요약 텍스트
- `summary-more` 더보기 링크
- `<hr class="summary-sep" />`

### 3. `themes/hago/scss/style.scss`

기존 `.post-summary` 규칙 이후에 아래 추가:

```scss
.post-list-item {
  display: flex;
  align-items: baseline;
  padding: 5px 0;
  border-bottom: 1px solid #f3f3f3;
  gap: 10px;

  .post-list-date {
    font-size: 0.78em;
    color: #aaa;
    white-space: nowrap;
    min-width: 80px;
  }

  .post-list-title {
    font-size: 0.9em;
    color: $heading-color;
    text-decoration: none;
    line-height: 1.4;
    &:hover { opacity: 0.7; }
  }
}
```

## 렌더링 결과 예시

```
2026.05.14  GSD + Superpowers + Hookify 조합으로 AI 개발 워크플로우 구축하기
2026.05.09  Claude Code로 풀 개발팀 운영하기: 5개 폴더로 완성하는 ADK 시스템
2026.05.09  ctx2skill: 레포를 스킬·메모리 엔진으로 쓰는 방법
2026.05.09  π 코딩 에이전트 실전 사용기
2026.05.08  local GPT image studio 사용기
...
```

## 검증 방법

1. `task build` 로 빌드 오류 없음 확인
2. 홈페이지에서 30개 항목 노출 확인
3. 카테고리/태그 페이지에서 동일 스타일 확인
4. 날짜 포맷 `2026.01.02` 정상 출력 확인
