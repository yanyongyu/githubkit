"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict

from .group_0003 import SimpleUserType
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType
from .group_0474 import RepositoryWebhooksType


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


WebhookRepositoryDispatchSamplePropClientPayloadType: TypeAlias = dict[str, Any]
"""WebhookRepositoryDispatchSamplePropClientPayload

The `client_payload` that was specified in the `POST
/repos/{owner}/{repo}/dispatches` request body.
"""


__all__ = (
    "WebhookRepositoryDispatchSamplePropClientPayloadType",
    "WebhookRepositoryDispatchSampleType",
)
