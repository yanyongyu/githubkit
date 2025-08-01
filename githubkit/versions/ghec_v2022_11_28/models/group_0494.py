"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0010 import Integration
from .group_0178 import MinimalRepository
from .group_0257 import PullRequestMinimal


class SimpleCheckSuite(GitHubModel):
    """SimpleCheckSuite

    A suite of checks performed on the code of a given code change
    """

    after: Missing[Union[str, None]] = Field(default=UNSET)
    app: Missing[Union[Integration, None]] = Field(
        default=UNSET,
        title="GitHub app",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    before: Missing[Union[str, None]] = Field(default=UNSET)
    conclusion: Missing[
        Union[
            None,
            Literal[
                "success",
                "failure",
                "neutral",
                "cancelled",
                "skipped",
                "timed_out",
                "action_required",
                "stale",
                "startup_failure",
            ],
        ]
    ] = Field(default=UNSET)
    created_at: Missing[datetime] = Field(default=UNSET)
    head_branch: Missing[Union[str, None]] = Field(default=UNSET)
    head_sha: Missing[str] = Field(
        default=UNSET, description="The SHA of the head commit that is being checked."
    )
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    pull_requests: Missing[list[PullRequestMinimal]] = Field(default=UNSET)
    repository: Missing[MinimalRepository] = Field(
        default=UNSET, title="Minimal Repository", description="Minimal Repository"
    )
    status: Missing[
        Literal["queued", "in_progress", "completed", "pending", "waiting"]
    ] = Field(default=UNSET)
    updated_at: Missing[datetime] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(SimpleCheckSuite)

__all__ = ("SimpleCheckSuite",)
