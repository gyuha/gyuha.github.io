---
title: "Anthropic Managed Agents: 자율 수행 에이전트를 만드는 9종 오픈소스 워크숍 분석"
date: 2026-08-11T10:00:00+09:00
draft: false
categories:
  - AI
tags:
  - anthropic
  - agents
  - claude-code
  - open-source
  - workflow
description: "앤트로픽이 공개한 Apache-2.0 라이선스 기반의 비동기 자율 에이전트(Managed Agents) 9종 워크숍과 아키텍처 가이드를 분석합니다."
---

단순 1:1 대화형 챗봇에서 벗어나, 사용자가 상위 목표(Objective)를 부여하고 자리를 비워도 비동기로 긴 호흡의 엔지니어링 및 리서치를 자율 수행하는 **매니지드 에이전트(Managed Agents)** 시스템이 주목받고 있습니다.

앤트로픽(Anthropic)은 이러한 자율 에이전트 파이프라인 구축 노하우를 집약한 **9종의 공식 오픈소스 워크숍 저장소**를 공개했습니다.

<!--more-->

## Sources

- [Anthropic Managed Agents 공식 워크숍 안내](https://qjc.app/blog/anthropic-managed-agents-guide)
- [분석 유튜브 숏츠 리포트](https://youtube.com/shorts/02aq7ZVBu_Y)

## 1. Managed Agents 시스템의 핵심 특징

* **비동기 자율 수행 (Async Execution)**: 실시간 대기 방식이 아니라, 에이전트에게 샌드박스와 권한을 부여하고 백그라운드에서 오랫동안 유효한 결과물(Evidence)을 만들어내도록 격리 조율합니다.
* **Apache-2.0 100% 오픈 라이선스**: 앤트로픽이 공개한 워크숍 코드는 라이선스 제약 없이 자유롭게 수정 및 사내 프라이빗 시스템으로 상업적 도입이 가능합니다.
* **높은 관심도**: 공개 직후 GitHub에서 Star 1,950+ 개, Fork 550+ 개를 기록하며 표준 에이전트 패턴으로 입지를 다지고 있습니다.

## 2. 9종 워크숍이 다루는 3대 핵심 패턴

1. **상태 분리 및 오케스트레이션**: 메인 제어 커널(Control Plane)과 실제 코드를 실행하는 개별 런타임 샌드박스를 분리 관리하는 기술.
2. **증거 기반 평가 (Evidence-based Assessment)**: 에이전트가 만든 변경 사항이 올바른지 단위 테스트 및 검증 로그를 스스로 제출하게 만드는 패턴.
3. **휴먼 게이트(Human-in-the-loop)**: 비가역적인 데이터베이스 삭제나 위험한 외부 결제 액션 전 사람의 승인을 대기하는 관문 설계.
