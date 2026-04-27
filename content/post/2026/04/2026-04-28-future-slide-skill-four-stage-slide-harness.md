---
title: "future-slide-skill이 좋은 이유: 슬라이드를 한 번에 만들지 않고 4단계 하네스로 쪼갠다"
date: 2026-04-28T00:00:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - slides
  - design
  - codex
description: "jyoung105/future-slide-skill 저장소를 바탕으로, 이 프로젝트를 단순 슬라이드 생성 스킬이 아니라 DESIGN.md → 계획 JSON → 페이지 프롬프트 JSON → 순차 렌더의 4단계 하네스로 정리합니다."
---

대부분의 AI 슬라이드 생성은 “참고 이미지 하나 주고 덱 하나 만들어 줘”라는 단일 프롬프트에서 시작합니다. 그리고 거의 항상 비슷한 문제로 망가집니다. 디자인 분석과 스토리 구성이 섞이고, 슬라이드 간 일관성이 무너지고, 본문 페이지가 점점 일반론으로 흐르고, 마지막엔 프롬프트만 써 놓고 실제 이미지 렌더링은 멈춥니다. `future-slide-skill` 이 흥미로운 이유는 바로 이 실패 패턴을 전제로 설계됐기 때문입니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)
<!--more-->

README는 이를 아주 명확하게 풀어냅니다. 이 번들은 한 번에 다 하게 만드는 게 아니라, 네 단계로 강제로 분리합니다.

1. 참고 슬라이드에서 `DESIGN.md` 추출  
2. 설득력 있는 슬라이드 플랜 JSON 생성  
3. 페이지별 슬라이드 프롬프트 JSON 작성  
4. 프롬프트 JSON을 바탕으로 페이지 이미지를 순차 생성

즉 이 프로젝트는 슬라이드 생성기가 아니라, **슬라이드 생성 실패를 줄이기 위한 하네스** 로 보는 편이 더 정확합니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

## Sources

- https://github.com/jyoung105/future-slide-skill

## 1. 이 프로젝트의 핵심은 “디자인 먼저, 내용 나중”이다

README가 가장 먼저 강조하는 것은 `theme extraction first, content second` 입니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

이 원칙은 중요합니다. 보통 프레젠테이션 작업에서 디자인과 내용은 동시에 떠오르기 쉽지만, AI에게 둘을 한 번에 맡기면 거의 항상 섞여 버립니다.

- 참조 이미지의 문구를 그대로 따라 하거나
- 눈에 보이는 텍스트를 과적합하거나
- 슬라이드 디자인 규칙을 추상화하지 못한 채
- 그 장면 하나만 흉내 낸 결과로 끝납니다

`future-slide-skill` 은 그래서 첫 단계를 아예 `gpt-slide-design` 으로 떼어 냅니다. 이 단계는 오직:

- 배치 규칙
- header / body / footer 흐름
- 타이틀/본문/엔드페이지 구조
- 아이콘/인포그래픽/표/차트 처리 방식

만을 `DESIGN.md` 로 뽑아내는 데 집중합니다.

즉 이 프로젝트는 슬라이드 내용을 쓰기 전에 **디자인 시스템을 먼저 언어화** 합니다.

## 2. 왜 4단계로 쪼개야 하나: 단일 프롬프트의 실패를 구조적으로 막기 위해서다

README는 단일 프롬프트가 실패하는 전형적인 패턴을 직접 적어 둡니다.

- 디자인 추출 전에 슬라이드를 바로 쓰기 시작함
- 디자인 분석과 덱 전략을 섞어 버림
- 이야기 흐름 없이 페이지 프롬프트만 뽑음
- 본문 슬라이드의 일관성을 잃음
- 참조 이미지의 텍스트를 과적합함
- 프롬프트만 쓰고 실제 렌더를 안 함

이 목록은 정확합니다. 그리고 `future-slide-skill` 의 4단계는 사실 이 실패 패턴 하나씩을 끊어내기 위해 존재합니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

즉 단계 분리는 기능 분해가 아니라, **AI가 자주 망가지는 지점을 미리 분리해 놓은 안전장치** 입니다.

## 3. `DESIGN.md` 는 단순 스타일 메모가 아니라 재사용 가능한 규칙 문서다

