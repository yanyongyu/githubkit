"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0400 import SimpleInstallationType
from .group_0401 import OrganizationSimpleWebhooksType
from .group_0402 import RepositoryWebhooksType
from .group_0426 import MergeGroupType


class WebhookMergeGroupChecksRequestedType(TypedDict):
    """WebhookMergeGroupChecksRequested"""

    action: Literal["checks_requested"]
    installation: NotRequired[SimpleInstallationType]
    merge_group: MergeGroupType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookMergeGroupChecksRequestedType",)
