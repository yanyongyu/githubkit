"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class SimpleClassroomRepository(GitHubModel):
    """Simple Classroom Repository

    A GitHub repository view for Classroom
    """

    id: int = Field(description="A unique identifier of the repository.")
    full_name: str = Field(
        description="The full, globally unique name of the repository."
    )
    html_url: str = Field(description="The URL to view the repository on GitHub.com.")
    node_id: str = Field(description="The GraphQL identifier of the repository.")
    private: bool = Field(description="Whether the repository is private.")
    default_branch: str = Field(description="The default branch for the repository.")


model_rebuild(SimpleClassroomRepository)

__all__ = ("SimpleClassroomRepository",)
