"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0005 import IntegrationType


class DeploymentSimpleType(TypedDict):
    """Deployment

    A deployment created as the result of an Actions check run from a workflow that
    references an environment
    """

    url: str
    id: int
    node_id: str
    task: str
    original_environment: NotRequired[str]
    environment: str
    description: Union[str, None]
    created_at: datetime
    updated_at: datetime
    statuses_url: str
    repository_url: str
    transient_environment: NotRequired[bool]
    production_environment: NotRequired[bool]
    performed_via_github_app: NotRequired[Union[None, IntegrationType]]


__all__ = ("DeploymentSimpleType",)
