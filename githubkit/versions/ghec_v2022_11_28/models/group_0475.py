"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0002 import SimpleUser


class SecretScanningAlertWebhook(GitHubModel):
    """SecretScanningAlertWebhook"""

    number: Missing[int] = Field(
        default=UNSET, description="The security alert number."
    )
    created_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    updated_at: Missing[Union[None, datetime]] = Field(default=UNSET)
    url: Missing[str] = Field(
        default=UNSET, description="The REST API URL of the alert resource."
    )
    html_url: Missing[str] = Field(
        default=UNSET, description="The GitHub URL of the alert resource."
    )
    locations_url: Missing[str] = Field(
        default=UNSET,
        description="The REST API URL of the code locations for this alert.",
    )
    resolution: Missing[
        Union[
            None,
            Literal[
                "false_positive",
                "wont_fix",
                "revoked",
                "used_in_tests",
                "pattern_deleted",
                "pattern_edited",
            ],
        ]
    ] = Field(default=UNSET, description="The reason for resolving the alert.")
    resolved_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    resolved_by: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    resolution_comment: Missing[Union[str, None]] = Field(
        default=UNSET, description="An optional comment to resolve an alert."
    )
    secret_type: Missing[str] = Field(
        default=UNSET, description="The type of secret that secret scanning detected."
    )
    secret_type_display_name: Missing[str] = Field(
        default=UNSET,
        description='User-friendly name for the detected secret, matching the `secret_type`.\nFor a list of built-in patterns, see "[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest//code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)."',
    )
    validity: Missing[Literal["active", "inactive", "unknown"]] = Field(
        default=UNSET, description="The token status as of the latest validity check."
    )
    push_protection_bypassed: Missing[Union[bool, None]] = Field(
        default=UNSET,
        description="Whether push protection was bypassed for the detected secret.",
    )
    push_protection_bypassed_by: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    push_protection_bypassed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    push_protection_bypass_request_reviewer: Missing[Union[None, SimpleUser]] = Field(
        default=UNSET
    )
    push_protection_bypass_request_comment: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="An optional comment when requesting a push protection bypass.",
    )
    push_protection_bypass_request_html_url: Missing[Union[str, None]] = Field(
        default=UNSET, description="The URL to a push protection bypass request."
    )
    publicly_leaked: Missing[Union[bool, None]] = Field(
        default=UNSET, description="Whether the detected secret was publicly leaked."
    )
    multi_repo: Missing[Union[bool, None]] = Field(
        default=UNSET,
        description="Whether the detected secret was found in multiple repositories in the same organization or business.",
    )


model_rebuild(SecretScanningAlertWebhook)

__all__ = ("SecretScanningAlertWebhook",)
