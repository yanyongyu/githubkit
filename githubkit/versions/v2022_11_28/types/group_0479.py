"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0418 import SimpleInstallationType
from .group_0419 import OrganizationSimpleWebhooksType
from .group_0420 import RepositoryWebhooksType
from .group_0423 import CheckRunWithSimpleCheckSuiteType


class WebhookCheckRunRerequestedType(TypedDict):
    """Check Run Re-Requested Event"""

    action: Literal["rerequested"]
    check_run: CheckRunWithSimpleCheckSuiteType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookCheckRunRerequestedType",)
