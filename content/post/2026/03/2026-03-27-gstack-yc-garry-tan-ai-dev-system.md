---
title: "G스택 — YC 대표 게리탄이 혼자 60만 줄을 짠 AI 개발 팀 시스템"
date: 2026-03-27T00:00:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - claude-code
  - agents
  - vibe-coding
description: "G스택은 YC 대표 게리탄이 공개한 AI 전문가 팀 시스템입니다. Claude Code에 28개 전문 역할을 부여해 기획·설계·코딩·디자인 리뷰·보안·배포를 하나의 흐름으로 연결합니다. 소크라테스식 오피스 아워, AI 슬롭 탐지 디자인 리뷰, 7단계 워크플로우를 상세히 정리합니다."
---

YC 대표 게리탄이 60일 동안 혼자 60만 줄의 코드를 짰습니다. 비결은 코딩 실력이 아닙니다. **AI로 팀을 만들었기 때문입니다.** 그 팀의 이름이 G스택(G-Stack)입니다. GitHub에 올린 지 2주 만에 좋아요 48,000개를 돌파한 이 시스템을 완전히 파헤칩니다.

<!--more-->

## Sources

- https://youtu.be/7ozueqcLWt0?si=R-ApSLM09LiWJ8cy

---

## AI한테 코딩만 시키면 생기는 문제

AI 코딩 도구를 써봤다면 익숙한 상황이 있습니다. 결과물은 나오는데 품질이 의심스럽고, 보안 구멍이 있는지 없는지 모르고, 디자인은 왜 다 비슷비슷하게 촌스럽습니다.

이유는 단순합니다. **AI에게 코딩만 시키기 때문**입니다.

```mermaid
flowchart TD
    A["소프트웨어 개발 전체 과정"]
    B1["기획"]
    B2["설계"]
    B3["코딩"]
    B4["검수"]
    B5["테스트"]
    B6["배포"]
    B7["회고"]
    C["기존 AI 활용"]
    D["AI한테 코딩만 시킴"]
    E["품질 불안·보안 누락·촌스러운 디자인"]

    A --> B1 --> B2 --> B3 --> B4 --> B5 --> B6 --> B7
    C --> D --> E

    classDef all fill:#c5dcef,color:#333
    classDef missing fill:#ffc8c4,color:#333
    classDef only fill:#fde8c0,color:#333
    class B1,B2,B4,B5,B6,B7 missing
    class B3 only
    class C,D,E missing
```

식당에 비유하면 요리사만 있는 셈입니다. 메뉴 기획, 인테리어, 위생 검사, 서빙, 회계 없이 주방만 있는 식당이죠. 게리탄은 이 문제를 **AI에게 역할을 주는 방식**으로 해결했습니다.

---

## G스택이란

G스택은 AI 하나를 28개 전문가 역할의 개발 팀으로 바꿔주는 시스템입니다.

```mermaid
flowchart TD
    GS["G스택 (G-Stack)"]
    R1["대표 (CEO)<br>기획·범위 결정"]
    R2["개발 팀장<br>설계·기술 결정"]
    R3["디자이너<br>UI 검토"]
    R4["품질 관리자 (QA)<br>실제 브라우저 테스트"]
    R5["보안 담당자<br>취약점 점검"]
    R6["출시 담당자<br>배포·모니터링"]
    R7["+ 22개 전문 역할"]

    GS --> R1
    GS --> R2
    GS --> R3
    GS --> R4
    GS --> R5
    GS --> R6
    GS --> R7

    classDef main fill:#fde8c0,color:#333
    classDef role fill:#c5dcef,color:#333
    classDef extra fill:#c0ecd3,color:#333
    class GS main
    class R1,R2,R3,R4,R5,R6 role
    class R7 extra
```

각 역할은 자기 일만 합니다. 대표 역할은 기획만 보고, 디자이너는 디자인만 보고, 품질 관리자는 실제 브라우저를 열어 직접 클릭하며 테스트합니다. 그리고 **앞 사람의 결과물이 다음 사람에게 자동으로 넘어갑니다.**

사용법은 간단합니다. 채팅창에 슬래시 명령어를 입력하면 해당 전문가가 나옵니다.

---

## 오피스 아워 (Office Hours) — 소크라테스식 아이디어 검증

G스택에서 가장 감탄할 기능입니다. `/office-hours`를 실행하면 AI가 코드를 한 줄도 짜기 전에 **날카로운 질문 6개**를 합니다.

보통 AI는 "이거 만들어 줘"라고 하면 바로 만들기 시작합니다. 오피스 아워는 그러지 않습니다. "그거 진짜로 필요한 거 맞아요?"부터 물어봅니다.

### 소크라테스 방법의 현대적 구현

