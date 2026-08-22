---
title: "fluent-korean: 국어학 관점에서 클로드 코드의 한국어 어투와 조사를 교정하는 스킬 플러그인"
date: 2026-08-22T08:04:00+09:00
draft: false
categories:
  - AI
tags:
  - claude-code
  - productivity
description: "클로드 코드(Claude Code)의 어색한 번역투, 부자연스러운 조사와 어미 종결을 국어학적 문법 규칙으로 교정하여 자연스러운 한국어 개발 환경을 구축하는 fluent-korean 플러그인을 소개합니다."
---

Claude Code는 영어 프롬프트뿐만 아니라 한국어 지시에도 높은 수준의 코드 생성 성능을 보여주지만, 한국어로 설명하거나 요약할 때 **"특유의 직역체 번역투나 부자연스러운 조사 결합, 어색한 어미 종결"**이 종종 나타납니다.

국어학 전공자가 개발하여 공개한 **`snflkd/fluent-korean`** 플러그인은 클로드의 언어 생성 프롬프트를 교정하여 **개발 맥락에 맞는 깔끔하고 자연스러운 한국어 문장으로 답변하도록 돕는 Claude Code 전용 스킬**입니다.

<!--more-->

## Sources

- [원문 X 게시물 (H)](https://x.com/hmmmmmm1458/status/2090250855278874949)

---

## 1. fluent-korean 동작 흐름

```mermaid
flowchart TD
    classDef inputNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef pluginNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef outNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    Input["사용자 질문 / 프롬프트"] --> Core["Claude Code 엔진"]
    Core --> Plugin["fluent-korean 플러그인<br>(번역투 제거 & 조사/어미 교정 룰)"]
    Plugin --> Output["자연스럽고 정확한 한국어 개발 답변"]

    class Input inputNode;
    class Core,Plugin pluginNode;
    class Output outNode;
```

---

## 2. 설치 및 적용 방법 (단 2줄)

Claude Code 터미널 환경에서 마켓플레이스 등록과 플러그인 설치를 2줄의 명령어로 완료할 수 있습니다:

```bash
# 1. 마켓플레이스 저장소 추가
/plugin marketplace add snflkd/fluent-korean

# 2. fluent-korean 플러그인 설치
/plugin install fluent-korean@fluent-korean

# 3. 세션 초기화 및 플러그인 적용
/clear
```

---

## 3. 주요 개선 효과

* **직역체/번역투 표현 완화**: 영어 문장 구조를 그대로 직역하면서 발생하는 긴 관형절과 수동태 표현을 한국어 고유의 능동형 문장으로 간결하게 교정.
* **자연스러운 기술 용어 결합**: 영문 프로그래밍 용어(API, 훅, 컴포넌트 등) 뒤에 붙는 한국어 조사(은/는, 이/가, 을/를)의 오류를 방지.
* **명확한 종결 어미 톤**: 개발 설명에 최적화된 명료하고 전문적인 서술 어투 확립.
