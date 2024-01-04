"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0005 import Integration


class AddedToProjectIssueEvent(GitHubModel):
    """Added to Project Issue Event

    Added to Project Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["added_to_project"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    project_card: Missing[AddedToProjectIssueEventPropProjectCard] = Field(
        default=UNSET
    )


class AddedToProjectIssueEventPropProjectCard(GitHubModel):
    """AddedToProjectIssueEventPropProjectCard"""

    id: int = Field()
    url: str = Field()
    project_id: int = Field()
    project_url: str = Field()
    column_name: str = Field()
    previous_column_name: Missing[str] = Field(default=UNSET)


model_rebuild(AddedToProjectIssueEvent)
model_rebuild(AddedToProjectIssueEventPropProjectCard)

__all__ = (
    "AddedToProjectIssueEvent",
    "AddedToProjectIssueEventPropProjectCard",
)
