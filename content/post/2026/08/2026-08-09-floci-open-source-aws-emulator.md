---
title: "Floci: 유료 제한 없는 오픈소스 로컬 AWS 에뮬레이터 구조 분석"
date: 2026-08-09T08:37:00+09:00
draft: false
categories:
  - Infrastructure
tags:
  - open-source
  - aws
  - devops
  - testing
  - docker
description: "AWS 계정, 유료 플랜, 기능 제한 없이 로컬에서 Lambda, RDS, ECS, EKS 등 AWS 인프라를 실행할 수 있는 오픈소스 에뮬레이터 Floci의 특징과 도입 방법을 분석합니다."
---

클라우드 기반 애플리케이션을 개발하고 CI/CD 테스트 파이프라인을 구축할 때, 실제 AWS 환경에 매번 리소스를 배포하거나 유료 에뮬레이터 플랜에 의존하는 것은 비용과 속도 측면에서 부담이 됩니다.

**Floci**(`floci-io/floci`)는 AWS 계정, 인증 토큰, 유료 라이선스 제약 없이 단일 로컬 엔드포인트에서 AWS 인프라 서비스를 에뮬레이트해 주는 오픈소스 로컬 AWS 환경 제공 도구(LocalStack 대안)입니다.

<!--more-->

## Sources

- [Floci GitHub 저장소](https://github.com/floci-io/floci)
- [Floci 공식 문서](https://floci.io/floci/)
- [Floci CLI 저장소](https://github.com/floci-io/floci-cli)

## 1. Floci의 등장 배경

기존 로컬 AWS 에뮬레이터 환경에서는 일부 고도화된 기능(예: 고급 서버리스, 복잡한 인프라 서비스)을 사용하기 위해 유료 티어 가입이 필요하거나, 단순 껍데기 흉내(Shallow Mock)만 제공하여 테스트 신뢰도가 떨어지는 문제점이 존재했습니다.

Floci는 이러한 결제 및 라이선스 장벽을 제거하고, `docker compose up` 또는 단순 CLI 명령어만으로 팀 내 모든 개발자가 완전한 로컬 AWS 인프라 환경을 구축할 수 있도록 지원합니다.

## 2. 주요 핵심 특징 및 장점

### 유료 기능 제약 없는 완전 오픈소스 (Always Free)
* 별도의 AWS 클라우드 계정 생성이나 인증 토큰 등록 없이 실행됩니다.
* 특정 기능에 유료 락(Feature Gate)을 걸지 않고 모든 호환 서비스를 오픈소스로 제공합니다.

### 실제 Docker 기반 정밀 재현 (High-Fidelity)
* 단순 텍스트 흉내를 넘어 **Lambda, RDS, ElastiCache, MSK, ECS, EC2, EKS, OpenSearch, CodeBuild** 등 정밀도가 중요한 서비스들을 실제 Docker 컨테이너 기반으로 독립 실행합니다.

### 기존 AWS 도구 100% 드롭인 호환
* 표준 엔드포인트 `http://localhost:4566`를 기본으로 제공합니다.
* 기존에 사용하던 **AWS CLI, AWS SDK, Terraform, AWS CDK, OpenTofu, Testcontainers** 코드를 변경 없이 환경 변수 및 엔드포인트 지정만으로 사용할 수 있습니다.

### CI/CD에 최적화된 경량화
* 네이티브 이미지를 기반으로 밀리초(ms) 단위의 빠른 시작 속도를 제공하며 유휴 메모리 점유율을 대폭 줄여 파이프라인 실행 시간을 단축합니다.

## 3. 빠른 시작 가이드

**전용 CLI 사용 시:**
```bash
# Floci 시작 및 환경 변수 자동 설정
floci start
eval $(floci env)

# 표준 AWS CLI 사용
aws s3 mb s3://my-bucket
aws dynamodb list-tables
```

**Docker Compose 설정 (`compose.yaml`):**
```yaml
services:
  floci:
    image: floci/floci:latest
    ports:
      - "4566:4566"
```

AWS 기반 애플리케이션 개발 시 클라우드 비용을 절감하고 독립적인 로컬 integration 테스트 환경을 구축하려는 팀에게 매우 유용한 최신 오픈소스 프로젝트입니다.
