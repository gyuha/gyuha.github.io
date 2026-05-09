---
title: "Claude Code로 풀 개발팀 운영하기: 5개 폴더로 완성하는 ADK 시스템"
date: 2026-05-09T00:00:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - claude-code
  - agents
  - workflow
description: "CLAUDE.md, skills, hooks, subagents, plugins — 다섯 개 레이어로 Claude Code를 개발팀처럼 운용하는 Agent Development Kit 완전 해설"
---

Claude Code를 혼자 쓰면 강력한 어시스턴트다.<br>
5개 폴더를 갖추면 개발팀이 된다.

이 글은 **Agent Development Kit(ADK)** — Claude Code를 팀 수준으로 끌어올리는 5계층 구조를 해설한다.

<!--more-->

## 왜 5개 레이어인가

AI 코딩 도구 대부분은 "대화"로 끝난다. 요청 → 응답 → 끝. 컨텍스트는 세션마다 초기화되고, 팀원끼리 같은 환경을 공유할 방법이 없다.

ADK는 이 문제를 구조로 푼다. 각 레이어가 서로 다른 책임을 맡고, 합쳐지면 일관된 개발 환경이 만들어진다.

```mermaid
flowchart TD
    U([사용자 요청]) --> CM

    CM["📄 CLAUDE.md<br/>Memory · 컨텍스트 헌법"]
    SK["🧠 skills/<br/>Knowledge · 재사용 워크플로"]
    HK["🛡️ hooks/<br/>Guardrails · 결정론적 제어"]
    SA["🤖 subagents/<br/>Delegation · 격리 에이전트"]
    PL["📦 plugins/<br/>Distribution · 팀 배포"]

    CM --> SK
    SK --> HK
    HK --> SA
    SA --> PL

    classDef memory fill:#c5dcef,color:#333
    classDef knowledge fill:#c0ecd3,color:#333
    classDef guard fill:#fde8c0,color:#333
    classDef delegate fill:#e0c8ef,color:#333
    classDef dist fill:#ffc8c4,color:#333

    class CM memory
    class SK knowledge
    class HK guard
    class SA delegate
    class PL dist
```

---

## Layer 1. CLAUDE.md — Memory

> Your repo's constitution. Naming rules, structure, expectations.<br>
> One global file for all projects, one local file per repo.

**CLAUDE.md** 는 Claude가 세션을 시작할 때 가장 먼저 읽는 파일이다. 팀의 코딩 컨벤션, 금지 명령어, 디렉터리 구조, 배포 규칙이 여기에 담긴다.

두 단계로 운용한다.

```mermaid
flowchart TD
    G["~/.claude/CLAUDE.md<br/>글로벌 파일<br/>모든 프로젝트에 적용"]
    L["./CLAUDE.md<br/>로컬 파일<br/>이 레포에만 적용"]
    C["Claude 세션 시작"]

    G --> C
    L --> C
    C --> R["컨텍스트 적용 완료<br/>규칙·기대치 로드"]

    classDef global fill:#c5dcef,color:#333
    classDef local fill:#c0ecd3,color:#333
    classDef session fill:#e0c8ef,color:#333
    classDef result fill:#fde8c0,color:#333

    class G global
    class L local
    class C session
    class R result
```

글로벌 파일에는 모든 프로젝트에 공통으로 적용할 원칙(페르소나, 언어 감지, 금지 표현 등)을 넣는다.<br>
로컬 파일에는 이 레포 특화 규칙(빌드 커맨드, 카테고리 제한, 파일 네이밍 등)을 넣는다.

**CLAUDE.md가 없으면** Claude는 매 세션마다 같은 질문을 반복하고, 팀마다 다른 결과를 낸다.

---

## Layer 2. skills/ — Knowledge

> Reusable workflows Claude auto-invokes by matching the task description.<br>
> No slash commands. It just knows.

**스킬** 은 재사용 가능한 워크플로 명세다. Claude는 사용자의 요청을 읽고, 매칭되는 스킬을 자동으로 불러와 실행한다. 슬래시 커맨드를 외울 필요가 없다.

