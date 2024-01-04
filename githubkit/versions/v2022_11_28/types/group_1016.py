"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoHooksPostBodyType(TypedDict):
    """ReposOwnerRepoHooksPostBody"""

    name: NotRequired[str]
    config: NotRequired[ReposOwnerRepoHooksPostBodyPropConfigType]
    events: NotRequired[List[str]]
    active: NotRequired[bool]


class ReposOwnerRepoHooksPostBodyPropConfigType(TypedDict):
    """ReposOwnerRepoHooksPostBodyPropConfig

    Key/value pairs to provide settings for this webhook.
    """

    url: NotRequired[str]
    content_type: NotRequired[str]
    secret: NotRequired[str]
    insecure_ssl: NotRequired[Union[str, float]]
    token: NotRequired[str]
    digest: NotRequired[str]


__all__ = (
    "ReposOwnerRepoHooksPostBodyType",
    "ReposOwnerRepoHooksPostBodyPropConfigType",
)
