---
title: "FreeLLMAPI: 29개 AI 프로바이더의 무료 티어를 하나로 묶는 오픈소스 통합 라우터 분석"
date: 2026-08-08T07:30:00+09:00
draft: false
categories:
  - AI
tags:
  - open-source
  - llm
  - proxy
  - model-router
  - claude-code
description: "29개 주요 AI 프로바이더의 무료 티어(월 40억 토큰 규모)를 하나의 OpenAI 호환 /v1 엔드포인트로 묶어주는 오픈소스 스마트 라우터 FreeLLMAPI의 주요 구조와 작동 원리를 분석합니다."
---

글로벌 AI 연구소와 클라우드 기업들이 연이어 무료 티어 API를 선보이면서, 개발자가 개별적으로 활용 가능한 무료 유추(Inference) 용량이 크게 증가했습니다. 하지만 수십 개의 서비스 API 키를 직접 등록하고 각기 다른 Rate Limit과 SDK, 페일오버 처리를 구현하는 작업은 결코 만만치 않습니다.

**FreeLLMAPI**(`tashfeenahmed/freellmapi`)는 이러한 파편화된 무료 API를 하나의 로컬 OpenAI 호환 `/v1` 엔드포인트로 집계해 주는 오픈소스 프록시 및 스마트 라우팅 엔진입니다.

<!--more-->

## Sources

- [FreeLLMAPI GitHub 저장소](https://github.com/tashfeenahmed/freellmapi)
- [FreeLLMAPI 공식 웹사이트 및 모델 카탈로그](https://freellmapi.co)
- [FreeLLMAPI 클라이언트 & 에이전트 설정 가이드](https://github.com/tashfeenahmed/freellmapi/blob/main/docs/clients.md)
- [FreeLLMAPI 아키텍처 및 내부 라우팅 명세](https://github.com/tashfeenahmed/freellmapi/blob/main/docs/architecture.md)

## 1. FreeLLMAPI의 탄생 배경

주요 AI 기술 기업들은 자사 모델의 저변 확대를 위해 매월 수백만 토큰에서 일 수천 회 이상의 무료 API 호출 한도를 제공하고 있습니다. 하지만 개별 서비스 하나만으로는 본격적인 개발이나 에이전트 루프를 감당하기 부족합니다.

FreeLLMAPI는 약 29개 프로바이더(ModelScope, DeepSeek, GLM, Groq, OpenRouter, Together 등), 251개 모델 파이프라인 / 358개 엔드포인트를 묶어 **월 약 40억 토큰 규모의 인퍼런스 용량**을 하나의 추상화된 백엔드로 전환합니다.

## 2. 주요 핵심 기능

### 단일 엔드포인트 추상화 (`/v1`)
애플리케이션이나 코딩 에이전트는 로컬에 띄운 `http://localhost:3001/v1` 하나의 호스트만 바라보고 하나의 발급된 베어러 토큰(Unified Key)으로 호출을 진행합니다.

### 지능형 라우팅 및 429/5xx 자동 페일오버 (Failover)
* 지연 시간, 가용성, 성능 점수를 바탕으로 6가지 전략에 따라 동적으로 최적의 모델을 선택합니다.
* 특정 프로바이더가 속도 제한(Rate Limit 429)이나 서버 오류(5xx)를 반환하면 즉시 다른 가용 모델로 자동 페일오버를 수행합니다.
* 프로바이더별 키 단위 호출 수(RPM, TPM)를 실시간 카운트하여 캡 초과를 사전에 방지합니다.

### 다양한 API 규격 완벽 지원
* **OpenAI API**: Chat Completion, Responses, Embeddings, Image Generation, Speech(TTS)
* **Anthropic Messages API**: `/v1/messages` 프로토콜을 백엔드 라우터와 직접 연결하여 **Claude Code**나 Anthropic SDK가 무료 풀을 직접 활용하도록 지원합니다.
* **Gemini & Ollama 프로토콜**: Gemini CLI용 `/v1beta` 엔드포인트와 Zed, JetBrains 연동용 Ollama 이뮬레이션 모드를 제공합니다.

### Fusion (다중 모델 결과 합성)
가상 모델 `fusion`을 호출하면 프롬프트를 복수의 서로 다른 프론티어/오픈소스 모델로 동시 병렬 전송한 후, 평가 모델(Judge Model)이 렌더링된Draft 결과를 단일의 최적 응답으로 합성해 줍니다.

## 3. 원클릭 에이전트 연동 지원

FreeLLMAPI는 개발 에이전트와 CLI 도구의 자동 연동 명령어를 내장하고 있습니다:

```bash
# Claude Code 연동 자동 생성
npx freellmapi setup-claude

# Codex CLI 및 Aider 연동
npx freellmapi setup-codex
npx freellmapi setup-aider
```

환경 설정 파일의 유효성 백업을 자동으로 처리하며, 자식 프로세스에만 자격 증명을 주입하는 `freellmapi launch` 같은 제로-퍼시스턴스 런처도 포함되어 있습니다.

## 4. 보안 및 대시보드 구조

* **AES-256-GCM 암호화**: 등록된 프로바이더 API 키는 SQLite 데이터베이스 내에 암호화되어 저장되며 인메모리로만 복호화되어 동작합니다.
* **React 관리 UI 및 데스크톱 앱**: 지연 시간(p50/p95), 요청 통계, 폴백 체인 순서를 시각적으로 관리할 수 있는 웹 UI 및 전용 데스크톱 앱(macOS/Windows)을 제공합니다.

무료 티어를 효율적으로 집계하여 에이전트 및 로컬 개발 환경의 인퍼런스 비용을 극적으로 절감하고자 할 때 유용한 레퍼런스 프로젝트입니다.
