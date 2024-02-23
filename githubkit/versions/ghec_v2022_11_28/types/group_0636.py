"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict

from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0393 import SimpleUserWebhooksType
from .group_0398 import PersonalAccessTokenRequestType


class WebhookPersonalAccessTokenRequestCreatedType(TypedDict):
    """personal_access_token_request created event"""

    action: Literal["created"]
    personal_access_token_request: PersonalAccessTokenRequestType
    organization: OrganizationSimpleWebhooksType
    sender: SimpleUserWebhooksType
    installation: SimpleInstallationType


__all__ = ("WebhookPersonalAccessTokenRequestCreatedType",)
