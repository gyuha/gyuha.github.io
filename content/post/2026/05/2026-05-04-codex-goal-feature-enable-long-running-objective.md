---
title: "Codex의 /goal이 중요한 이유: 한 번의 목표를 장기 작업 루프로 올리는 기능"
date: 2026-05-04T00:00:00+09:00
draft: false
categories:
  - "Developer Tools"
tags:
  - "Codex"
  - "Workflow"
  - "Goals"
description: "Threads에서 소개된 Codex /goal 활성화 팁을 바탕으로, 이 기능을 단순 숨겨진 명령이 아니라 장기 목표 실행 모드 관점에서 정리한다."
---

Threads에서 소개한 팁은 짧다.

- Codex를 `0.128.0`으로 올리고
- `config.toml`의 `[features]` 아래에
- `goals = true`

를 넣으면 `/goal`을 쓸 수 있다는 것이다.

겉으로는 단순한 기능 활성화 팁처럼 보이지만, 이건 사실 **Codex를 단발성 채팅에서 장기 목표 실행기로 바꾸는 스위치**에 가깝다.

<!--more-->

## Sources

- Threads: <https://www.threads.com/@unclejobs.ai/post/DX5a5pZk7RU>
- GitHub: <https://github.com/openai/codex>
- Codex PRs mentioning goal mode:
  - <https://github.com/openai/codex/pull/20838>
  - <https://github.com/openai/codex/pull/20800>
  - <https://github.com/openai/codex/pull/20799>
  - <https://github.com/openai/codex/pull/20746>

## 1. Threads가 말하는 팁은 단순하다

Threads 원문 요지는 이렇다.

1. Codex를 `0.128.0`으로 업그레이드  
2. `config.toml` 파일을 연다  
3. `[features]` 아래에 `goals = true`를 추가한다  
4. Codex를 다시 시작한다  
5. 이후 `/goal`을 입력하면 된다

즉 사용 방식 자체는 복잡하지 않다.  
핵심은 “기능이 숨어 있다”는 사실보다, **왜 이런 기능이 따로 존재하느냐**다.

## 2. `/goal`은 새 명령어가 아니라 작업 단위를 바꾸는 기능이다

보통 Codex CLI는 프롬프트-응답 루프에 가깝다.

- 이 파일 수정해 줘
- 이 버그 고쳐 줘
- 이 함수 설명해 줘

하지만 `/goal`은 이름부터 다르다.

이건 “지금 한 번 할 일”이 아니라  
**계속 추적해야 할 목적(objective)** 을 다루려는 인터페이스다.

즉 요청 단위가:

- 단발 작업

에서

- 장기 목표
- 상태 전이
- 중간 중단/재개

로 바뀐다.

## 3. 공식 저장소에도 goal mode는 실제로 진행 중인 기능으로 보인다

로컬 환경의 Codex CLI `0.124.0`에서는 현재 `features list`에 `goals`가 아직 보이지 않는다.  
하지만 공식 `openai/codex` 저장소에는 goal 관련 PR이 여러 개 올라와 있다.

예를 들면:

- `Pause goals while in Plan mode`
- `Show /goal-started threads in resume picker`
- `Add goal lifecycle metrics`
- `Validate /goal objective length in TUI`

이건 `/goal`이 단순 루머나 비공식 해킹이 아니라,  
**실제 제품 레벨에서 goal lifecycle을 갖춘 기능으로 개발되고 있다**는 신호로 읽힌다.

즉 Threads 팁은 “없는 기능을 억지로 켠다”기보다,  
**더 최신 릴리스에서 열리는 feature flag를 먼저 쓰는 방법**에 가깝다.

## 4. 왜 이런 기능이 필요한가: 코딩 에이전트의 병목은 종종 “목표 유지”다

코딩 에이전트를 조금만 오래 써 보면 문제는 자주 구현력이 아니라 목표 유지에서 생긴다.

