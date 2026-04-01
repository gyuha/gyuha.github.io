---
title: "cokacdir: Rust로 만든 AI 코딩 에이전트 원격 제어 — Telegram에서 Claude Code를 다룬다"
date: 2026-04-01T00:00:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - claude-code
  - automation
  - terminal
description: "Rust로 작성된 TUI 파일 관리자 cokacdir는 Claude Code, Codex CLI, Gemini CLI를 Telegram 봇으로 원격 제어할 수 있게 해줍니다. 추가 API 비용 없이, 기존 구독 안에서 폰으로 코딩 에이전트를 다룰 수 있습니다."
---

GitHub 스타 192개의 작은 프로젝트지만, 개념은 단순하고 강력합니다. Claude Code를 이미 쓰고 있다면, 그 세션을 Telegram에서 그대로 이어받을 수 있습니다. cokacdir는 AI 에이전트가 아닙니다 — 이미 사용 중인 코딩 에이전트에 위임하고, 그 결과를 Telegram으로 스트리밍해주는 원격 제어 브릿지입니다.

<!--more-->

## Sources

- https://github.com/kstost/cokacdir

---

## cokacdir란 무엇인가

```mermaid
flowchart TD
    User[👤 사용자<br/>Telegram] -->|메시지 전송| Bot[Telegram 봇<br/>cokacdir]
    Bot -->|위임| Agents[코딩 에이전트]
    Agents --> A1[Claude Code]
    Agents --> A2[Codex CLI]
    Agents --> A3[Gemini CLI]
    Agents --> A4[OpenCode]
    A1 & A2 & A3 & A4 -->|실행 결과 스트리밍| Bot
    Bot -->|실시간 스트리밍| User

    Note1[⚠️ LLM 없음<br/>AI 에이전트 아님]
    Note2[✅ 추가 비용 없음<br/>기존 구독 사용]

    classDef userStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef botStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef agentStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef noteStyle fill:#e0c8ef,stroke:#7b5ea7,color:#333
    class User userStyle
    class Bot botStyle
    class A1,A2,A3,A4 agentStyle
    class Note1,Note2 noteStyle
```

**핵심 정의:**

> "cokacdir is **not** an AI agent — it does not include an LLM or reasoning engine. Instead, it delegates tasks to the coding agent you are already using (Claude Code, Codex CLI, Gemini CLI, OpenCode) and lets you control it from Telegram."

이미 사용 중인 에이전트의 구독(또는 무료 티어) 안에서 실행되므로 **추가 API 비용이 없습니다.** 폰에서 Telegram 메시지를 보내면, 로컬 컴퓨터의 Claude Code가 코드를 실행하고 파일을 편집하고 셸 명령을 수행한 뒤 결과를 실시간으로 스트리밍해줍니다.

---

## 빠른 시작: 3단계

```mermaid
flowchart TD
    A["curl -fsSL https://cokacdir.cokac.com/manage.sh | bash && cokacctl"] --> B[cokacdir 관리 TUI 열림]
    B --> C["i 키 → 설치 시작"]
    C --> D[Telegram 봇 토큰 입력<br/>@BotFather에서 생성]
    D --> E["s 키 → 서버 시작"]
    E --> F[Telegram 열고 봇에게 메시지]
    F --> G[✅ Claude Code 원격 제어 시작]

    classDef cmdStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef actionStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef doneStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class A cmdStyle
    class B,C,D,E,F actionStyle
    class G doneStyle
```

**macOS / Linux:**
```bash
curl -fsSL https://cokacdir.cokac.com/manage.sh | bash && cokacctl
```

**Windows (PowerShell 관리자):**
```powershell
irm https://cokacdir.cokac.com/manage.ps1 | iex; cokacctl
```

---

## 두 개의 얼굴: TUI 파일 관리자 + Telegram 봇

cokacdir는 두 가지 역할을 합니다. 로컬에서는 풀기능 TUI 파일 관리자로, 원격에서는 Telegram 봇 인터페이스로 동작합니다.

### TUI 파일 관리자 기능

```mermaid
flowchart TD
    TUI[cokacdir TUI] --> AI[AI 명령<br/>. 키 → 자연어 입력<br/>Claude/Codex/Gemini/OpenCode 위임]
    TUI --> Files[파일 관리]
    TUI --> Code[코드 도구]
    TUI --> Remote[원격 접근]
    TUI --> Security[보안 도구]

    Files --> F1[멀티 패널 파일 탐색]
    Files --> F2[재귀 파일 검색]
    Files --> F3[중복 파일 감지<br/>해시 기반 비교]
    Files --> F4[사이드바이사이드 Diff<br/>폴더/파일]

    Code --> C1[내장 에디터<br/>20개+ 언어 신택스 하이라이팅]
    Code --> C2[Git 통합<br/>status, commit, log, branch, diff]
    Code --> C3[프로세스 매니저<br/>정렬 가능한 컬럼]

    Remote --> R1[SSH/SFTP 원격 탐색<br/>저장된 프로필]
    Remote --> R2[이미지 뷰어<br/>Kitty, iTerm2, Sixel]

    Security --> S1["AES-256 파일 암호화<br/>청크 분할 설정 가능"]

    classDef tuiStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef catStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef featStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class TUI tuiStyle
    class AI,Files,Code,Remote,Security catStyle
    class F1,F2,F3,F4,C1,C2,C3,R1,R2,S1 featStyle
```

