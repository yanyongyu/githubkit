"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0021 import SimpleClassroomRepository


class ClassroomAssignment(GitHubModel):
    """Classroom Assignment

    A GitHub Classroom assignment
    """

    id: int = Field(description="Unique identifier of the repository.")
    public_repo: bool = Field(
        description="Whether an accepted assignment creates a public repository."
    )
    title: str = Field(description="Assignment title.")
    type: Literal["individual", "group"] = Field(
        description="Whether it's a group assignment or individual assignment."
    )
    invite_link: str = Field(
        description="The link that a student can use to accept the assignment."
    )
    invitations_enabled: bool = Field(
        description="Whether the invitation link is enabled. Visiting an enabled invitation link will accept the assignment."
    )
    slug: str = Field(description="Sluggified name of the assignment.")
    students_are_repo_admins: bool = Field(
        description="Whether students are admins on created repository when a student accepts the assignment."
    )
    feedback_pull_requests_enabled: bool = Field(
        description="Whether feedback pull request will be created when a student accepts the assignment."
    )
    max_teams: Union[int, None] = Field(
        description="The maximum allowable teams for the assignment."
    )
    max_members: Union[int, None] = Field(
        description="The maximum allowable members per team."
    )
    editor: str = Field(description="The selected editor for the assignment.")
    accepted: int = Field(
        description="The number of students that have accepted the assignment."
    )
    submitted: int = Field(
        description="The number of students that have submitted the assignment."
    )
    passing: int = Field(
        description="The number of students that have passed the assignment."
    )
    language: str = Field(
        description="The programming language used in the assignment."
    )
    deadline: Union[datetime, None] = Field(
        description="The time at which the assignment is due."
    )
    starter_code_repository: SimpleClassroomRepository = Field(
        title="Simple Classroom Repository",
        description="A GitHub repository view for Classroom",
    )
    classroom: Classroom = Field(
        title="Classroom", description="A GitHub Classroom classroom"
    )


class Classroom(GitHubModel):
    """Classroom

    A GitHub Classroom classroom
    """

    id: int = Field(description="Unique identifier of the classroom.")
    name: str = Field(description="The name of the classroom.")
    archived: bool = Field(description="Whether classroom is archived.")
    organization: SimpleClassroomOrganization = Field(
        title="Organization Simple for Classroom", description="A GitHub organization."
    )
    url: str = Field(description="The URL of the classroom on GitHub Classroom.")


class SimpleClassroomOrganization(GitHubModel):
    """Organization Simple for Classroom

    A GitHub organization.
    """

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    html_url: str = Field()
    name: Union[str, None] = Field()
    avatar_url: str = Field()


model_rebuild(ClassroomAssignment)
model_rebuild(Classroom)
model_rebuild(SimpleClassroomOrganization)

__all__ = (
    "ClassroomAssignment",
    "Classroom",
    "SimpleClassroomOrganization",
)