첫 번째 스킬인 `gpt-slide-design` 의 출력은 `DESIGN.md` 입니다. 이 파일은 그냥 “파란색 위주, 미니멀 디자인” 같은 모호한 메모가 아닙니다. README는 명시적으로:

- layout placement
- header/body/footer zoning
- title page / body page / end page flow
- icon usage
- infographic card logic
- table/chart treatment
- diagram behavior

를 담는 문서라고 설명합니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

즉 `DESIGN.md` 는 시각적 취향이 아니라, **슬라이드가 페이지 유형별로 어떻게 동작해야 하는지 적어 둔 운영 규칙 문서** 입니다.

이 문서가 있으면 이후 단계들은 더 이상 참조 이미지 자체를 붙잡고 있지 않아도 됩니다. 디자인 규칙이 문서화됐기 때문입니다.

## 4. 두 번째 단계의 진짜 역할은 “슬라이드 플랜”이 아니라 서사와 증거 맵핑이다

`gpt-slide-plan` 은 흔히 생각하는 목차 작성기보다 더 강한 역할을 맡습니다. README는 이 단계의 출력이 단순 순서표가 아니라:

- slide ordering
- narrative flow
- evidence mapping

을 담는 deck plan JSON 이라고 말합니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

이게 중요한 이유는 많은 슬라이드 자동화가 “문장 몇 개씩 채운 페이지 나열”로 끝나기 때문입니다. 하지만 좋은 발표 자료는:

- 왜 이 순서로 말하는지
- 어떤 페이지가 어떤 주장을 받치는지
- 어디서 표/차트/카드를 써야 하는지

가 먼저 정리돼야 합니다.

즉 두 번째 단계는 내용을 쓰는 게 아니라, **설득 구조를 먼저 고정하는 단계** 입니다.

```mermaid
flowchart LR
    A["참고 슬라이드 이미지"] --> B["gpt-slide-design"]
    B --> C["DESIGN.md"]
    C --> D["gpt-slide-plan"]
    D --> E["slide_plan.json"]
    E --> F["gpt-slide-prompt"]
    F --> G["slide_prompts.json"]
    G --> H["gpt-slide-generate"]
    H --> I["page_1.png ... page_N.png"]
```

## 5. 페이지별 프롬프트 JSON은 ‘그림 요청’이 아니라 레이아웃 제약을 넘기는 단계다

세 번째 스킬 `gpt-slide-prompt` 는 plan JSON과 DESIGN.md를 바탕으로 페이지별 프롬프트 JSON을 만듭니다. README는 여기서 explicit header/body/footer zoning, table/chart/card hierarchy, anti-generic constraints 같은 표현을 씁니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

이 점이 중요합니다. 보통 이미지 생성 프롬프트는 한 장면을 예쁘게 묘사하는 데 집중하지만, 슬라이드 프롬프트는 그보다 훨씬 엄격해야 합니다.

- 이 페이지는 body-slide family 중 어떤 타입인가
- 제목/본문/푸터의 영역 분리가 어떻게 되는가
- 표와 차트 중 무엇이 핵심인가
- 아이콘은 주도 요소인가 보조 요소인가
- generic corporate slide처럼 흐르지 않게 무엇을 금지할 것인가

즉 이 단계는 “한 장씩 예쁘게 그려 줘”가 아니라, **각 페이지의 역할과 제약을 기계가 해석 가능한 구조로 바꾸는 일** 입니다.

## 6. 생성 단계가 따로 분리된 이유: 이미지 캐시가 아니라 프로젝트 산출물로 남겨야 하기 때문이다

마지막 `gpt-slide-generate` 단계는 의도적으로 분리돼 있습니다. README는 이 단계가 페이지를 하나씩 보고, 덱 전체 일관성을 유지하고, 최종 산출물을 tool cache가 아니라 프로젝트 안에 `page_1.png`, `page_2.png`처럼 저장하는 역할을 한다고 설명합니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

이 분리가 중요한 이유는 두 가지입니다.

- 페이지마다 생성 상태를 점검할 수 있음
- 결과가 일회성 채팅 출력이 아니라 실제 프로젝트 자산으로 남음

즉 이 프로젝트는 슬라이드를 “대화 속 이미지”가 아니라 **버전 관리 가능한 작업 산출물** 로 취급합니다. 이것이 슬라이드 제작을 진짜 워크플로로 바꾸는 지점입니다.

