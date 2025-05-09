"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class IntegrationPropPermissionsType(TypedDict):
    """IntegrationPropPermissions

    The set of permissions for the GitHub app

    Examples:
        {'issues': 'read', 'deployments': 'write'}
    """

    issues: NotRequired[str]
    checks: NotRequired[str]
    metadata: NotRequired[str]
    contents: NotRequired[str]
    deployments: NotRequired[str]


__all__ = ("IntegrationPropPermissionsType",)
