---
title: "LongHorizon-Harness: AI 에이전트의 장시간 복합 작업 붕괴를 방지하는 3인 1조 검증 아키텍처"
date: 2026-08-24T17:40:00+09:00
draft: false
categories:
  - AI
tags:
  - agents
  - testing
  - workflow
description: "고덕지도(AMAP) 팀이 오픈소스로 공개한 LongHorizon-Harness를 통해 진도관리관, 단기실행관, 독립검수관의 3인 1조 분업으로 장기 복합 작업 성공률을 80%로 높이고 토큰을 24% 절감하는 아키텍처를 분석합니다."
---

Claude Code, Codex, Agy 등 최신 AI 에이전트에게 1~2시간 이상 소요되는 복합적인 작업을 맡기면, 초기 1~2시간은 순조롭게 진행되다가 뒤로 갈수록 맥락이 오염되어 엉뚱한 결론을 내리거나 절반만 만들고 "완료했습니다"라고 거짓 보고(Hallucinated Completion)하는 붕괴 현상이 발생합니다.

고덕지도(AMAP-ML) 팀이 개발하여 Hugging Face 주간 1위를 기록한 **`LongHorizon-Harness`**는 에이전트 단일 세션에 모든 히스토리를 누적하지 않고, **진도 관리관(Planner), 단기 실행관(Worker), 독립 검수관(Verifier)으로 역할을 명확히 쪼갠 3인 1조 하네스 시스템**을 구축하여 **작업 완수율을 50%에서 80%로 대폭 향상시키고 토큰을 24% 절감**했습니다.

<!--more-->

## Sources

- [원문 X 게시물: Ryrenz](https://x.com/Ryrenz/status/2091322231997571450)
- [LongHorizon-Harness GitHub 공식 저장소](https://github.com/AMAP-ML/LongHorizon-Harness)
- [AMAP-ML 연구 논문 (arXiv)]

---

## 1. 3인 1조 분업 및 물리 검증 아키텍처

```mermaid
flowchart TD
    classDef goalNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef planNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef workNode fill:#fde8c0,stroke:#d69e2e,stroke-width:1.5px,color:#333;
    classDef verifNode fill:#ffc8c4,stroke:#e53e3e,stroke-width:1.5px,color:#333;
    classDef doneNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    Goal["장기 복합 목표 입력<br>(Long-Horizon Task)"] --> Planner["1. 진도 관리관 (Planner)<br>(전체 로드맵 관리 & 다음 단위 작업 지정)"]
    Planner --> Worker["2. 단기 실행관 (Worker)<br>(오염 없는 깨끗한 컨텍스트로 단일 작업 수행)"]
    Worker --> Verifier["3. 독립 검수관 (Verifier)<br>(실제 파일·UI·로그·테스트 스크립트 물리 검증)"]
    Verifier -->|"검증 실패 (불일치 증거 확보)"| Planner
    Verifier -->|"검증 통과"| Finish["최종 완수 (성공률 80% 달성)"]

    class Goal goalNode;
    class Planner planNode;
    class Worker workNode;
    class Verifier verifNode;
    class Finish doneNode;
```

---

## 2. 역할별 핵심 원리와 차별점

1. **진도 관리관 (Planner / Orchestrator)**:
   * 전체 목표의 진행 상황과 마일스톤만 추적하며, 오직 *"다음에 실행해야 할 단위 태스크가 무엇인가"*만 판단하여 실행관에게 전달합니다.
2. **단기 실행관 (Worker / Executor)**:
   * 이전 단계의 불필요한 노이즈가 없는 깨끗한 컨텍스트(Fresh Context)를 주입받아 배정된 한 가지 작업에만 집중합니다.
3. **엄격한 독립 검수관 (Verifier / Ground-Truth Inspector)**:
   * 실행관의 "완료했습니다"라는 텍스트 응답을 절대 신뢰하지 않고, 실제 OS 파일 시스템, GUI 화면 상태, 터미널 실행 로그, 유닛 테스트 스크립트를 직접 실행하여 물리적 증거(Ground Truth)를 확인합니다. 검증 실패 시 구체적 실패 증거를 첨부해 재작업을 지시합니다.

---

## 3. 주요 성과 및 지원 범위

* **크로스 애플리케이션 지원**: 터미널 코딩뿐만 아니라 브라우저, 스프레드시트, 오피스 문서, 디자인/3D 소프트웨어 등 OS 전반의 GUI/CLI 작업을 통합 오케스트레이션.
* **모델 독립성**: Claude, GPT, Qwen 등 다양한 모델을 연결할 수 있으며, 기획/실행/검수 단계별로 최적의 모델을 분리 매핑 가능.
* **토큰 및 성공률**: 다중 앱 연동 작업 성공률을 기존 50% ➔ **80%로 격상**, 불필요한 방황을 줄여 **토큰 소모량 24% 절감**.
