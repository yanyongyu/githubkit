"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPullsPullNumberReviewsReviewIdEventsPostBody(GitHubModel):
    """ReposOwnerRepoPullsPullNumberReviewsReviewIdEventsPostBody"""

    body: Missing[str] = Field(
        default=UNSET, description="The body text of the pull request review"
    )
    event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"] = Field(
        description="The review action you want to perform. The review actions include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. When you leave this blank, the API returns _HTTP 422 (Unrecognizable entity)_ and sets the review action state to `PENDING`, which means you will need to re-submit the pull request review using a review action."
    )


model_rebuild(ReposOwnerRepoPullsPullNumberReviewsReviewIdEventsPostBody)

__all__ = ("ReposOwnerRepoPullsPullNumberReviewsReviewIdEventsPostBody",)