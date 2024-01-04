"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ActionsPublicKeyType(TypedDict):
    """ActionsPublicKey

    The public key used for setting Actions Secrets.
    """

    key_id: str
    key: str
    id: NotRequired[int]
    url: NotRequired[str]
    title: NotRequired[str]
    created_at: NotRequired[str]


__all__ = ("ActionsPublicKeyType",)
