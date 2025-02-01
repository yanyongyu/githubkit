"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class DatadogConfig(GitHubModel):
    """DatadogConfig

    Datadog Config for audit log streaming configuration.
    """

    encrypted_token: str = Field(description="Encrypted Splunk token.")
    site: Literal["US", "US3", "US5", "EU1", "US1-FED", "AP1"] = Field(
        description="Datadog Site to use."
    )
    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )


model_rebuild(DatadogConfig)

__all__ = ("DatadogConfig",)
