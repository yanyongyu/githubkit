"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0427 import EnterpriseWebhooksType
from .group_0428 import SimpleInstallationType
from .group_0430 import RepositoryWebhooksType
from .group_0429 import OrganizationSimpleWebhooksType


class WebhookRepositoryDispatchSampleType(TypedDict):
    """repository_dispatch event"""

    action: str
    branch: str
    client_payload: Union[WebhookRepositoryDispatchSamplePropClientPayloadType, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: SimpleInstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryDispatchSamplePropClientPayloadType(TypedDict):
    """WebhookRepositoryDispatchSamplePropClientPayload

    The `client_payload` that was specified in the `POST
    /repos/{owner}/{repo}/dispatches` request body.
    """


__all__ = (
    "WebhookRepositoryDispatchSampleType",
    "WebhookRepositoryDispatchSamplePropClientPayloadType",
)
