"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class GistComment(GitHubModel):
    """Gist Comment

    A comment made to a gist.
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    body: str = Field(max_length=65535, description="The comment text.")
    user: Union[None, SimpleUser] = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="author_association",
        description="How the author is associated with the repository.",
    )


model_rebuild(GistComment)

__all__ = ("GistComment",)
