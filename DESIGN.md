---
name: 신규하 블로그
description: 개발 기록 보관소 — 인터넷의 URL을 모아 남기는 개인 아카이브
colors:
  harbor-blue: "#0057a7"
  signal-cyan: "#3fa4ff"
  night-field: "#010205"
  footer-veil: "#010205cb"
  ink: "#000000"
  body-ink: "#555555"
  page-marker: "#999999"
  mist: "#aaaaaa"
  hairline: "#f1f1f1"
  divider: "#dddddd"
  code-surface: "#f5f5f5"
  code-ink: "#333333"
  link-blue: "#0000ff"
  quote-violet: "#5551d7"
  highlight-indigo: "#223399"
  alert-note: "#0969da"
  alert-important: "#8250df"
  alert-warning: "#9a6700"
  alert-caution: "#cf222e"
typography:
  display:
    fontFamily: "Noto Sans KR, sans-serif"
    fontSize: "25.2px"
    fontWeight: 500
    lineHeight: 1.5
  headline:
    fontFamily: "Noto Sans KR, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.5
  title:
    fontFamily: "Noto Sans KR, sans-serif"
    fontSize: "17.6px"
    fontWeight: 500
    lineHeight: 1.5
  body:
    fontFamily: "Noto Sans KR, sans-serif"
    fontSize: "15.2px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Noto Sans KR, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.5
  meta:
    fontFamily: "Noto Sans KR, sans-serif"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.5
  code:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "14.4px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  square: "0"
  xs: "3px"
  sm: "4px"
  md: "5px"
  pill: "18px"
  circle: "50%"
spacing:
  gutter: "15px"
  hair: "2px"
  xs: "5px"
  sm: "8px"
  md: "20px"
  lg: "30px"
  container: "1440px"
components:
  nav-link:
    textColor: "{colors.mist}"
    typography: "{typography.label}"
    padding: "0.5em 1em"
  nav-link-hover:
    textColor: "#ffffff"
  post-list-row:
    backgroundColor: "#ffffff"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "5px 0"
  post-list-row-hover:
    textColor: "{colors.harbor-blue}"
  tag-chip:
    backgroundColor: "#6c757d"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "3px 5px"
    typography: "{typography.meta}"
  tag-chip-hover:
    backgroundColor: "{colors.harbor-blue}"
  hero-title:
    backgroundColor: "{colors.night-field}"
    textColor: "#ffffff"
    typography: "{typography.display}"
  search-field:
    backgroundColor: "#ffffff"
    textColor: "{colors.body-ink}"
    rounded: "{rounded.pill}"
    height: "56px"
    padding: "0 1.35rem"
  search-submit:
    textColor: "#ffffff"
    rounded: "{rounded.pill}"
    height: "56px"
    padding: "0 1.6rem"
  code-block:
    backgroundColor: "{colors.code-surface}"
    textColor: "{colors.code-ink}"
    rounded: "{rounded.md}"
    padding: "20px"
    typography: "{typography.code}"
  pagination-active:
    backgroundColor: "{colors.page-marker}"
    textColor: "#ffffff"
---

# Design System: 신규하 블로그

## Overview

**Creative North Star: "관측소 (The Observatory)"**

어두운 상단 띠 위로 신호가 흐르고, 그 아래로는 흰 종이 같은 목록이 끝없이 이어진다. 이 사이트의 시각 언어는 **밤의 관측 기록**이다. 히어로의 별자리 애니메이션은 장식이 아니라 "지금 무언가를 관측하고 있다"는 유일한 표정이고, 본문 영역은 그 표정을 완전히 버린다. 색도 그림자도 거의 쓰지 않고, 오직 **괘선(hairline)** 으로 정보를 나눈다.

밀도는 높고 장식은 낮다. 목록 한 줄은 날짜와 제목 두 조각뿐이고, 요약문도 썸네일도 없다. 이것은 게시판이 아니라 **장부**에 가깝다. 사이드바는 2px 세로선 하나로 본문과 갈라지고, 위젯마다 2px 가로선으로 끊긴다. 여백은 넉넉하지 않고, 대신 선이 정확하다.

