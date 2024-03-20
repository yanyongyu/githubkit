"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0703 import (
    WebhookReleasePublishedPropReleaseAllof0PropAssetsItemsPropUploader,
)


class WebhookReleasePublishedPropReleaseAllof0PropAssetsItems(GitHubModel):
    """Release Asset

    Data related to a release.
    """

    browser_download_url: str = Field()
    content_type: str = Field()
    created_at: datetime = Field()
    download_count: int = Field()
    id: int = Field()
    label: Union[str, None] = Field()
    name: str = Field(description="The file name of the asset.")
    node_id: str = Field()
    size: int = Field()
    state: Literal["uploaded"] = Field(description="State of the release asset.")
    updated_at: datetime = Field()
    uploader: Missing[
        Union[WebhookReleasePublishedPropReleaseAllof0PropAssetsItemsPropUploader, None]
    ] = Field(default=UNSET, title="User")
    url: str = Field()


model_rebuild(WebhookReleasePublishedPropReleaseAllof0PropAssetsItems)

__all__ = ("WebhookReleasePublishedPropReleaseAllof0PropAssetsItems",)
