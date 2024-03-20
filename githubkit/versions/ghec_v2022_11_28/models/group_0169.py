"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class RateLimit(GitHubModel):
    """Rate Limit"""

    limit: int = Field()
    remaining: int = Field()
    reset: int = Field()
    used: int = Field()


model_rebuild(RateLimit)

__all__ = ("RateLimit",)