차분하고 조용히 기술적이다. 화려함은 상단 띠에서 한 번만 허용되고, 그 아래에서는 색이 정보를 돕는 역할로 물러난다.

홈에서는 그 띠가 장식이 아니라 **기록 그 자체**가 된다. 2018년부터의 월별 편수를 막대로 그린 띠가 제목 아래 놓이고, 목록은 달 단위 러닝 헤드로 묶인다. 글 상세에서는 같은 자리에 별자리 애니메이션이 남는다.

**Key Characteristics:**
- 상단 밤하늘 띠(홈 260px, 글 150px)와 그 아래 흰 기록면의 이분 구조
- 홈의 띠는 장식이 아니라 8년치 월별 편수를 그린 데이터 띠
- 그림자 없는 평면. 구분은 1–2px 회색 선이 전담
- 날짜 + 제목 두 열짜리 목록 행이 사이트의 기본 단위
- 사이드바 위젯 = 아이콘 + 18px 굵은 제목 + 2px 하단 괘선
- 남색 한 색(`#0057a7`)이 상호작용을, 시안 한 색(`#3fa4ff`)이 살아있는 상태를 맡는 분업
- 한국어 본문에 Noto Sans KR, 코드에만 JetBrains Mono

## Colors

거의 무채색 위에 남색 하나와 시안 하나만 얹은 구조다. 색이 늘어나면 이 시스템은 무너진다.

