# Post List Compact UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 홈페이지 및 카테고리/태그 목록 페이지의 글 목록을 페이지당 30개, 제목+날짜만 표시하는 콤팩트 리스트 스타일로 전환한다.

**Architecture:** `config.toml`에서 pagerSize를 30으로 변경하고, `summary.html`을 콤팩트 div 구조로 교체한다. `style.scss`에 `.post-list-item` 스타일을 추가하고 SCSS를 재컴파일한다. `list.html`과 `index.html`은 수정하지 않는다.

**Tech Stack:** Hugo 0.155, SCSS (node-sass), Taskfile

---

## File Map

| 파일 | 변경 유형 | 내용 |
|------|----------|------|
| `config.toml` | Modify | pagerSize 7 → 30 |
| `themes/hago/layouts/_default/summary.html` | Modify (전체 교체) | 콤팩트 list item HTML |
| `themes/hago/scss/style.scss` | Modify (추가) | `.post-list-item` 스타일 블록 (line 258 이후) |
| `themes/hago/static/css/style.css` | Auto-generated | SCSS 컴파일 결과 |

---

### Task 1: pagerSize 변경

**Files:**
- Modify: `config.toml:10-12`

- [ ] **Step 1: pagerSize 수정**

`config.toml` 의 `[pagination]` 블록을 아래로 교체:

```toml
[pagination]
  pagerSize = 30
```

- [ ] **Step 2: 빌드 확인**

```bash
task build 2>&1 | tail -5
```

Expected: 오류 없이 `Total in ...` 출력

- [ ] **Step 3: 커밋**

```bash
git add config.toml
git commit -m "config: increase pagerSize from 7 to 30"
```

---

### Task 2: summary.html 콤팩트 리스트로 교체

**Files:**
- Modify: `themes/hago/layouts/_default/summary.html` (전체 교체)

- [ ] **Step 1: summary.html 전체 내용 교체**

파일 전체를 아래 내용으로 교체:

```html
<div class="post-list-item">
  <span class="post-list-date">{{ .Date.Format "2006.01.02" }}</span>
  <a href="{{ .Permalink }}" class="post-list-title" title="{{ .Title }}">{{ .Title }}</a>
</div>
```

- [ ] **Step 2: 빌드 확인**

```bash
task build 2>&1 | tail -5
```

Expected: 오류 없이 `Total in ...` 출력

- [ ] **Step 3: 커밋**

```bash
git -C themes/hago add layouts/_default/summary.html
git -C themes/hago commit -m "feat: replace summary card with compact list item"
```

---

### Task 3: SCSS 스타일 추가 및 컴파일

**Files:**
- Modify: `themes/hago/scss/style.scss:257` (`.post-summary {}` 블록 직후 line 258에 삽입)
- Auto-generated: `themes/hago/static/css/style.css`

- [ ] **Step 1: style.scss에 스타일 추가**

`themes/hago/scss/style.scss`의 line 257 (`.post-summary { overflow: hidden; }` 바로 다음) 이후에 아래 블록 삽입:

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

- [ ] **Step 2: SCSS 컴파일**

```bash
cd themes/hago && npm run sass:build
```

Expected: `themes/hago/static/css/style.css` 가 갱신됨, 오류 없음

- [ ] **Step 3: 최종 빌드 확인**

```bash
task build 2>&1 | tail -5
```

Expected: `Pages │ 804` 수준, 오류 없음

- [ ] **Step 4: 커밋**

```bash
git -C themes/hago add scss/style.scss static/css/style.css
git -C themes/hago commit -m "feat: add .post-list-item compact styles"
```

---

### Task 4: 부모 레포 submodule 업데이트 및 최종 확인

**Files:**
- Modify: `themes/hago` (submodule pointer 갱신)

- [ ] **Step 1: 부모 레포에서 submodule 변경 스테이징**

```bash
git add themes/hago
git status
```

Expected: `themes/hago` 가 modified로 표시

- [ ] **Step 2: 부모 레포 커밋**

```bash
git commit -m "build: update hago submodule for compact post list"
```

- [ ] **Step 3: 검증**

아래 4가지를 확인:
1. 홈페이지 목록에서 아이템이 30개 표시
2. 날짜가 `2026.01.02` 포맷으로 출력
3. 요약 텍스트 없음, 제목 링크만 표시
4. 카테고리/태그 목록 페이지도 동일 스타일 적용

```bash
task build 2>&1 | tail -8
```

Expected: 빌드 오류 없음
