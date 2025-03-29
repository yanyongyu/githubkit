"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0068 import CopilotSeatDetailsType


class EnterprisesEnterpriseCopilotBillingSeatsGetResponse200Type(TypedDict):
    """EnterprisesEnterpriseCopilotBillingSeatsGetResponse200"""

    total_seats: NotRequired[int]
    seats: NotRequired[list[CopilotSeatDetailsType]]


__all__ = ("EnterprisesEnterpriseCopilotBillingSeatsGetResponse200Type",)
