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

from .group_0476 import ExemptionResponse


class ExemptionRequest(GitHubModel):
    """Exemption Request

    A request from a user to be exempted from a set of rules.
    """

    id: Missing[int] = Field(
        default=UNSET, description="The ID of the exemption request."
    )
    number: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="The number uniquely identifying the exemption request within it's repository.",
    )
    repository_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the repository the exemption request is for.",
    )
    requester_id: Missing[int] = Field(
        default=UNSET, description="The ID of the user who requested the exemption."
    )
    requester_login: Missing[str] = Field(
        default=UNSET, description="The login of the user who requested the exemption."
    )
    request_type: Missing[
        Literal[
            "push_ruleset_bypass",
            "secret_scanning",
            "secret_scanning_closure",
            "code_scanning_alert_dismissal",
        ]
    ] = Field(default=UNSET, description="The type of request.")
    exemption_request_data: Missing[
        Union[
            ExemptionRequestPushRulesetBypass,
            ExemptionRequestSecretScanning,
            DismissalRequestSecretScanning,
            DismissalRequestCodeScanning,
        ]
    ] = Field(default=UNSET)
    resource_identifier: Missing[str] = Field(
        default=UNSET,
        description="The unique identifier for the request type of the exemption request. For example, a commit SHA.",
    )
    status: Missing[Literal["pending", "rejected", "cancelled", "completed"]] = Field(
        default=UNSET, description="The status of the exemption request."
    )
    requester_comment: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The comment the requester provided when creating the exemption request.",
    )
    metadata: Missing[
        Union[
            ExemptionRequestSecretScanningMetadata,
            DismissalRequestSecretScanningMetadata,
            DismissalRequestCodeScanningMetadata,
            None,
        ]
    ] = Field(default=UNSET, description="Metadata about the exemption request.")
    expires_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time the exemption request will expire.",
    )
    created_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time the exemption request was created.",
    )
    responses: Missing[Union[list[ExemptionResponse], None]] = Field(
        default=UNSET, description="The responses to the exemption request."
    )
    html_url: Missing[str] = Field(
        default=UNSET, description="The URL to view the exemption request in a browser."
    )


class ExemptionRequestSecretScanningMetadata(GitHubModel):
    """Secret Scanning Push Protection Exemption Request Metadata

    Metadata for a secret scanning push protection exemption request.
    """

    label: Missing[str] = Field(
        default=UNSET, description="The label for the secret type"
    )
    reason: Missing[Literal["fixed_later", "false_positive", "tests"]] = Field(
        default=UNSET, description="The reason for the exemption request"
    )


class DismissalRequestSecretScanningMetadata(GitHubModel):
    """Secret scanning alert dismissal request metadata

    Metadata for a secret scanning alert dismissal request.
    """

    alert_title: Missing[str] = Field(
        default=UNSET, description="The title of the secret alert"
    )
    reason: Missing[Literal["fixed_later", "false_positive", "tests", "revoked"]] = (
        Field(default=UNSET, description="The reason for the dismissal request")
    )


class DismissalRequestCodeScanningMetadata(GitHubModel):
    """Code scanning alert dismissal request metadata

    Metadata for a code scanning alert dismissal request.
    """

    alert_title: Missing[str] = Field(
        default=UNSET, description="The title of the code scanning alert"
    )
    reason: Missing[Literal["false positive", "won't fix", "used in tests"]] = Field(
        default=UNSET, description="The reason for the dismissal request"
    )


class ExemptionRequestPushRulesetBypass(GitHubModel):
    """Push ruleset bypass exemption request data

    Push rules that are being requested to be bypassed.
    """

    type: Missing[Literal["push_ruleset_bypass"]] = Field(
        default=UNSET, description="The type of request"
    )
    data: Missing[list[ExemptionRequestPushRulesetBypassPropDataItems]] = Field(
        default=UNSET,
        description="The data pertaining to the push rules that are being requested to be bypassed.",
    )


class ExemptionRequestPushRulesetBypassPropDataItems(GitHubModel):
    """ExemptionRequestPushRulesetBypassPropDataItems"""

    ruleset_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the ruleset for the rules that were violated",
    )
    ruleset_name: Missing[str] = Field(
        default=UNSET,
        description="The name of the ruleset for the rules that were violated",
    )
    total_violations: Missing[int] = Field(
        default=UNSET, description="The number of violations"
    )
    rule_type: Missing[str] = Field(
        default=UNSET, description="The type of rule that was violated"
    )


