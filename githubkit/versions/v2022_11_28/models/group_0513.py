"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0407 import RepositoryWebhooks
from .group_0417 import Discussion


class WebhookDiscussionTransferredPropChanges(GitHubModel):
    """WebhookDiscussionTransferredPropChanges"""

    new_discussion: Discussion = Field(
        title="Discussion", description="A Discussion in a repository."
    )
    new_repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )


model_rebuild(WebhookDiscussionTransferredPropChanges)

__all__ = ("WebhookDiscussionTransferredPropChanges",)
