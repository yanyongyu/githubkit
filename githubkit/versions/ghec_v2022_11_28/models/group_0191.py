"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ActionsSecret(GitHubModel):
    """Actions Secret

    Set secrets for GitHub Actions.
    """

    name: str = Field(description="The name of the secret.")
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(ActionsSecret)

__all__ = ("ActionsSecret",)
