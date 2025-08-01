"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0071 import ActionsHostedRunnerMachineSpecType


class ActionsHostedRunnerType(TypedDict):
    """GitHub-hosted hosted runner

    A Github-hosted hosted runner.
    """

    id: int
    name: str
    runner_group_id: NotRequired[int]
    image_details: Union[None, ActionsHostedRunnerPoolImageType]
    machine_size_details: ActionsHostedRunnerMachineSpecType
    status: Literal["Ready", "Provisioning", "Shutdown", "Deleting", "Stuck"]
    platform: str
    maximum_runners: NotRequired[int]
    public_ip_enabled: bool
    public_ips: NotRequired[list[PublicIpType]]
    last_active_on: NotRequired[Union[datetime, None]]


class ActionsHostedRunnerPoolImageType(TypedDict):
    """GitHub-hosted runner image details.

    Provides details of a hosted runner image
    """

    id: str
    size_gb: int
    display_name: str
    source: Literal["github", "partner", "custom"]


class PublicIpType(TypedDict):
    """Public IP for a GitHub-hosted larger runners.

    Provides details of Public IP for a GitHub-hosted larger runners
    """

    enabled: NotRequired[bool]
    prefix: NotRequired[str]
    length: NotRequired[int]


__all__ = (
    "ActionsHostedRunnerPoolImageType",
    "ActionsHostedRunnerType",
    "PublicIpType",
)
