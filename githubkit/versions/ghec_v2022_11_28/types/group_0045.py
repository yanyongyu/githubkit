"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict


class AnnouncementType(TypedDict):
    """Enterprise Announcement

    Enterprise global announcement
    """

    announcement: Union[str, None]
    expires_at: NotRequired[Union[datetime, None]]
    user_dismissible: NotRequired[Union[bool, None]]


__all__ = ("AnnouncementType",)
