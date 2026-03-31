---
title: "이슈 트래킹은 죽었다: 바이브코딩 시대, 기획서 대신 프로토타입"
date: 2026-03-31T00:00:00+09:00
draft: false
categories:
  - Engineering
tags:
  - vibe-coding
  - workflow
  - agents
description: "Linear CEO가 '이슈 트래킹은 죽었다'고 선언했습니다. 기획서 3일 쓰는 대신 프로토타입 3일 만드는 게 왜 더 나은지, 그리고 AI 시대 개발 프로세스는 어떻게 바뀌어야 하는지 분석합니다."
---

회사에서 앱 하나를 만든다고 할 때, 제일 먼저 뭘 하시나요? 기획서를 쓰시나요, 아니면 바로 코드를 짜시나요? 지금까지 정답은 당연히 기획서였습니다. 그런데 불과 며칠 전, 이 당연한 방식에 정면으로 도전하는 선언이 나왔습니다.

> [프로젝트 관리 도구 Linear의 CEO가 "이슈 트래킹은 죽었다"고 선언했습니다.](https://youtu.be/dZG3-9lKpIA?t=0)

기획서 쓰고 티켓 만들고 상태 관리하는 그 프로세스 자체가 개발을 느리게 만든다는 겁니다. 이 주장이 맞는지, 그렇다면 뭘로 바꿔야 하는지 분석합니다.

<!--more-->

## Sources

- https://youtu.be/dZG3-9lKpIA

---

## Linear의 선언: 이슈 트래킹은 죽었다

[2026년 3월 25일, Linear가 Linear Agents를 출시하며 충격적인 수치를 공개했습니다.](https://youtu.be/dZG3-9lKpIA?t=50)

- 기업 워크스페이스의 **75% 이상**이 이미 AI 에이전트를 사용 중
- 새로운 이슈의 **25%를 AI가 직접 생성**

```mermaid
flowchart TD
    Linear[Linear CEO 선언<br/>2026-03-25] --> A[이슈 트래킹은 죽었다]
    Linear --> B[Linear Agents 출시]
    B --> C[기업 워크스페이스 75%+<br/>이미 AI 에이전트 사용]
    B --> D[새 이슈의 25%<br/>AI가 직접 생성]

    A --> E[왜?]
    E --> F[전통 프로세스가<br/>개발을 느리게 만든다]

    classDef announceStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef statStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef questionStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    class Linear,A announceStyle
    class C,D statStyle
    class E,F questionStyle
```

발표 자체보다 더 중요한 것은 그 뒤에 깔린 본질적인 질문입니다. **왜 이런 변화가 필요한가?**

---

## 진짜 문제: 관리에 최적화된 도구

[전통적인 프로젝트 관리 도구들은 만드는 것이 아니라 관리에 최적화되어 있습니다.](https://youtu.be/dZG3-9lKpIA?t=80) Jira가 나쁜 도구라는 게 아닙니다. 20년 넘게 살아남은 이유가 있습니다. 하지만 핵심 문제가 있습니다.

### 개발자의 하루 재현

[5명짜리 백엔드 개발자 팀을 상상해 봅시다.](https://youtu.be/dZG3-9lKpIA?t=100)

```mermaid
sequenceDiagram
    participant Dev as 개발자
    participant Jira as Jira
    participant Slack as Slack
    participant Git as GitHub

    Note over Dev: 09:00 출근, 코드 짜려 함
    Dev->>Jira: 오늘 티켓 확인
    Jira-->>Dev: 로딩 3초 + 보드 로딩
    Dev->>Jira: 티켓 클릭
    Jira-->>Dev: 로딩 + "사용자 인증 개선"만 적혀 있음
    Dev->>Slack: PM에게 질문
    Slack-->>Dev: 아직 출근 안 함. 대기 중...
    Jira-->>Dev: 알림 - 리뷰 요청 수신
    Dev->>Jira: PR 링크 찾기
    Dev->>Git: 리뷰 완료
    Dev->>Jira: 상태 변경 클릭
    Jira-->>Dev: 드롭다운 12개<br/>In Review? In Repo? QA? QA In Progress?
    Note over Dev: 10:00 - 코드 한 줄도 못 짬
```

이게 과장이 아닙니다. 실제로 많은 개발 팀에서 매일 벌어지는 일입니다.

### 관리 비용의 실제 수치

[숫자로 따져 보면 더 심각합니다.](https://youtu.be/dZG3-9lKpIA?t=170)

| 항목 | 낭비 시간 |
|---|---|
| PM 티켓 1개 작성 | 15~30분 |
| 스프린트 30개 티켓 | PM 하루 전체 |
| 알림 후 집중력 복구 | 평균 **23분** |
| 주당 스프린트/백로그/스탠드업 미팅 | **8시간** |
| 미팅 중 "이 티켓 무슨 뜻이야?" | 미팅 시간의 절반 |
| **실제 코딩 시간** | **하루 4시간 미만** |

```mermaid
flowchart TD
    Day[개발자 하루 8시간] --> Code[실제 코딩<br/>4시간 미만 🔴]
    Day --> Process[프로세스 관리<br/>4시간 이상 🟡]
    Process --> P1[Jira 확인 & 상태 변경]
    Process --> P2[미팅 참여]
    Process --> P3[알림 대응 & 집중력 복구]
    Process --> P4[컨텍스트 스위칭]

    classDef codeStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef processStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef detailStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    class Code codeStyle
    class Process processStyle
    class P1,P2,P3,P4 detailStyle
```

Linear가 Jira보다 인기를 얻은 건 이 관리 비용을 극단적으로 줄였기 때문입니다. 하지만 Linear가 아무리 빠르더라도, 근본적인 문제는 해결하지 못합니다. **진짜 문제는 도구가 아니라 그 위에서 돌아가는 프로세스**에 있기 때문입니다.

---

## 기획서의 본질적 한계

[기획서는 왜 필요했을까요?](https://youtu.be/dZG3-9lKpIA?t=250) PM은 비즈니스 관점을, 디자이너는 사용자 경험을, 개발자는 기술적 가능성을 압니다. 이 세 사람의 머릿속을 맞추려면 공유 문서가 필요합니다. 여기까지는 맞습니다.

하지만 기획서에는 구조적 한계가 있습니다.

> **"기획서를 쓰는 사람은 실제로 만들어 본 적이 없으니까요. 기획서에는 아는 것만 적을 수 있어요. 모르는 것은 적을 수가 없습니다."**

### 프로필 사진 업로드 기능 예시

[간단해 보이는 기능 하나를 분석해 봅시다.](https://youtu.be/dZG3-9lKpIA?t=290)

**기획서에 적힌 것:**
```
JPG, PNG, 외부 파일 지원
최대 5MB
200×200 자동 크롭
사진 30일 보관 후 삭제
```

**기획서로 알 수 없는 것들:**

```mermaid
flowchart TD
    Spec[기획서 완성] --> Q1{크롭은 자동?<br/>사용자 선택?}
    Spec --> Q2{모바일에서도<br/>같은 방식?}
    Spec --> Q3{최대 5MB가<br/>실제로 합리적인가?}

    Q1 --> A1[답: 이틀 뒤...]
    Q2 --> A2[답: 이틀 뒤...]
    Q3 --> Problem[아이폰 16 기본 사진<br/>6~8MB ‼️]
    Problem --> Fail[사용자 10명 중<br/>7명이 첫 시도 실패]

    classDef specStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef questionStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef failStyle fill:#ffc8c4,stroke:#e05050,color:#333
    class Spec specStyle
    class Q1,Q2,Q3 questionStyle
    class Problem,Fail,A1,A2 failStyle
```

[아이폰 16의 기본 사진 용량은 6~8MB입니다.](https://youtu.be/dZG3-9lKpIA?t=290) 기획서에 5MB라고 적어도 현실에서 사용자 10명 중 7명이 첫 시도에서 실패합니다. **이걸 기획서 단계에서 알 수 있었을까요? 절대 불가능합니다. 만들어 봐야 아는 거예요.**

---

## 해결책: 기획서 3일 → 프로토타입 3일

[같은 기능을 프로토타입 접근으로 바꾸면 이렇게 됩니다.](https://youtu.be/dZG3-9lKpIA?t=330)

```mermaid
flowchart TD
    subgraph spec["📄 기획서 접근 (3일)"]
        S1[1일차: JPG/PNG 스펙 작성]
        S2[2일차: 5MB/크롭/보관 정책]
        S3[3일차: 문서 리뷰 & 승인]
        S1 --> S2 --> S3
        S3 --> SW[코드 0줄<br/>+ 질문 응답 대기 이틀]
    end

    subgraph proto["⚡ 프로토타입 접근 (3일)"]
        P1[1일차: 업로드 API + 버튼 연결]
        P2[2일차: 크롭 UI 붙이기]
        P3[3일차: 보관 로직 구현]
        D1[발견: 아이폰 사진 6MB<br/>→ 서버 리사이즈 필요]
        D2[발견: 200×200 너무 작음<br/>→ 핀치 줌 > 드래그]
        D3[발견: 스케줄러, 삭제 알림,<br/>용량 정책 필요]
        P1 --> D1 --> P2 --> D2 --> P3 --> D3
        P3 --> PW[동작하는 결과물<br/>+ 숨은 문제 5~6개 해결]
    end

    classDef specItemStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef protoItemStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef discoverStyle fill:#fde8c0,stroke:#e6a817,color:#333
    class S1,S2,S3,SW specItemStyle
    class P1,P2,P3,PW protoItemStyle
    class D1,D2,D3 discoverStyle
```

**비유:** 기획서로 제품 만드는 건 레시피만 읽고 요리를 평가하는 것과 같습니다. 짠지 싱거운지는 먹어봐야 알듯, 소프트웨어도 만들어봐야 압니다.

### 왜 지금 이게 가능한가?

[이 접근이 가능한 이유는 프로토타입 비용이 거의 제로에 수렴했기 때문입니다.](https://youtu.be/dZG3-9lKpIA?t=410)

> "AI 코딩 도구에게 이미지 업로드 프로토타입 만들어 달라고 프롬프팅하면 **30분 내에 동작하는 코드**가 나오는 시대입니다. 프로토타입 비용이 거의 제로인 시대에 기획서를 3일 쓰는 건 시대착오예요."

```mermaid
flowchart TD
    OldCost[과거 프로토타입 비용] --> High[높음<br/>개발자 수일 필요]
    NewCost[현재 프로토타입 비용] --> Zero[거의 제로<br/>AI 코딩 도구 30분]

    High --> OldRatio[기획서 > 프로토타입<br/>기획서가 합리적]
    Zero --> NewRatio[기획서 << 프로토타입 가치<br/>프로토타입이 합리적]

    NewRatio --> Conclusion[기획서 3일 = 시대착오]

    classDef oldStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef newStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef conclusionStyle fill:#fde8c0,stroke:#e6a817,color:#333
    class OldCost,High,OldRatio oldStyle
    class NewCost,Zero,NewRatio newStyle
    class Conclusion conclusionStyle
```

---

## 기획서가 여전히 필요한 경우

[프로토타입 우선 방식이 모든 상황의 답은 아닙니다.](https://youtu.be/dZG3-9lKpIA?t=460)

```mermaid
flowchart TD
    Q{어떤 상황인가?}

    Q --> A[이해관계자 다수<br/>법적 문서화 필수<br/>금융/의료 산업<br/>대규모 비동기 팀]
    Q --> B[5~10명 이하 팀<br/>에이전트 코딩 가능한<br/>개발자 있음<br/>빠른 반복 필요]

    A --> Doc[문서 필수<br/>기획서 유지]
    B --> Proto[80% 이상<br/>프로토타입으로 대체 가능]

    classDef docStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef protoStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    classDef qStyle fill:#fde8c0,stroke:#e6a817,color:#333
    class Q qStyle
    class A,Doc docStyle
    class B,Proto protoStyle
```

**조건:** 팀 내에 에이전트 코딩에 익숙한 개발자가 있을 때 가능합니다. 기획서를 아예 없애라는 뜻이 아닙니다.

---

## AI 시대 사람의 역할

[AI가 기획, 코딩, 테스트를 모두 한다면 사람은 뭘 하나?](https://youtu.be/dZG3-9lKpIA?t=490) PM·디자이너·프론트·백엔드·QA라는 직군 분류가 존재하는 이유는 **인간의 인지 한계** 때문에 분업한 것입니다. AI는 그 한계가 없습니다.

사람의 역할은 세 가지로 압축됩니다.

```mermaid
flowchart TD
    Human[사람의 핵심 역할] --> Intent[의도<br/>우리 제품을 어떤 방향으로<br/>가져갈 것인가?<br/>시장 이해 + 사용자 관찰]
    Human --> Judgment[판단<br/>이 기능을 지금 만들 건지 말 건지<br/>무엇을 하고 무엇을 안 할지<br/>경험과 직관 필요]
    Human --> Taste[취향<br/>이 버튼이 여기 있는 게 맞나?<br/>이 애니메이션이 자연스러운가?<br/>미세한 품질 차이 감지]

    Intent --> Role[실행자 → 의사결정자]
    Judgment --> Role
    Taste --> Role

    classDef humanStyle fill:#c5dcef,stroke:#4a90d9,color:#333
    classDef roleStyle fill:#fde8c0,stroke:#e6a817,color:#333
    classDef resultStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class Human humanStyle
    class Intent,Judgment,Taste roleStyle
    class Role resultStyle
```

> "코드를 짜는 사람이 아니라, 어떤 코드를 짤 건지 방향을 잡는 사람."

---

## 리스크: 균형 있게 보기

[변화에는 리스크도 있습니다.](https://youtu.be/dZG3-9lKpIA?t=530) 세 가지를 짚어야 합니다.

```mermaid
flowchart TD
    Risks[리스크] --> R1[AI 에이전트 보안<br/>Linear Agents가 코드 읽고<br/>수정까지 하는데<br/>프롬프트 인젝션 취약점<br/>아직 불투명]
    Risks --> R2[기록의 부재<br/>프로토타입 중심으로 가면<br/>의사결정 히스토리 유실<br/>"왜 이렇게 만들었더라?"<br/>2개월 뒤 알 수 없음]
    Risks --> R3[팀 적합성 한계<br/>금융/의료 등 규제 산업<br/>문서화가 법적 의무<br/>프로토타입 우선 불가]

    R1 --> M1[업계 전체가<br/>풀어야 할 숙제]
    R2 --> M2[핵심 결정은<br/>어딘가 반드시 기록]
    R3 --> M3[산업별 판단 필요]

    classDef riskStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef mitigateStyle fill:#fde8c0,stroke:#e6a817,color:#333
    class Risks,R1,R2,R3 riskStyle
    class M1,M2,M3 mitigateStyle
```

---

## 기획서의 새로운 형태: plan.md

[기획서가 완전히 사라지는 것이 아닙니다.](https://youtu.be/dZG3-9lKpIA?t=600) 형태가 바뀌는 것입니다.

> "기획이란 에이전트에게 알려줄 **plan.md 파일을 함께 만들어 나가는 것**이 기획서의 역할이 되게 될 겁니다."

```mermaid
flowchart TD
    subgraph old["📄 기존 기획서"]
        O1[PM이 혼자 작성]
        O2[개발자에게 넘김]
        O3[티켓으로 분해]
        O4[상태 관리 & 미팅]
        O1 --> O2 --> O3 --> O4
    end

    subgraph new["⚡ 새로운 plan.md"]
        N1[팀이 함께 작성]
        N2[AI 에이전트가 읽음]
        N3[프로토타입으로 검증]
        N4[실시간 업데이트]
        N1 --> N2 --> N3 --> N4 --> N1
    end

    classDef oldStyle fill:#ffc8c4,stroke:#e05050,color:#333
    classDef newStyle fill:#c0ecd3,stroke:#3aaa6c,color:#333
    class O1,O2,O3,O4 oldStyle
    class N1,N2,N3,N4 newStyle
```

이슈 트래킹이 완전히 사라지진 않겠지만, **사람이 일일이 티켓 만들고 상태 바꾸고 미팅하는 시대는 끝나가고 있습니다.**

---

## 핵심 요약

```mermaid
mindmap
  root((바이브코딩 시대<br/>개발 프로세스 변혁))
    문제
      Jira 관리 비용
      코딩 4시간 미만
      기획서 한계
      알 수 없는 걸 글로 해결
    해결
      프로토타입 우선
      30분 AI 프로토타이핑
      plan.md로 전환
    변화
      이슈 트래킹 자동화
      사람 역할 변화
      의도·판단·취향
    리스크
      AI 보안
      기록 부재
      팀 적합성
```

| 항목 | 기존 방식 | 새로운 방식 |
|---|---|---|
| 시작점 | 기획서(PRD) | 프로토타입 |
| 티켓 생성 | PM이 30분씩 | AI가 자동 생성 |
| 프로세스 도구 | Jira (관리 최적화) | 프로토타입 중심 |
| 기획서 형태 | 긴 문서 | plan.md (에이전트용) |
| 사람 역할 | 실행자 | 의사결정자 |
| 발견 시점 | 배포 후 | 1일차부터 |

---

## 결론

Linear CEO의 선언은 단순한 도구 교체 이야기가 아닙니다. 개발 프로세스의 근본적인 패러다임 전환입니다.

기존 프로젝트 관리 도구들은 만드는 것보다 관리하는 데 시간을 더 쓰게 만들었습니다. 기획서는 유용하지만 만들어봐야 발견할 수 있는 문제들을 미리 글로 해결하려 했습니다. 프로토타입 비용이 거의 제로에 수렴한 지금, 방식을 바꿔야 합니다.

기획서 10페이지 쓰는 대신 AI에게 30분 만에 프로토타입을 뽑아보고 그걸 보면서 판단하는 시대가 왔습니다. 우리는 대비해야 합니다.
