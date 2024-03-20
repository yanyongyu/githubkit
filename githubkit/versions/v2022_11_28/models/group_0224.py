"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class Contributor(GitHubModel):
    """Contributor

    Contributor
    """

    login: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    avatar_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[Union[str, None]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    type: str = Field()
    site_admin: Missing[bool] = Field(default=UNSET)
    contributions: int = Field()
    email: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)


model_rebuild(Contributor)

__all__ = ("Contributor",)
