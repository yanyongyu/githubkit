"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookIssuesLockedPropIssueAllof0PropPullRequest(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof0PropPullRequest"""

    diff_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    merged_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    patch_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssuesLockedPropIssueAllof0PropPullRequest)

__all__ = ("WebhookIssuesLockedPropIssueAllof0PropPullRequest",)
