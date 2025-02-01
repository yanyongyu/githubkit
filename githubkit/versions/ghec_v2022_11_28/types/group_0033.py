"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class ActionsHostedRunnerLimitsType(TypedDict):
    """ActionsHostedRunnerLimits"""

    public_ips: ActionsHostedRunnerLimitsPropPublicIpsType


class ActionsHostedRunnerLimitsPropPublicIpsType(TypedDict):
    """Static public IP Limits for GitHub-hosted Hosted Runners.

    Provides details of static public IP limits for GitHub-hosted Hosted Runners
    """

    maximum: int
    current_usage: int


__all__ = (
    "ActionsHostedRunnerLimitsPropPublicIpsType",
    "ActionsHostedRunnerLimitsType",
)
