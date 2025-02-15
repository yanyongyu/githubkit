"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0564 import (
    WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
    WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType,
)


class WebhookIssueCommentEditedPropIssueMergedPerformedViaGithubAppType(TypedDict):
    """WebhookIssueCommentEditedPropIssueMergedPerformedViaGithubApp"""

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[list[str]]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


__all__ = ("WebhookIssueCommentEditedPropIssueMergedPerformedViaGithubAppType",)
