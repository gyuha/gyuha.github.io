---
title: "한국 주식 MCP 서버: API 키 없는 무료 KOSPI·KOSDAQ 데이터 커넥터 분석"
date: 2026-08-11T08:00:00+09:00
draft: false
categories:
  - AI
tags:
  - mcp
  - open-source
  - llm
  - claude-code
  - stocks
description: "DART나 증권사 API 키 발급 없이 Claude 및 ChatGPT에 주소 하나로 연결되는 한국 주식 MCP 서버(com.aikstockdata/mcp)의 기능과 12개 주요 도구를 분석합니다."
---

Claude 및 ChatGPT와 같은 대형 언어 모델(LLM)에 Model Context Protocol(MCP) 커넥터를 붙여 실시간 인공지능 주식 분석 환경을 만드는 개발 사례가 크게 늘고 있습니다. 하지만 기존 한국 주식 MCP 구현체들은 대다수 한국투자증권 Open API나 금융감독원 OpenDART 사용자 발급 키를 필수로 요구하여 최초 설정 장벽이 높았습니다.

공개 서비스인 **한국주식데이터 MCP 서버**(`com.aikstockdata/mcp`)는 별도의 API 키, 회원가입, 복잡한 인증 헤더 없이 단 하나의 엔드포인트 URL 등록으로 국내 KOSPI·KOSDAQ 1,463개 종목의 데이터 조회를 지원하는 무료 커넥터입니다.

<!--more-->

## Sources

- [한국주식데이터 AI / MCP 공식 안내페이지](https://aikstockdata.com/ai)
- [공식 MCP 레지스트리 Entry](https://mcp.aikstockdata.com/mcp)

## 1. 주요 핵심 차별점

### 회원가입 및 API 키 제로 (Zero Credentials)
한국투자증권이나 OpenDART API 키를 개별적으로 발급받을 필요가 없으며, CORS가 오픈된 Streamable HTTP 백엔드로 서빙되어 URL 한 줄 등록만으로 즉시 작동합니다.

### DART 공시의 접수 시각(HH:MM) 자체 수집 및 분리
OpenDART 표준 API가 제공하는 공시 정보는 날짜(`YYYYMMDD`)까지만 포함되어 있어 장중에 나온 공시인지 장 마감 후에 나온 공시인지 구별이 불가능했습니다. 한국주식데이터 MCP는 최근공시 타임라인을 매 거래일 자체 수집하여 **장중 공시(즉시 반영)**와 **장후 공시(다음 날 반영)**를 명확히 구분합니다.

### 빠른 잠정 실적 캡처
정기 보고서(분기·반기·사업보고서) 제출보다 약 2주 빠르게 공개되는 **기업 잠정 실적** 데이터를 우선 반영하여 실적 모멘텀 조회의 즉시성을 높였습니다.

## 2. 제공되는 12개 주요 MCP 도구 (Tools)

| 도구 이름 | 제공 기능 설명 |
|---|---|
| `get_today` | 오늘의 시장 지수, 등락 폭, 주요 공시 및 성장 랭킹 종합 요약 |
| `search_stock` | 종목명 한글 부분일치 검색 |
| `get_stock` | 특정 종목의 시세, 분기/잠정 실적, 랭킹 신호 상세 조회 |
| `list_stocks` | 흑자전환, 52주 신고/신저가, 시총/영업이익 배수 등 조건 검색 |
| `get_earnings` | 잠정 실적 포함 신속 실적 데이터 조회 |
| `get_history` | 250거래일 일별 시세 + 고점 대비 낙폭 + 거래량 배수 조회 |
| `get_disclosure_impact` | 공시 유형별 발표 이후 주가 반응 통계 제공 |
| `get_disclosures` | HH:MM 접수 시각 및 장 구분이 들어간 공시 타임라인 조회 |
| `get_earnings_calendar` | 기업 실적 발표 캘린더 및 마감 D-day 정보 |

## 3. 원클릭 연결 및 설정 방법

**Claude Code / CLI 연동:**
```bash
claude mcp add --transport http aikstockdata https://mcp.aikstockdata.com/mcp
```

**MCP JSON 설정 파일 방식:**
```json
{
  "mcpServers": {
    "aikstockdata": {
      "type": "http",
      "url": "https://mcp.aikstockdata.com/mcp"
    }
  }
}
```

**Claude & ChatGPT GUI 설정:**
* **Claude 웹/앱**: 설정 → 커넥터 → 커스텀 커넥터 추가 → URL 등록 (`https://mcp.aikstockdata.com/mcp`)
* **ChatGPT**: 설정 → 커넥터 → 개발자 모드 → 커넥터 만들기 → URL 등록 (인증 '없음' 선택)

개인 개발자 및 AI 파이낸스 에이전트 구축 시 신속하고 유용한 오픈소스 주식 데이터 커넥터로 활용도가 높습니다.
