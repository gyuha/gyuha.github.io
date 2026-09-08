---
title: "Blender MCP 연동 가이드: ChatGPT와 Claude로 3D 모델링 직접 제어하기"
date: 2026-09-09T08:30:00+09:00
draft: false
categories:
  - Developer Tools
tags:
  - mcp
  - ai
  - workflow
description: "복잡한 파이썬 스크립트 없이 Blender 애드온 ZIP 설치와 ChatGPT 앱 연동으로 자연어 프롬프트를 통해 3D 메시 생성, 머티리얼 수정, 씬 제어를 자동화하는 실전 가이드를 정리합니다."
---

3D 모델링 도구인 블렌더(Blender)는 방대한 기능만큼이나 초보자에게 가파른 학습 곡선을 요구합니다. 최근 LLM의 함수 호출(Tool Calling)과 **MCP(Model Context Protocol)** 가 발전하면서, 복잡한 3D 뷰포트 조작과 파이썬 스크립트 작성 없이 **자연어 프롬프트만으로 블렌더 씬을 직접 구축하고 수정** 하는 작업이 현실화되었습니다.

`@geekknowit` 님이 공유한 **Blender MCP 연동 가이드** 는 복잡한 터미널 환경 설정 없이, **단일 ZIP 애드온 파일 설치로 Blender와 ChatGPT 데스크톱 앱을 스트리밍 HTTP(SSE)로 연결** 하는 가장 직관적인 실전 워크플로우를 제시합니다.

<!--more-->

## Sources

- [Threads 원문 포스트: geekknowit](https://www.threads.com/share/BADOEUhNh8/)
- [GitHub 저장소: emeryporter/blender-mcp](https://github.com/emeryporter/blender-mcp)
- [대안 오픈소스: ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)

---

## 1. Blender MCP 동작 구조

```mermaid
flowchart TD
    classDef clientNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef mcpNode fill:#e0c8ef,stroke:#6b46c1,stroke-width:1.5px,color:#333;
    classDef toolNode fill:#fde8c0,stroke:#d69e2e,stroke-width:1.5px,color:#333;
    classDef blendNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    User["사용자 자연어 프롬프트<br>('테이블 위에 빨간 세라믹 머그잔 생성해줘')"] --> LLM["ChatGPT 데스크톱 / Claude"]
    LLM --> Protocol["MCP 스트리밍 HTTP (SSE 연결)<br>http://localhost:8000"]
    Protocol --> Server["Blender MCP 서버 (Add-on 내장)"]

    Server --> T1["86개 3D 특화 도구 실행<br>(지오메트리, 재질, 조명, 모디파이어)"]
    T1 --> Blender["Blender 3D 뷰포트 실시간 렌더링"]

    class User,LLM clientNode;
    class Protocol,Server mcpNode;
    class T1 toolNode;
    class Blender blendNode;
```

---

## 2. 초간단 7단계 설치 및 연동 워크플로우

```mermaid
flowchart TD
    classDef stepNode fill:#c5dcef,stroke:#2b6cb0,stroke-width:1.5px,color:#333;
    classDef actionNode fill:#c0ecd3,stroke:#38a169,stroke-width:1.5px,color:#333;

    Step1["1. blender_mcp.zip 릴리즈 다운로드"] --> Step2["2. Blender 설정 -> Add-ons -> Install from Disk"]
    Step2 --> Step3["3. N키 패널에서 'Start Server' 클릭 (포트 확인)"]
    Step3 --> Step4["4. ChatGPT 앱 설정 -> 플러그인 / 개발자 -> Add MCP"]
    Step4 --> Step5["5. 스트리밍 HTTP 선택 후 로컬 주소 입력 및 저장"]
    Step5 --> Step6["6. 연결 활성화 확인 및 프롬프트 명령 시작"]

    class Step1,Step2,Step3 stepNode;
    class Step4,Step5,Step6 actionNode;
```

1. **ZIP 다운로드**: `emeryporter/blender-mcp` 릴리즈 페이지에서 `blender_mcp.zip` 을 내려받습니다.
2. **블렌더 애드온 등록**: Blender 메뉴의 `Edit` ➔ `Preferences` ➔ `Add-ons` 우측 상단 `Install from Disk` 를 눌러 ZIP 파일을 선택하고 체크박스를 활성화합니다.
3. **로컬 서버 기동**: 3D 뷰포트에서 `N` 키를 눌러 사이드 패널을 열거나 설정 화면에서 **`Start Server`** 를 누르고 로컬 HTTP 주소(예: `http://localhost:8000`)를 확인합니다.
4. **ChatGPT 앱 연동**: ChatGPT 데스크톱 앱의 `설정` ➔ `플러그인 / 개발자 도구` ➔ `Add MCP Server` 를 클릭합니다.
5. **엔드포인트 등록**: Server Type을 `스트리밍 가능한 HTTP(SSE)` 로 선택하고, 이름과 로컬 URL을 입력해 저장합니다.
6. **프롬프트 입력**: 연동 완료 후 모델에게 명령을 전달합니다.

---

## 3. 실전 사용 시 주의점과 꿀팁

* **MCP 서버 이름 명시하기**:
  * ChatGPT 앱에 지시할 때 *"Blender MCP를 사용해서 원뿔형 탑을 세우고 금속 재질을 입혀줘"* 처럼 **서버 명칭을 명시적으로 언급** 해야 합니다.
  * 서버 이름을 생략하면 모델이 MCP 도구 대신 `Computer Use` 기능(화면 마우스 클릭 자동화)을 시도할 수 있습니다.
* **풍부한 3D 도구군**:
  * 단순 스크립트 실행뿐만 아니라 씬 계층(Scene Hierarchy) 탐색, 메시 변형, 유니티(Unity) 엔진 호환성 검증 등 86개 이상의 정교한 API를 지원합니다.
