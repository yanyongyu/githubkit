"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0059 import ReactionRollupType
from .group_0318 import ReleaseAssetType


class ReleaseType(TypedDict):
    """Release

    A release.
    """

    url: str
    html_url: str
    assets_url: str
    upload_url: str
    tarball_url: Union[str, None]
    zipball_url: Union[str, None]
    id: int
    node_id: str
    tag_name: str
    target_commitish: str
    name: Union[str, None]
    body: NotRequired[Union[str, None]]
    draft: bool
    prerelease: bool
    created_at: datetime
    published_at: Union[datetime, None]
    author: SimpleUserType
    assets: List[ReleaseAssetType]
    body_html: NotRequired[Union[str, None]]
    body_text: NotRequired[Union[str, None]]
    mentions_count: NotRequired[int]
    discussion_url: NotRequired[str]
    reactions: NotRequired[ReactionRollupType]


__all__ = ("ReleaseType",)
