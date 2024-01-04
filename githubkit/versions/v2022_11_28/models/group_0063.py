"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RunnerApplication(GitHubModel):
    """Runner Application

    Runner Application
    """

    os: str = Field()
    architecture: str = Field()
    download_url: str = Field()
    filename: str = Field()
    temp_download_token: Missing[str] = Field(
        default=UNSET,
        description="A short lived bearer token used to download the runner, if needed.",
    )
    sha256_checksum: Missing[str] = Field(default=UNSET)


model_rebuild(RunnerApplication)

__all__ = ("RunnerApplication",)
