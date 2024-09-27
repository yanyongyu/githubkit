"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0351 import Traffic


class CloneTraffic(GitHubModel):
    """Clone Traffic

    Clone Traffic
    """

    count: int = Field()
    uniques: int = Field()
    clones: List[Traffic] = Field()


model_rebuild(CloneTraffic)

__all__ = ("CloneTraffic",)
