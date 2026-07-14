# SolutionBlogAuto

## 프로젝트 소개

SolutionBlogAuto는 Hermes Worker 기반의 AI 블로그 자동화 프로젝트입니다.

AI가 하나의 주제를 입력받아

- 자료 조사
- 글 작성
- 이미지 생성
- Blogger 게시

까지 자동으로 수행하는 것을 목표로 합니다.

---

# 개발 목표

1차 목표

MVP를 빠르게 완성한다.

2차 목표

운영 가능한 수준으로 안정화한다.

3차 목표

Workflow를 확장하여 다양한 콘텐츠를 자동 생성한다.

---

# 개발 원칙

- 실행 가능한 코드 우선
- 작은 단위 개발
- Sprint 기반 개발
- 테스트 가능한 코드
- 유지보수 가능한 구조

---

# 프로젝트 구조

```
solution_blog_auto/

agents/

core/

services/

workflows/

tests/

docs/
```

---

# Workflow

Topic

↓

Research

↓

Writer

↓

Image

↓

Publisher

↓

Complete

---

# 실행

```
uv sync

uv run python main.py
```

---

# 테스트

```
uv run pytest
```

---

# 코드 스타일

```
uv run ruff check

uv run ruff format
```

---

# 브랜치 전략

main

항상 실행 가능한 상태를 유지한다.

---

# 개발 방식

ChatGPT

- CTO
- 설계
- 코드 리뷰

Codex

- 구현
- 테스트
- 리팩토링

---

# 라이선스

Private Project

---

## Sprint 3B OpenRouter MVP

Set the OpenRouter provider in `.env` before running the MVP workflow.

```
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your-openrouter-api-key
OPENROUTER_MODEL=deepseek/deepseek-chat-v3-0324:free
```

The workflow returns its result without printing. `main.py` prints the topic,
research result, and final Markdown article.
