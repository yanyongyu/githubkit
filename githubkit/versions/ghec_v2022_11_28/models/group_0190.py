"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0020 import Repository


class Migration(GitHubModel):
    """Migration

    A migration.
    """

    id: int = Field()
    owner: Union[None, SimpleUser] = Field()
    guid: str = Field()
    state: str = Field()
    lock_repositories: bool = Field()
    exclude_metadata: bool = Field()
    exclude_git_data: bool = Field()
    exclude_attachments: bool = Field()
    exclude_releases: bool = Field()
    exclude_owner_projects: bool = Field()
    org_metadata_only: bool = Field()
    repositories: list[Repository] = Field(
        description="The repositories included in the migration. Only returned for export migrations."
    )
    url: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    node_id: str = Field()
    archive_url: Missing[str] = Field(default=UNSET)
    exclude: Missing[list[str]] = Field(
        default=UNSET,
        description='Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: `"repositories"`.',
    )


model_rebuild(Migration)

__all__ = ("Migration",)
