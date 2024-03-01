"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0071 import Codespace


class ReposOwnerRepoCodespacesGetResponse200(GitHubModel):
    """ReposOwnerRepoCodespacesGetResponse200"""

    total_count: int = Field()
    codespaces: List[Codespace] = Field()


model_rebuild(ReposOwnerRepoCodespacesGetResponse200)

__all__ = ("ReposOwnerRepoCodespacesGetResponse200",)
