"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0358 import SimpleInstallationType
from .group_0359 import OrganizationSimpleWebhooksType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0365 import MergeGroupType


class WebhookMergeGroupChecksRequestedType(TypedDict):
    """WebhookMergeGroupChecksRequested"""

    action: Literal["checks_requested"]
    installation: NotRequired[SimpleInstallationType]
    merge_group: MergeGroupType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookMergeGroupChecksRequestedType",)
