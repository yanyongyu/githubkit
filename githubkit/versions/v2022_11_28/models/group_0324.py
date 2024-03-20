"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0001 import SimpleUser


class ContributorActivity(GitHubModel):
    """Contributor Activity

    Contributor Activity
    """

    author: Union[None, SimpleUser] = Field()
    total: int = Field()
    weeks: List[ContributorActivityPropWeeksItems] = Field()


class ContributorActivityPropWeeksItems(GitHubModel):
    """ContributorActivityPropWeeksItems"""

    w: Missing[int] = Field(default=UNSET)
    a: Missing[int] = Field(default=UNSET)
    d: Missing[int] = Field(default=UNSET)
    c: Missing[int] = Field(default=UNSET)


model_rebuild(ContributorActivity)
model_rebuild(ContributorActivityPropWeeksItems)

__all__ = (
    "ContributorActivity",
    "ContributorActivityPropWeeksItems",
)
