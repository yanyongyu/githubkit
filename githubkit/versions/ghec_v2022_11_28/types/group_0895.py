"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class EnterprisesEnterpriseActionsHostedRunnersHostedRunnerIdPatchBodyType(TypedDict):
    """EnterprisesEnterpriseActionsHostedRunnersHostedRunnerIdPatchBody"""

    name: NotRequired[str]
    runner_group_id: NotRequired[int]
    maximum_runners: NotRequired[int]
    enable_static_ip: NotRequired[bool]


__all__ = ("EnterprisesEnterpriseActionsHostedRunnersHostedRunnerIdPatchBodyType",)
