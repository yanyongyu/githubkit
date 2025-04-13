"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0331 import EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItemsType


class EnvironmentPropProtectionRulesItemsAnyof1Type(TypedDict):
    """EnvironmentPropProtectionRulesItemsAnyof1"""

    id: int
    node_id: str
    prevent_self_review: NotRequired[bool]
    type: str
    reviewers: NotRequired[
        list[EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItemsType]
    ]


__all__ = ("EnvironmentPropProtectionRulesItemsAnyof1Type",)
