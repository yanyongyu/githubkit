"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ProjectsColumnsCardsCardIdMovesPostResponse403Type(TypedDict):
    """ProjectsColumnsCardsCardIdMovesPostResponse403"""

    message: NotRequired[str]
    documentation_url: NotRequired[str]
    errors: NotRequired[
        List[ProjectsColumnsCardsCardIdMovesPostResponse403PropErrorsItemsType]
    ]


class ProjectsColumnsCardsCardIdMovesPostResponse403PropErrorsItemsType(TypedDict):
    """ProjectsColumnsCardsCardIdMovesPostResponse403PropErrorsItems"""

    code: NotRequired[str]
    message: NotRequired[str]
    resource: NotRequired[str]
    field: NotRequired[str]


__all__ = (
    "ProjectsColumnsCardsCardIdMovesPostResponse403Type",
    "ProjectsColumnsCardsCardIdMovesPostResponse403PropErrorsItemsType",
)