**성능:** Rust로 작성, LTO + strip 최적화. 단일 바이너리 15~20MB (플랫폼별 상이).

---

### Telegram 봇 기능

```mermaid
flowchart TD
    TelegramBot[Telegram 봇] --> Stream[실시간 스트리밍<br/>Claude Code 출력 그대로]
    TelegramBot --> Session[세션 관리]
    TelegramBot --> Schedule[스케줄 태스크]
    TelegramBot --> Multi[멀티 에이전트]
    TelegramBot --> Files2[파일 전송]

    Session --> S1[세션 지속성<br/>재연결 후에도 컨텍스트 유지]
    Session --> S2[크로스 프로바이더<br/>세션 해석]
    Session --> S3[멀티 프로바이더<br/>Claude, Codex, Gemini, OpenCode]

    Schedule --> Sc1[cron 표현식]
    Schedule --> Sc2[절대 시간 지정]

    Multi --> M1[그룹 채팅 지원<br/>여러 봇이 컨텍스트 공유]
    Multi --> M2[봇 간 메시지<br/>멀티 에이전트 워크플로우]

    Files2 --> Fi1[파일 업로드/다운로드]
    Files2 --> Fi2[도구 관리]
    Files2 --> Fi3[디버그 로깅]

    classDef botStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef catStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef featStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class TelegramBot botStyle
    class Stream,Session,Schedule,Multi,Files2 catStyle
    class S1,S2,S3,Sc1,Sc2,M1,M2,Fi1,Fi2,Fi3 featStyle
```

**Telegram 명령어 전체 목록:**

```
/start       세션 시작
/stop        세션 중지
/clear       컨텍스트 초기화
/help        도움말
/session     세션 정보
/pwd         현재 디렉토리
/model       AI 모델 변경
/down        파일 다운로드
/instruction 지시사항 설정
/instruction_clear  지시사항 초기화
/allowed     허용된 작업 목록
/allowedtools       허용된 도구 목록
/availabletools     사용 가능한 도구 목록
/context     현재 컨텍스트 보기
/query       직접 쿼리
/public      공개 모드
/direct      직접 모드
/setpollingtime     폴링 간격 설정
/debug       디버그 모드
/silent      무음 모드
```

---

## 멀티 에이전트 워크플로우

봇 간 메시지 기능으로 여러 에이전트가 협력하는 워크플로우를 구성할 수 있습니다.

```mermaid
sequenceDiagram
    participant U as 사용자 (Telegram)
    participant B1 as Bot 1 (Claude Code)
    participant B2 as Bot 2 (Gemini CLI)
    participant B3 as Bot 3 (Codex CLI)

    U->>B1: "프론트엔드 컴포넌트 구현해줘"
    B1->>B1: Claude Code로 구현
    B1->>B2: "이 코드 테스트 작성해줘"
    B2->>B2: Gemini CLI로 테스트 생성
    B2->>B3: "성능 최적화 검토해줘"
    B3->>B3: Codex CLI로 최적화 분석
    B3-->>B1: 최적화 제안
    B1-->>U: 최종 결과 스트리밍
```

그룹 채팅 지원으로 여러 봇이 동일한 컨텍스트를 공유하며 협력할 수도 있습니다.

---

## 지원 플랫폼

| 플랫폼 | 아키텍처 |
|---|---|
| macOS | Apple Silicon (M1/M2/M3) & Intel |
| Linux | x86_64 & ARM64 |
| Windows | x86_64 & ARM64 |

---

## 핵심 요약

```mermaid
flowchart TD
    Why[왜 cokacdir인가?] --> W1[📱 이동 중에도<br/>Claude Code 제어]
    Why --> W2[💰 추가 비용 없음<br/>기존 구독 사용]
    Why --> W3[⚡ Rust 성능<br/>15~20MB 단일 바이너리]
    Why --> W4[🤖 멀티 에이전트<br/>봇 간 협업]
    Why --> W5[🔧 완전한 TUI<br/>파일 관리자까지]

    classDef whyStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef featStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class Why whyStyle
    class W1,W2,W3,W4,W5 featStyle
```

| 항목 | 내용 |
|---|---|
| **저장소** | github.com/kstost/cokacdir |
| **언어** | Rust |
| **바이너리 크기** | 15~20MB |
| **라이선스** | MIT |
| **GitHub 스타** | ⭐ 192 |
| **지원 에이전트** | Claude Code, Codex CLI, Gemini CLI, OpenCode |
| **추가 비용** | 없음 (기존 구독 사용) |
| **Telegram 명령어** | 20개+ |
| **플랫폼** | macOS, Linux, Windows (Apple Silicon 포함) |

---

## 결론

cokacdir는 "Telegram으로 Claude Code를 원격 제어한다"는 아이디어를 Rust로 구현한 도구입니다. 별도의 AI 모델이나 API 비용이 없고, 이미 사용 중인 Claude Code 세션에 Telegram이라는 인터페이스를 추가하는 방식입니다.

TUI 파일 관리자로서의 기능(Git, SSH/SFTP, AES-256 암호화, 내장 에디터)도 충분히 풍부하지만, 핵심 가치는 하나입니다 — 폰에서 Telegram 메시지 하나로 로컬 컴퓨터의 코딩 에이전트에게 일을 시키는 것.
