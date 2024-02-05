"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class InteractionLimitResponse(GitHubModel):
    """Interaction Limits

    Interaction limit settings.
    """

    limit: Literal["existing_users", "contributors_only", "collaborators_only"] = Field(
        description="The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect."
    )
    origin: str = Field()
    expires_at: datetime = Field()


model_rebuild(InteractionLimitResponse)

__all__ = ("InteractionLimitResponse",)
