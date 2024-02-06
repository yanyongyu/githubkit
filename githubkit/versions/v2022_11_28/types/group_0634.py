"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0365 import ProjectsV2Type
from .group_0356 import SimpleInstallationType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ProjectReopenedType(TypedDict):
    """Projects v2 Project Reopened Event"""

    action: Literal["reopened"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2: ProjectsV2Type
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectsV2ProjectReopenedType",)