```mermaid
flowchart TD
    REQ["사용자 요청<br/>예: '이 URL로 포스팅 써줘'"]
    MATCH{"스킬 매칭"}
    S1["url-only-to-blog-post<br/>SKILL.md"]
    S2["youtube-to-blog-post<br/>SKILL.md"]
    S3["mermaid-diagrams<br/>SKILL.md"]
    EXEC["스킬 워크플로 실행<br/>체크리스트 · 품질 게이트"]
    OUT["결과물 생성"]

    REQ --> MATCH
    MATCH -->|"URL 감지"| S1
    MATCH -->|"YouTube URL"| S2
    MATCH -->|"다이어그램 요청"| S3
    S1 --> EXEC
    S2 --> EXEC
    S3 --> EXEC
    EXEC --> OUT

    classDef req fill:#c5dcef,color:#333
    classDef match fill:#fde8c0,color:#333
    classDef skill fill:#c0ecd3,color:#333
    classDef exec fill:#e0c8ef,color:#333
    classDef out fill:#ffc8c4,color:#333

    class REQ req
    class MATCH match
    class S1,S2,S3 skill
    class EXEC exec
    class OUT out
```

좋은 스킬은 세 가지를 포함한다.
1. **트리거 조건** — 어떤 상황에서 이 스킬을 쓸지
2. **단계별 워크플로** — 순서가 명확한 체크리스트
3. **품질 게이트** — 완료 전 검증 기준

스킬이 없으면 Claude는 매번 맥락 없이 즉흥적으로 판단한다. 팀원마다 결과가 달라진다.

---

## Layer 3. hooks/ — Guardrails

> Shell scripts that run before and after every tool call.<br>
> Block dangerous commands. Auto-lint on save. Ping Slack on deploy.<br>
> Deterministic. Not AI.

**훅** 은 AI가 아니다. 도구 호출 전후에 실행되는 쉘 스크립트다. Claude가 파일을 쓰기 전, 명령어를 실행하기 전 — 훅이 먼저 동작한다.

```mermaid
flowchart TD
    REQ["Claude 도구 호출 시도"]
    PRE["PreToolUse Hook<br/>실행 전 검사"]
    BLOCK{"위험 명령어?"}
    DENY["🚫 차단<br/>실행 취소"]
    ALLOW["✅ 허용<br/>도구 실행"]
    POST["PostToolUse Hook<br/>실행 후 처리"]
    LINT["자동 린트"]
    NOTIF["Slack 알림<br/>(배포 시)"]

    REQ --> PRE
    PRE --> BLOCK
    BLOCK -->|"Yes"| DENY
    BLOCK -->|"No"| ALLOW
    ALLOW --> POST
    POST --> LINT
    POST --> NOTIF

    classDef req fill:#c5dcef,color:#333
    classDef hook fill:#fde8c0,color:#333
    classDef check fill:#e0c8ef,color:#333
    classDef deny fill:#ffc8c4,color:#333
    classDef allow fill:#c0ecd3,color:#333
    classDef post fill:#fde8c0,color:#333

    class REQ req
    class PRE,POST hook
    class BLOCK check
    class DENY deny
    class ALLOW allow
    class LINT,NOTIF post
```

실제 활용 예시:
- `rm -rf /` 같은 파괴적 명령어 차단
- 파일 저장 시 자동 prettier 실행
- `git push` 후 Slack 채널에 배포 알림
- 커밋 전 테스트 통과 확인

훅의 핵심은 **결정론적** 이라는 점이다. AI가 판단하는 게 아니라 규칙이 실행된다. "이번엔 잊어버리지 않겠지"가 아니라 "물리적으로 불가능하다"가 된다.

---

## Layer 4. subagents/ — Delegation

> Isolated agents with their own context window.<br>
> A code reviewer that only sees the diff. A test runner with custom permissions.<br>
> Keeps your main session clean.

**서브에이전트** 는 격리된 컨텍스트 윈도우를 가진 독립 에이전트다. 메인 세션의 컨텍스트를 오염시키지 않고 특정 작업을 위임할 수 있다.

```mermaid
flowchart TD
    MAIN["메인 세션<br/>사용자 ↔ Claude"]
    TASK{"복잡한 작업 감지"}

    MAIN --> TASK

    TASK -->|"코드 리뷰"| CR
    TASK -->|"테스트 실행"| TR
    TASK -->|"문서 생성"| DG

    CR["코드 리뷰 에이전트<br/>diff만 본다<br/>읽기 전용 권한"]
    TR["테스트 에이전트<br/>테스트 파일만 접근<br/>실행 권한"]
    DG["문서 에이전트<br/>소스 코드 읽기<br/>md 파일 쓰기"]

    CR --> RES
    TR --> RES
    DG --> RES

    RES["결과 요약 반환<br/>메인 세션으로"]

    classDef main fill:#c5dcef,color:#333
    classDef task fill:#fde8c0,color:#333
    classDef agent fill:#c0ecd3,color:#333
    classDef result fill:#e0c8ef,color:#333

    class MAIN main
    class TASK task
    class CR,TR,DG agent
    class RES result
```

