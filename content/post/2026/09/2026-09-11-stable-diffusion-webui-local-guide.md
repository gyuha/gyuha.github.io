---
title: "AUTOMATIC1111 Stable Diffusion WebUI: 로컬 무제한 이미지 생성 가이드"
date: 2026-09-11T22:40:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - ai
  - python
  - workflow
description: "유료 API 비용 없이 로컬 GPU에서 무료로 고품질 이미지를 생성하는 txt2img, img2img, 인페인팅, ControlNet 포즈 제어 및 LoRA 화풍 적용의 표준 오픈소스 Stable Diffusion WebUI를 소개합니다."
---

미드저니(Midjourney)나 유료 이미지 생성 API를 사용하다 보면, 원하는 컷이 나올 때까지 수십 번 생성 버튼을 누르느라 월 구독료와 크레딧 소모가 눈덩이처럼 불어납니다. 생성 비용에 구애받지 않고 무제한으로 연구·테스트하고 싶다면 **로컬 GPU 기반의 오픈소스 환경** 으로 전환하는 것이 정답입니다.

`@aiwire_kr` 님이 공유한 **AUTOMATIC1111 Stable Diffusion WebUI** 는 깃허브 스타 16만 개를 돌파하며 전 세계 AI 크리에이터와 개발자들에게 **'오픈소스 이미지 생성의 사실상 표준(Defacto Standard)'** 으로 확고히 자리 잡은 대표적인 브라우저 기반 GUI 플랫폼입니다.

<!--more-->

## Sources

- [Threads 원문 포스트: aiwire_kr](https://www.threads.com/share/_nzQ7V8ma/)
- [공식 GitHub 저장소: AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

---

## 1. Stable Diffusion WebUI의 핵심 파이프라인

```mermaid
flowchart TD
    classDef inputNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef coreNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef extNode fill:#fde8c0,stroke:#d69e2e,stroke-width:1.5px,color:#333;
    classDef outNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    Prompt["프롬프트 (Positive & Negative)"] --> Core["WebUI 핵심 생성 엔진<br>(로컬 GPU 무제한 연산)"]
    RefImg["참조 이미지 (img2img / Inpainting)"] --> Core

    Ext1["ControlNet (뼈대 포즈 & 윤곽선 고정)"] --> Core
    Ext2["LoRA (특정 인물 & 전용 화풍 가중치)"] --> Core

    Core --> Upscale["초해상도 업스케일러 (4K/8K 디테일 보정)"]
    Upscale --> Out["비용 0원의 프로덕션급 이미지"]

    class Prompt,RefImg inputNode;
    class Core coreNode;
    class Ext1,Ext2 extNode;
    class Upscale,Out outNode;
```

---

## 2. 4대 핵심 생성 기능

1. **txt2img (Text-to-Image)**:
   * 텍스트 설명문만으로 상상 속 장면을 실사, 일러스트, 3D 등 원하는 스타일로 자유롭게 렌더링.
2. **img2img (Image-to-Image)**:
   * 기존 이미지의 구도와 색감, 윤곽을 유지한 채 스타일만 변경하거나 새로운 요소를 추가.
3. **인페인팅 (Inpainting)**:
   * 어색하게 나온 손가락, 눈매, 옷자락 등 특정 영역만 브러시로 칠해 해당 부위만 정교하게 재렌더링.
4. **업스케일링 (Upscaling)**:
   * 고화질 복원 모델(R-ESRGAN 등)을 활용해 깨짐 없이 4K 이상의 초고해상도로 출력.

---

## 3. 막강한 확장 생태계: ControlNet과 LoRA

* **ControlNet (형태 통제권 확보)**:
  * AI가 포즈나 구도를 멋대로 바꾸지 못하도록 인체 관절(OpenPose), 외곽선(Canny), 깊이 맵(Depth)을 강제 고정.
* **LoRA (경량 모델 갈아끼우기)**:
  * 수십 MB의 작은 가중치 파일만으로 특정 연예인, 버추얼 인플루언서, 웹툰 화풍을 완벽하게 재현.
