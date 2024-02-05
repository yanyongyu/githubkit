"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0356 import SimpleInstallationType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType
from .group_0364 import PersonalAccessTokenRequestType


class WebhookPersonalAccessTokenRequestCreatedType(TypedDict):
    """personal_access_token_request created event"""

    action: Literal["created"]
    personal_access_token_request: PersonalAccessTokenRequestType
    organization: OrganizationSimpleWebhooksType
    sender: SimpleUserWebhooksType
    installation: SimpleInstallationType


__all__ = ("WebhookPersonalAccessTokenRequestCreatedType",)
