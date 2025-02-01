"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0606 import (
    WebhookIssueCommentDeletedPropIssueAllof0PropPerformedViaGithubAppPropOwner,
    WebhookIssueCommentDeletedPropIssueAllof0PropPerformedViaGithubAppPropPermissions,
)


class WebhookIssueCommentDeletedPropIssueMergedPerformedViaGithubApp(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueMergedPerformedViaGithubApp"""

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[list[str]] = Field(
        default=UNSET, description="The list of events for the GitHub app"
    )
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookIssueCommentDeletedPropIssueAllof0PropPerformedViaGithubAppPropOwner,
        None,
    ] = Field(title="User")
    permissions: Missing[
        WebhookIssueCommentDeletedPropIssueAllof0PropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


model_rebuild(WebhookIssueCommentDeletedPropIssueMergedPerformedViaGithubApp)

__all__ = ("WebhookIssueCommentDeletedPropIssueMergedPerformedViaGithubApp",)
