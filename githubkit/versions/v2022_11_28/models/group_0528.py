"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0523 import (
    WebhookIssuesMilestonedPropIssueAllof0PropPerformedViaGithubAppPropOwner,
    WebhookIssuesMilestonedPropIssueAllof0PropPerformedViaGithubAppPropPermissions,
)


class WebhookIssuesMilestonedPropIssueMergedPerformedViaGithubApp(GitHubModel):
    """WebhookIssuesMilestonedPropIssueMergedPerformedViaGithubApp"""

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[
        List[
            Literal[
                "branch_protection_rule",
                "check_run",
                "check_suite",
                "code_scanning_alert",
                "commit_comment",
                "content_reference",
                "create",
                "delete",
                "deployment",
                "deployment_review",
                "deployment_status",
                "deploy_key",
                "discussion",
                "discussion_comment",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "member",
                "membership",
                "milestone",
                "organization",
                "org_block",
                "page_build",
                "project",
                "project_card",
                "project_column",
                "public",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "registry_package",
                "release",
                "repository",
                "repository_dispatch",
                "secret_scanning_alert",
                "star",
                "status",
                "team",
                "team_add",
                "watch",
                "workflow_dispatch",
                "workflow_run",
                "reminder",
            ]
        ]
    ] = Field(default=UNSET, description="The list of events for the GitHub app")
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookIssuesMilestonedPropIssueAllof0PropPerformedViaGithubAppPropOwner, None
    ] = Field(title="User")
    permissions: Missing[
        WebhookIssuesMilestonedPropIssueAllof0PropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


model_rebuild(WebhookIssuesMilestonedPropIssueMergedPerformedViaGithubApp)

__all__ = ("WebhookIssuesMilestonedPropIssueMergedPerformedViaGithubApp",)
