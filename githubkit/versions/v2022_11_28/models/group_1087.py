"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody(GitHubModel):
    """ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody"""

    state: Literal["open", "resolved"] = Field(
        description="Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`."
    )
    resolution: Missing[
        Union[None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]]
    ] = Field(
        default=UNSET,
        description="**Required when the `state` is `resolved`.** The reason for resolving the alert.",
    )
    resolution_comment: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="An optional comment when closing an alert. Cannot be updated or deleted. Must be `null` when changing `state` to `open`.",
    )


model_rebuild(ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody)

__all__ = ("ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody",)
