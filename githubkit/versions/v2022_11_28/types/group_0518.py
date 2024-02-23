"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0513 import (
    WebhookIssuesLockedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
    WebhookIssuesLockedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType,
)


class WebhookIssuesLockedPropIssueMergedPerformedViaGithubAppType(TypedDict):
    """WebhookIssuesLockedPropIssueMergedPerformedViaGithubApp"""

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[
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
                "security_and_analysis",
            ]
        ]
    ]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookIssuesLockedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType, None
    ]
    permissions: NotRequired[
        WebhookIssuesLockedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


__all__ = ("WebhookIssuesLockedPropIssueMergedPerformedViaGithubAppType",)
