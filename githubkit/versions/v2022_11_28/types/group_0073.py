"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class CopilotOrganizationDetailsType(TypedDict):
    """Copilot Business Organization Details

    Information about the seat breakdown and policies set for an organization with a
    Copilot Business subscription.
    """

    seat_breakdown: CopilotSeatBreakdownType
    public_code_suggestions: Literal["allow", "block", "unconfigured", "unknown"]
    ide_chat: NotRequired[Literal["enabled", "disabled", "unconfigured"]]
    platform_chat: NotRequired[Literal["enabled", "disabled", "unconfigured"]]
    cli: NotRequired[Literal["enabled", "disabled", "unconfigured"]]
    seat_management_setting: Literal[
        "assign_all", "assign_selected", "disabled", "unconfigured"
    ]


class CopilotSeatBreakdownType(TypedDict):
    """Copilot Business Seat Breakdown

    The breakdown of Copilot Business seats for the organization.
    """

    total: NotRequired[int]
    added_this_cycle: NotRequired[int]
    pending_cancellation: NotRequired[int]
    pending_invitation: NotRequired[int]
    active_this_cycle: NotRequired[int]
    inactive_this_cycle: NotRequired[int]


__all__ = (
    "CopilotOrganizationDetailsType",
    "CopilotSeatBreakdownType",
)