이 방식은 2,500년 된 교육 철학에서 왔습니다. 소크라테스는 답을 주지 않고 질문으로 상대방이 스스로 모순을 발견하게 했습니다. UCLA 로버트 비어크 교수 연구에 따르면, 스스로 질문에 답하려고 애쓴 사람이 설명을 들은 사람보다 장기 기억률이 60% 이상 높습니다. 대학생 74명 실험에서 93%가 소크라테스식 수업을 더 선호했습니다.

G스택은 이 방법을 AI로 구현했습니다.

### 6가지 질문

```mermaid
flowchart TD
    OH["/office-hours 실행"]
    Q1["1. 진짜 수요가 있는가?<br>없으면 화날 정도로 원하는 사람이 있나요?<br>→ 가짜 수요 필터"]
    Q2["2. 지금은 어떻게 하고 있는가?<br>대안이 없다면 진짜 문제가 아닐 수 있음"]
    Q3["3. 구체적으로 누구한테 필요한가?<br>직업·고민이 구체적인 한 사람만 말하기"]
    Q4["4. 가장 작은 시작은 뭔가?<br>이번 주 안에 돈을 낼 정도의 최소 버전"]
    Q5["5. 직접 본 적 있는가?<br>사용자가 쓰는 걸 옆에서 본 적 있나요?"]
    Q6["6. 미래에도 필요한가?<br>3년 뒤에도 더 필요해질 제품인가?"]
    R["결과물: 코드가 아닌 기획서<br>생각이 먼저, 만드는 건 나중"]

    OH --> Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> Q6 --> R

    classDef q fill:#c5dcef,color:#333
    classDef start fill:#fde8c0,color:#333
    classDef result fill:#c0ecd3,color:#333
    class OH start
    class Q1,Q2,Q3,Q4,Q5,Q6 q
    class R result
```

이 과정에서 AI는 절대 아부하지 않습니다. "좋은 아이디어네요"나 "여러 방법이 있죠" 같은 말이 금지되어 있습니다. 무조건 자기 입장을 잡고 근거를 대고 반박합니다.

실제 예시: 사용자가 "일정 앱을 만들고 싶다"고 하자, AI가 "잠깐요. 당신이 말한 건 알림이 아닙니다. 당신이 실제로 묘사한 건 개인 비서 AI입니다"라고 응답했습니다. 사용자가 스스로도 몰랐던 진짜 제품을 찾아낸 것입니다.

---

## 디자인 리뷰 — AI 슬롭 탐지

AI로 웹사이트를 만들어 본 분이라면 알 겁니다. 보라색 그라데이션 배경, 동그란 아이콘 3개, "Unlock the Power of..." 같은 문구. G스택은 이걸 **AI 슬롭(AI Slop)**이라고 부릅니다.

`/design-review`를 실행하면 AI가 실제 브라우저를 열어 80개 항목을 하나하나 체크합니다.

```mermaid
flowchart TD
    DR["/design-review 실행"]
    subgraph "80개 체크 항목"
        F["글꼴 15개"]
        C["색상 10개"]
        S["여백·배치 12개"]
        I["버튼·메뉴 반응 10개"]
        R["화면 크기 대응 8개"]
        A["애니메이션 6개"]
        AI["AI 슬롭 탐지 10개"]
    end
    SCORE["성적표 출력<br>디자인 점수 (A~F)<br>AI 슬롭 점수 (A~F)"]
    FIX["코드 직접 수정<br>수정 전후 스크린샷 비교<br>마음 안 들면 되돌리기"]

    DR --> F & C & S & I & R & A & AI --> SCORE --> FIX

    classDef check fill:#c5dcef,color:#333
    classDef main fill:#fde8c0,color:#333
    classDef result fill:#c0ecd3,color:#333
    class DR main
    class F,C,S,I,R,A,AI check
    class SCORE,FIX result
```

### AI 슬롭 탐지 10가지

| 번호 | 패턴 |
|------|------|
| 1 | 보라색·남색 그라데이션 배경 |
| 2 | 3열 구성 — 동그란 아이콘 + 굵은 제목 + 2줄 설명 |
| 3 | 색깔 원 안에 아이콘 넣기 |
| 4 | 모든 요소 가운데 정렬 |
| 5 | 모든 모서리 둥글게 |
| 6 | 불필요한 물방울·물결 장식 |
| 7 | 제목에 로켓 이모지 |
| 8 | 카드 왼쪽에 색깔 줄 넣기 |
| 9 | "Welcome to X", "The one solution" 같은 AI 냄새 문구 |
| 10 | 기능·후기·가격·버튼 판에 박힌 순서 |

10가지 중 하나만 걸려도 점수가 깎입니다.

다른 AI 도구(Codex, Gemini, Cursor)가 설치되어 있으면 동시에 리뷰를 시킵니다. 두 AI가 같은 디자인을 각자 보는 **교차 검증**입니다.

---

## 7단계 전체 워크플로우

기획부터 배포 후 회고까지 28개 역할이 하나의 흐름으로 연결됩니다.

