---
title: "AGENTS.md 완벽 가이드: 점진적 공개(Progressive Disclosure)와 Instruction Budget 관리"
date: 2026-08-14T00:30:00+09:00
draft: false
categories:
  - AI
tags:
  - agents
  - prompt-engineering
  - architecture
  - claude-code
  - context-engineering
  - testing
description: "AGENTS.md를 비대한 프로젝트 설명서가 아닌 고비용 작업 컨텍스트로 재정의하고, 점진적 공개(Progressive Disclosure)와 명령어 예산(Instruction Budget) 최적화를 통해 코딩 에이전트 성능을 극대화하는 Matt Pocock의 완벽 가이드를 분석합니다."
---

Claude Code, Cursor, Codex, OpenCode 등 다양한 AI 코딩 에이전트 생태계에서 `AGENTS.md` 파일은 에이전트에게 프로젝트의 지침을 전달하는 핵심 표준 관문으로 자리 잡았습니다. 하지만 많은 팀들이 `/init` 커맨드로 자동 생성된 파일이나 프로젝트 전체 매뉴얼을 `AGENTS.md`에 무비판적으로 채워 넣으면서, 에이전트가 지시를 혼동하고 성능이 급격히 저하되는 **'진흙 뭉치(Ball of Mud)'** 문제를 겪고 있습니다.

TypeScript 및 AI 엔지니어링 전문가 **Matt Pocock**의 심층 가이드([A Complete Guide to AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md))를 바탕으로, **AGENTS.md의 올바른 정체성, 명령어 예산(Instruction Budget) 관리법, 점진적 공개(Progressive Disclosure) 트리 구조, 모노레포 운용법, 그리고 즉시 적용 가능한 5단계 리팩토링 프롬프트**를 체계적으로 정리합니다.

<!--more-->

## Sources

