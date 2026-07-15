from typing import TypedDict


class BlogState(TypedDict, total=False):
    """State shared by the blog workflow nodes."""

    topic: str
    research: str
    contract_name: str
    article: str
    publish_result: str
