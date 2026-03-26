---
title: "Ollama v0.18.3, VS Code에서 무료 AI 코딩 — Copilot 구독 없이 로컬로 돌린다"
date: 2026-03-26
draft: false
categories:
  - Developer Tools
tags:
  - vscode
  - productivity
description: "Ollama v0.18.3이 VS Code 네이티브 통합을 지원합니다. 'ollama launch vscode' 한 줄이면 채팅 사이드바에서 Qwen3-Coder, DeepSeek, Gemma3를 무료로 쓸 수 있습니다. 설치 방법, 모델 선택 가이드, KV 캐시 공유 원리까지 정리합니다."
---

GitHub Copilot은 월 10달러, Cursor Pro는 월 20달러입니다. **Ollama v0.18.3**은 같은 일을 내 컴퓨터에서, VS Code 안에서, 구독료 0원으로 합니다.<br>
`ollama launch vscode` 명령어 한 줄이면 채팅 사이드바에서 Qwen3-Coder, DeepSeek, Gemma3 같은 오픈소스 모델을 바로 쓸 수 있습니다. 코드는 외부 서버로 나가지 않고, 인터넷이 끊겨도 동작합니다.

<!--more-->

## Sources

- https://managerkim.com/news/2026-03-26-ollama-0-18-3-vscode-free-ai-coding-local

---

## Ollama란 무엇인가

Ollama는 세계에서 가장 많이 쓰이는 **로컬 AI 실행 도구**입니다. LLM 모델을 내 컴퓨터에서 직접 실행할 수 있게 해줍니다.

| 지표 | 수치 |
|------|------|
| GitHub 스타 | 166,000개 |
| 월간 다운로드 | 5,200만 회 (2026년 1분기) |
| 연동 앱/서비스 | 40,000개 이상 (Claude Code, n8n, LangChain 등) |
| 가격 | 완전 무료 (오픈소스) |

기존에는 Ollama를 쓰려면 터미널에서 직접 대화해야 했습니다. 코딩 중에 터미널로 왔다 갔다 하는 것은 불편합니다. **v0.18.3부터는 VS Code 안에서 바로 Ollama 모델을 사용할 수 있습니다.**

```mermaid
flowchart TD
    A["기존 방식"]
    B["유료 AI 코딩 도구<br>Copilot $10/월, Cursor $20/월"]
    C["코드가 외부 서버로 전송"]
    D["인터넷 필수"]

    A2["v0.18.3 이후"]
    B2["Ollama + VS Code<br>완전 무료"]
    C2["코드가 내 컴퓨터 안에서만 처리"]
    D2["오프라인 동작 가능"]

    A --> B --> C --> D
    A2 --> B2 --> C2 --> D2

    classDef old fill:#ffc8c4,color:#333
    classDef new fill:#c0ecd3,color:#333
    class A,B,C,D old
    class A2,B2,C2,D2 new
```

---

## v0.18.3 핵심: VS Code 네이티브 통합

이번 업데이트의 핵심은 VS Code의 기본 모델 관리 기능에 Ollama가 직접 연결된다는 점입니다. 별도 확장 프로그램 없이도 채팅 사이드바에서 Ollama 모델을 선택하고 바로 사용할 수 있습니다.

```mermaid
flowchart TD
    A["VS Code 채팅 사이드바"]
    B["모델 드롭다운"]
    C["Manage Models 클릭"]
    D["Ollama 설치 모델 자동 표시"]
    E1["Gemma3 4B<br>(로컬)"]
    E2["Qwen3-Coder 30B<br>(로컬)"]
    E3["DeepSeek v3.1 671B<br>(Ollama 클라우드)"]
    F["코딩 질문 / 코드 리뷰<br>VS Code 안에서 바로"]

    A --> B --> C --> D
    D --> E1
    D --> E2
    D --> E3
    E1 --> F
    E2 --> F
    E3 --> F

    classDef ui fill:#c5dcef,color:#333
    classDef model fill:#e0c8ef,color:#333
    classDef action fill:#c0ecd3,color:#333
    class A,B,C,D ui
    class E1,E2,E3 model
    class F action
```

