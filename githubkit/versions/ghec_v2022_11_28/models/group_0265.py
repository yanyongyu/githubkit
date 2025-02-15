"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0055 import CodeScanningAnalysisTool
from .group_0056 import CodeScanningAlertInstance


class CodeScanningAlert(GitHubModel):
    """CodeScanningAlert"""

    number: int = Field(description="The security alert number.")
    created_at: datetime = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    updated_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    url: str = Field(description="The REST API URL of the alert resource.")
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    instances_url: str = Field(
        description="The REST API URL for fetching the list of instances for an alert."
    )
    state: Union[None, Literal["open", "dismissed", "fixed"]] = Field(
        description="State of a code scanning alert."
    )
    fixed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_by: Union[None, SimpleUser] = Field()
    dismissed_at: Union[datetime, None] = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ] = Field(
        description="**Required when the state is dismissed.** The reason for dismissing or closing the alert."
    )
    dismissed_comment: Missing[Union[Annotated[str, Field(max_length=280)], None]] = (
        Field(
            default=UNSET,
            description="The dismissal comment associated with the dismissal of the alert.",
        )
    )
    rule: CodeScanningAlertRule = Field()
    tool: CodeScanningAnalysisTool = Field()
    most_recent_instance: CodeScanningAlertInstance = Field()
    dismissal_approved_by: Missing[Union[None, SimpleUser]] = Field(default=UNSET)


class CodeScanningAlertRule(GitHubModel):
    """CodeScanningAlertRule"""

    id: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="A unique identifier for the rule used to detect the alert.",
    )
    name: Missing[str] = Field(
        default=UNSET, description="The name of the rule used to detect the alert."
    )
    severity: Missing[Union[None, Literal["none", "note", "warning", "error"]]] = Field(
        default=UNSET, description="The severity of the alert."
    )
    security_severity_level: Missing[
        Union[None, Literal["low", "medium", "high", "critical"]]
    ] = Field(default=UNSET, description="The security severity of the alert.")
    description: Missing[str] = Field(
        default=UNSET,
        description="A short description of the rule used to detect the alert.",
    )
    full_description: Missing[str] = Field(
        default=UNSET, description="A description of the rule used to detect the alert."
    )
    tags: Missing[Union[list[str], None]] = Field(
        default=UNSET, description="A set of tags applicable for the rule."
    )
    help_: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="help",
        description="Detailed documentation for the rule as GitHub Flavored Markdown.",
    )
    help_uri: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="A link to the documentation for the rule used to detect the alert.",
    )


model_rebuild(CodeScanningAlert)
model_rebuild(CodeScanningAlertRule)

__all__ = (
    "CodeScanningAlert",
    "CodeScanningAlertRule",
)
