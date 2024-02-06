"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0005 import Integration


class UnlabeledIssueEvent(GitHubModel):
    """Unlabeled Issue Event

    Unlabeled Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["unlabeled"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    label: UnlabeledIssueEventPropLabel = Field()


class UnlabeledIssueEventPropLabel(GitHubModel):
    """UnlabeledIssueEventPropLabel"""

    name: str = Field()
    color: str = Field()


model_rebuild(UnlabeledIssueEvent)
model_rebuild(UnlabeledIssueEventPropLabel)

__all__ = (
    "UnlabeledIssueEvent",
    "UnlabeledIssueEventPropLabel",
)
