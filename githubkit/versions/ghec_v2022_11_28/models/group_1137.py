"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Annotated, Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody(GitHubModel):
    """ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody"""

    state: Literal["open", "dismissed"] = Field(
        description="Sets the state of the code scanning alert. You must provide `dismissed_reason` when you set the state to `dismissed`."
    )
    dismissed_reason: Missing[
        Union[None, Literal["false positive", "won't fix", "used in tests"]]
    ] = Field(
        default=UNSET,
        description="**Required when the state is dismissed.** The reason for dismissing or closing the alert.",
    )
    dismissed_comment: Missing[Union[Annotated[str, Field(max_length=280)], None]] = (
        Field(
            default=UNSET,
            description="The dismissal comment associated with the dismissal of the alert.",
        )
    )
    create_request: Missing[bool] = Field(
        default=UNSET,
        description="If `true`, attempt to create an alert dismissal request.",
    )


model_rebuild(ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody)

__all__ = ("ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody",)
