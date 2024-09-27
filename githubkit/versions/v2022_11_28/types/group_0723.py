"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0102 import FullRepositoryType
from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType
from .group_0724 import WebhookSecurityAndAnalysisPropChangesType


class WebhookSecurityAndAnalysisType(TypedDict):
    """security_and_analysis event"""

    changes: WebhookSecurityAndAnalysisPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: FullRepositoryType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookSecurityAndAnalysisType",)
