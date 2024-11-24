"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0002 import SimpleUser


class ProjectsV2Item(GitHubModel):
    """Projects v2 Item

    An item belonging to a project
    """

    id: float = Field()
    node_id: Missing[str] = Field(default=UNSET)
    project_node_id: Missing[str] = Field(default=UNSET)
    content_node_id: str = Field()
    content_type: Literal["Issue", "PullRequest", "DraftIssue"] = Field(
        title="Projects v2 Item Content Type",
        description="The type of content tracked in a project item",
    )
    creator: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    created_at: datetime = Field()
    updated_at: datetime = Field()
    archived_at: Union[datetime, None] = Field()


model_rebuild(ProjectsV2Item)

__all__ = ("ProjectsV2Item",)
