"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0385 import EnterpriseWebhooksType
from .group_0386 import SimpleInstallationType
from .group_0387 import OrganizationSimpleWebhooksType
from .group_0388 import RepositoryWebhooksType
from .group_0500 import WebhookForkPropForkeeType


class WebhookForkType(TypedDict):
    """fork event

    A user forks a repository.
    """

    enterprise: NotRequired[EnterpriseWebhooksType]
    forkee: WebhookForkPropForkeeType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookForkType",)
