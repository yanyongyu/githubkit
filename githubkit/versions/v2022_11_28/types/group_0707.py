"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0096 import FullRepositoryType
from .group_0367 import EnterpriseWebhooksType
from .group_0368 import SimpleInstallationType
from .group_0371 import SimpleUserWebhooksType
from .group_0369 import OrganizationSimpleWebhooksType
from .group_0708 import WebhookSecurityAndAnalysisPropChangesType


class WebhookSecurityAndAnalysisType(TypedDict):
    """security_and_analysis event"""

    changes: WebhookSecurityAndAnalysisPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: FullRepositoryType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookSecurityAndAnalysisType",)
