"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0154 import MinimalRepository


class Thread(GitHubModel):
    """Thread

    Thread
    """

    id: str = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    subject: ThreadPropSubject = Field()
    reason: str = Field()
    unread: bool = Field()
    updated_at: str = Field()
    last_read_at: Union[str, None] = Field()
    url: str = Field()
    subscription_url: str = Field()


class ThreadPropSubject(GitHubModel):
    """ThreadPropSubject"""

    title: str = Field()
    url: str = Field()
    latest_comment_url: str = Field()
    type: str = Field()


model_rebuild(Thread)
model_rebuild(ThreadPropSubject)

__all__ = (
    "Thread",
    "ThreadPropSubject",
)
