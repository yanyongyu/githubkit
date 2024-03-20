"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0245 import DependabotAlertPropDependency
from .group_0049 import DependabotAlertSecurityAdvisory
from .group_0048 import DependabotAlertSecurityVulnerability


class DependabotAlert(GitHubModel):
    """DependabotAlert

    A Dependabot alert.
    """

    number: int = Field(description="The security alert number.")
    state: Literal["auto_dismissed", "dismissed", "fixed", "open"] = Field(
        description="The state of the Dependabot alert."
    )
    dependency: DependabotAlertPropDependency = Field(
        description="Details for the vulnerable dependency."
    )
    security_advisory: DependabotAlertSecurityAdvisory = Field(
        description="Details for the GitHub Security Advisory."
    )
    security_vulnerability: DependabotAlertSecurityVulnerability = Field(
        description="Details pertaining to one vulnerable version range for the advisory."
    )
    url: str = Field(description="The REST API URL of the alert resource.")
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    created_at: datetime = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    updated_at: datetime = Field(
        description="The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_at: Union[datetime, None] = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_by: Union[None, SimpleUser] = Field()
    dismissed_reason: Union[
        None,
        Literal[
            "fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"
        ],
    ] = Field(description="The reason that the alert was dismissed.")
    dismissed_comment: Union[Annotated[str, Field(max_length=280)], None] = Field(
        description="An optional comment associated with the alert's dismissal."
    )
    fixed_at: Union[datetime, None] = Field(
        description="The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    auto_dismissed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )


model_rebuild(DependabotAlert)

__all__ = ("DependabotAlert",)