- 처음 목적을 잊는다
- 중간에 사이드 퀘스트로 빠진다
- 작업은 했는데 왜 하는지 흐려진다
- 재개했을 때 문맥은 있어도 의도는 약해진다

`/goal`은 바로 이 지점을 겨냥하는 기능으로 보인다.

즉 “명령을 더 많이 넣는 것”이 아니라,

- 목표를 별도 객체처럼 유지하고
- 상태를 추적하고
- 재개 가능하게 만들고
- lifecycle을 관리하는 쪽

으로 인터페이스를 옮기는 것이다.

```mermaid
flowchart LR
    A[단발 프롬프트] --> B[즉시 실행]
    B --> C[한 번 응답]

    D[/goal] --> E[목표 등록]
    E --> F[진행 상태 추적]
    F --> G[중단 / 재개 / 수명주기 관리]
```

## 5. `/goal`이 열리면 Codex는 더 ‘작업 관리자’처럼 보이기 시작한다

goal mode 관련 PR 이름들을 보면 단순 명령어 추가가 아니다.

- goal started threads
- lifecycle metrics
- pause while in plan mode

이런 표현은 모두 **작업 단위가 스레드와 세션을 넘어 지속**된다는 뜻에 가깝다.

즉 Codex는 점점:

- 한 번 답하는 CLI

에서

- 장기 작업을 들고 가는 실행 환경

으로 옮겨 가는 중이라고 볼 수 있다.

이건 중요한 변화다.  
왜냐하면 좋은 에이전트 UX의 핵심은 자주 “더 똑똑한 답변”보다 **목표를 잃지 않는 것**이기 때문이다.

## 6. 설정 팁 그 자체보다 더 흥미로운 건 feature flag 구조다

Threads는 `[features]` 아래에 `goals = true`를 넣으라고 말한다.

이 방식이 뜻하는 바도 꽤 크다.

즉 Codex는 새 기능을:

- 바로 모두에게 여는 대신
- flag로 감추고
- 점진적으로 노출하고
- 사용자가 먼저 켜 보게 하는

구조를 택하고 있다는 뜻이다.

로컬 `codex-cli 0.124.0` 기준으로도 `features` 시스템 자체는 분명히 존재한다.

- `codex features list`
- `codex features enable`
- `codex features disable`

즉 `/goal`은 완전히 별도 제품이라기보다,  
**기존 Codex feature-flag 메커니즘 위에서 확장되는 차세대 작업 모드**에 가깝다.

## 7. 지금 시점에서 가장 현실적인 해석

현재 확인 가능한 사실을 나누면 이렇다.

### 확인된 것

- Threads는 `0.128.0 + goals = true` 조합을 제안한다
- 공식 Codex 저장소에는 goal mode 관련 PR이 다수 존재한다
- Codex CLI에는 feature flag 체계가 실제로 있다

### 주의할 점

- 로컬 `0.124.0`에서는 아직 `goals`가 보이지 않는다
- 즉 Threads 팁은 더 최신 릴리스 또는 점진 배포 상태를 전제로 할 수 있다

그래서 가장 안전한 표현은:

**`/goal`은 실제 개발 중인 최신 목표 실행 모드이고, Threads는 그 기능을 먼저 여는 방법을 공유한 것`** 이다.

## 8. 결국 `/goal`의 진짜 의미는 “프롬프트를 목표로 승격하는 것”이다

에이전트 툴이 더 유용해질수록 사용자는 기능보다 운영 단위를 바꾸게 된다.

- prompt
- task
- workflow
- goal

이 순서로 올라간다.

`/goal`은 바로 그 다음 단계다.

즉 Codex는 이제:

- 한 번 시키고 끝나는 조수

보다

- 지속되는 목적을 붙잡고 가는 작업 시스템

쪽으로 진화하려는 신호를 내고 있다.

그래서 이 기능의 본질은 “숨은 명령어”가 아니다.  
**프롬프트를 목표 객체로 바꾸는 인터페이스 변화**다.
