"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0006 import IntegrationPropPermissions


class Integration(GitHubModel):
    """GitHub app

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    id: int = Field(description="Unique identifier of the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    node_id: str = Field()
    owner: Union[None, SimpleUser] = Field()
    name: str = Field(description="The name of the GitHub app")
    description: Union[str, None] = Field()
    external_url: str = Field()
    html_url: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    permissions: IntegrationPropPermissions = Field(
        description="The set of permissions for the GitHub app"
    )
    events: List[str] = Field(description="The list of events for the GitHub app")
    installations_count: Missing[int] = Field(
        default=UNSET,
        description="The number of installations associated with the GitHub app",
    )
    client_id: Missing[str] = Field(default=UNSET)
    client_secret: Missing[str] = Field(default=UNSET)
    webhook_secret: Missing[Union[str, None]] = Field(default=UNSET)
    pem: Missing[str] = Field(default=UNSET)


model_rebuild(Integration)

__all__ = ("Integration",)
