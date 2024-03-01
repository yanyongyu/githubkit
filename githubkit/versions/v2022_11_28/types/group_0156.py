"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


class ActionsSecretType(TypedDict):
    """Actions Secret

    Set secrets for GitHub Actions.
    """

    name: str
    created_at: datetime
    updated_at: datetime


__all__ = ("ActionsSecretType",)
