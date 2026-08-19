---
title: "ScrapeGraphAI: LLM과 유향 그래프(Graph) 기반 차세대 Python 웹 스크래핑 라이브러리 분석"
date: 2026-08-19T22:05:00+09:00
draft: false
categories:
  - AI
tags:
  - open-source
  - python
  - web-scraping
  - llm
  - graph-engineering
description: "CSS/XPath 셀렉터 작성 없이 자연어 프롬프트와 유향 그래프 파이프라인으로 웹페이지, 검색 결과, 로컬 문서를 구조화된 JSON 데이터로 자동 추출하는 ScrapeGraphAI의 구조와 핵심 활용법을 분석합니다."
---

웹 스크래핑과 데이터 파이프라인 구축에서 개발자들을 가장 괴롭히는 문제는 **"웹사이트 UI와 DOM 구조의 빈번한 변경"**입니다. 아무리 정교하게 작성한 BeautifulSoup이나 Selenium 코드라도 클래스명이나 레이아웃이 조금만 바뀌면 CSS/XPath 셀렉터가 깨져 전체 파이프라인이 중단되곤 합니다.

**ScrapeGraphAI**(`Scrapegraph-ai`)는 대형 언어 모델(LLM)의 문맥 이해 능력과 유향 비순환 그래프(DAG) 기반의 **직접 그래프 논리(Direct Graph Logic)**를 결합하여, **자연어 프롬프트 지시만으로 웹페이지 및 로컬 문서에서 구조화된 데이터를 무설정(Zero-Config)으로 추출**하는 오픈소스 Python 라이브러리입니다.

<!--more-->

## Sources

- [ScrapeGraphAI GitHub 공식 저장소](https://github.com/ScrapeGraphAI/Scrapegraph-ai)
- [ScrapeGraphAI 공식 기술 문서](https://docs.scrapegraphai.com/)

---

## 1. ScrapeGraphAI의 핵심 차별점

* **CSS/XPath 셀렉터 없는 자연어 추출**:  
  복잡한 태그 경로를 파싱할 필요 없이 *"이 페이지에서 제품명, 가격, 할인율, 재고 여부를 JSON으로 뽑아줘"*라고 프롬프트를 주면 LLM이 페이지 전체 맥락을 분석해 정확한 데이터를 추출합니다.
* **레이아웃 변화에 대한 자가 적응(Self-Adapting)**:  
  웹사이트의 HTML 구조나 클래스명이 바뀌어도 LLM이 의미론적으로 내용을 파악하므로 스크래퍼 코드를 수정할 필요가 없습니다.
* **로컬 LLM (Ollama) 완벽 지원**:  
  OpenAI, Gemini, Claude, Groq 등 상용 API뿐만 아니라, **Ollama**를 통해 Llama 3, Qwen, DeepSeek 등 로컬 오픈소스 모델을 무료 및 완벽한 보안 환경에서 가동할 수 있습니다.

---

## 2. 모듈형 그래프(Graph) 아키텍처

ScrapeGraphAI는 스크래핑 요구사항에 맞춘 4가지 사전 정의된 그래프 파이프라인을 제공합니다:

1. **`SmartScraperGraph`**: 단일 웹페이지 URL에서 프롬프트에 맞춰 정확한 JSON 스키마를 추출하는 기본 그래프.
2. **`SearchGraph`**: 구글/덕덕고 등 검색 엔진에서 키워드를 검색하고 상위 N개 페이지를 자동으로 탐색하여 취합하는 멀티 페이지 그래프.
3. **`OmniScraperGraph`**: 복잡한 조건 분기와 다단계 뎁스(Depth) 크롤링을 처리하는 고급 그래프.
4. **`SpeechGraph`**: 스크랩한 웹 데이터를 요약하여 즉시 음성(TTS) 오디오 파일로 생성해 주는 파이프라인.

---

## 3. 실전 사용 코드 예시

```python
from scrapegraphai.graphs import SmartScraperGraph

# 그래프 설정 (OpenAI, Gemini 또는 Ollama 로컬 모델 지정)
graph_config = {
    "llm": {
        "model": "openai/gpt-4o-mini",
        "api_key": "YOUR_API_KEY",
    },
    "verbose": True,
    "headless": True,
}

# 스마트 스크래퍼 생성 및 실행
smart_scraper = SmartScraperGraph(
    prompt="모든 프로젝트의 이름과 설명을 JSON 배열 형태로 추출해 줘.",
    source="https://example.com/projects",
    config=graph_config
)

result = smart_scraper.run()
print(result)
```

Playwright 기반의 동적 JavaScript(SPA) 렌더링과 프록시 로테이션까지 지원하여, 복잡한 웹 데이터 수집 파이프라인을 단 몇 줄의 코드로 구축할 수 있습니다.
