"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0358 import Discussion
from .group_0354 import RepositoryWebhooks


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
