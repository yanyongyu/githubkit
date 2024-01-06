"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class AutoMergeType(TypedDict):
    """Auto merge

    The status of auto merging a pull request.
    """

    enabled_by: SimpleUserType
    merge_method: Literal["merge", "squash", "rebase"]
    commit_title: Union[str, None]
    commit_message: Union[str, None]


__all__ = ("AutoMergeType",)