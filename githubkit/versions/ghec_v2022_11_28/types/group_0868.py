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


class WebhookWorkflowDispatchType(TypedDict):
    """workflow_dispatch event"""

    enterprise: NotRequired[EnterpriseWebhooksType]
    inputs: Union[WebhookWorkflowDispatchPropInputsType, None]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    ref: str
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow: str


WebhookWorkflowDispatchPropInputsType: TypeAlias = dict[str, Any]
"""WebhookWorkflowDispatchPropInputs
"""


__all__ = (
    "WebhookWorkflowDispatchPropInputsType",
    "WebhookWorkflowDispatchType",
)
