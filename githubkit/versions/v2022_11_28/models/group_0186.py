"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0003 import SimpleUser


class Reaction(GitHubModel):
    """Reaction

    Reactions to conversations provide a way to help people express their feelings
    more simply and effectively.
    """

    id: int = Field()
    node_id: str = Field()
    user: Union[None, SimpleUser] = Field()
    content: Literal[
        "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
    ] = Field(description="The reaction to use")
    created_at: datetime = Field()


model_rebuild(Reaction)

__all__ = ("Reaction",)
