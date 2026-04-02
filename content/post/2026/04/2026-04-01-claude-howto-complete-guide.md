---
title: "주말 만에 Claude Code 마스터하기: claude-howto 완전 분석"
date: 2026-04-01T00:00:00+09:00
draft: false
categories:
  - AI
tags:
  - claude-code
  - skills
  - hooks
description: "GitHub 스타 5,900개를 돌파한 claude-howto 리포지토리를 분석합니다. 슬래시 커맨드부터 서브에이전트, MCP, 훅, 플러그인까지 10개 모듈로 구성된 체계적인 Claude Code 학습 경로를 소개합니다."
---

Claude Code를 설치하고 몇 가지 프롬프트를 실행했습니다. 이제 뭘 해야 할까요? 공식 문서는 기능을 설명하지만, 기능들을 어떻게 조합하는지는 알려주지 않습니다. 학습 경로도 없고, 예시는 너무 기초적입니다. GitHub 스타 5,900개를 돌파한 [claude-howto](https://github.com/luongnv89/claude-howto)는 이 공백을 메우는 구조적인 가이드입니다.

<!--more-->

## Sources

- https://github.com/luongnv89/claude-howto

---

## 프로젝트 개요

```mermaid
flowchart TD
    Problem[Claude Code 설치 후<br/>막막함] --> Solution[claude-howto]

    Solution --> S1[10개 모듈<br/>모든 기능 커버]
    Solution --> S2[Mermaid 다이어그램<br/>내부 동작 시각화]
    Solution --> S3[복사 즉시 사용<br/>프로덕션 템플릿]
    Solution --> S4[11~13시간<br/>가이드 학습 경로]
    Solution --> S5[자기 평가<br/>내장 퀴즈]

    Stats[현황] --> St1["⭐ 5,900+"]
    Stats --> St2[🍴 690+ forks]
    Stats --> St3[v2.2.0 March 2026]
    Stats --> St4[MIT 라이선스<br/>무료 영원히]

    classDef problemStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef solutionStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef featureStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef statStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    class Problem problemStyle
    class Solution solutionStyle
    class S1,S2,S3,S4,S5 featureStyle
    class Stats,St1,St2,St3,St4 statStyle
```

**공식 문서 vs claude-howto:**

| | 공식 문서 | claude-howto |
|---|---|---|
| **형식** | 참조 문서 | Mermaid 다이어그램 포함 시각적 튜토리얼 |
| **깊이** | 기능 설명 | 내부 작동 원리까지 |
| **예시** | 기초 스니펫 | 즉시 사용 가능한 프로덕션 템플릿 |
| **구조** | 기능 중심 | 점진적 학습 경로 (초급→고급) |
| **온보딩** | 자기 주도형 | 시간 추정 포함 가이드 로드맵 |
| **자기 평가** | 없음 | 내장 퀴즈로 갭 파악 |

---

## 학습 경로: 10개 모듈

```mermaid
flowchart TD
    Start[시작] --> L1{내 레벨?}

    L1 -->|초급| B1[01 슬래시 커맨드<br/>30분]
    L1 -->|중급| M1[03 Skills<br/>1시간]
    L1 -->|고급| A1[09 고급 기능<br/>2~3시간]

    B1 --> B2[02 Memory<br/>45분]
    B2 --> B3[08 Checkpoints<br/>45분]
    B3 --> B4[10 CLI 기초<br/>30분]
    B4 --> M1
    M1 --> M2[06 Hooks<br/>1시간]
    M2 --> M3[05 MCP<br/>1시간]
    M3 --> M4[04 Subagents<br/>1.5시간]
    M4 --> A1
    A1 --> A2[07 Plugins<br/>2시간]
    A2 --> Done[완료<br/>총 11~13시간]

    classDef beginStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef midStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef advStyle fill:#e0c8ef,stroke:#7b5ea7,color:#333
    classDef doneStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    class B1,B2,B3,B4 beginStyle
    class M1,M2,M3,M4 midStyle
    class A1,A2 advStyle
    class Done doneStyle
```

| 순서 | 모듈 | 레벨 | 시간 |
|---|---|---|---|
| 1 | 슬래시 커맨드 | 초급 | 30분 |
| 2 | Memory | 초급+ | 45분 |
| 3 | Checkpoints | 중급 | 45분 |
| 4 | CLI 기초 | 초급+ | 30분 |
| 5 | Skills | 중급 | 1시간 |
| 6 | Hooks | 중급 | 1시간 |
| 7 | MCP | 중급+ | 1시간 |
| 8 | Subagents | 중급+ | 1.5시간 |
| 9 | 고급 기능 | 고급 | 2~3시간 |
| 10 | Plugins | 고급 | 2시간 |

---

## 기능별 심층 분석

### 01. 슬래시 커맨드

사용자가 `/cmd` 형식으로 직접 호출하는 단축키입니다. `.claude/commands/` 폴더에 Markdown 파일로 저장됩니다.

```bash
# 포함된 예시 커맨드
optimize.md       # 코드 최적화 분석
pr.md             # PR 준비
generate-api-docs.md  # API 문서 자동 생성
```

```bash
# 설치
cp 01-slash-commands/*.md /path/to/project/.claude/commands/

# 사용
/optimize
/pr
/generate-api-docs
```

### 02. Memory (영구 컨텍스트)

세션이 끊겨도 유지되는 영구 컨텍스트입니다. CLAUDE.md 파일 계층으로 관리합니다.

```mermaid
flowchart TD
    Memory[Memory 시스템] --> Personal["~/.claude/CLAUDE.md<br/>개인 선호 설정<br/>모든 프로젝트 적용"]
    Memory --> Project["./CLAUDE.md<br/>팀 공유 프로젝트 표준<br/>Git으로 공유"]
    Memory --> Directory["src/api/CLAUDE.md<br/>디렉토리별 규칙<br/>해당 폴더 작업 시만 로드"]

    classDef personalStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef projectStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef dirStyle fill:#fde8c0,stroke:#e6a817,color:#333
    class Personal personalStyle
    class Project projectStyle
    class Directory dirStyle
```

### 03. Skills (재사용 가능한 능력)

관련 작업 감지 시 자동 호출되는 재사용 능력입니다. 지시사항과 스크립트 묶음으로 구성됩니다.

**포함된 스킬:**
- `code-review/` — 스크립트 포함 종합 코드 리뷰
- `brand-voice/` — 브랜드 보이스 일관성 검사
- `doc-generator/` — API 문서 생성기

```bash
# 개인 설치
cp -r 03-skills/code-review ~/.claude/skills/
# 프로젝트 설치
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

### 04. Subagents (전문 AI 어시스턴트)

격리된 컨텍스트에서 특정 역할을 수행하는 전문 에이전트입니다.

```mermaid
flowchart TD
    Main[메인 Claude Code] --> SA1[code-reviewer<br/>코드 품질 분석]
    Main --> SA2[test-engineer<br/>테스트 전략 & 커버리지]
    Main --> SA3[documentation-writer<br/>기술 문서 작성]
    Main --> SA4[secure-reviewer<br/>보안 취약점 검토<br/>읽기 전용 모드]
    Main --> SA5[implementation-agent<br/>전체 기능 구현]

    classDef mainStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef agentStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class Main mainStyle
    class SA1,SA2,SA3,SA4,SA5 agentStyle
```

```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

### 05. MCP Protocol

외부 도구 및 API에 접근하는 Model Context Protocol입니다.

```bash
# 예시: GitHub MCP 설정
export GITHUB_TOKEN="your_token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

포함 설정 파일: `github-mcp.json`, `database-mcp.json`, `filesystem-mcp.json`, `multi-mcp.json`

### 06. Hooks (이벤트 기반 자동화)

Claude Code 이벤트에 반응해 자동 실행되는 셸 스크립트입니다. **4가지 타입, 25개 이벤트**를 지원합니다.

```mermaid
flowchart TD
    HookTypes[Hook 타입] --> Tool[Tool Hooks<br/>PreToolUse<br/>PostToolUse<br/>PostToolUseFailure<br/>PermissionRequest]
    HookTypes --> Session[Session Hooks<br/>SessionStart<br/>SessionEnd<br/>Stop / StopFailure<br/>SubagentStart / SubagentStop]
    HookTypes --> Task[Task Hooks<br/>UserPromptSubmit<br/>TaskCompleted<br/>TaskCreated<br/>TeammateIdle]
    HookTypes --> Lifecycle[Lifecycle Hooks<br/>ConfigChange / CwdChanged<br/>FileChanged<br/>PreCompact / PostCompact<br/>WorktreeCreate / Remove<br/>... 11개]

    classDef toolStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef sessionStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef taskStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef lifecycleStyle fill:#e0c8ef,stroke:#7b5ea7,color:#333
    class Tool,toolStyle toolStyle
    class Session sessionStyle
    class Task taskStyle
    class Lifecycle lifecycleStyle
```

**포함된 훅 스크립트:**
- `format-code.sh` — 쓰기 전 자동 코드 포맷
- `pre-commit.sh` — 커밋 전 테스트 실행
- `security-scan.sh` — 보안 취약점 스캔
- `log-bash.sh` — 모든 Bash 명령 로깅
- `validate-prompt.sh` — 사용자 프롬프트 검증
- `notify-team.sh` — 이벤트 발생 시 알림

**설정 예시 (`~/.claude/settings.json`):**

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

### 07. Plugins (기능 번들)

슬래시 커맨드 + 에이전트 + MCP + 훅을 하나의 패키지로 묶은 완전한 솔루션입니다.

```bash
/plugin install pr-review         # PR 리뷰 워크플로우
/plugin install devops-automation # 배포 & 모니터링
/plugin install documentation     # 문서 생성
```

### 08. Checkpoints (세션 스냅샷 & 되감기)

대화 상태를 저장하고 이전 지점으로 되돌아가 다른 접근법을 탐색합니다.

```mermaid
flowchart TD
    A[작업 시작] --> CP1[체크포인트 1<br/>자동 생성]
    CP1 --> B[구현 A 시도]
    B --> CP2[체크포인트 2]
    CP2 --> C{결과가 좋지 않음}
    C -->|"/rewind"| CP1
    CP1 --> D[구현 B 시도]
    D --> CP3[체크포인트 3]
    CP3 --> E[성공!]

    Rewind["/rewind 옵션"] --> R1[코드 + 대화 복원]
    Rewind --> R2[대화만 복원]
    Rewind --> R3[코드만 복원]
    Rewind --> R4[여기서부터 요약]
    Rewind --> R5[취소]

    classDef cpStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef actionStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef rewindStyle fill:#e0c8ef,stroke:#7b5ea7,color:#333
    class CP1,CP2,CP3 cpStyle
    class A,B,D,E actionStyle
    class Rewind,R1,R2,R3,R4,R5 rewindStyle
```

- **체크포인트**: 매 사용자 프롬프트마다 자동 생성
- **되감기**: Esc 두 번 또는 `/rewind`

### 09. 고급 기능

| 기능 | 설명 | 단축키/명령 |
|---|---|---|
| Planning Mode | 코딩 전 상세 구현 계획 수립 | 자동/수동 |
| Extended Thinking | 복잡한 문제 심층 추론 | `Alt+T` / `Option+T` |
| Background Tasks | 블로킹 없는 장시간 작업 | 자동 |
| Headless Mode | CI/CD에서 Claude Code 실행 | `claude -p "..."` |
| Session Management | 세션 재개/이름변경/분기 | `/resume`, `/rename`, `/fork` |

**권한 모드 5가지:** `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`

### 10. CLI Reference

```bash
# 인터랙티브 모드
claude "explain this project"

# 출력 모드 (비대화형)
claude -p "review this code"

# 파일 내용 처리
cat error.log | claude -p "explain this error"

# JSON 출력 (스크립트 연동)
claude -p --output-format json "list functions"

# 세션 재개
claude -r "feature-auth" "continue implementation"
```

---

## 기능 비교표

```mermaid
flowchart TD
    Features[Claude Code 기능] --> Manual[수동 호출]
    Features --> Auto[자동 실행]
    Features --> Bundle[번들]

    Manual --> SC["슬래시 커맨드<br/>/cmd<br/>세션 한정<br/>빠른 단축키"]
    Manual --> CLI["CLI Reference<br/>터미널 명령<br/>CI/CD 자동화"]

    Auto --> Mem["Memory<br/>자동 로딩<br/>세션 간 지속<br/>장기 학습"]
    Auto --> Skill["Skills<br/>자동 호출<br/>파일시스템 기반<br/>자동화 워크플로우"]
    Auto --> Agent["Subagents<br/>자동 위임<br/>격리 컨텍스트<br/>태스크 분배"]
    Auto --> MCP["MCP<br/>자동 쿼리<br/>실시간<br/>외부 데이터"]
    Auto --> Hook["Hooks<br/>이벤트 트리거<br/>4타입 25이벤트<br/>자동화 & 검증"]

    Bundle --> Plugin["Plugins<br/>한 명령 설치<br/>전체 기능 묶음<br/>완전한 솔루션"]

    classDef manualStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef autoStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef bundleStyle fill:#e0c8ef,stroke:#7b5ea7,color:#333
    class SC,CLI manualStyle
    class Mem,Skill,Agent,MCP,Hook autoStyle
    class Plugin bundleStyle
```

---

## 실전 워크플로우

### 자동화 코드 리뷰

```mermaid
sequenceDiagram
    participant U as 사용자
    participant C as Claude Code
    participant M as Memory
    participant G as GitHub MCP
    participant CR as code-reviewer
    participant TE as test-engineer

    U->>C: /review-pr
    C->>M: 프로젝트 코딩 표준 로드
    C->>G: PR 내용 가져오기
    C->>CR: 코드 품질 분석 위임
    C->>TE: 테스트 커버리지 분석 위임
    CR-->>C: 코드 리뷰 결과
    TE-->>C: 테스트 분석 결과
    C->>U: 종합 리뷰 보고서
```

### DevOps 배포 파이프라인

```mermaid
sequenceDiagram
    participant U as 사용자
    participant C as Claude Code
    participant H as Hooks
    participant D as Deployment Agent
    participant K as Kubernetes MCP

    U->>C: /deploy production
    C->>H: pre-deploy hook (환경 검증)
    H-->>C: 검증 통과
    C->>D: 배포 전문 에이전트 위임
    D->>K: 쿠버네티스 배포 실행
    K-->>D: 배포 진행 상황
    D-->>C: 배포 완료
    C->>H: post-deploy hook (헬스 체크)
    H-->>C: 정상 동작 확인
    C->>U: 배포 완료 보고
```

---

## 15분 빠른 시작

```bash
# 1. 가이드 클론
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 첫 번째 슬래시 커맨드 복사
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Claude Code에서 실행
# /optimize

# 4. 프로젝트 Memory 설정
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 스킬 설치
cp -r 03-skills/code-review ~/.claude/skills/
```

**1시간 핵심 설정:**

```bash
cp 01-slash-commands/*.md .claude/commands/    # 슬래시 커맨드 (15분)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md     # Memory (15분)
cp -r 03-skills/code-review ~/.claude/skills/  # Skills (15분)
# 주말 목표: Hooks + Subagents + MCP + Plugins
```

---

## 자기 평가 & 내장 퀴즈

Claude Code 내에서 바로 실행할 수 있는 자기 평가 시스템이 내장되어 있습니다.

```bash
# 전체 자기 평가 (자신의 레벨 파악)
/self-assessment

# 모듈별 퀴즈 (갭 파악)
/lesson-quiz hooks
/lesson-quiz subagents
/lesson-quiz mcp
```

---

## 오프라인 EPUB 생성

전체 가이드를 Mermaid 다이어그램이 렌더링된 EPUB 전자책으로 변환할 수 있습니다.

```bash
uv run scripts/build_epub.py
# → claude-howto-guide.epub 생성
```

---

## 핵심 요약

```mermaid
mindmap
  root((claude-howto))
    기본 정보
      GitHub ⭐5900+
      MIT 무료 영원히
      v2.2.0 March 2026
      Claude Code 2.1+
    10개 모듈
      초급: 슬래시커맨드, Memory, CLI
      중급: Skills, Hooks, MCP, Checkpoints
      고급: Subagents, Advanced, Plugins
    핵심 가치
      11~13시간 완전 마스터
      15분 즉시 시작
      프로덕션 복사 즉시 사용 템플릿
    특별 기능
      내장 자기평가 퀴즈
      EPUB 오프라인 변환
      Mermaid 내부 동작 시각화
```

| 레벨 | 시작 모듈 | 예상 시간 |
|---|---|---|
| 초급 (Claude Code 시작 단계) | 01 슬래시 커맨드 | ~2.5시간 |
| 중급 (CLAUDE.md, 커스텀 커맨드) | 03 Skills | ~3.5시간 |
| 고급 (MCP, Hooks 설정 경험) | 09 고급 기능 | ~5시간 |

---

## 결론

claude-howto는 "Claude Code 사용법"이 아니라 "Claude Code 마스터"를 위한 가이드입니다. 공식 문서가 기능 참조를 담당한다면, claude-howto는 그 기능들을 조합해 실제로 쓸 수 있는 워크플로우를 만드는 방법을 알려줍니다.

슬래시 커맨드 하나를 복사하는 15분에서 시작해, 주말 동안 11~13시간을 투자하면 서브에이전트와 훅과 MCP를 연결한 자동화 파이프라인을 직접 구축할 수 있습니다. MIT 라이선스, 무료, 즉시 클론 가능합니다.
