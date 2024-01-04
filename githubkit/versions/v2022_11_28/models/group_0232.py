"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0075 import Team
from .group_0001 import SimpleUser


class EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems(GitHubModel):
    """EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems"""

    type: Missing[Literal["User", "Team"]] = Field(
        default=UNSET, description="The type of reviewer."
    )
    reviewer: Missing[Union[SimpleUser, Team]] = Field(default=UNSET)


model_rebuild(EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems)

__all__ = ("EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItems",)
