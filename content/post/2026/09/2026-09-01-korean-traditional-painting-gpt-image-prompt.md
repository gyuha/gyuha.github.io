---
title: "사진 속 얼굴과 포즈를 그대로 살려 조선시대 진채화 화보로 변환하는 GPT 이미지 프롬프트"
date: 2026-09-01T08:21:00+09:00
draft: false
categories:
  - Design
tags:
  - prompt-engineering
  - productivity
  - workflow
description: "인물이나 반려동물 사진의 고유한 이목구비, 표정, 포즈를 원본 그대로 보존하면서 한지 질감, 세필 붓선, 광물 안료 느낌의 고급 조선시대 진채화·민화풍으로 변환하는 GPT 프롬프트를 분석합니다."
---

AI 이미지 생성 도구로 사진을 동양화나 예술 화보로 변환할 때 가장 큰 문제는 원본 인물의 얼굴이 완전히 다른 사람으로 바뀌거나(Identity Loss), 어색한 일본풍/중국풍 화풍이 섞여 나오는 점입니다.

프롬프트 엔지니어 neotypeska 님이 공개한 **`한국 전통 진채화 변환 프롬프트 기법`**은 원본 사진 속 인물이나 반려동물의 **이목구비와 표정, 시선, 포즈를 정밀하게 보존하면서, 한지(Hanji) 질감, 섬세한 세필 붓선, 천연 광물 안료의 색감, 한옥 창호와 붉은 낙관 인장을 더해 고급스러운 조선시대 정통 채색화 화보를 완성**해 줍니다.

<!--more-->

## Sources

- [원문 Threads 게시물 (neotypeska)](https://www.threads.com/@neotypeska/post/Dcs5PtjEoiq)
- [GPT Image 생성 프롬프트 엔지니어링 가이드]

---

## 1. 한국화 화보 변환 파이프라인

```mermaid
flowchart TD
    classDef imgNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef promptNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef styleNode fill:#fde8c0,stroke:#d69e2e,stroke-width:1.5px,color:#333;
    classDef outNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    Photo["원본 사진 첨부<br>(인물 / 반려동물 / 캐릭터)"] --> Prompt["한국화 변환 프롬프트 주입<br>(이목구비·표정·포즈 보존 지시)"]
    Prompt --> Style["한국 정통 회화 미학 연출<br>(한지 질감·세필 붓선·광물 안료·창호·낙관)"]
    Style --> Result["고급스러운 조선시대 진채화·민화풍 프로필 화보 완성"]

    class Photo imgNode;
    class Prompt promptNode;
    class Style styleNode;
    class Result outNode;
```

---

## 2. 주요 핵심 연출 요소

1. **원본 인물의 정체성 보존 (Identity & Pose Preservation)**:
   * 얼굴의 이목구비 비율, 미소나 눈빛, 고개의 각도와 손동작을 유지하도록 프롬프트 제약을 설정하여 '나만의 맞춤 화보'를 구현합니다.
2. **한국 정통 진채화(眞彩畵) 및 세필채색 미학**:
   * 거친 수묵화나 왜색 짙은 화풍 대신, 고운 붓으로 꼼꼼히 칠한 세필채색과 한지의 자연스러운 질감, 광물성 안료의 깊이 있는 색감을 표현합니다.
3. **전통 소품 및 배경 오브제 조화**:
   * 배경에 은은한 한옥 창호 격자문, 소나무, 들국화, 모란 등을 배치하고, 귀퉁이에 붉은 전통 낙관 인장(Red Seal)을 찍어 완성도를 높입니다.
4. **무료/Plus 모든 환경 지원**:
   * ChatGPT 무료 버전 및 Plus/Pro 환경의 DALL-E / GPT Image 모델 모두에서 간편하게 사진을 업로드하고 복사-붙여넣기만으로 생성할 수 있습니다.

---

## 3. 시사점

단순한 화풍 필터를 씌우는 수준을 넘어, **원본 피사체의 정체성을 유지하면서 국가/문화권 고유의 전통 회화 양식을 정밀하게 입히는 프롬프트 엔지니어링의 실전 활용법**을 보여줍니다.
