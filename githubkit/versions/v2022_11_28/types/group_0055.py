"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


class OidcCustomSubType(TypedDict):
    """Actions OIDC Subject customization

    Actions OIDC Subject customization
    """

    include_claim_keys: List[str]


__all__ = ("OidcCustomSubType",)
