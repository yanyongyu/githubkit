"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild


class CopilotOrganizationDetails(ExtraGitHubModel):
    """Copilot Business Organization Details

    Information about the seat breakdown and policies set for an organization with a
    Copilot Business subscription.
    """

    seat_breakdown: CopilotSeatBreakdown = Field(
        title="Copilot Business Seat Breakdown",
        description="The breakdown of Copilot Business seats for the organization.",
    )
    public_code_suggestions: Literal[
        "allow", "block", "unconfigured", "unknown"
    ] = Field(
        description="The organization policy for allowing or disallowing Copilot to make suggestions that match public code."
    )
    ide_chat: Missing[Literal["enabled", "disabled", "unconfigured"]] = Field(
        default=UNSET,
        description="The organization policy for allowing or disallowing organization members to use Copilot Chat within their editor.",
    )
    platform_chat: Missing[Literal["enabled", "disabled", "unconfigured"]] = Field(
        default=UNSET,
        description="The organization policy for allowing or disallowing organization members to use Copilot features within github.com.",
    )
    cli: Missing[Literal["enabled", "disabled", "unconfigured"]] = Field(
        default=UNSET,
        description="The organization policy for allowing or disallowing organization members to use Copilot within their CLI.",
    )
    seat_management_setting: Literal[
        "assign_all", "assign_selected", "disabled", "unconfigured"
    ] = Field(description="The mode of assigning new seats.")


class CopilotSeatBreakdown(GitHubModel):
    """Copilot Business Seat Breakdown

    The breakdown of Copilot Business seats for the organization.
    """

    total: Missing[int] = Field(
        default=UNSET,
        description="The total number of seats being billed for the organization as of the current billing cycle.",
    )
    added_this_cycle: Missing[int] = Field(
        default=UNSET, description="Seats added during the current billing cycle."
    )
    pending_cancellation: Missing[int] = Field(
        default=UNSET,
        description="The number of seats that are pending cancellation at the end of the current billing cycle.",
    )
    pending_invitation: Missing[int] = Field(
        default=UNSET,
        description="The number of seats that have been assigned to users that have not yet accepted an invitation to this organization.",
    )
    active_this_cycle: Missing[int] = Field(
        default=UNSET,
        description="The number of seats that have used Copilot during the current billing cycle.",
    )
    inactive_this_cycle: Missing[int] = Field(
        default=UNSET,
        description="The number of seats that have not used Copilot during the current billing cycle.",
    )


model_rebuild(CopilotOrganizationDetails)
model_rebuild(CopilotSeatBreakdown)

__all__ = (
    "CopilotOrganizationDetails",
    "CopilotSeatBreakdown",
)