```mermaid
flowchart TD
    S1["/office-hours<br>아이디어 검증 6 질문<br>→ 기획서 출력"]
    S2["/plan CEO review<br>대표 관점 범위 조정<br>키울지·줄일지·일지할지"]
    S3["/plan review<br>기술 설계 + 테스트 계획"]
    S4["코드 작성"]
    S5["/review<br>10년차 개발자 코드 검수<br>겉은 멀쩡한데 터지는 문제 탐지"]
    S6["/QA<br>실제 브라우저 클릭·입력·캡처<br>사람 테스트와 동일"]
    S7["/SO (Security)<br>해커 시점 보안 점검<br>취약점 탐지"]
    S8["/10<br>출시 준비"]
    S9["/land-and-deploy<br>실제 배포"]
    S10["/canary<br>출시 후 5~10분 모니터링<br>문제 여부 감시"]
    S11["/retro<br>주간 회고<br>뭘 했는지·품질·개선점"]

    S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11

    classDef plan fill:#fde8c0,color:#333
    classDef build fill:#c5dcef,color:#333
    classDef release fill:#c0ecd3,color:#333
    classDef retro fill:#e0c8ef,color:#333
    class S1,S2,S3 plan
    class S4,S5,S6,S7 build
    class S8,S9,S10 release
    class S11 retro
```

앞 사람의 결과물이 다음 사람의 출발점이 됩니다. 이것이 그냥 "AI한테 만들어 줘"와 근본적으로 다른 점입니다.

---

## 설치 및 사용법

**설치 (30초):**

```bash
# G-Stack 다운로드 (GitHub에서 gstack 검색)
# Claude Code + GitHub Actions 필요 (둘 다 무료)
```

**추천 시작 순서:**

```
1. /office-hours    → 아이디어 검증
2. /plan review     → 설계 확정
3. (코드 작성)
4. /review          → 코드 검수
5. /design-review   → 디자인 점검
6. /land-and-deploy → 배포
```

**다중 AI 지원:** Claude Code 외에 Codex, Gemini, Cursor에서도 사용 가능합니다. 설치 시 옵션 하나만 바꾸면 됩니다. 팀이라면 프로젝트 폴더 안에 직접 넣으면 팀 전체가 같은 기준으로 일할 수 있습니다.

---

## 장단점

```mermaid
flowchart TD
    subgraph "장점"
        P1["기획·설계·검수·배포 전 과정 커버"]
        P2["소크라테스식 아이디어 검증"]
        P3["AI 슬롭 탐지 디자인 리뷰"]
        P4["실제 브라우저 QA 자동화"]
        P5["보안 취약점 자동 탐지"]
        P6["무료·오픈소스"]
    end

    subgraph "단점"
        N1["훅(hooks) 자동 트리거 미지원"]
        N2["코드 테스트(unit test) 커버리지 부족"]
        N3["개발 전문가보다 기획·PO 관점 강함"]
    end

    classDef pro fill:#c0ecd3,color:#333
    classDef con fill:#ffc8c4,color:#333
    class P1,P2,P3,P4,P5,P6 pro
    class N1,N2,N3 con
```

**가장 잘 맞는 사용자:** 개발자 출신으로 혼자 사업하는 분, 또는 개발자 출신으로 PO·PM 역할을 해야 하는 분. 코딩은 할 줄 아는데 기획·디자인·보안·배포까지 혼자 다 해야 하는 상황에서 빛납니다.

---

## 핵심 요약

| 항목 | 내용 |
|------|------|
| **이름** | G스택 (G-Stack) |
| **만든 사람** | 게리탄 (Garry Tan, YC 대표) |
| **결과** | 60일 · 60만 줄 · 혼자 · GitHub 2주 48,000+ ★ |
| **핵심 개념** | AI에게 역할 부여 → 28개 전문가 팀 |
| **오피스 아워** | 소크라테스식 6 질문 아이디어 검증 → 기획서 출력 |
| **디자인 리뷰** | 80개 항목 체크 + AI 슬롭 탐지 10가지 |
| **워크플로우** | 7단계: 기획 → 설계 → 코딩 → 검수 → QA → 보안 → 배포 → 회고 |
| **지원 도구** | Claude Code · Codex · Gemini · Cursor |
| **비용** | 무료 오픈소스 |

---

## 결론

G스택이 보여주는 핵심 인사이트는 단순합니다. AI에게 코딩만 시키는 것이 아니라 **전체 개발 과정의 각 역할을 맡기는 것**입니다. 혼자서 28명분의 전문성으로 일하는 방법이죠.<br>
특히 오피스 아워의 소크라테스식 6 질문은 "만들기 전에 제대로 생각했는가"를 강제합니다. 아이디어가 있을 때 코드부터 짜는 습관이 있다면, G스택의 `/office-hours`를 먼저 실행하는 것만으로도 실패 확률을 크게 줄일 수 있습니다.
