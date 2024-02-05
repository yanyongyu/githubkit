"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ActionsOrganizationPermissionsType(TypedDict):
    """ActionsOrganizationPermissions"""

    enabled_repositories: Literal["all", "none", "selected"]
    selected_repositories_url: NotRequired[str]
    allowed_actions: NotRequired[Literal["all", "local_only", "selected"]]
    selected_actions_url: NotRequired[str]


__all__ = ("ActionsOrganizationPermissionsType",)