모델 드롭다운에서 Manage Models를 클릭하면 Ollama에서 내려받은 모델이 자동으로 표시됩니다. 원하는 모델을 체크하면 즉시 사용 가능합니다.

---

## 5분 안에 설정 완료하는 방법

시작하는 방법은 3단계입니다.

### 1단계 — Ollama 설치

Mac/Linux는 터미널에서 한 줄을 실행합니다. Windows는 [ollama.com](https://ollama.com)에서 설치 파일을 받습니다.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2단계 — AI 모델 다운로드

코딩용 모델을 하나 받아둡니다.

```bash
# 코딩 전문 모델 (30B, 약 18GB 저장공간 필요)
ollama pull qwen3-coder:30b

# 가벼운 범용 모델 (4B, 약 2.5GB 저장공간 필요)
ollama pull gemma3:4b
```

### 3단계 — VS Code에서 연결

```bash
ollama launch vscode
```

이 명령어 한 줄이면 VS Code가 열리면서 Ollama가 자동으로 연결됩니다. 수동으로 연결하려면 **채팅 사이드바 → 모델 드롭다운 → Manage Models → Provider: Ollama**를 선택합니다.

```mermaid
flowchart LR
    A["Ollama 설치<br>curl 한 줄"] --> B["모델 pull<br>gemma3:4b 등"]
    B --> C["ollama launch vscode<br>한 줄 실행"]
    C --> D["VS Code 채팅에서<br>AI 코딩 시작"]

    classDef step fill:#c5dcef,color:#333
    classDef done fill:#c0ecd3,color:#333
    class A,B,C step
    class D done
```

---

## 어떤 모델을 골라야 할까

용도와 RAM 사양에 따라 모델을 선택합니다.

```mermaid
flowchart TD
    Q["내 RAM은?"]
    Q --> R8["8GB"]
    Q --> R16["16GB 이상"]

    R8 --> M1["Gemma3 4B<br>용량 약 2.5GB<br>간단한 코드 설명, 버그 찾기,<br>함수 작성"]
    R16 --> M2["Qwen3-Coder 30B<br>용량 약 18GB<br>복잡한 로직 구현,<br>리팩토링, 테스트 코드"]
    R16 --> M3["DeepSeek v3.1 671B<br>Ollama 클라우드 사용<br>대규모 코드베이스 분석,<br>복잡한 아키텍처 설계"]

    classDef req fill:#fde8c0,color:#333
    classDef model fill:#c0ecd3,color:#333
    class Q,R8,R16 req
    class M1,M2,M3 model
```

**Gemma3 4B** — Google이 만든 오픈소스 모델. 8GB RAM이면 충분합니다. 입문용으로 가장 적합합니다.<br>
**Qwen3-Coder 30B** — 현재 오픈소스 코딩 모델 중 최상위 성능. 16GB RAM 이상 권장합니다. 복잡한 코드 작업에 적합합니다.<br>
**DeepSeek v3.1 671B** — 내 컴퓨터에서 직접 돌리기엔 너무 크지만, Ollama 클라우드를 통해 사용할 수 있습니다. 대규모 작업에 활용합니다.

---

## KV 캐시 공유: 연속 질문이 빨라지는 원리

v0.18.3의 또 다른 핵심 업데이트입니다. **KV(Key-Value) 캐시 공유**는 AI에게 같은 프로젝트에 대해 연속으로 질문할 때 이전 대화의 맥락을 재활용하는 기능입니다.

```mermaid
flowchart TD
    subgraph "KV 캐시 없는 경우 (이전)"
        A1["질문 1: 이 함수가 뭘 하는지 설명해줘"]
        B1["AI: 전체 코드 처음부터 처리"]
        C1["답변 생성"]
        D1["질문 2: 에러 처리를 추가해줘"]
        E1["AI: 전체 코드 다시 처음부터 처리"]
        F1["답변 생성 (느림)"]
        A1 --> B1 --> C1 --> D1 --> E1 --> F1
    end

    subgraph "KV 캐시 공유 (v0.18.3)"
        A2["질문 1: 이 함수가 뭘 하는지 설명해줘"]
        B2["AI: 전체 코드 처리 + 캐시 저장"]
        C2["답변 생성"]
        D2["질문 2: 에러 처리를 추가해줘"]
        E2["AI: 캐시에서 맥락 재활용"]
        F2["답변 생성 (빠름)"]
        A2 --> B2 --> C2 --> D2 --> E2 --> F2
    end

    classDef slow fill:#ffc8c4,color:#333
    classDef fast fill:#c0ecd3,color:#333
    class A1,B1,C1,D1,E1,F1 slow
    class A2,B2,C2,D2,E2,F2 fast
```

> "AI가 처음부터 다시 코드를 읽지 않고 이미 이해한 맥락 위에서 바로 답합니다. Apple Silicon(M1/M2/M3/M4) 맥북에서 특히 효과적입니다."

프로젝트가 클수록 이 성능 차이가 체감상 두드러집니다. 같은 파일에 대한 후속 질문을 반복하는 일반적인 코딩 작업에서 응답 속도가 눈에 띄게 향상됩니다.

---

## 더 강력하게: Continue 확장 프로그램

VS Code 기본 연동으로도 채팅 기반 코딩이 가능하지만, **Continue 확장 프로그램**을 설치하면 자동 코드 완성(탭 키로 제안 수락)까지 사용할 수 있습니다.

```mermaid
flowchart TD
    A["Ollama + VS Code 기본 연동"]
    B["Continue 확장 프로그램 추가"]

    A --> F1["채팅 기반 코딩 질문"]
    A --> F2["모델 선택 및 교체"]

    B --> G1["자동 코드 완성<br>(탭 키로 수락)"]
    B --> G2["@codebase: 프로젝트 전체 코드 검색"]
    B --> G3["@docs: 공식 문서 참조 답변"]
    B --> G4["모든 처리 로컬에서 완료"]

    classDef basic fill:#c5dcef,color:#333
    classDef advanced fill:#c0ecd3,color:#333
    class A,F1,F2 basic
    class B,G1,G2,G3,G4 advanced
```

Continue 설정 파일 예시입니다.

```json
{
  "models": [{
    "title": "Qwen3-Coder",
    "provider": "ollama",
    "model": "qwen3-coder:30b"
  }],
  "tabAutocompleteModel": {
    "title": "코드 자동 완성",
    "provider": "ollama",
    "model": "gemma3:4b"
  }
}
```

채팅(고품질 응답)과 자동 완성(빠른 응답)에 서로 다른 모델을 할당할 수 있습니다. 무거운 모델은 채팅에, 가벼운 모델은 실시간 자동 완성에 쓰는 방식이 실용적입니다.

---

## 핵심 요약

| 항목 | 내용 |
|------|------|
| **업데이트** | Ollama v0.18.3 — VS Code 네이티브 통합 |
| **핵심 명령어** | `ollama launch vscode` |
| **지원 모델** | Gemma3 4B, Qwen3-Coder 30B, DeepSeek v3.1 671B 등 |
| **최소 사양** | 8GB RAM (Gemma3 4B) / 16GB+ (Qwen3-Coder 30B) |
| **주요 신기능** | KV 캐시 공유 — 연속 질문 시 응답 속도 향상, Apple Silicon 특히 효과적 |
| **비용** | 완전 무료 |
| **보안** | 코드가 외부 서버로 나가지 않음, 오프라인 동작 가능 |
| **확장 옵션** | Continue 확장으로 자동 코드 완성, @codebase, @docs 지원 |

---

## 결론

Ollama v0.18.3은 "로컬 AI = 터미널만 가능"이라는 고정관념을 깼습니다.<br>
VS Code 채팅 사이드바에서 클릭 한 번으로 모델을 선택하고, `ollama launch vscode` 한 줄로 설정이 끝나는 경험은 유료 AI 코딩 도구와 실질적으로 차이가 없습니다.<br>
회사 코드 보안이 걱정되거나, AI 도구 구독료를 줄이고 싶거나, 오프라인 환경에서 코딩해야 한다면 — 지금 바로 시작해볼 수 있습니다.
