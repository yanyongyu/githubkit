"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class IntegrationPropPermissions(ExtraGitHubModel):
    """IntegrationPropPermissions

    The set of permissions for the GitHub app

    Examples:
        {'issues': 'read', 'deployments': 'write'}
    """

    issues: Missing[str] = Field(default=UNSET)
    checks: Missing[str] = Field(default=UNSET)
    metadata: Missing[str] = Field(default=UNSET)
    contents: Missing[str] = Field(default=UNSET)
    deployments: Missing[str] = Field(default=UNSET)


model_rebuild(IntegrationPropPermissions)

__all__ = ("IntegrationPropPermissions",)
