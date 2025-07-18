"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class CodeScanningAlertDismissalRequestType(TypedDict):
    """Code scanning alert dismissal request

    Alert dismisal request made by a user asking to dismiss a code scanning alert.
    """

    id: NotRequired[int]
    number: NotRequired[int]
    repository: NotRequired[CodeScanningAlertDismissalRequestPropRepositoryType]
    organization: NotRequired[CodeScanningAlertDismissalRequestPropOrganizationType]
    requester: NotRequired[CodeScanningAlertDismissalRequestPropRequesterType]
    request_type: NotRequired[str]
    data: NotRequired[
        Union[list[CodeScanningAlertDismissalRequestPropDataItemsType], None]
    ]
    resource_identifier: NotRequired[str]
    status: NotRequired[Literal["pending", "denied", "approved", "expired"]]
    requester_comment: NotRequired[Union[str, None]]
    expires_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    responses: NotRequired[Union[list[DismissalRequestResponseType], None]]
    url: NotRequired[str]
    html_url: NotRequired[str]


class CodeScanningAlertDismissalRequestPropRepositoryType(TypedDict):
    """CodeScanningAlertDismissalRequestPropRepository

    The repository the dismissal request is for.
    """

    id: NotRequired[int]
    name: NotRequired[str]
    full_name: NotRequired[str]


class CodeScanningAlertDismissalRequestPropOrganizationType(TypedDict):
    """CodeScanningAlertDismissalRequestPropOrganization

    The organization associated with the repository the dismissal request is for.
    """

    id: NotRequired[int]
    name: NotRequired[str]


class CodeScanningAlertDismissalRequestPropRequesterType(TypedDict):
    """CodeScanningAlertDismissalRequestPropRequester

    The user who requested the dismissal request.
    """

    actor_id: NotRequired[int]
    actor_name: NotRequired[str]


class CodeScanningAlertDismissalRequestPropDataItemsType(TypedDict):
    """CodeScanningAlertDismissalRequestPropDataItems"""

    reason: NotRequired[str]
    alert_number: NotRequired[str]
    pr_review_thread_id: NotRequired[str]


class DismissalRequestResponseType(TypedDict):
    """Dismissal request response

    A response made by a requester to dismiss the request.
    """

    id: NotRequired[int]
    reviewer: NotRequired[DismissalRequestResponsePropReviewerType]
    message: NotRequired[Union[str, None]]
    status: NotRequired[Literal["approved", "denied", "dismissed"]]
    created_at: NotRequired[datetime]


class DismissalRequestResponsePropReviewerType(TypedDict):
    """DismissalRequestResponsePropReviewer

    The user who reviewed the dismissal request.
    """

    actor_id: NotRequired[int]
    actor_name: NotRequired[str]


__all__ = (
    "CodeScanningAlertDismissalRequestPropDataItemsType",
    "CodeScanningAlertDismissalRequestPropOrganizationType",
    "CodeScanningAlertDismissalRequestPropRepositoryType",
    "CodeScanningAlertDismissalRequestPropRequesterType",
    "CodeScanningAlertDismissalRequestType",
    "DismissalRequestResponsePropReviewerType",
    "DismissalRequestResponseType",
)
