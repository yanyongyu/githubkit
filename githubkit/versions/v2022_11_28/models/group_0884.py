"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0071 import Codespace


class OrgsOrgMembersUsernameCodespacesGetResponse200(GitHubModel):
    """OrgsOrgMembersUsernameCodespacesGetResponse200"""

    total_count: int = Field()
    codespaces: List[Codespace] = Field()


model_rebuild(OrgsOrgMembersUsernameCodespacesGetResponse200)

__all__ = ("OrgsOrgMembersUsernameCodespacesGetResponse200",)
