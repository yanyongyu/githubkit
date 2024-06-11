"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookCreateType(TypedDict):
    """create event"""

    description: Union[str, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    master_branch: str
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pusher_type: str
    ref: str
    ref_type: Literal["tag", "branch"]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookCreateType",)
