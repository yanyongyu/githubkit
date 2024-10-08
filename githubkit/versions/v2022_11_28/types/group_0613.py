"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0409 import WebhooksProjectCardType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookProjectCardEditedType(TypedDict):
    """project_card edited event"""

    action: Literal["edited"]
    changes: WebhookProjectCardEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhooksProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


class WebhookProjectCardEditedPropChangesType(TypedDict):
    """WebhookProjectCardEditedPropChanges"""

    note: WebhookProjectCardEditedPropChangesPropNoteType


class WebhookProjectCardEditedPropChangesPropNoteType(TypedDict):
    """WebhookProjectCardEditedPropChangesPropNote"""

    from_: Union[str, None]


__all__ = (
    "WebhookProjectCardEditedType",
    "WebhookProjectCardEditedPropChangesType",
    "WebhookProjectCardEditedPropChangesPropNoteType",
)
