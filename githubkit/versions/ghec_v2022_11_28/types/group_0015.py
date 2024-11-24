"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0014 import EnterpriseType


class IntegrationInstallationRequestType(TypedDict):
    """Integration Installation Request

    Request to install an integration on a target
    """

    id: int
    node_id: NotRequired[str]
    account: Union[SimpleUserType, EnterpriseType]
    requester: SimpleUserType
    created_at: datetime


__all__ = ("IntegrationInstallationRequestType",)
