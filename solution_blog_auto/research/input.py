from dataclasses import dataclass


@dataclass
class ResearchInput:
    """Research 수행에 필요한 입력 정보를 묶은 객체.

    블로그 글 작성을 위해 ResearchAgent에 전달되는 구조화된 입력.
    Research 입력을 하나의 객체로 통합하여 Prompt 생성에 사용한다.
    """

    topic: str
    purpose: str
    audience: str
    content_direction: str
    must_include: list[str]
    avoid: list[str]
