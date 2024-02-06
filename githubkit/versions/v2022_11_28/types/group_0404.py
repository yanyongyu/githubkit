"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookDeployKeyCreatedType(TypedDict):
    """deploy_key created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    key: WebhookDeployKeyCreatedPropKeyType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookDeployKeyCreatedPropKeyType(TypedDict):
    """WebhookDeployKeyCreatedPropKey

    The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-
    deploy-key) resource.
    """

    added_by: NotRequired[Union[str, None]]
    created_at: str
    id: int
    key: str
    last_used: NotRequired[Union[str, None]]
    read_only: bool
    title: str
    url: str
    verified: bool


__all__ = (
    "WebhookDeployKeyCreatedType",
    "WebhookDeployKeyCreatedPropKeyType",
)
