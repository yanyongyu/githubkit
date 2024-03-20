"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0131 import RepositoryRuleUpdatePropParameters


class RepositoryRuleUpdate(GitHubModel):
    """update

    Only allow users with bypass permission to update matching refs.
    """

    type: Literal["update"] = Field()
    parameters: Missing[RepositoryRuleUpdatePropParameters] = Field(default=UNSET)


model_rebuild(RepositoryRuleUpdate)

__all__ = ("RepositoryRuleUpdate",)
