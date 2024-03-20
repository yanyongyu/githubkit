"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Any, List, Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class GpgKeyType(TypedDict):
    """GPG Key

    A unique encryption key
    """

    id: int
    name: NotRequired[Union[str, None]]
    primary_key_id: Union[int, None]
    key_id: str
    public_key: str
    emails: List[GpgKeyPropEmailsItemsType]
    subkeys: List[GpgKeyPropSubkeysItemsType]
    can_sign: bool
    can_encrypt_comms: bool
    can_encrypt_storage: bool
    can_certify: bool
    created_at: datetime
    expires_at: Union[datetime, None]
    revoked: bool
    raw_key: Union[str, None]


class GpgKeyPropEmailsItemsType(TypedDict):
    """GpgKeyPropEmailsItems"""

    email: NotRequired[str]
    verified: NotRequired[bool]


class GpgKeyPropSubkeysItemsType(TypedDict):
    """GpgKeyPropSubkeysItems"""

    id: NotRequired[int]
    primary_key_id: NotRequired[int]
    key_id: NotRequired[str]
    public_key: NotRequired[str]
    emails: NotRequired[List[GpgKeyPropSubkeysItemsPropEmailsItemsType]]
    subkeys: NotRequired[List[Any]]
    can_sign: NotRequired[bool]
    can_encrypt_comms: NotRequired[bool]
    can_encrypt_storage: NotRequired[bool]
    can_certify: NotRequired[bool]
    created_at: NotRequired[str]
    expires_at: NotRequired[Union[str, None]]
    raw_key: NotRequired[Union[str, None]]
    revoked: NotRequired[bool]


class GpgKeyPropSubkeysItemsPropEmailsItemsType(TypedDict):
    """GpgKeyPropSubkeysItemsPropEmailsItems"""

    email: NotRequired[str]
    verified: NotRequired[bool]


__all__ = (
    "GpgKeyType",
    "GpgKeyPropEmailsItemsType",
    "GpgKeyPropSubkeysItemsType",
    "GpgKeyPropSubkeysItemsPropEmailsItemsType",
)
