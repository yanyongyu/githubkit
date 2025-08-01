"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0487 import EnterpriseWebhooksType
from .group_0488 import SimpleInstallationType
from .group_0489 import OrganizationSimpleWebhooksType
from .group_0490 import RepositoryWebhooksType


class WebhookGollumType(TypedDict):
    """gollum event"""

    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pages: list[WebhookGollumPropPagesItemsType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookGollumPropPagesItemsType(TypedDict):
    """WebhookGollumPropPagesItems"""

    action: Literal["created", "edited"]
    html_url: str
    page_name: str
    sha: str
    summary: Union[str, None]
    title: str


__all__ = (
    "WebhookGollumPropPagesItemsType",
    "WebhookGollumType",
)
