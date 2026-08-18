---
title: "Qwen 3.8-27B 무검열(Uncensored) MLX 버전 공개: 안전 가드레일 제거와 거부율 0%대 하락 분석"
date: 2026-08-19T08:15:00+09:00
draft: false
categories:
  - AI
tags:
  - open-source
  - qwen
  - llm
  - security
  - mlx
description: "Orca가 공개한 Qwen 3.8-27B 무검열(Uncensored) MLX 모델의 주요 벤치마크별 거부율(Rejection Rate) 변화와 Apple Silicon 로컬 구동 특성을 분석합니다."
---

최근 오픈소스 언어 모델 생태계에서 과도한 안전 정렬(Safety Alignment)로 인한 출력 거부 및 성능 저하(Alignment Tax)를 해소하기 위한 시도가 활발히 이어지고 있습니다.

Orca 팀은 Qwen 3.8-27B 모델에서 안전 가드레일을 완전히 걷어낸 **Qwen 3.8-27B 무검열(Uncensored)** 버전을 공개했습니다. 취약점 연구, 익스플로잇 분석, 침투 테스트 등 보안 연구 목적의 요청에 대해 거의 0%에 가까운 거부율을 기록하며, Apple Silicon Mac에서 즉시 구동 가능한 MLX 포맷으로 제공됩니다.

<!--more-->

## Sources

- [율무커피 분석 리포트](https://x.com/yulmu_coffee/status/2089526490530762887)
- [Qwen 3.8 공식 오픈소스 레포지토리]

---

## 1. 벤치마크별 거부율(Rejection Rate) 변화 지표

안전성 평가 벤치마크에서 원본 모델 대비 거부율이 극적으로 하락했습니다:

### Thinking OFF 모드 기준
* **AdvBench**: 99.0% ➔ **0.0%**
* **JailbreakBench**: 94.0% ➔ **0.0%**
* **MaliciousInstruct**: 99.0% ➔ **0.0%**
* **StrongREJECT**: 97.3% ➔ **2.0%**
* **HarmBench**: 98.7% ➔ **2.7%**
* **SimpleSafetyTests**: 64.0% ➔ **6.0%**
* **ForbiddenQuestions**: 73.3% ➔ **4.7%**

> **Thinking ON 모드**에서는 심층 추론 과정에서 가드레일 우회가 더욱 완벽해져 거부율이 **0 ~ 1.7%** 수준으로 떨어집니다.

---

## 2. 주요 특징 및 생성 역량

1. **보안 연구 및 민감 요청에 대한 다이렉트 응답**:
   * 악성코드 역공학, 익스플로잇 취약점 분석, 모의 해킹 시나리오 등 원본 모델이 '안전상의 이유'로 회피하던 요청에 직접적인 가이드라인과 코드를 생성합니다.
   * 다만 약 30~50%의 케이스에서는 사전 학습 코퍼스에 잔존하는 면책/경고 문구를 함께 출력하면서도 실제 콘텐츠는 정상 생성합니다.
2. **Alignment Tax 해소로 인한 기본 성능 소폭 향상**:
   * 모델의 출력을 인위적으로 억제하는 가드레일이 제거되면서 코딩 및 논리 추론 벤치마크 점수가 소폭 상승했습니다.
3. **Apple Silicon MLX 프레임워크 지원**:
   * Mac 사용자는 별도의 무거운 컨테이너나 리눅스 서버 없이도 로컬 환경에서 양자화된 27B 모델을 고속으로 직접 가동할 수 있습니다.