- [Matt Pocock: A Complete Guide to AGENTS.md (AI Hero)](https://www.aihero.dev/a-complete-guide-to-agents-md)
- [원문 X 게시물 및 리팩토링 프롬프트 공유](https://x.com/i/status/2087820511099203769)
- [Humanlayer: The Instruction Budget Concept](https://www.humanlayer.io)

---

## 1. AGENTS.md의 본질: "고비용 작업 컨텍스트"

`AGENTS.md`는 Git 저장소에 커밋되어 AI 코딩 에이전트의 행동 방식을 커스터마이징하는 마크다운 파일입니다. 에이전트가 실행될 때 **시스템 프롬프트(System Prompt) 바로 아래, 대화 히스토리 최상단**에 자동으로 주입되는 구성 계층(Configuration Layer)입니다.

이 파일은 크게 두 가지 영역의 지침을 다룹니다:
* **개인 스코프 (Personal Scope)**: 개발자의 커밋 메시지 작성 스타일, 선호하는 코딩 패턴.
* **프로젝트 스코프 (Project Scope)**: 프로젝트의 핵심 목적, 패키지 매니저, 핵심 아키텍처 결정.

> **💡 도구 간 호환 팁 (CLAUDE.md):**  
> Claude Code는 `AGENTS.md` 대신 `CLAUDE.md`를 기본으로 인식합니다. 심볼릭 링크를 걸어두면 단일 파일로 모든 도구를 통일할 수 있습니다:
> ```bash
> ln -s AGENTS.md CLAUDE.md
> ```

---

## 2. 거대한 AGENTS.md가 초래하는 치명적 문제

### 1) '진흙 뭉치(Ball of Mud)'의 악순환 루프
`AGENTS.md`가 위험할 정도로 비대해지는 전형적인 패턴이 있습니다:
1. 에이전트가 마음에 들지 않는 동작을 수행함.
2. 개발자가 이를 방지하기 위해 `AGENTS.md`에 새로운 규칙을 한 줄 추가함.
3. 수개월에 걸쳐 수백 번 반복됨.
4. 여러 개발자의 상충되는 지시가 엉키고 누구도 전체 스타일을 정리하지 않아 거대한 '진흙 뭉치'가 됨.

### 2) `/init` 자동 생성 스크립트의 함정
`/init` 같은 명령어로 `AGENTS.md`를 자동 생성하면, 프로젝트 구조, 모든 종속성, 명령어, 세부 경로 등 '대부분의 시나리오에 유용할 법한' 정보가 한꺼번에 쏟아져 들어옵니다. 자동 생성 도구는 **절제(Restraint)보다 포괄성(Comprehensiveness)**을 우선시하므로 에이전트의 컨텍스트를 불필요한 소음으로 오염시킵니다.

### 3) 명령어 예산 (The Instruction Budget)
Humanlayer의 분석에 따르면, 최신 프론티어 Thinking LLM(Claude 3.7 Sonnet, Opus 등)이라 하더라도 일관되게 준수할 수 있는 지시사항의 한도는 **약 150~200개** 내외입니다. 비Thinking 모델이나 소형 모델은 이보다 훨씬 적은 지시만 처리할 수 있습니다.

`AGENTS.md`에 포함된 모든 토큰은 **현재 작업과의 관련성 여부와 상관없이 매 단일 요청(Request)마다 로드**됩니다:
* **작고 집중된 AGENTS.md**: 현재 태스크 수행에 필요한 토큰과 주의력이 온전히 확보됨.
* **비대하고 장황한 AGENTS.md**: 에이전트가 핵심 작업에 집중하지 못하고 주의력이 분산되어 성능 저하.
* **불필요한 세부 규칙**: 토큰 낭비와 지시 충돌을 유발.

### 4) 오래된 문서의 컨텍스트 독성 (Stale Documentation Poisons Context)
인간 개발자는 오래된 문서를 보면 비판적으로 의심하지만, AI 에이전트는 문서에 적힌 내용을 사실로 신뢰합니다.
* **파일 경로 직접 명시의 위험**: `AGENTS.md`에 *"인증 로직은 src/auth/handlers.ts에 있다"*라고 적어두었는데 파일이 리팩토링되어 이동하면, 에이전트는 엉뚱한 곳을 끝없이 헤매게 됩니다.
* **해법**: 파일 경로 대신 **시스템의 역량(Capabilities)과 전체적인 프로젝트 형태(Shape)**를 설명하고, 에이전트가 탐색 도구(`grep`, `ls` 등)를 사용해 필요한 문맥을 스스로 찾게 해야 합니다.

---

## 3. AGENTS.md의 절대적 최소 구성 (The Absolute Minimum)

루트 `AGENTS.md`에 들어가야 할 필수 요소는 단 세 가지뿐입니다:

1. **한 문장 프로젝트 설명 (One-Sentence Project Description)**:  
   에이전트에게 이 저장소에서 일하는 근본적인 목적(Why)을 정박(Anchor)시킵니다.  
   *(예: "This is a React component library for accessible data visualization.")*
2. **패키지 매니저 명시 (Package Manager)**:  
   npm이 아닌 도구를 사용할 경우 명확히 지정하여 잘못된 명령 생성을 방지합니다.  
   *(예: "This project uses pnpm workspaces.")*
3. **비표준 빌드 및 검증 명령어 (Build / Typecheck Commands)**:  
   표준과 다른 특수한 빌드, 테스트, 타입체크 커맨드만 간결하게 기술합니다.

그 외의 모든 세부 규칙은 별도 위치로 분리해야 합니다.

---

## 4. 점진적 공개 (Progressive Disclosure) 아키텍처

점진적 공개의 핵심은 **에이전트에게 지금 당장 필요한 것만 제공하고, 세부 지침은 필요할 때 찾아갈 수 있는 이정표(Breadcrumbs)만 남기는 것**입니다.

### 1) 언어 및 영역별 규칙 분리
기존 `AGENTS.md`에 들어있던 상세 코딩 규칙(예: `const`만 사용, `interface` 선언 규칙 등)을 `docs/TYPESCRIPT.md`로 분리합니다:

```markdown
# 루트 AGENTS.md 예시
This is a high-performance analytics dashboard.
This project uses pnpm workspaces.

For TypeScript conventions, see docs/TYPESCRIPT.md
For testing workflows, see docs/TESTING.md
```

> **작성 톤의 차이:** 'ALWAYS', 'NEVER' 같은 대문자 강제 표현 대신, 가볍고 자연스러운 링크 참조(Conversational Reference)를 사용하는 것이 모델의 유연성을 높입니다.

### 2) 중첩된 문서 트리 (Nested Documentation Tree)
문서 간에 계층형 참조를 구축하여 에이전트가 필요에 따라 자연스럽게 깊이를 탐색하도록 만듭니다:

```text
docs/
├── TYPESCRIPT.md    ──▶ (필요 시 TESTING.md 참조)
├── TESTING.md       ──▶ (테스트 러너 세부 명세 참조)
└── BUILD.md         ──▶ (esbuild / 번들러 설정 참조)
```

### 3) Agent Skills 연계
반복적인 워크플로우나 복잡한 도메인 지식은 `SKILL.md` 형태의 에이전트 스킬로 패키징하여, 에이전트가 특정 작업을 시작할 때만 온디맨드(On-demand)로 지식을 불러오게 설계합니다.

---

## 5. Monorepo에서의 다단계 AGENTS.md 운용

모노레포 환경에서는 루트와 서브 디렉토리에 각각 `AGENTS.md`를 배치할 수 있으며, 이들은 실행 시 **상위 스코프와 자연스럽게 병합(Merge)**됩니다:

* **루트 레벨 (`/AGENTS.md`)**:  
  모노레포의 전체 목적, 패키지 간 이동 방법, 공통 도구(`pnpm workspaces`).
* **패키지 레벨 (`packages/api/AGENTS.md`)**:  
  해당 패키지의 목적, 기술 스택(Node.js GraphQL, Prisma), 로컬 API 설계 규격(`docs/API_CONVENTIONS.md`).

각 레벨이 자신의 스코프에만 집중함으로써 컨텍스트 낭비를 원천 차단할 수 있습니다.

---

## 6. 망가진 AGENTS.md를 즉시 고치는 5단계 리팩토링 프롬프트

현재 저장소의 비대해진 `AGENTS.md`를 점진적 공개 구조로 다이어트하고 싶다면, 코딩 에이전트에 다음 프롬프트를 입력하여 즉시 리팩토링을 수행할 수 있습니다:

```text
I want you to refactor my AGENTS.md file to follow progressive disclosure principles.

Follow these steps:
1. **Find contradictions**: Identify any instructions that conflict with each other. For each contradiction, ask me which version I want to keep.
2. **Identify the essentials**: Extract only what belongs in the root AGENTS.md:
   - One-sentence project description
   - Package manager (if not npm)
   - Non-standard build/typecheck commands
   - Anything truly relevant to every single task
3. **Group the rest**: Organize remaining instructions into logical categories (e.g., TypeScript conventions, testing patterns, API design, Git workflow). For each group, create a separate markdown file.
4. **Create the file structure**: Output:
   - A minimal root AGENTS.md with markdown links to the separate files
   - Each separate file with its relevant instructions
   - A suggested docs/ folder structure
5. **Flag for deletion**: Identify any instructions that are:
   - Redundant (the agent already knows this)
   - Too vague to be actionable
   - Overly obvious (like "write clean code")
```

---

## 7. 결론: "Less is More"

새로운 지침을 `AGENTS.md`에 추가하려 할 때마다 스스로에게 물어야 합니다:

* **이 정보가 모든 단일 작업에서 에이전트의 주의력 예산을 점유할 만큼 중요한가?**  
  → **YES**: 루트 `AGENTS.md`에 추가.  
  → **NO**: 특정 도메인 문서(`docs/`), 스킬(`SKILL.md`), 또는 에이전트가 스스로 탐색할 코드베이스로 이관.

`AGENTS.md`를 슬림하게 유지하는 것은 단순한 파일 정리가 아니라 **에이전트의 인지 용량을 통제하고 작업 성공률을 극대화하는 핵심 프롬프트 하네스 엔지니어링**입니다.
