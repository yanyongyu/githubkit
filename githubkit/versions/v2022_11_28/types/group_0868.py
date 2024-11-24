"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgReposPostBodyType(TypedDict):
    """OrgsOrgReposPostBody"""

    name: str
    description: NotRequired[str]
    homepage: NotRequired[str]
    private: NotRequired[bool]
    visibility: NotRequired[Literal["public", "private"]]
    has_issues: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    has_downloads: NotRequired[bool]
    is_template: NotRequired[bool]
    team_id: NotRequired[int]
    auto_init: NotRequired[bool]
    gitignore_template: NotRequired[str]
    license_template: NotRequired[str]
    allow_squash_merge: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    custom_properties: NotRequired[OrgsOrgReposPostBodyPropCustomPropertiesType]


class OrgsOrgReposPostBodyPropCustomPropertiesType(TypedDict):
    """OrgsOrgReposPostBodyPropCustomProperties

    The custom properties for the new repository. The keys are the custom property
    names, and the values are the corresponding custom property values.
    """


__all__ = (
    "OrgsOrgReposPostBodyPropCustomPropertiesType",
    "OrgsOrgReposPostBodyType",
)
