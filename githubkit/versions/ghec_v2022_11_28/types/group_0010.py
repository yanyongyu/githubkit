"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0008 import EnterpriseType
from .group_0009 import IntegrationPropPermissionsType


class IntegrationType(TypedDict):
    """GitHub app

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    id: int
    slug: NotRequired[str]
    node_id: str
    client_id: NotRequired[str]
    owner: Union[SimpleUserType, EnterpriseType]
    name: str
    description: Union[str, None]
    external_url: str
    html_url: str
    created_at: datetime
    updated_at: datetime
    permissions: IntegrationPropPermissionsType
    events: list[str]
    installations_count: NotRequired[int]


__all__ = ("IntegrationType",)
