---
title: "AGENTS.md 슬림화 가이드: 점진적 공개(Progressive Disclosure)와 Instruction Budget 관리"
date: 2026-08-14T00:30:00+09:00
draft: false
categories:
  - AI
tags:
  - agents
  - prompt-engineering
  - architecture
  - claude-code
  - context-engineering
description: "AGENTS.md를 완벽한 프로젝트 설명서가 아닌 고비용 컨텍스트로 재정의하고, 점진적 공개 아키텍처를 적용하여 에이전트의 주의력(Instruction Budget)을 최적화하는 3가지 작성 규칙을 분석합니다."
---

Claude Code, Cursor, Codex 등 코딩 에이전트 생태계에서 `AGENTS.md` 파일은 에이전트에게 프로젝트의 지침을 전달하는 핵심 관문으로 자리 잡았습니다. 하지만 많은 개발자들이 `/init` 커맨드로 자동 생성된 파일이나 프로젝트 전체 설명서를 `AGENTS.md`에 무비판적으로 채워 넣으면서, 에이전트의 성능이 오히려 저하되는 현상을 겪곤 합니다.

Matt Pocock(`@mattpocockuk`)의 리팩토링 가이드와 최신 코딩 에이전트 노하우를 바탕으로, **AGENTS.md를 슬림하게 다이어트하고 점진적 공개(Progressive Disclosure) 구조를 도입해야 하는 이유와 작성 규칙**을 정리합니다.

<!--more-->

## Sources

- [원문 트윗 및 리팩토링 프롬프트](https://x.com/i/status/2087820511099203769)
- [Matt Pocock: Refactoring AGENTS.md](https://t.co/WvAD4AOlvW)

## 1. AGENTS.md의 새로운 정체성: "고비용 작업 컨텍스트"

`AGENTS.md`를 프로젝트의 모든 내용이 담긴 '완벽한 설명서'로 생각하고 접근하면 안 됩니다. 

`AGENTS.md`는 **"에이전트가 매 미션(Task)을 시작할 때마다 주의력(Instruction Budget)과 컨텍스트 한도를 필연적으로 점유하는 고비용 작업 컨텍스트"**로 재정의해야 합니다. 모든 미션에 불필요한 정보가 들어가면 에이전트의 오케스트레이션 성능이 떨어지고 지시 충돌이 발생하기 쉽습니다.

## 2. AGENTS.md 슬림화를 위한 3대 핵심 규칙

### 1) `/init` 자동 생성 기능으로 무분별하게 채우지 말 것
자동 생성 툴은 포괄성을 추구하느라 프로젝트 구조, 패키지 목록, 파일 경로, 기술 스택 등을 과도하게 집어넣습니다. 이러한 정보 중 상당수는 에이전트가 코드와 `package.json` 등 설정 파일에서 스스로 발견할 수 있는 내용이며, 코드베이스가 변경되면 금방 구식(Outdated) 정보가 되어 매 미션마다 에이전트의 판단을 교란시킵니다.

### 2) 코드를 통해 쉽게 알 수 있는 구현 세부사항 제거
특정 모듈이 어느 폴더에 있는지, 현재 어떤 서비스 클래스가 기능을 맡고 있는지 등 자주 바뀌는 실체 정보는 작성하지 않습니다. 대신 **프로젝트의 최종 목표, 비가역적 제약조건, 커스텀 툴체인 규칙, 절대 어기면 안 되는 가버넌스** 등 코드 텍스트만으로는 추론하기 어려운 정보만 정제하여 담아야 합니다.

### 3) 점진적 공개 (Progressive Disclosure) 아키텍처 도입
모든 세부 규칙(테스트 규격, TypeScript 컨벤션, API 스키마, DB 마이그레이션 등)을 루트 `AGENTS.md`에 몰아 넣지 않습니다.
* 루트 `AGENTS.md`는 **"매우 얇은 라우터(Router) 및 입구"** 역할만 수행합니다.
* 세부 규칙은 독립 문서, **Skills**, 또는 **Rules**로 분리하여, 에이전트가 해당 과제를 실제 수행하는 시점에만 필요한 스킬을 불러오도록 설계합니다.

## 3. 핵심 질문: "주의력(Instruction Budget) 점유 가치가 있는가?"

`AGENTS.md`에 문장을 하나 추가할 때마다 스스로 물어야 합니다:

> **"이 항목이 매번 에이전트의 주의력(Instruction Budget)과 컨텍스트 한도를 점유할 가치가 있는가?"**

그렇지 않다면 코드 자체, 독립된 문서, 스킬, 혹(Hook) 등 필요할 때 불러오는(On-demand) 구조로 이관해야 합니다. `AGENTS.md`를 다이어트하는 것은 단순 토큰 절감을 넘어 **에이전트의 한정된 인지 한도를 핵심 작업에 집중시키는 필수 엔지니어링**입니다.
