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
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0053 import BypassResponse


class PushRuleBypassRequest(GitHubModel):
    """Push rule bypass request

    A bypass request made by a user asking to be exempted from a push rule in this
    repository.
    """

    id: Missing[int] = Field(
        default=UNSET, description="The unique identifier of the bypass request."
    )
    number: Missing[int] = Field(
        default=UNSET,
        description="The number uniquely identifying the bypass request within its repository.",
    )
    repository: Missing[PushRuleBypassRequestPropRepository] = Field(
        default=UNSET, description="The repository the bypass request is for."
    )
    organization: Missing[PushRuleBypassRequestPropOrganization] = Field(
        default=UNSET,
        description="The organization associated with the repository the bypass request is for.",
    )
    requester: Missing[PushRuleBypassRequestPropRequester] = Field(
        default=UNSET, description="The user who requested the bypass."
    )
    request_type: Missing[str] = Field(
        default=UNSET, description="The type of request."
    )
    data: Missing[Union[list[PushRuleBypassRequestPropDataItems], None]] = Field(
        default=UNSET,
        description="Data describing the push rules that are being requested to be bypassed.",
    )
    resource_identifier: Missing[str] = Field(
        default=UNSET,
        description="The unique identifier for the request type of the bypass request. For example, a commit SHA.",
    )
    status: Missing[
        Literal[
            "pending",
            "denied",
            "approved",
            "cancelled",
            "completed",
            "expired",
            "deleted",
            "open",
        ]
    ] = Field(default=UNSET, description="The status of the bypass request.")
    requester_comment: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The comment the requester provided when creating the bypass request.",
    )
    expires_at: Missing[datetime] = Field(
        default=UNSET, description="The date and time the bypass request will expire."
    )
    created_at: Missing[datetime] = Field(
        default=UNSET, description="The date and time the bypass request was created."
    )
    responses: Missing[Union[list[BypassResponse], None]] = Field(
        default=UNSET, description="The responses to the bypass request."
    )
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(
        default=UNSET, description="The URL to view the bypass request in a browser."
    )


class PushRuleBypassRequestPropRepository(GitHubModel):
    """PushRuleBypassRequestPropRepository

    The repository the bypass request is for.
    """

    id: Missing[Union[int, None]] = Field(
        default=UNSET, description="The ID of the repository the bypass request is for."
    )
    name: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The name of the repository the bypass request is for.",
    )
    full_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The full name of the repository the bypass request is for.",
    )


class PushRuleBypassRequestPropOrganization(GitHubModel):
    """PushRuleBypassRequestPropOrganization

    The organization associated with the repository the bypass request is for.
    """

    id: Missing[Union[int, None]] = Field(
        default=UNSET, description="The ID of the organization."
    )
    name: Missing[Union[str, None]] = Field(
        default=UNSET, description="The name of the organization."
    )


class PushRuleBypassRequestPropRequester(GitHubModel):
    """PushRuleBypassRequestPropRequester

    The user who requested the bypass.
    """

    actor_id: Missing[int] = Field(
        default=UNSET, description="The ID of the GitHub user who requested the bypass."
    )
    actor_name: Missing[str] = Field(
        default=UNSET,
        description="The name of the GitHub user who requested the bypass.",
    )


class PushRuleBypassRequestPropDataItems(GitHubModel):
    """PushRuleBypassRequestPropDataItems"""

    ruleset_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the ruleset for the rules that were violated.",
    )
    ruleset_name: Missing[str] = Field(
        default=UNSET,
        description="The name of the ruleset for the rules that were violated.",
    )
    total_violations: Missing[int] = Field(
        default=UNSET,
        description="The number of rule violations generated from the push associated with this request.",
    )
    rule_type: Missing[str] = Field(
        default=UNSET, description="The type of rule that was violated."
    )


model_rebuild(PushRuleBypassRequest)
model_rebuild(PushRuleBypassRequestPropRepository)
model_rebuild(PushRuleBypassRequestPropOrganization)
model_rebuild(PushRuleBypassRequestPropRequester)
model_rebuild(PushRuleBypassRequestPropDataItems)

__all__ = (
    "PushRuleBypassRequest",
    "PushRuleBypassRequestPropDataItems",
    "PushRuleBypassRequestPropOrganization",
    "PushRuleBypassRequestPropRepository",
    "PushRuleBypassRequestPropRequester",
)
