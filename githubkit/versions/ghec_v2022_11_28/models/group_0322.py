"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0019 import LicenseSimple
from .group_0229 import CodeOfConductSimple


class CommunityProfilePropFiles(GitHubModel):
    """CommunityProfilePropFiles"""

    code_of_conduct: Union[None, CodeOfConductSimple] = Field()
    code_of_conduct_file: Union[None, CommunityHealthFile] = Field()
    license_: Union[None, LicenseSimple] = Field(alias="license")
    contributing: Union[None, CommunityHealthFile] = Field()
    readme: Union[None, CommunityHealthFile] = Field()
    issue_template: Union[None, CommunityHealthFile] = Field()
    pull_request_template: Union[None, CommunityHealthFile] = Field()


class CommunityHealthFile(GitHubModel):
    """Community Health File"""

    url: str = Field()
    html_url: str = Field()


class CommunityProfile(GitHubModel):
    """Community Profile

    Community Profile
    """

    health_percentage: int = Field()
    description: Union[str, None] = Field()
    documentation: Union[str, None] = Field()
    files: CommunityProfilePropFiles = Field()
    updated_at: Union[datetime, None] = Field()
    content_reports_enabled: Missing[bool] = Field(default=UNSET)


model_rebuild(CommunityProfilePropFiles)
model_rebuild(CommunityHealthFile)
model_rebuild(CommunityProfile)

__all__ = (
    "CommunityHealthFile",
    "CommunityProfile",
    "CommunityProfilePropFiles",
)
