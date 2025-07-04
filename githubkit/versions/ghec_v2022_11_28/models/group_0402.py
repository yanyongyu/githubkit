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

from .group_0003 import SimpleUser


class ReleaseAsset(GitHubModel):
    """Release Asset

    Data related to a release.
    """

    url: str = Field()
    browser_download_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    name: str = Field(description="The file name of the asset.")
    label: Union[str, None] = Field()
    state: Literal["uploaded", "open"] = Field(
        description="State of the release asset."
    )
    content_type: str = Field()
    size: int = Field()
    digest: Union[str, None] = Field()
    download_count: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    uploader: Union[None, SimpleUser] = Field()


model_rebuild(ReleaseAsset)

__all__ = ("ReleaseAsset",)
