---
title: "하네스/루프/그래프 엔지니어링: 프롬프트에서 결정론적 계약까지의 5단계 에이전트 진화 분석"
date: 2026-08-18T07:40:00+09:00
draft: false
categories:
  - AI
tags:
  - agents
  - architecture
  - harness
  - graph-engineering
  - claude-code
  - langgraph
description: "Prompt Engineering에서 Context, Harness, Loop, 그리고 Graph Engineering까지 지난 3년간 AI 에이전트 아키텍처가 발전해 온 흐름과 결정론적 계약(Contract) 및 자동 검증의 중요성을 분석합니다."
---

지난 3년간 생성형 AI와 코딩 에이전트 생태계는 단일 프롬프트 문구를 깎던 **'프롬프트 엔지니어링'** 시대를 지나, **컨텍스트(Context), 하네스(Harness), 루프(Loop), 그리고 그래프(Graph) 엔지니어링**으로 빠르게 패러다임 전환을 거듭해 왔습니다.

2023년 Auto-GPT의 무한 루프 실패와 에이전트 환멸기를 거쳐, ReAct 에이전트의 발전, 롱러닝 에이전트 하네스, 그리고 다시 결정론적 계약(Contract)과 그래프로 통제권을 되돌리기까지의 진화 맥락을 체계적으로 정리합니다.

<!--more-->

## Sources

- [발표 영상: 하네스/루프/그래프 엔지니어링, 순서대로 이해하기 (with Noto)](https://youtu.be/lokHQ8_b5Rk)
- [발표자료 노션 문서](https://bustling-pea-9a9.notion.site/3b093e636af1801f84c8f97785a7704b)
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [LangChain: The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering)

---

## 1. 에이전트 아키텍처 진화의 5단계 흐름

### 1) Prompt Engineering (2022~2023)
단일 입력 프롬프트의 뉘앙스, Few-shot 예시, CoT(Chain of Thought) 문구 튜닝에 집중하던 시기입니다. 2023년 Auto-GPT가 등장하며 자율 에이전트의 가능성을 보여주었으나, 컨텍스트 망각과 무한 루프, 탈선 문제로 인해 '하네스 무용론'과 에이전트 환멸기가 찾아왔습니다.

### 2) Context Engineering & Skills (2023~2024)
모델의 지능 자체보다 **"어떤 컨텍스트를 언제, 얼마나 압축하여 주입할 것인가"**가 성패를 가르기 시작했습니다.
* ReAct(Reasoning + Acting) 구조가 성숙해지며 결정론적 워크플로우를 흡수.
* 모든 규칙을 한꺼번에 밀어 넣지 않고 필요할 때 온디맨드로 지식을 불러오는 **스킬(Skills)**과 계층적 문서 구조(`AGENTS.md`)의 개념이 정립되었습니다.

### 3) Harness Engineering (2024~2025)
* **정의**: 에이전트가 장시간(Long-running) 다단계 작업을 수행할 때 탈선하거나 시스템을 망가뜨리지 않도록 둘러싸는 **런타임 틀(Harness/마구)**을 설계하는 엔지니어링.
* **핵심 요소**: 격리된 샌드박스 실행 환경, 엄격한 도구 호출 인터페이스, 자동 체크포인트 저장, 계층화된 규칙 주입.
* **대표 사례**: Anthropic의 롱러닝 에이전트 하네스 가이드, Nous Research의 Hermes Agent 'Fat Harness'.

### 4) Loop Engineering (2025~2026)
* **정의**: 에이전트의 자율적 탐색-실행-검증 반복 루프(Agent Loop)를 어떻게 제어하고 종료 조건을 정의할 것인가의 문제.
* **핵심 요소**: OpenAI Codex의 `/goal` 구조, LangChain의 4대 에이전트 루프 패턴, 자동 에러 복구 루프 및 Dynamic Workflow.

### 5) Graph Engineering (2026~현재)
* **정의**: 완전 자율 루프의 예측 불가능성을 통제하기 위해, **에이전트의 상태 전이와 멀티 에이전트 분기/합류를 유향 비순환 그래프(DAG / State Graph)와 엄격한 계약(Contract)**으로 제약하는 결정론적 설계.
* **의의**: 복잡한 엔터프라이즈 환경에서 환각과 탈선을 배제하고 100% 재현 가능한 신뢰성을 보장합니다.

---

## 2. "코드를 보지 않는 개발"과 검증(Verification)의 부상

에이전트가 한 번에 수만 줄의 코드를 생성하는 시대에는 인간 개발자가 모든 코드를 라인 바이 라인으로 검토하는 것이 불가능합니다.

따라서 최신 소프트웨어 엔지니어링의 핵심은 다음과 같이 이동했습니다:
1. **하네스(Harness)**를 통해 에이전트의 행동 반경과 인터페이스 계약(Contract)을 견고하게 정의한다.
2. **루프(Loop)와 그래프(Graph)**를 통해 자율 작업과 결정론적 검증 파이프라인을 결합한다.
3. 인간은 코드 세부 구현 대신 **시스템 아키텍처 이해와 검증 기준 설계**에 집중한다.