서브에이전트가 중요한 이유:
- **컨텍스트 격리** — 메인 세션이 100k 토큰으로 오염되지 않는다
- **권한 분리** — 각 에이전트가 필요한 권한만 갖는다
- **병렬 실행** — 독립적인 작업을 동시에 처리한다
- **전문화** — 코드 리뷰어는 diff만, 테스트 러너는 테스트만 본다

---

## Layer 5. plugins/ — Distribution

> Bundle the whole system into one install.<br>
> Every teammate gets the same skills, same hooks, same agents.<br>
> Aligned from day one.

**플러그인** 은 위의 4개 레이어를 하나로 묶어 배포하는 단위다. 팀에 새 멤버가 합류하면 플러그인 하나를 설치하는 것으로 같은 환경을 갖는다.

```mermaid
flowchart TD
    BUNDLE["📦 Plugin Bundle"]
    BUNDLE --> CM2["CLAUDE.md 규칙"]
    BUNDLE --> SK2["skills/ 워크플로"]
    BUNDLE --> HK2["hooks/ 가드레일"]
    BUNDLE --> SA2["subagents/ 정의"]

    CM2 --> TEAM
    SK2 --> TEAM
    HK2 --> TEAM
    SA2 --> TEAM

    TEAM["팀 전체 설치"]
    TEAM --> DEV1["개발자 A<br/>동일한 환경"]
    TEAM --> DEV2["개발자 B<br/>동일한 환경"]
    TEAM --> DEV3["신규 합류<br/>Day 1부터 동일"]

    classDef bundle fill:#fde8c0,color:#333
    classDef layer fill:#c5dcef,color:#333
    classDef team fill:#e0c8ef,color:#333
    classDef dev fill:#c0ecd3,color:#333

    class BUNDLE bundle
    class CM2,SK2,HK2,SA2 layer
    class TEAM team
    class DEV1,DEV2,DEV3 dev
```

플러그인이 없으면 팀원마다 다른 CLAUDE.md를 쓰고, 다른 스킬을 갖고, 다른 결과를 낸다. "Claude가 내 팀원 것은 되는데 내 것은 안 돼" 같은 상황이 생긴다.

---

## 전체 시스템: 5계층이 합쳐지면

```mermaid
flowchart TD
    IN(["사용자 요청"])

    subgraph ADK ["Agent Development Kit"]
        direction TD
        L1["Layer 1: CLAUDE.md<br/>컨텍스트 · 규칙 · 기대치"]
        L2["Layer 2: skills/<br/>재사용 워크플로 자동 매칭"]
        L3["Layer 3: hooks/<br/>실행 전후 결정론적 제어"]
        L4["Layer 4: subagents/<br/>격리 컨텍스트 위임 처리"]
        L5["Layer 5: plugins/<br/>팀 전체 일괄 배포"]

        L1 --> L2 --> L3 --> L4 --> L5
    end

    IN --> L1
    L5 --> OUT(["결과물 · 팀 전체 동일 품질"])

    classDef layer1 fill:#c5dcef,color:#333
    classDef layer2 fill:#c0ecd3,color:#333
    classDef layer3 fill:#fde8c0,color:#333
    classDef layer4 fill:#e0c8ef,color:#333
    classDef layer5 fill:#ffc8c4,color:#333

    class L1 layer1
    class L2 layer2
    class L3 layer3
    class L4 layer4
    class L5 layer5
```

각 레이어가 하는 일을 한 줄로 정리하면:

| 레이어 | 폴더 | 역할 | 성격 |
|--------|------|------|------|
| 1 | `CLAUDE.md` | 기억 · 컨텍스트 헌법 | 정적 |
| 2 | `skills/` | 지식 · 워크플로 자동 실행 | AI |
| 3 | `hooks/` | 가드레일 · 결정론적 제어 | 결정론적 |
| 4 | `subagents/` | 위임 · 격리 에이전트 | AI |
| 5 | `plugins/` | 배포 · 팀 정렬 | 정적 |

---

## 마치며

Claude Code는 도구다. ADK는 그 도구를 조직으로 만드는 구조다.

5개 폴더. 그게 전부다.<br>
갖추고 나면 Claude는 질문에 답하는 챗봇이 아니라 — 규칙을 기억하고, 워크플로를 실행하고, 위험을 차단하고, 작업을 위임하고, 팀 전체에 일관성을 제공하는 시스템이 된다.

시작점은 간단하다: `CLAUDE.md` 하나를 써라. 나머지 레이어는 필요가 생길 때 추가하면 된다.