### Primary
- **Deep Harbor / 심해 남색** (#0057a7): 링크·메뉴·태그의 호버 상태, 그리고 검색 버튼의 그림자 색. "누를 수 있는 것"을 알리는 유일한 신호다. 평상시에는 화면에 보이지 않는다.

### Secondary
- **Signal Cyan / 관측 시안** (#3fa4ff): 히어로 별자리의 연결선과 목차의 현재 위치. **지금 살아 움직이는 상태**에만 쓴다. 정적인 요소에 이 색을 칠하면 관측소가 아니라 네온사인이 된다.

### Neutral
- **Night Field / 밤의 바탕** (#010205): 상단 띠와 푸터의 바탕. 사이트에서 유일하게 어두운 면이다.
- **Footer Veil / 푸터 장막** (#010205cb): 푸터 전용 반투명 변형. 콘텐츠가 비쳐 보이는 것을 의도한다.
- **Ink / 먹** (#000000): 제목과 목록 항목 제목. 본문에는 쓰지 않는다.
- **Body Ink / 본문 먹** (#555555): 문단, 목록, 사이드바 링크. 대비를 일부러 낮춰 장시간 읽기를 배려한다.
- **Page Marker / 페이지 표식** (#999999): 페이지네이션의 현재 페이지, 히어로 부제.
- **Mist / 안개** (#aaaaaa): 날짜 열, 내비게이션 링크의 평상시 색, 히어로 부제.
- **Hairline / 괘선** (#f1f1f1): 목록 행 구분, 사이드바 세로선, 위젯 하단선, 인라인 코드 테두리.
- **Divider / 구분선** (#dddddd): 본문 h2 밑줄, 헤더 라인, 표 셀 테두리.
- **Code Surface / 코드면** (#f5f5f5) · **Code Ink** (#333333): 코드 블록과 인라인 코드.

### Tertiary (본문 전용 예외색)
- **Link Blue / 날 링크 파랑** (#0000ff): 본문 안의 하이퍼링크. 팔레트와 어긋나는 것을 **의도된 표식**으로 확정했다. 본문에서 "이건 밖으로 나가는 링크"라는 사실이 즉시 읽히는 것이 우선이다. 절대 UI 요소(버튼·메뉴·태그)에 쓰지 않는다.
- **Quote Violet** (#5551d7): 인용문 좌측 띠.
- **Highlight Indigo** (#223399): 카테고리 탭의 활성 밑줄.
- **Alert 계열** (#0969da 참고 / #8250df 중요 / #9a6700 경고 / #cf222e 주의): GitHub 경보 색을 그대로 차용한 콜아웃. 띠와 아이콘에만 쓰고 배경은 칠하지 않는다.

### Named Rules
**The Night Band Rule.** 어두운 면은 상단 띠와 푸터 두 곳뿐이다. 페이지 전체를 다크 모드로 만들지 않는다. 밤은 관측 창밖에만 있다.

**The Signal Rule.** `#3fa4ff` 는 "지금 반응하고 있다"는 뜻이다. 별자리 애니메이션과 목차의 현재 항목, 이 둘 외에는 쓰지 않는다.

**The Body Link Rule.** `#0000ff` 는 본문 링크 전용이다. 다른 파랑(`#0057a7`)과 섞지 않는다. 두 파랑이 같은 화면에서 다른 일을 하기 때문이다.

## Typography

**Display Font:** Noto Sans KR (with `sans-serif`)
**Body Font:** Noto Sans KR (with `sans-serif`)
**Label/Mono Font:** JetBrains Mono (코드·인용 전용, 폴백 없이 단일 지정)

**Character:** 단일 한글 산세리프가 모든 계층을 맡는다. 크기 차이가 작고(15.2px ~ 25.2px) 굵기 차이로 위계를 만드는 것이 이 시스템의 방식이다. 제목은 500, 강조 제목과 내비게이션은 700. 서체를 바꿔 분위기를 내지 않는다.

### Hierarchy
- **Display** (500, 25.2px / 1.8em, 1.5): 히어로의 사이트명 또는 글 제목. 페이지당 한 번.
- **Headline** (700, 18px, 1.5): 사이드바 위젯 제목, 카테고리 탭 제목. 30px 왼쪽 들여쓰기를 동반한다.
- **Title** (500, 17.6px / 1.1em, 1.5): 본문 h2. 1px `#dddddd` 밑줄, 위쪽 26.4px 여백.
- **Body** (400, 15.2px / 0.95em, 1.5): 글 본문. 왼쪽 1em 들여쓰기, 문단 간 0.8em. 안정적인 행 길이를 위해 한글 기준 약 40자 내외에서 끊는다.
- **Label** (700, 16px, 1.5): 내비게이션 링크. 굵게, 그리고 회색.
- **Meta** (400, 12.5px / 0.78em, 1.5): 목록의 날짜 열. 줄바꿈 금지, 최소 폭 80px.
- **Code** (400, 14.4px / 0.9em, 1.5): 코드 블록. JetBrains Mono.

### Named Rules
**The Two Weight Rule.** 400과 700만 쓴다. 중간 굵기(500)는 제목 계열에만 허용된다. 세 가지 굵기로 위계를 만들려 하지 않는다.

**The Mono Rule.** JetBrains Mono는 코드와 인용문에만 등장한다. 라벨이나 UI 텍스트에 모노스페이스를 쓰지 않는다.

## Layout

Bootstrap 4의 12열 그리드를 8/4로 나눈 2단 구조다. 본문 66.67%, 사이드바 33.33%, 양쪽에 15px 거터. 컨테이너 최대 폭은 1440px(1200px 이상에서만 적용).

- **상단 띠**: 홈은 260px(제목 + 축 헤더 + 데이터 띠), 개별 글은 150px. 사이트에서 유일하게 "큰" 요소이며, 그 아래 모든 것은 조밀하다.
- **사이드바**: `2px solid #f1f1f1` 세로선으로 본문과 분리. 위젯마다 `2px solid #f1f1f1` 하단선, 마지막 위젯은 선 없음.
- **위젯 내부**: 위젯 제목은 왼쪽 30px 들여쓰기 + 12px 상하 패딩. 내용은 `8px 0 30px 20px`.
- **반응형**: 767px 이하에서 사이드바는 통째로 사라진다. 767px 이하 본문 문단은 17.6px / 1.7em으로 커지고 들여쓰기가 줄어 읽기 폭을 확보한다. 992~1199px에서는 내비게이션 간격이 0.5em으로 좁아진다.
- **목록 리듬**: 행 간 5px 상하 패딩, `1px solid #f3f3f3` 하단선, 날짜와 제목 사이 10px.

### Named Rules
**The One Column Rule.** 본문은 어떤 화면 폭에서도 2단을 넘지 않는다. 사이드바는 세 번째 열이 아니라 없어지는 부속이다.

**The Compressed Ledger Rule.** 목록 행의 높이는 5px 패딩으로 고정한다. 썸네일·요약문·여백 확대는 이 리듬을 깬다.

## Elevation & Depth

**그림자를 쓰지 않는다.** 위계는 오직 괘선과 굵기로 만든다. 카드, 목록 행, 사이드바 위젯, 알림 상자는 모두 평평하고 배경색도 갖지 않는다.

예외는 **떠 있는 요소**뿐이다. 스크롤에 붙는 상단 바, 펼침 메뉴, 맨 위로 버튼, 그리고 검색 입력/버튼. 이것들은 문서 흐름에서 분리되었기 때문에만 그림자를 얻는다.

### Shadow Vocabulary
- **스크롤 고정 바** (`0 5px 15px rgba(0, 0, 0, 0.15)`): 상단 바가 sticky 상태로 전환될 때만.
- **펼침 메뉴** (`0 5px 12px rgba(0, 0, 0, 0.15)`): 드롭다운. 모서리 3px.
- **맨 위로** (`0 2px 6px rgba(0, 0, 0, 0.3)`): 우하단 원형 버튼. 767px 이하에서는 불투명도 0.6으로 물러난다.
- **검색 필드** (`0 12px 30px rgba(35, 35, 35, 0.08)`): 검색 페이지의 입력란. 포커스 시 `0 16px 36px rgba(0, 87, 167, 0.12)`.
- **검색 버튼** (`0 14px 32px rgba(0, 89, 172, 0.2)`): 그라디언트 버튼 아래. 호버 시 `0 18px 36px rgba(0, 89, 172, 0.24)`.

### Named Rules
**The Hairline Rule.** 문서 안의 면은 절대 떠 보이지 않는다. 무엇인가를 나눠야 하면 그림자가 아니라 1–2px 선을 긋는다. 선으로 해결되지 않을 때만 여백을 늘린다.

**The Floating Exception Rule.** 그림자는 "스크롤해도 제자리에 있는 것"에만 준다. 정적인 콘텐츠 상자에는 어떤 경우에도 주지 않는다.

**The Opaque Bar Rule.** 상단 바가 스크롤로 고정되면 배경은 불투명 `#010205`다. 반투명 장막은 푸터 전용이며, 본문이 헤더를 통과해 비치면 그것은 디자인이 아니라 결함이다.

## Shapes

기본은 **각**이다. 모서리 반경 0이 기본값이고, 반경을 준다면 그건 그 요소가 "도구"라는 표시다.

- **0**: 드롭다운 메뉴(카테고리 탭 내), 표, 구분 영역
- **3px**: 인라인 코드, 드롭다운 메뉴(헤더)
- **4px**: 태그 칩
- **5px**: 코드 블록, 인용문
- **18px**: 검색 입력과 검색 버튼 — 이 사이트에서 유일하게 부드러운 형태. 검색은 예외적으로 "손에 쥐는 도구"로 취급한다.
- **50%**: 맨 위로 버튼, SNS 아이콘, 검색 아이콘

원(circle)은 떠 있는 것과 소셜 링크에만. 나머지 문서 요소에 둥근 모서리를 남용하지 않는다.

### Named Rules
**The One Soft Element Rule.** 부드러운 곡선(18px 알약)은 검색 컨트롤 하나에만 허용된다. 두 번째 알약형 요소를 추가하면 시스템이 아니라 취향이 된다.

## Components

날카롭고 조용한 도구. 버튼다운 버튼은 거의 없고, 대부분의 상호작용은 **글자와 선**으로 이루어진다.

### Archive Strip (홈 전용 시그니처)
- **Shape:** 반경 0의 세로 막대 97개. 높이 56px, 위아래 1px `rgba(255,255,255,0.14)` 괘선, 연도 사이 12px, 같은 해 월 사이 2px.
- **Scale:** 월별 편수를 **아카이브 전체 최대치**로 나눈 선형 비율, 최소 높이 5px. 수치는 빌드 시점에 계산되며 문서에 고정하지 않는다. 편수가 0인 달은 칠하지 않는다 — 빈 구간이 보이는 것이 이 띠의 목적이다.
- **Color:** `rgba(255,255,255,0.42)` (어두운 바탕 대비 3.4:1). 마지막 달(현재)만 `#3fa4ff`.
- **Label:** 연도만 `#aaaaaa` 11px로 아래에. 월 이름은 쓰지 않고, 각 막대에 `YYYY.MM · N편` 형식의 네이티브 툴팁을 단다.
- **Axis Header:** 띠 위 한 줄. 왼쪽 **총 편수**(15px / 700 / `#ffffff`), 오른쪽 `시작연도–끝연도 · 최다 N편 (YYYY.MM)`(11px / `#aaaaaa`). 총량과 범위와 최대치를 여기서 못박는다. 세 값 모두 빌드 시점 계산값이다.
- **Entrance:** 막대가 아래에서 620ms 동안 한 번 올라온다. 4ms 간격으로 순차. `prefers-reduced-motion`에서는 끈다.
- **Mobile:** 월 막대를 감추고 **연도 9칸**으로 요약한다. 97개를 390px에 밀어 넣으면 잡음이 되기 때문이다.
- **금지:** 그림자, 축 격자, 범례, 반복 애니메이션. 이 띠는 읽는 도표가 아니라 초상이다.

### Month Ledger Head (홈 전용)
- **Shape:** 반경 0. 하단 `1px solid #dddddd`. 스크롤 시 `top: 55px`(고정 헤더의 실제 높이)에 붙어 지금 보는 달을 알린다.
- **Structure:** 왼쪽 `2026.11`(15px / 700 / `#000000`), 오른쪽 편수(12.5px / 400 / `#555555`). 둘 다 tabular-nums.
- **Count:** 그 달의 **아카이브 전체** 편수. 그 달이 페이지에 걸쳐 잘렸으면 `보이는 수 / 전체 수편`처럼 두 수를 함께 쓴다.
- **Hover:** 없다. 헤드는 링크가 아니므로 색이 변하지 않는다.

### Post List Row (시그니처)
- **Shape:** 반경 0. 하단 `1px solid #f3f3f3`.
- **Structure:** 날짜(12.5px, `#aaaaaa`, 줄바꿈 금지, 최소 80px) + 제목(15.2px, `#000000`). 사이 10px 간격, 위아래 5px 패딩.
- **Hover:** 제목이 불투명도 0.7로 흐려진다. 색이 아니라 투명도로 반응한다.
- **금지:** 요약문, 썸네일, 작성자, 조회수. 이 행에 세 번째 정보를 넣지 않는다.

### Sidebar Widget
- **Shape:** 반경 0. 하단 `2px solid #f1f1f1`(마지막 위젯 제외).
- **Title:** 18px / 700 / `#000000`, FontAwesome 아이콘 선행, 왼쪽 30px 들여쓰기, 12px 상하 패딩.
- **Content:** `8px 0 30px 20px`. 링크는 `#555555`.
- **금지:** 위젯 자체에 배경색이나 테두리를 두르지 않는다. 선은 아래쪽 한 줄뿐이다.

### Tag Chip
- **Shape:** 반경 4px, 패딩 3px 5px.
- **Default:** 배경 `#6c757d`(Bootstrap secondary), 흰 글자, 12px / 700.
- **Hover:** 배경이 `#0057a7` 로 바뀐다. 크기나 위치는 변하지 않는다.
- **용도:** 태그만. 카테고리는 아이콘 + 텍스트 링크로 표시하며 칩을 쓰지 않는다.

### Navigation
- **Style:** 상단 고정, 높이 55px, 하단 `2px solid #ffffff`.
- **Links:** 16px / 700 / `#aaaaaa`, 패딩 `0.5em 1em`. 호버와 현재 항목은 `#ffffff`.
- **Sticky:** 스크롤 시 배경이 `#010205cb` 로 차고 위 그림자가 생긴다.
- **Mobile:** 767px 이하에서 햄버거. 펼친 패널은 검은 바탕 + 굵은 테두리, 하단 30px 패딩.

### Search Control
- **Field:** 높이 56px, 반경 18px, `0 12px 30px rgba(35,35,35,0.08)`. 포커스 시 테두리 `rgba(0,87,167,0.35)` 와 1px 상승.
- **Submit:** 반경 18px, 높이 56px, 로고 그라디언트(`#0059ac` → `#4490c3`) 배경, 흰 글자 600, 남색 그림자. 호버 시 1px 상승 + 그림자 확대.
- **Header 미니 검색:** 35px 원형 아이콘. 호버·포커스 시 폭 200px로 늘어나며 입력란이 드러난다.

### Code Block
- **Shape:** 반경 5px, 패딩 20px, `1px solid #e0e0e0`, 배경 `#f5f5f5`.
- **Typography:** JetBrains Mono 14.4px, 색 `#333333`.
- **Copy Button:** 우상단 8px, 32px 정사각, 반경 5px, 평상시 불투명도 0. 호버 시 나타나고 복사 성공 시 `#4CAF50` 배경 + 체크 아이콘으로 2초간 바뀐다.
- **Mermaid:** `pre.mermaid` 는 흰 배경, 테두리 없음, 가운데 정렬. 코드 블록과 시각적으로 분리된다.

### Callout (Alert)
- **Shape:** 반경 0, 좌측 5px 띠만.
- **Structure:** 아이콘 + 한국어 라벨(참고/팁/중요/경고/주의) 헤딩, 이어서 본문.
- **Color:** 띠와 아이콘과 라벨에만 경보색. **배경은 칠하지 않는다.**
- **본문 폰트:** 본문 계열(Noto Sans KR)로 돌아온다. 일반 인용문만 JetBrains Mono.

### Pagination
- **Style:** 가운데 정렬, 테두리 있는 사각 버튼 나열.
- **Default:** 글자 `#555555`.
- **Active:** 배경 `#999999`, 테두리 동일, 흰 글자. 남색을 쓰지 않는다 — 페이지 번호는 "현재 위치"이지 "행동"이 아니다.

## Do's and Don'ts

### Do:
- **Do** 정보를 나눌 때 1–2px 회색 선을 먼저 고려한다. 그림자는 떠 있는 요소 전용이다.
- **Do** 목록 행을 `날짜 + 제목` 두 조각으로 유지한다. 날짜는 12.5px `#aaaaaa`, 최소 폭 80px, 줄바꿈 금지.
- **Do** 사이드바 위젯에 아이콘 + 18px/700 제목 + 2px 하단선을 세트로 쓴다.
- **Do** 상호작용은 `#0057a7`, 살아있는 상태는 `#3fa4ff` 로 분업을 지킨다.
- **Do** 한국어 본문을 Noto Sans KR로, 굵기 400과 700으로 위계를 만든다.
- **Do** 상단 띠 높이를 홈 260px / 글 150px로 유지한다.
- **Do** 767px 이하에서 사이드바를 숨기고 본문 문단을 17.6px / 1.7em으로 키운다.

### Don't:
- **Don't** 문서 안의 카드·목록·위젯에 그림자를 준다. 이 시스템은 평면이다.
- **Don't** 다크 모드를 전역으로 확장한다. 어두운 면은 상단 띠와 푸터뿐이다.
- **Don't** 목록 행에 요약문이나 썸네일을 추가한다. 장부는 한 줄이다.
- **Don't** `#3fa4ff` 를 정적인 요소(테두리, 배경, 아이콘 장식)에 쓴다. 그 색은 "지금 반응 중"을 뜻한다.
- **Don't** `#0000ff` 를 버튼·메뉴·태그에 쓴다. 그 파랑은 본문 링크 전용이다.
- **Don't** 18px 알약형 반경을 검색 외 요소로 확장한다. 두 번째 알약은 시스템이 아니다.
- **Don't** 콜아웃 배경을 경보색으로 칠한다. 띠·아이콘·라벨까지만.
- **Don't** JetBrains Mono를 라벨이나 내비게이션에 쓴다. 모노는 코드와 인용 전용이다.
- **Don't** 홈의 데이터 띠에 축 격자·범례·반복 애니메이션을 붙인다. 진입 모션 한 번은 허용된다.
- **Don't** 월 러닝 헤드의 편수를 페이지 조각에서 세게 한다. 아카이브 전체 편수여야 한다.
- **Don't** 광고·배너·프로모션 자리를 설계한다. 이 사이트에는 수익화 구조가 없다.
