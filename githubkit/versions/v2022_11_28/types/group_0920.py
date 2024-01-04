"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ProjectsColumnsColumnIdCardsPostResponse503Type(TypedDict):
    """ProjectsColumnsColumnIdCardsPostResponse503"""

    code: NotRequired[str]
    message: NotRequired[str]
    documentation_url: NotRequired[str]
    errors: NotRequired[
        List[ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItemsType]
    ]


class ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItemsType(TypedDict):
    """ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItems"""

    code: NotRequired[str]
    message: NotRequired[str]


__all__ = (
    "ProjectsColumnsColumnIdCardsPostResponse503Type",
    "ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItemsType",
)
