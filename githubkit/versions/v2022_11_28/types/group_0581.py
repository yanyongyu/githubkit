"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0406 import MergeGroupType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookMergeGroupChecksRequestedType(TypedDict):
    """WebhookMergeGroupChecksRequested"""

    action: Literal["checks_requested"]
    installation: NotRequired[SimpleInstallationType]
    merge_group: MergeGroupType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookMergeGroupChecksRequestedType",)
