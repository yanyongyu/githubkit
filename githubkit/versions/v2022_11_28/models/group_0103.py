"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrganizationUpdateIssueType(GitHubModel):
    """OrganizationUpdateIssueType"""

    name: str = Field(description="Name of the issue type.")
    is_enabled: bool = Field(
        description="Whether or not the issue type is enabled at the organization level."
    )
    is_private: Missing[bool] = Field(
        default=UNSET,
        description="Whether or not the issue type is restricted to issues in private repositories.",
    )
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Description of the issue type."
    )
    color: Missing[
        Union[
            None,
            Literal[
                "gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"
            ],
        ]
    ] = Field(default=UNSET, description="Color for the issue type.")


model_rebuild(OrganizationUpdateIssueType)

__all__ = ("OrganizationUpdateIssueType",)
