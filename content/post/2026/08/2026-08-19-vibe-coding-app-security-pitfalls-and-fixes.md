---
title: "AI로 만든 앱이 털릴 수밖에 없는 이유: Vibe Coding 시 놓치기 쉬운 9가지 보안 취약점과 방어 수칙"
date: 2026-08-19T12:30:00+09:00
draft: false
categories:
  - Security
tags:
  - security
  - vibe-coding
  - supabase
  - api-keys
  - web-dev
description: "Claude, Cursor, v0 등으로 빠르게 웹/앱을 개발(Vibe Coding)할 때 프론트엔드와 Supabase 데이터베이스에서 가장 빈번하게 발생하는 9대 보안 취약점과 실전 방어 수칙을 정리합니다."
---

Claude Code, Cursor, v0, Bolt 등 바이브 코딩(Vibe Coding) 도구 덕분에 비개발자나 1인 창업자도 단 며칠 만에 완전한 웹 서비스를 만들어 배포할 수 있게 되었습니다. 

하지만 AI는 기능 구현 코드를 완벽하게 짜줄 수는 있어도, **키 관리와 데이터베이스 접근 제어 같은 인프라 보안 설정**까지 알아서 챙겨주지는 않습니다. 이로 인해 서비스 출시 직후 API 키가 털려 수백만 원의 요금이 청구되거나 데이터베이스 전체가 유출되는 사고가 빈번하게 발생하고 있습니다.

AI로 앱을 개발할 때 반드시 점검해야 할 **API 키와 데이터베이스(Supabase/Firebase) 9대 핵심 보안 수칙**을 정리합니다.

<!--more-->

## Sources

- [원문 유튜브 영상: AI로 만든 앱이 털릴 수 밖에 없는 이유](https://youtu.be/UzsLfQjpXJw)
- [Supabase 공식 RLS(Row Level Security) 보안 가이드](https://supabase.com/docs/guides/database/postgres/row-level-security)

---

## 1. API 키 보안 5대 수칙

1. **`.env` 파일 격리 및 `.gitignore` 등록**:
   * 환경 변수 파일(`.env`)이 GitHub 공개 저장소에 푸시되지 않도록 `.gitignore`에 반드시 포함해야 합니다.
2. **프론트엔드(클라이언트) 코드에 시크릿 키 노출 금지**:
   * Next.js의 `NEXT_PUBLIC_` 접두사나 React 클라이언트 컴포넌트에 OpenAI, Stripe, Replicate의 시크릿 키를 하드코딩하면, 브라우저 개발자 도구(F12)에서 누구나 탈취할 수 있습니다.
   * 모든 민감한 API 호출은 백엔드 API Route나 Server Action에서 처리해야 합니다.
3. **AI 채팅창에 실제 API 키 입력 금지**:
   * ChatGPT나 Claude에게 코드 디버깅을 요청할 때 실제 키 값을 그대로 복사하지 말고, 반드시 더미 값(`sk-xxxx`)으로 치환하여 질문합니다.
4. **유출된 키는 즉시 폐기(Revoke) 및 재발급**:
   * 실수로 커밋된 키는 git 기록을 덮어쓰는 것만으로 안전하지 않습니다. 즉시 제공사 콘솔에서 키를 삭제하고 재생성해야 합니다.
5. **최소 권한 원칙(Least Privilege)과 유효기간 관리**:
   * API 키에 불필요한 전체 관리자 권한을 주지 말고, 필요한 기능에만 한정된 스코프를 부여합니다.

---

## 2. 데이터베이스 & 스토리지 보안 4대 수칙 (Supabase 등)

6. **RLS (Row Level Security, 행 단위 보안) 필수 활성화**:
   * Supabase에서 RLS를 켜지 않으면, 퍼블릭에 공개되는 익명(anon) 키만으로도 악의적인 사용자가 DB 전체 테이블을 쿼리하거나 삭제할 수 있습니다.
7. **Service Role (관리자) 키 노출 절대 금지**:
   * RLS를 완전히 무시하고 모든 데이터에 접근할 수 있는 `service_role` 마스터 키는 절대 브라우저(클라이언트) 코드에 들어가서는 안 되며, 보안된 서버 백엔드 환경에서만 사용해야 합니다.
8. **RLS 정책(Policy)의 정밀한 작성**:
   * 테이블에 RLS를 활성화한 뒤 `true`(모두 허용) 조건으로 대충 열어두지 말고, `auth.uid() = user_id`와 같이 로그인한 사용자 본인의 데이터만 CRUD 할 수 있도록 엄격한 정책을 수립합니다.
9. **파일 스토리지(Storage) 버킷 공개 범위 점검**:
   * 사용자 개인정보, 신분증, 영수증이 저장되는 스토리지 버킷을 Public으로 설정하지 말고, 서명된 URL(Signed URL)이나 RLS가 적용된 Private 버킷으로 보호합니다.
