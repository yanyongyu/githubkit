"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict


class OrgsOrgPersonalAccessTokensPostBodyType(TypedDict):
    """OrgsOrgPersonalAccessTokensPostBody"""

    action: Literal["revoke"]
    pat_ids: List[int]


__all__ = ("OrgsOrgPersonalAccessTokensPostBodyType",)
