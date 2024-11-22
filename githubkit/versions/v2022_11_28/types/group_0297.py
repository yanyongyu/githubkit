"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0042 import IssueType


class TimelineCrossReferencedEventPropSourceType(TypedDict):
    """TimelineCrossReferencedEventPropSource"""

    type: NotRequired[str]
    issue: NotRequired[IssueType]


__all__ = ("TimelineCrossReferencedEventPropSourceType",)
