"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class InstallableOrganization(GitHubModel):
    """Installable Organization

    A GitHub organization on which a GitHub App can be installed.
    """

    id: int = Field()
    login: str = Field()
    accessible_repositories_url: Missing[str] = Field(default=UNSET)


model_rebuild(InstallableOrganization)

__all__ = ("InstallableOrganization",)
