"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0041 import Runner


class EnterprisesEnterpriseActionsRunnersGetResponse200(GitHubModel):
    """EnterprisesEnterpriseActionsRunnersGetResponse200"""

    total_count: Missing[float] = Field(default=UNSET)
    runners: Missing[list[Runner]] = Field(default=UNSET)


model_rebuild(EnterprisesEnterpriseActionsRunnersGetResponse200)

__all__ = ("EnterprisesEnterpriseActionsRunnersGetResponse200",)
