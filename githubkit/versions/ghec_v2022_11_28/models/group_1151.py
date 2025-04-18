"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoDependabotAlertsAlertNumberPatchBody(GitHubModel):
    """ReposOwnerRepoDependabotAlertsAlertNumberPatchBody"""

    state: Literal["dismissed", "open"] = Field(
        description="The state of the Dependabot alert.\nA `dismissed_reason` must be provided when setting the state to `dismissed`."
    )
    dismissed_reason: Missing[
        Literal[
            "fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"
        ]
    ] = Field(
        default=UNSET,
        description="**Required when `state` is `dismissed`.** A reason for dismissing the alert.",
    )
    dismissed_comment: Missing[str] = Field(
        max_length=280,
        default=UNSET,
        description="An optional comment associated with dismissing the alert.",
    )


model_rebuild(ReposOwnerRepoDependabotAlertsAlertNumberPatchBody)

__all__ = ("ReposOwnerRepoDependabotAlertsAlertNumberPatchBody",)
