"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0012 import EnterpriseType
from .group_0014 import AppPermissionsType


class InstallationType(TypedDict):
    """Installation

    Installation
    """

    id: int
    account: Union[SimpleUserType, EnterpriseType, None]
    repository_selection: Literal["all", "selected"]
    access_tokens_url: str
    repositories_url: str
    html_url: str
    app_id: int
    target_id: int
    target_type: str
    permissions: AppPermissionsType
    events: List[str]
    created_at: datetime
    updated_at: datetime
    single_file_name: Union[str, None]
    has_multiple_single_files: NotRequired[bool]
    single_file_paths: NotRequired[List[str]]
    app_slug: str
    suspended_by: Union[None, SimpleUserType]
    suspended_at: Union[datetime, None]
    contact_email: NotRequired[Union[str, None]]


__all__ = ("InstallationType",)
