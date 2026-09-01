---
title: "AI에게 맡기는 주식 자동매매: Codex와 NH투자증권 Namuh PLUG API로 투자 에이전트 만들기"
date: 2026-09-01T20:12:00+09:00
draft: false
categories:
  - Finance
tags:
  - agents
  - automation
  - python
description: "NH투자증권의 신규 OpenAPI 플랫폼인 Namuh PLUG와 OpenAI Codex를 연동하여 모의투자부터 실전 매매까지 전 과정을 자율 수행하는 주식 자동매매 에이전트 구축 튜토리얼을 분석합니다."
---

복잡한 HTS/MTS 조작이나 까다로운 증권사 개별 인증 절차 없이, 나만의 투자 전략을 파이썬 코드로 자동화하려는 개인 투자자들의 수요가 급증하고 있습니다.

유튜버 조코딩(JoCoding) 님이 공개한 **`Codex와 NH투자증권 Namuh PLUG API 기반 주식 자동매매 에이전트 튜토리얼`**은 **통합 계좌 관리와 모의투자를 지원하는 Namuh PLUG OpenAPI와 OpenAI Codex의 바이브코딩을 결합하여, 코딩 초보자도 몇 시간 만에 퀀트 트레이딩 봇을 구축하고 실전 배포하는 4단계 프로세스**를 제공합니다.

<!--more-->

## Sources

- [원문 유튜브 영상: AI에게 맡기는 주식 자동매매 - Codex와 NH투자증권 API로 투자 에이전트 만들기](https://youtu.be/CGDibbwGfvk)
- [GitHub 공식 저장소 (youtube-jocoding/nhplug-auto-trader)](https://github.com/youtube-jocoding/nhplug-auto-trader)
- [Namuh PLUG 공식 포털](https://nhplug.com)

---

## 1. AI 자동매매 에이전트 파이프라인

```mermaid
flowchart TD
    classDef apiNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef codexNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef stratNode fill:#fde8c0,stroke:#d69e2e,stroke-width:1.5px,color:#333;
    classDef outNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    API["1. Namuh PLUG API 키 발급<br>(통합 계좌 관리 & 모의투자 연동)"] --> Codex["2. Codex CLI 바이브코딩<br>(API 명세 주입 및 스크립트 자동 생성)"]
    Codex --> Strategy["3. 트레이딩 전략 로직 구현<br>(변동성 돌파 / 골든크로스 / 손절 룰)"]
    Strategy --> Deploy["4. 모의투자 검증 & 실전 매매<br>(예외 처리 및 자동 주문 체결)"]

    class API apiNode;
    class Codex codexNode;
    class Strategy stratNode;
    class Deploy outNode;
```

---

## 2. 자동매매 구축 4단계 실전 프로세스

1. **1단계: Namuh PLUG API 발급 및 모의투자 환경 설정**:
   * 나무증권 앱과 NH PLUG 포털에서 API Key/Secret을 발급받고 모의투자 계좌를 연결합니다. 여러 계좌를 하나의 인증 키로 제어할 수 있어 관리가 간편합니다.
2. **2단계: Codex CLI 기반 바이브코딩 연동**:
   * Namuh PLUG의 REST API 엔드포인트 명세서(잔고 조회, 시세 수집, 매수/매도 주문)를 Codex에 주입하여 기본 파이썬 연동 모듈을 생성합니다.
3. **3단계: 투자 전략 알고리즘 구현**:
   * 이동평균선 골든크로스, 변동성 돌파 전략(래리 윌리엄스), 익절 및 손절(Stop-loss) 규칙 등 원하는 투자 로직을 자연어로 설명하여 코드로 구현합니다.
4. **4단계: 모의투자 시뮬레이션 및 실전 전환**:
   * 정규장 시간 동안 모의투자 환경에서 주문 체결 속도, 미체결 취소, 네트워크 장애 예외 처리를 검증한 뒤 실전 계좌로 전환합니다.

---

## 3. Namuh PLUG의 주요 경쟁력

* **통합 계좌 제어**: 계좌별로 보안 인증서를 발급해야 했던 기존 환경과 달리 단일 키로 다계좌 제어 가능.
* **폭넓은 자산 거래**: 국내 주식뿐만 아니라 해외 주식, 채권, 파생상품까지 자동매매 지원.
* **최적화된 수수료**: 국내 0.01%, 해외 0.09%의 경쟁력 있는 수수료 구조.

---

## 4. 시사점

AI 코딩 에이전트와 모던 증권사 OpenAPI의 결합을 통해, **전문 퀀트 트레이더의 전유물이었던 알고리즘 자동매매를 개인 투자자도 손쉽게 구현하고 운영할 수 있는 대중화 시대**가 열렸습니다.