class DismissalRequestSecretScanning(GitHubModel):
    """Secret scanning alert dismissal request data

    Secret scanning alerts that have dismissal requests.
    """

    type: Missing[Literal["secret_scanning_closure"]] = Field(
        default=UNSET, description="The type of request"
    )
    data: Missing[list[DismissalRequestSecretScanningPropDataItems]] = Field(
        default=UNSET,
        description="The data related to the secret scanning alerts that have dismissal requests.",
    )


class DismissalRequestSecretScanningPropDataItems(GitHubModel):
    """DismissalRequestSecretScanningPropDataItems"""

    secret_type: Missing[str] = Field(
        default=UNSET, description="The type of secret that was detected"
    )
    alert_number: Missing[str] = Field(
        default=UNSET, description="The number of the alert that was detected"
    )


class DismissalRequestCodeScanning(GitHubModel):
    """Code scanning alert dismissal request data

    Code scanning alerts that have dismissal requests.
    """

    type: Missing[Literal["code_scanning_alert_dismissal"]] = Field(
        default=UNSET, description="The type of request"
    )
    data: Missing[list[DismissalRequestCodeScanningPropDataItems]] = Field(
        default=UNSET,
        description="The data related to the code scanning alerts that have dismissal requests.",
    )


class DismissalRequestCodeScanningPropDataItems(GitHubModel):
    """DismissalRequestCodeScanningPropDataItems"""

    alert_number: Missing[str] = Field(
        default=UNSET, description="The number of the alert to be dismissed"
    )


class ExemptionRequestSecretScanning(GitHubModel):
    """Secret scanning push protection exemption request data

    Secret scanning push protections that are being requested to be bypassed.
    """

    type: Missing[Literal["secret_scanning"]] = Field(
        default=UNSET, description="The type of request"
    )
    data: Missing[list[ExemptionRequestSecretScanningPropDataItems]] = Field(
        default=UNSET,
        description="The data pertaining to the secret scanning push protections that are being requested to be bypassed.",
    )


class ExemptionRequestSecretScanningPropDataItems(GitHubModel):
    """ExemptionRequestSecretScanningPropDataItems"""

    secret_type: Missing[str] = Field(
        default=UNSET, description="The type of secret that was detected"
    )
    locations: Missing[
        list[ExemptionRequestSecretScanningPropDataItemsPropLocationsItems]
    ] = Field(
        default=UNSET, description="The location data of the secret that was detected"
    )


class ExemptionRequestSecretScanningPropDataItemsPropLocationsItems(GitHubModel):
    """ExemptionRequestSecretScanningPropDataItemsPropLocationsItems"""

    commit: Missing[str] = Field(
        default=UNSET, description="The commit SHA where the secret was detected"
    )
    branch: Missing[str] = Field(
        default=UNSET, description="The branch where the secret was detected"
    )
    path: Missing[str] = Field(
        default=UNSET, description="The path of the file where the secret was detected"
    )


model_rebuild(ExemptionRequest)
model_rebuild(ExemptionRequestSecretScanningMetadata)
model_rebuild(DismissalRequestSecretScanningMetadata)
model_rebuild(DismissalRequestCodeScanningMetadata)
model_rebuild(ExemptionRequestPushRulesetBypass)
model_rebuild(ExemptionRequestPushRulesetBypassPropDataItems)
model_rebuild(DismissalRequestSecretScanning)
model_rebuild(DismissalRequestSecretScanningPropDataItems)
model_rebuild(DismissalRequestCodeScanning)
model_rebuild(DismissalRequestCodeScanningPropDataItems)
model_rebuild(ExemptionRequestSecretScanning)
model_rebuild(ExemptionRequestSecretScanningPropDataItems)
model_rebuild(ExemptionRequestSecretScanningPropDataItemsPropLocationsItems)

__all__ = (
    "DismissalRequestCodeScanning",
    "DismissalRequestCodeScanningMetadata",
    "DismissalRequestCodeScanningPropDataItems",
    "DismissalRequestSecretScanning",
    "DismissalRequestSecretScanningMetadata",
    "DismissalRequestSecretScanningPropDataItems",
    "ExemptionRequest",
    "ExemptionRequestPushRulesetBypass",
    "ExemptionRequestPushRulesetBypassPropDataItems",
    "ExemptionRequestSecretScanning",
    "ExemptionRequestSecretScanningMetadata",
    "ExemptionRequestSecretScanningPropDataItems",
    "ExemptionRequestSecretScanningPropDataItemsPropLocationsItems",
)
