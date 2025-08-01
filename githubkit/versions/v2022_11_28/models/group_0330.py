"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0331 import TimelineCrossReferencedEventPropSource


class TimelineCrossReferencedEvent(GitHubModel):
    """Timeline Cross Referenced Event

    Timeline Cross Referenced Event
    """

    event: Literal["cross-referenced"] = Field()
    actor: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    created_at: datetime = Field()
    updated_at: datetime = Field()
    source: TimelineCrossReferencedEventPropSource = Field()


model_rebuild(TimelineCrossReferencedEvent)

__all__ = ("TimelineCrossReferencedEvent",)
