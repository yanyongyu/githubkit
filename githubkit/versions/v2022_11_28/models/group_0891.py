"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class OrgsOrgOutsideCollaboratorsUsernamePutBody(GitHubModel):
    """OrgsOrgOutsideCollaboratorsUsernamePutBody"""

    async_: Missing[bool] = Field(
        default=UNSET,
        alias="async",
        description="When set to `true`, the request will be performed asynchronously. Returns a 202 status code when the job is successfully queued.",
    )


model_rebuild(OrgsOrgOutsideCollaboratorsUsernamePutBody)

__all__ = ("OrgsOrgOutsideCollaboratorsUsernamePutBody",)
