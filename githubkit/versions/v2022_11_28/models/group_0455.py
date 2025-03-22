"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser


class ProjectsV2StatusUpdate(GitHubModel):
    """Projects v2 Status Update

    An status update belonging to a project
    """

    id: float = Field()
    node_id: str = Field()
    project_node_id: Missing[str] = Field(default=UNSET)
    creator: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    created_at: datetime = Field()
    updated_at: datetime = Field()
    status: Missing[
        Union[None, Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"]]
    ] = Field(default=UNSET)
    start_date: Missing[date] = Field(default=UNSET)
    target_date: Missing[date] = Field(default=UNSET)
    body: Missing[Union[str, None]] = Field(
        default=UNSET, description="Body of the status update"
    )


model_rebuild(ProjectsV2StatusUpdate)

__all__ = ("ProjectsV2StatusUpdate",)
