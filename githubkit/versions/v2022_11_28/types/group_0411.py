"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict


class WebhooksDeployKeyType(TypedDict):
    """WebhooksDeployKey

    The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-
    deploy-key) resource.
    """

    added_by: NotRequired[Union[str, None]]
    created_at: str
    id: int
    key: str
    last_used: NotRequired[Union[str, None]]
    read_only: bool
    title: str
    url: str
    verified: bool
    enabled: NotRequired[bool]


__all__ = ("WebhooksDeployKeyType",)
