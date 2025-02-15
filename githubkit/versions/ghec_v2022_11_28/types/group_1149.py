"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoInvitationsInvitationIdPatchBodyType(TypedDict):
    """ReposOwnerRepoInvitationsInvitationIdPatchBody"""

    permissions: NotRequired[Literal["read", "write", "maintain", "triage", "admin"]]


__all__ = ("ReposOwnerRepoInvitationsInvitationIdPatchBodyType",)
