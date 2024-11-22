"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0570 import (
    WebhookIssueCommentCreatedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
    WebhookIssueCommentCreatedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType,
)


class WebhookIssueCommentCreatedPropIssueMergedPerformedViaGithubAppType(TypedDict):
    """WebhookIssueCommentCreatedPropIssueMergedPerformedViaGithubApp"""

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[list[str]]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookIssueCommentCreatedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookIssueCommentCreatedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


__all__ = ("WebhookIssueCommentCreatedPropIssueMergedPerformedViaGithubAppType",)
