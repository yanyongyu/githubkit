"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class AnnouncementBanner(GitHubModel):
    """Announcement Banner

    Announcement at either the repository, organization, or enterprise level
    """

    announcement: Union[str, None] = Field(
        description='The announcement text in GitHub Flavored Markdown. For more information about GitHub Flavored Markdown, see "[Basic writing and formatting syntax](https://docs.github.com/enterprise-cloud@latest//github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)."'
    )
    expires_at: Union[datetime, None] = Field(
        description="The time at which the announcement expires. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. To set an announcement that never expires, omit this parameter, set it to `null`, or set it to an empty string."
    )
    user_dismissible: Union[bool, None] = Field(
        default=False,
        description="Whether an announcement can be dismissed by the user.",
    )


model_rebuild(AnnouncementBanner)

__all__ = ("AnnouncementBanner",)
