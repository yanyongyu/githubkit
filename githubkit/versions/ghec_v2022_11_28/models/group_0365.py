"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0153 import Issue


class TimelineCrossReferencedEventPropSource(GitHubModel):
    """TimelineCrossReferencedEventPropSource"""

    type: Missing[str] = Field(default=UNSET)
    issue: Missing[Issue] = Field(
        default=UNSET,
        title="Issue",
        description="Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.",
    )


model_rebuild(TimelineCrossReferencedEventPropSource)

__all__ = ("TimelineCrossReferencedEventPropSource",)
