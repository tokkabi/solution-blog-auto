from solution_blog_auto.research.input import ResearchInput


def test_research_input_creates_with_all_fields() -> None:
    """ResearchInput should store all provided field values."""
    research_input = ResearchInput(
        topic="ETF란 무엇인가?",
        purpose="블로그 글 작성을 위한 핵심 정보 조사",
        audience="일반 독자",
        content_direction="정확하고 이해하기 쉬운 정보 중심",
        must_include=["정의", "장단점"],
        avoid=["전문 용어 남용"],
    )

    assert research_input.topic == "ETF란 무엇인가?"
    assert research_input.purpose == "블로그 글 작성을 위한 핵심 정보 조사"
    assert research_input.audience == "일반 독자"
    assert research_input.content_direction == "정확하고 이해하기 쉬운 정보 중심"
    assert research_input.must_include == ["정의", "장단점"]
    assert research_input.avoid == ["전문 용어 남용"]


def test_research_input_allows_empty_lists() -> None:
    """ResearchInput should allow empty must_include and avoid lists."""
    research_input = ResearchInput(
        topic="주제",
        purpose="목적",
        audience="독자",
        content_direction="방향",
        must_include=[],
        avoid=[],
    )

    assert research_input.must_include == []
    assert research_input.avoid == []
