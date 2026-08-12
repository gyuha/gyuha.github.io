---
title: "Understanding is the new bottleneck: Notion 엔지니어가 밝힌 코딩 에이전트 시대의 진짜 병목"
date: 2026-08-12T17:55:00+09:00
draft: false
categories:
  - AI
tags:
  - agents
  - cognitive-debt
  - software-engineering
  - notion
  - vibe-coding
description: "5만 5천 줄의 코드 PR을 1분 만에 뽑아내는 AI 에이전트 시대에, 진정한 병목은 단순 검증(Verification)이 아니라 개발자의 제품 이해(Understanding)와 주도적 참여(Participation)에 있다는 제프리 리트의 발표를 분석합니다."
---

에이전트 하나가 파일 372개, 5만 5천 줄의 추가 코드, 69개의 커밋이 담긴 대규모 Pull Request(PR)를 단 몇 분 만에 올려놓는 시대가 되었습니다. 개발 커뮤니티에서는 이제 소프트웨어 개발의 병목이 '코드를 작성하는 시간'에서 '사람이 코드를 읽고 검증하는 시간'으로 옮겨갔다고 진단하곤 합니다.

하지만 Notion의 디자인 엔지니어이자 MIT HCI 박사인 **제프리 리트(Geoffrey Litt)**는 AI Engineer World's Fair 2026 발표(*Understanding is the new bottleneck*)를 통해 이 진단을 절반만 인정하며, **"진짜 병목은 검증(Verification)이 아니라 이해(Understanding)와 주도적 참여(Participation)"**라는 새로운 화두를 던졌습니다.

<!--more-->

## Sources

- [원문 발표 아티클: Understanding is the new bottleneck](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck)
- [AI Engineer World's Fair 2026 발표 영상](https://www.youtube.com/watch?v=WkBPX-oDMnA)
- [해설 분석 유튜브 영상](https://youtu.be/81EIe6h7mnw)

## 1. 검증(Verification) vs 참여(Participation)

* **검증 (Verification)**: 코드가 기대대로 작동하는지 체크하는 역할. 에이전트의 성능이 발전할수록 검증에 들어가는 사람의 개입 수고는 점차 줄어들며 AI에 위임할 수 있습니다.
* **참여 (Participation)**: 시스템 구축 루프는 한 번으로 끝나지 않으며, 이전 한 바퀴에서 개발자가 얻은 **깊은 내면화와 이해**가 다음 아이디어 및 설계의 재료가 됩니다.
* **핵심 명제**: 검증은 AI에 위임할 수 있어도, **제품의 구조를 이해하고 다음 방향을 결정하는 개발자의 참여 자리**는 결코 위임할 수 없습니다.

## 2. 인지 부채 (Cognitive Debt)의 누적

에이전트가 만든 코드가 오류 없이 돌아간다고 해서 이해 없이 수용을 계속하면 **인지 부채(Cognitive Debt)**가 쌓이게 됩니다. 

기술 부채(Technical Debt)가 코드 구조를 엉키게 만들듯, 인지 부채는 개발자 자신의 머릿속에서 시스템의 통제력을 빼앗아 갑니다. 어느 순간 시스템은 멀쩡히 돌아가지만, 개발자 자신은 자사 제품의 아키텍처에 더 이상 수정이나 개입을 할 수 없는 외톨이가 됩니다.

## 3. 교육학에서 빌려온 2가지 해결책

제프리 리트는 사람이 복잡한 대상 시스템을 이해하도록 만드는 해법을 새로 만들 필요 없이, 이미 교육학에서 수십 년간 연구해 온 방법론을 적용할 것을 제안합니다:

### 1) 4단계 Rich Diff 문맥화 & 퀴즈
코드 diff를 단순 라인 변경 모음이 아니라 다음과 같은 4단계 문서 구조로 재작성합니다:
* **1단계**: 배경 (Background)
* **2단계**: 디테일 전의 직관적 아키텍처 (Intuition)
* **3단계**: 만져볼 수 있는 시각적 그림 (Interactive Diagram)
* **4단계**: 산문(Prose)이 결합된 코드 Diff

문서 하단에는 5문항의 Self-Quiz를 붙여, 개발자 스스로 퀴즈를 풀며 이해하지 못했다면 리뷰를 요청하거나 머지하지 않는 팀 규칙을 적용합니다.

### 2) 마이크로월드 (Microworlds)
시모어 패퍼트(Seymour Papert)의 매스랜드(Mathland) 개념처럼, 복잡한 텍스트 코드 대신 **개념과 작동 원리를 직접 시각적으로 조작하고 반응을 관찰할 수 있는 미니 샌드박스/인터랙티브 UI**를 구축합니다.

## 4. 결론의 확장

발표의 결론은 *"사람이 코드가 어떻게 동작하는지 이해하는 것은 중요하다"*에서 **"사람이 모든 것(시스템 전체)이 어떻게 동작하는지 이해하는 것은 중요하다"**로 확장됩니다. 

코드 자동 생성이 대중화될수록 역설적으로 **시스템 전체 구조를 비판적으로 이해하고 설계하는 인간의 인지 능력**이 가장 희소하고 가치 있는 자산이 될 것임을 시사합니다.
