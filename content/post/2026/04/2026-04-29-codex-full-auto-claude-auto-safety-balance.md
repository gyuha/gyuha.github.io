---
title: "Codex는 `--full-auto`, Claude Code는 `--permission-mode auto`가 좋은 이유"
date: 2026-04-29T00:00:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - codex
  - claude-code
  - safety
description: "Threads의 짧은 팁을 바탕으로, Codex CLI의 `--full-auto`와 Claude Code의 `--permission-mode auto`가 왜 무권한 우회보다 더 현실적인 기본값인지 공식 문서와 CLI 도움말 기준으로 정리합니다."
---

Threads에 올라온 팁은 아주 짧지만 실전 감각이 있습니다. 요지는 이렇습니다. **Codex 작업은 `--full-auto`, Claude Code 작업은 `--permission-mode auto`가 체감상 가장 좋은 기본값** 이라는 것. 그리고 `--dangerously-...` 계열은 편하지만, 너무 많은 권한을 한 번에 열어 버린다는 경고가 함께 붙습니다. [Threads](https://www.threads.com/@claude_master_/post/DXqm_qZFT0H?xmt=AQF0hqzfGEjWA07XmMrQIjVaNoH9PnAXOMiflZTxmXFUtPlq0A6QIQafZVyNWHw9H7od4M5F&slof=1)
<!--more-->

이 주장이 흥미로운 이유는 단순히 “덜 귀찮다”가 아니라, **자동화와 안전 사이에서 어디를 기본값으로 둘 것인가** 에 대한 감각을 담고 있기 때문입니다. 2026년 4월 29일 기준으로 확인해 보면, Claude Code의 Auto Mode는 공식적으로 “permission prompt를 없애되 classifier가 위험 행동을 거른다”는 중간지대이고, 로컬 Codex CLI 도움말에서도 `--full-auto` 는 “low-friction sandboxed automatic execution” alias로 설명됩니다. 반면 Codex의 `--dangerously-bypass-approvals-and-sandbox` 나 Claude Code의 `--dangerously-skip-permissions` 는 이름 그대로 보호장치를 크게 걷어냅니다. [Claude Code Docs](https://code.claude.com/docs/en/permission-modes), [Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-auto-mode), `codex --help` (local CLI), `claude --help` (local CLI)

## Sources

- https://www.threads.com/@claude_master_/post/DXqm_qZFT0H?xmt=AQF0hqzfGEjWA07XmMrQIjVaNoH9PnAXOMiflZTxmXFUtPlq0A6QIQafZVyNWHw9H7od4M5F&slof=1
- https://code.claude.com/docs/en/permission-modes
- https://www.anthropic.com/engineering/claude-code-auto-mode
- https://developers.openai.com/codex/cli
- local CLI help on 2026-04-29:
  - `codex-cli 0.124.0`
  - `Claude Code 2.1.117`

## 1. Threads 원문의 핵심은 “가장 빠른 모드”가 아니라 “가장 덜 위험한 자동화”다

Threads 원문은 다음 대비를 깔고 있습니다.

- 완전 우회: `dangerously-...`
- 실용적 자동화: `auto`, `full-auto`

이 포인트가 중요합니다. 많은 사람이 에이전트 CLI를 쓸 때 처음에는 permission prompt가 너무 많아서, 결국 가장 센 우회 옵션으로 달려갑니다. 그런데 실제 문제는 속도보다도 **실수의 반경** 입니다.

- 잘못된 `rm`
- 과한 리팩터링
- 의도하지 않은 push
- 외부 네트워크 호출
- 프로젝트 밖 파일 접근

에이전트가 실수할 때 무서운 것은 “틀린 코드 한 줄”이 아니라, **너무 넓은 권한으로 너무 많은 일을 한 번에 해 버리는 것** 입니다. Threads의 감각은 바로 이 지점에 닿아 있습니다.

## 2. Claude Code의 `auto`는 그냥 “무조건 허용”이 아니다

Claude Code 공식 문서에서 Auto Mode는 명확히 중간 단계로 설명됩니다. prompt 없이 실행하게 해 주지만, 별도 classifier가 행동을 검토해서:

- 사용자의 요청 범위를 벗어나거나
- 외부 인프라를 건드리거나
- hostile content에 유도된 것으로 보이는 행동

을 막습니다. [Claude Code Docs](https://code.claude.com/docs/en/permission-modes)

특히 문서가 밝히는 기본 차단 항목은 꽤 중요합니다.

- `curl | bash` 같은 다운로드 후 즉시 실행
- 민감 정보 외부 전송
- production deploy / migration
- 대규모 삭제
- IAM / repo 권한 부여
- `main` 직접 push나 force push

즉 `--permission-mode auto` 는 “권한 질문 없이 편하게 쓰는 모드”이긴 하지만, 의미는 **검문소를 없앤 것** 이 아니라 **사람 대신 1차 검문을 맡긴 것** 에 가깝습니다. [Claude Code Docs](https://code.claude.com/docs/en/permission-modes)

Anthropic의 엔지니어링 글도 같은 맥락을 강조합니다. Auto Mode는 manual review와 no guardrails 사이의 middle ground이며, broad shell allow rule과 wildcard interpreter rule은 auto 진입 시 일부 떨어뜨립니다. 다시 말해, 평소 수동 모드에서 편하게 쓰던 광범위 allow rule을 auto에서 그대로 살려 두면 classifier가 볼 기회조차 사라지기 때문입니다. [Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-auto-mode)

## 3. Claude Code에서 진짜 비교 대상은 `auto`가 아니라 `dangerously-skip-permissions` 다

로컬 `claude --help` 기준으로 현재 관련 옵션은 이렇게 나뉩니다.

- `--permission-mode auto`
- `--dangerously-skip-permissions`
- `--allow-dangerously-skip-permissions`

여기서 `dangerously-skip-permissions` 는 이름 그대로 permission check 자체를 우회합니다. 반면 `auto` 는 우회가 아니라 classifier 기반 승인 위임입니다. [Claude Code Docs](https://code.claude.com/docs/en/permission-modes), `claude --help`

즉 Threads의 조언을 더 정확히 풀면 이렇습니다.

> Claude Code를 편하게 쓰고 싶다면, 먼저 `auto` 를 기본값으로 삼고 정말 외부에서 이미 격리된 환경일 때만 `dangerously-skip-permissions` 를 생각하라.

이건 단순 안전주의가 아니라 운영 감각에 가깝습니다. 로컬 머신, 업무용 리포지토리, 실제 API 키, 개인 문서가 다 붙어 있는 환경이라면 “완전 우회”는 생각보다 비싼 선택이 됩니다.

## 4. Codex CLI의 `--full-auto`는 “샌드박스 안 자동 실행”이라는 점이 핵심이다

Codex CLI 로컬 도움말(`codex-cli 0.124.0`)을 보면 `--full-auto` 는 이렇게 설명됩니다.

- `Convenience alias for low-friction sandboxed automatic execution`

반대로 더 강한 옵션은:

- `--dangerously-bypass-approvals-and-sandbox`

이며, 설명도 `EXTREMELY DANGEROUS` 라고 박혀 있습니다. 즉 Codex 쪽에서 Threads의 팁이 맞는 이유는, `full-auto` 가 단순 자동 실행이 아니라 **샌드박스를 유지한 자동 실행** 이기 때문입니다. `codex --help`

이 차이는 매우 큽니다.

- `--full-auto`: 자동화 + sandbox
- `--dangerously-bypass-approvals-and-sandbox`: 자동화 + no sandbox + no prompts

실전에서 우리가 원하는 건 대개 첫 번째입니다. 파일을 고치고 테스트를 돌리고 로컬 작업을 반복하는 동안 흐름은 빠르게 유지하되, 에이전트가 작업 디렉터리 바깥이나 완전 무방비 환경으로 튀어나가는 것은 막고 싶은 경우가 대부분이기 때문입니다.

## 5. 그래서 이 두 옵션은 같은 철학으로 읽을 수 있다

표면적으로는 이름이 다르지만, Threads가 제안한 조합은 같은 철학을 공유합니다.

- Claude Code: classifier가 위험 행동을 가르는 `auto`
- Codex CLI: sandbox를 유지한 채 friction을 줄이는 `full-auto`

둘 다 공통적으로 노리는 것은:

1. 매번 승인 버튼을 누르느라 흐름이 끊기지 않게 하고  
2. 그렇다고 완전 무권한 우회로 가서 사고 반경을 키우지 않는 것  

즉 “가드레일 없는 자유”보다 **가드레일 있는 자동화** 를 기본값으로 두자는 제안입니다.

```mermaid
flowchart LR
    A["수동 승인 모드"] --> B["Auto / Full-auto"]
    B --> C["Dangerous bypass"]
    A -->|"안전하지만 느림"| B
    B -->|"실전 기본값"| C
    C -->|"가장 빠르지만 사고 반경 큼"| D["무권한 우회"]
```

## 6. 언제 dangerous 모드가 필요할까

그렇다고 `dangerously-...` 계열이 무조건 나쁘다는 뜻은 아닙니다. 오히려 다음 조건이 맞으면 합리적일 수 있습니다.

- 이미 VM / 컨테이너 / 별도 계정으로 격리된 환경
- 네트워크, credentials, filesystem 범위가 외부에서 강하게 제한된 환경
- 완전 자동화 배치 실험
- throwaway repo

문제는 많은 사용자가 이런 외부 격리 없이, **개인 로컬 머신 자체를 실험장** 으로 써 버린다는 점입니다. 이 경우 dangerous 모드는 “한두 번 prompt를 덜 보는 대신, 실패 비용을 크게 늘리는 선택”이 됩니다.

## 7. 더 실전적으로 해석하면: 기본은 auto/full-auto, 예외적으로 dangerous

실무 기준으로는 다음 순서가 더 현실적입니다.

1. 기본값은 `auto` / `full-auto` 로 둔다  
2. allow rules, hooks, sandbox 범위를 먼저 다듬는다  
3. 반복적으로 막히는 행동이 있으면 정책을 좁게 열어 준다  
4. dangerous 모드는 외부 샌드박스가 있을 때만 쓴다  

이 순서가 좋은 이유는, 에이전트의 품질 문제를 무권한 우회로 해결하지 않게 해 주기 때문입니다. 대개 귀찮은 prompt의 절반은 도구 정책을 조정해서 해결할 수 있고, 나머지 절반은 작업을 더 잘 쪼개거나 working directory를 더 명확히 잡아서 줄일 수 있습니다.

## 핵심 요약

- Threads의 팁은 `가장 빠른 모드` 추천이 아니라 `가장 덜 위험한 자동화` 추천에 가깝다.
- Claude Code의 `--permission-mode auto` 는 classifier 기반 중간지대이지, 완전 우회 모드가 아니다.
- Codex CLI의 `--full-auto` 는 로컬 도움말 기준 `sandboxed automatic execution` alias다.
- 두 도구 모두 더 강한 `dangerously-...` 계열 옵션은 보호장치를 크게 줄인다.
- 실전 기본값은 대체로 `auto / full-auto`, dangerous는 예외적 선택으로 두는 편이 낫다.

## 결론

짧은 Threads 팁이지만, 실제로는 에이전트 운영의 중요한 감각을 잘 짚고 있습니다. 오늘날 코딩 에이전트의 병목은 “자동화를 얼마나 많이 여는가”보다, **얼마나 안전한 자동화를 기본값으로 삼는가** 에 더 가깝습니다.

그래서 Codex에서는 `--full-auto`, Claude Code에서는 `--permission-mode auto` 가 꽤 좋은 출발점이 됩니다. 두 옵션 모두 손을 덜 타게 해 주면서도, 완전 무권한 우회처럼 사고 반경을 무작정 키우지는 않기 때문입니다.
