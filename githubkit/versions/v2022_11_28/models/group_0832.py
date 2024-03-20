"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations


from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class GistsGistIdCommentsCommentIdPatchBody(GitHubModel):
    """GistsGistIdCommentsCommentIdPatchBody"""

    body: str = Field(max_length=65535, description="The comment text.")


model_rebuild(GistsGistIdCommentsCommentIdPatchBody)

__all__ = ("GistsGistIdCommentsCommentIdPatchBody",)
