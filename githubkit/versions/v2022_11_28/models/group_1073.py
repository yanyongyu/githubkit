"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPullsPullNumberReviewsPostBody(GitHubModel):
    """ReposOwnerRepoPullsPullNumberReviewsPostBody"""

    commit_id: Missing[str] = Field(
        default=UNSET,
        description="The SHA of the commit that needs a review. Not using the latest commit SHA may render your review comment outdated if a subsequent commit modifies the line you specify as the `position`. Defaults to the most recent commit in the pull request when you do not specify a value.",
    )
    body: Missing[str] = Field(
        default=UNSET,
        description="**Required** when using `REQUEST_CHANGES` or `COMMENT` for the `event` parameter. The body text of the pull request review.",
    )
    event: Missing[Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"]] = Field(
        default=UNSET,
        description="The review action you want to perform. The review actions include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. By leaving this blank, you set the review action state to `PENDING`, which means you will need to [submit the pull request review](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request) when you are ready.",
    )
    comments: Missing[
        List[ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItems]
    ] = Field(
        default=UNSET,
        description="Use the following table to specify the location, destination, and contents of the draft review comment.",
    )


class ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItems(GitHubModel):
    """ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItems"""

    path: str = Field(
        description="The relative path to the file that necessitates a review comment."
    )
    position: Missing[int] = Field(
        default=UNSET,
        description="The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. For help finding the position value, read the note below.",
    )
    body: str = Field(description="Text of the review comment.")
    line: Missing[int] = Field(default=UNSET)
    side: Missing[str] = Field(default=UNSET)
    start_line: Missing[int] = Field(default=UNSET)
    start_side: Missing[str] = Field(default=UNSET)


model_rebuild(ReposOwnerRepoPullsPullNumberReviewsPostBody)
model_rebuild(ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItems)

__all__ = (
    "ReposOwnerRepoPullsPullNumberReviewsPostBody",
    "ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItems",
)