## 7. 삼성바이오로직스 / 하나증권 예제가 보여 주는 방향

README 예시는 삼성바이오로직스와 하나증권 리서치 리포트를 바탕으로, 한국어 분석 슬라이드나 풀 덱을 만드는 방식으로 짜여 있습니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

이 예시가 흥미로운 이유는, 이 스킬이 단순 홍보용 랜딩 슬라이드보다:

- 리서치 리포트
- 분석형 보고서
- 증거 기반 자료

같은 문서형 슬라이드에 더 잘 맞도록 설계돼 있음을 보여 주기 때문입니다.

즉 `future-slide-skill` 은 예쁜 테마 복제보다도, **보고서성 프레젠테이션을 구조적으로 만드는 데 강한 번들** 로 읽힙니다.

## 8. 설치와 구조가 단순해서 오히려 재사용성이 높다

README는 설치 방법도 비교적 단순하게 제시합니다.

- `npx skills add jyoung105/future-slide-skill`
- 또는 GitHub URL 직접 설치
- 혹은 `~/.codex/skills/` 또는 프로젝트 로컬 `.codex/skills/` 에 수동 복사

구조도 명확합니다.

- `skills/gpt-slide-design/SKILL.md`
- `skills/gpt-slide-plan/SKILL.md`
- `skills/gpt-slide-prompt/SKILL.md`
- `skills/gpt-slide-generate/SKILL.md`
- `templates/DESIGN_TEMPLATE.md`

즉 무거운 서버나 앱이 아니라, **재사용 가능한 스킬 번들** 이라는 점이 장점입니다. 로컬 프로젝트 하네스에 끼워 넣기 좋기 때문입니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

## 9. 저장소 상태가 보여 주는 현재 위치

2026년 4월 28일 기준 GitHub 저장소 화면 기준으로 이 프로젝트는:

- stars 49
- forks 8
- 기본 브랜치 `dev`
- Apache-2.0 라이선스
- 최신 릴리스 `0.0.2` (2026-04-26)

상태를 보입니다. 저장소 소개 문구도 `Reusable slide-generation skill for image-based and HTML-based AI workflows` 라고 되어 있습니다. [GitHub 저장소](https://github.com/jyoung105/future-slide-skill)

아직 초기 프로젝트지만, README의 분해 방식 자체가 꽤 명확해서 “슬라이드 생성 실패를 줄이는 구조”로서의 아이디어가 선명합니다.

## 실전 적용 포인트

이 스킬 번들을 그대로 쓰지 않더라도, 슬라이드 자동화를 할 때는 아래 원칙만 가져가도 효과가 큽니다.

1. 참조 슬라이드에서 디자인 규칙을 먼저 문서화한다  
2. 이야기 흐름과 증거 맵핑을 먼저 만든다  
3. 페이지별 제약을 JSON으로 구조화한다  
4. 생성은 마지막에, 페이지 단위로 순차 실행한다  

즉 핵심은 “한 프롬프트로 끝내기”보다 **실패 지점을 잘라서 통제하기** 입니다.

## 핵심 요약

- `future-slide-skill` 은 슬라이드 생성기가 아니라 슬라이드 생성 하네스에 가깝다.
- 핵심은 `DESIGN.md → slide_plan.json → slide_prompts.json → page_N.png` 의 4단계 체인이다.
- 첫 단계에서 디자인 규칙을 먼저 추출해 내용 작성과 분리한다.
- 두 번째 단계는 목차 작성이 아니라 서사와 증거 맵핑을 고정한다.
- 세 번째 단계는 페이지별 제약을 구조화된 프롬프트 JSON으로 만든다.
- 마지막 단계는 결과를 프로젝트 산출물로 순차 저장한다.

## 결론

`future-slide-skill` 이 좋은 이유는 AI가 슬라이드를 못 만들기 때문이 아닙니다. 오히려 AI가 너무 쉽게 “그럴듯한 일반론”으로 미끄러지기 때문입니다. 이 프로젝트는 그 미끄러짐을 막기 위해, 디자인 분석과 이야기 구조와 페이지 생성과 실제 렌더를 강제로 분리합니다.

그래서 이 저장소는 단순한 슬라이드 스킬 묶음이 아니라, **슬라이드 자동화에서 AI가 자주 실패하는 지점을 구조적으로 잘라낸 작업 하네스** 로 보는 편이 맞습니다.
