---
title: "Buzz: 트위터 창업자 잭 도시의 Block이 공개한 오픈소스 인간-AI 에이전트 협업 워크스페이스"
date: 2026-08-27T07:50:00+09:00
draft: false
categories:
  - AI
tags:
  - agents
  - claude-code
  - productivity
description: "Claude Code, Codex, 로컬 LLM 등 여러 도구에 흩어져 있던 작업 결과와 피드백을 Slack 형태의 단일 채널·스레드에 모아 인간과 함께 팀으로 운영하는 오픈소스 플랫폼 Buzz를 분석합니다."
---

Claude Code, Codex, Cursor 등 다양한 AI 코딩 에이전트를 사용하다 보면, 각자의 작업 결과와 사람이 남긴 피드백, 의사결정 맥락이 도구마다 파편화되어 *"그때 왜 그렇게 판단하고 코드를 고쳤는지"* 사후 추적이 어려워지는 문제가 발생합니다.

트위터 창업자 잭 도시(Jack Dorsey)가 이끄는 블록(Block) 팀이 오픈소스로 공개한 **`Buzz`**(`block/buzz`)는 **인간과 여러 AI 에이전트가 Slack 형태의 단일 채널과 스레드에서 동등한 팀원으로 상주하며 협업할 수 있도록 설계된 인간-에이전트 통합 워크스페이스**입니다.

<!--more-->

## Sources

- [원문 유튜브 영상: 요즘 가장 핫한 AI툴 Buzz, 클로드코드·코덱스를 한 팀으로 쓰는 법!](https://youtu.be/3RApTxBeE7E)
- [Buzz 공식 웹사이트](https://buzz.xyz)
- [Buzz GitHub 공식 저장소 (block/buzz)](https://github.com/block/buzz)
- [Block 공식 발표 블로그](https://block.xyz/inside/introducing-buzz-where-humans-and-agents-work-together)

---

## 1. Buzz 협업 워크스페이스 아키텍처

```mermaid
flowchart TD
    classDef humanNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef hubNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef agentNode fill:#fde8c0,stroke:#d69e2e,stroke-width:1.5px,color:#333;
    classDef outNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    Human["개발자 & 인간 팀원"] --> Hub["Buzz 워크스페이스<br>(Slack 형태의 채널·스레드 허브)"]
    Hub <--> ClaudeAgent["Claude Code 에이전트<br>(기획 및 1차 구현 담당)"]
    Hub <--> CodexAgent["Codex / 로컬 LLM 에이전트<br>(반박 및 보안·코드 리뷰 담당)"]
    Hub --> History["단일 스레드에 작업 결과 & 판단 근거 완벽 보존"]

    class Human humanNode;
    class Hub hubNode;
    class ClaudeAgent,CodexAgent agentNode;
    class History outNode;
```

---

## 2. 주요 핵심 기능 및 차별점

1. **단일 스레드 기반의 컨텍스트 및 의사결정 보존**:
   * 개별 터미널에 흩어지던 대화 이력과 피드백을 단일 스레드에 누적하여, 프로젝트 참여자 누구나 에이전트의 결정 배경과 히스토리를 투명하게 열람할 수 있습니다.
2. **다자간 역할 분담 협업 (기획담당 vs 비판/보안담당)**:
   * 예를 들어 `@ClaudeCode`에게 1차 기능 설계를 지시하면, `@Codex`가 보안 취약점과 엣지 케이스를 반박하고, 인간 리더가 최종 컨펌하는 전문 팀 단위 워크플로우를 구성할 수 있습니다.
3. **유연한 모델 연결 및 로컬 LLM 지원**:
   * 상용 클라우드 API뿐만 아니라 Ollama 등을 통한 사내 로컬 오픈소스 모델도 팀원으로 등록하여 비용과 보안을 최적화할 수 있습니다.
4. **동료 초대 및 실시간 공유**:
   * 실제 팀원들을 채널에 초대하여 AI 에이전트들과 실시간으로 스레드를 공유하고 의견을 나눌 수 있습니다.

---

## 3. 시사점

개별 터미널에서 1:1로만 쓰이던 AI 코딩 도구를 팀 단위 커뮤니케이션 공간으로 통합하여, **사람과 다양한 AI 직원이 실시간으로 소통하고 기록을 공유하는 미래형 개발 협업 플랫폼의 표준**을 제시합니다.
