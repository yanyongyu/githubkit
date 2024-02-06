"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0016 import LicenseSimple


class LicenseContent(GitHubModel):
    """License Content

    License Content
    """

    name: str = Field()
    path: str = Field()
    sha: str = Field()
    size: int = Field()
    url: str = Field()
    html_url: Union[str, None] = Field()
    git_url: Union[str, None] = Field()
    download_url: Union[str, None] = Field()
    type: str = Field()
    content: str = Field()
    encoding: str = Field()
    links: LicenseContentPropLinks = Field(alias="_links")
    license_: Union[None, LicenseSimple] = Field(alias="license")


class LicenseContentPropLinks(GitHubModel):
    """LicenseContentPropLinks"""

    git: Union[str, None] = Field()
    html: Union[str, None] = Field()
    self_: str = Field(alias="self")


model_rebuild(LicenseContent)
model_rebuild(LicenseContentPropLinks)

__all__ = (
    "LicenseContent",
    "LicenseContentPropLinks",
)
