"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoDependencyGraphSnapshotsPostResponse201(GitHubModel):
    """ReposOwnerRepoDependencyGraphSnapshotsPostResponse201"""

    id: int = Field(description="ID of the created snapshot.")
    created_at: str = Field(description="The time at which the snapshot was created.")
    result: str = Field(
        description='Either "SUCCESS", "ACCEPTED", or "INVALID". "SUCCESS" indicates that the snapshot was successfully created and the repository\'s dependencies were updated. "ACCEPTED" indicates that the snapshot was successfully created, but the repository\'s dependencies were not updated. "INVALID" indicates that the snapshot was malformed.'
    )
    message: str = Field(
        description="A message providing further details about the result, such as why the dependencies were not updated."
    )


model_rebuild(ReposOwnerRepoDependencyGraphSnapshotsPostResponse201)

__all__ = ("ReposOwnerRepoDependencyGraphSnapshotsPostResponse201",)
