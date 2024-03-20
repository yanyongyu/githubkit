"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposTemplateOwnerTemplateRepoGeneratePostBodyType(TypedDict):
    """ReposTemplateOwnerTemplateRepoGeneratePostBody"""

    owner: NotRequired[str]
    name: str
    description: NotRequired[str]
    include_all_branches: NotRequired[bool]
    private: NotRequired[bool]


__all__ = ("ReposTemplateOwnerTemplateRepoGeneratePostBodyType",)
