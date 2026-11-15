---
version: 1
slug: "home"
primary_target: "home"
related_targets: []
---

---
version: 1
slug: "home"
primary_target: "home"
related_targets: []
---

---
surface: home
route: /
mode: read
---

# Home — 기록 보관소

## Scope and visitor mode

`/` 만 해당한다. 방문자 모드는 **Read** — 읽을 것을 고르고 파악하는 화면.
글 상세, 카테고리·태그·검색, 푸터, 댓글, 페이지네이션은 범위 밖이며 건드리지 않는다.

## Audience and job

1차 사용자는 작성자 본인, 2차는 링크를 받고 들어온 사람. 후자의 질문은
"여긴 무엇이 쌓인 곳이고, 최근에 뭘 했나". 성공은 3초 안에 그 답이 보이고
최신 글 세 줄 안에서 하나를 고르는 것.

## Chosen direction

시간순 장부를 유지한 채, 그 위에 8년치 기록을 실제 데이터로 그린 **관측 띠**를 얹는다.
장식 배경을 가진 큰 제목 히어로와 카드 그리드를 거부한다. 월 단위 러닝 헤드가
스크롤 중 위치를 알려준다. 기억에 남는 순간은 첫 화면의 막대 띠 자체 — 8년의
공백과 2026년의 밀집이 한 눈에 보인다.

## Unresolved

- 목록 날짜(`#aaaaaa`, 12.5px)는 흰 바탕에서 4.5:1에 못 미친다. 기존 시스템 전반의
  문제라 이번 범위에서 고치지 않았다.
- 띠에 진입 모션을 줄지는 미정. 현재는 정지 상태다.

## Direction contract

THESIS: 홈은 장부다. 최신순 목록을 유지하고, 그 위에 8년치 편수를 실제 데이터로 그린
가로 띠를 얹어 "수백 편의 아카이브"라는 사실을 첫 화면에서 증명한다. 큰 제목 + 장식 배경의
카테고리 기본 히어로와 카드 그리드를 거부한다.

OWN-WORLD: 밤의 바탕(#010205) 위 흰 괘선과 회색 눈금, 신호 시안 한 점(#3fa4ff).
컴포넌트는 월 러닝 헤드와 날짜·제목 두 조각 행. 색을 전부 지워도 남는 것: 가로로 긴
어두운 띠, 그 위의 막대 눈금, 흰 바탕의 1px 선 장부.

STORY: 방문자는 3초 안에 "8년간 쌓였고 대부분 최근에 몰렸다"를 읽고, 최신 글 세 줄
안에서 하나를 골라 들어간다.

FIRST VIEWPORT: 1440×900, 상단 띠 전체 높이 260px. 55px 고정 헤더(로고·블로그·
카테고리·태그·검색) → 104px 아래 h1 "개발 기록 보관소"(25.6px/500, 흰색) → 22px →
축 헤더 한 줄(왼쪽 총 편수 15px/700 흰색, 오른쪽 "범위 · 최다 N편 (YYYY.MM)" 11px 회색)
→ 9px → 월별 막대 띠(높이 56px, 위아래 1px 괘선, 슬롯 97개, 연도별 비례 폭, 빈 달은
칠하지 않음, 마지막 달만 시안) → 흰 면으로 전환 → 월 러닝 헤드(스크롤 시 top 55px 고정)
→ 행 13~15줄. 주 행동은 목록의 각 링크다.

FORM: 기존 세계의 확장(established world). 확정된 브리프가 구성을 고정했으므로 별도
구성 토너먼트를 돌리지 않았다. seed:daae112b4a5cb53a

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
