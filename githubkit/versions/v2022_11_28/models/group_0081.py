"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0080 import Team


class CampaignSummary(GitHubModel):
    """Campaign summary

    The campaign metadata and alert stats.
    """

    number: int = Field(description="The number of the newly created campaign")
    created_at: datetime = Field(
        description="The date and time the campaign was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    updated_at: datetime = Field(
        description="The date and time the campaign was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    name: Missing[str] = Field(default=UNSET, description="The campaign name")
    description: str = Field(description="The campaign description")
    managers: list[SimpleUser] = Field(description="The campaign managers")
    team_managers: Missing[list[Team]] = Field(
        default=UNSET, description="The campaign team managers"
    )
    published_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time the campaign was published, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ.",
    )
    ends_at: datetime = Field(
        description="The date and time the campaign has ended, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    closed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The date and time the campaign was closed, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. Will be null if the campaign is still open.",
    )
    state: Literal["open", "closed"] = Field(
        title="Campaign state",
        description="Indicates whether a campaign is open or closed",
    )
    contact_link: Union[str, None] = Field(
        description="The contact link of the campaign."
    )
    alert_stats: Missing[CampaignSummaryPropAlertStats] = Field(default=UNSET)


class CampaignSummaryPropAlertStats(GitHubModel):
    """CampaignSummaryPropAlertStats"""

    open_count: int = Field(description="The number of open alerts")
    closed_count: int = Field(description="The number of closed alerts")
    in_progress_count: int = Field(description="The number of in-progress alerts")


model_rebuild(CampaignSummary)
model_rebuild(CampaignSummaryPropAlertStats)

__all__ = (
    "CampaignSummary",
    "CampaignSummaryPropAlertStats",
)
