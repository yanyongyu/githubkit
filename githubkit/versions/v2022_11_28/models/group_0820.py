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
from .group_0008 import Enterprise
from .group_0009 import IntegrationPropPermissions


class AppManifestsCodeConversionsPostResponse201(GitHubModel):
    """AppManifestsCodeConversionsPostResponse201"""

    id: int = Field(description="Unique identifier of the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    node_id: str = Field()
    client_id: str = Field()
    owner: Union[SimpleUser, Enterprise] = Field()
    name: str = Field(description="The name of the GitHub app")
    description: Union[str, None] = Field()
    external_url: str = Field()
    html_url: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    permissions: IntegrationPropPermissions = Field(
        description="The set of permissions for the GitHub app"
    )
    events: list[str] = Field(description="The list of events for the GitHub app")
    installations_count: Missing[int] = Field(
        default=UNSET,
        description="The number of installations associated with the GitHub app",
    )
    client_secret: str = Field()
    webhook_secret: Union[Union[str, None], None] = Field()
    pem: str = Field()


model_rebuild(AppManifestsCodeConversionsPostResponse201)

__all__ = ("AppManifestsCodeConversionsPostResponse201",)
