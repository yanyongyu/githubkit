"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleParamsCodeScanningThreshold(GitHubModel):
    """CodeScanningThreshold

    A tool and its thresholds.
    """

    alerts: Literal["none", "errors", "errors_and_warnings", "all"] = Field(
        description="Code scanning alert threshold"
    )
    security_alerts: Literal[
        "none", "critical", "high_or_higher", "medium_or_higher", "all"
    ] = Field(description="Code scanning security alert threshold.")
    tool: str = Field(description="The name of a code scanning tool")


model_rebuild(RepositoryRuleParamsCodeScanningThreshold)

__all__ = ("RepositoryRuleParamsCodeScanningThreshold",)
