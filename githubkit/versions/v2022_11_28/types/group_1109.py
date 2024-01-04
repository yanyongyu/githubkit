"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class UserPatchBodyType(TypedDict):
    """UserPatchBody"""

    name: NotRequired[str]
    email: NotRequired[str]
    blog: NotRequired[str]
    twitter_username: NotRequired[Union[str, None]]
    company: NotRequired[str]
    location: NotRequired[str]
    hireable: NotRequired[bool]
    bio: NotRequired[str]


__all__ = ("UserPatchBodyType",)
