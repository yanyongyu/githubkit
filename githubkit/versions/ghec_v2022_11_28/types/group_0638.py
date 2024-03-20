"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict

from .group_0391 import SimpleInstallationType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0399 import PersonalAccessTokenRequestType


class WebhookPersonalAccessTokenRequestDeniedType(TypedDict):
    """personal_access_token_request denied event"""

    action: Literal["denied"]
    personal_access_token_request: PersonalAccessTokenRequestType
    organization: OrganizationSimpleWebhooksType
    sender: SimpleUserWebhooksType
    installation: SimpleInstallationType


__all__ = ("WebhookPersonalAccessTokenRequestDeniedType",)
