"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType


class PersonalAccessTokenRequestType(TypedDict):
    """Personal Access Token Request

    Details of a Personal Access Token Request.
    """

    id: int
    owner: SimpleUserType
    permissions_added: PersonalAccessTokenRequestPropPermissionsAddedType
    permissions_upgraded: PersonalAccessTokenRequestPropPermissionsUpgradedType
    permissions_result: PersonalAccessTokenRequestPropPermissionsResultType
    repository_selection: Literal["none", "all", "subset"]
    repository_count: Union[int, None]
    repositories: Union[list[PersonalAccessTokenRequestPropRepositoriesItemsType], None]
    created_at: str
    token_id: int
    token_name: str
    token_expired: bool
    token_expires_at: Union[str, None]
    token_last_used_at: Union[str, None]


class PersonalAccessTokenRequestPropRepositoriesItemsType(TypedDict):
    """PersonalAccessTokenRequestPropRepositoriesItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class PersonalAccessTokenRequestPropPermissionsAddedType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsAdded

    New requested permissions, categorized by type of permission.
    """

    organization: NotRequired[
        PersonalAccessTokenRequestPropPermissionsAddedPropOrganizationType
    ]
    repository: NotRequired[
        PersonalAccessTokenRequestPropPermissionsAddedPropRepositoryType
    ]
    other: NotRequired[PersonalAccessTokenRequestPropPermissionsAddedPropOtherType]


class PersonalAccessTokenRequestPropPermissionsAddedPropOrganizationType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsAddedPropOrganization"""


class PersonalAccessTokenRequestPropPermissionsAddedPropRepositoryType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsAddedPropRepository"""


class PersonalAccessTokenRequestPropPermissionsAddedPropOtherType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsAddedPropOther"""


class PersonalAccessTokenRequestPropPermissionsUpgradedType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsUpgraded

    Requested permissions that elevate access for a previously approved request for
    access, categorized by type of permission.
    """

    organization: NotRequired[
        PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganizationType
    ]
    repository: NotRequired[
        PersonalAccessTokenRequestPropPermissionsUpgradedPropRepositoryType
    ]
    other: NotRequired[PersonalAccessTokenRequestPropPermissionsUpgradedPropOtherType]


class PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganizationType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganization"""


class PersonalAccessTokenRequestPropPermissionsUpgradedPropRepositoryType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsUpgradedPropRepository"""


class PersonalAccessTokenRequestPropPermissionsUpgradedPropOtherType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsUpgradedPropOther"""


class PersonalAccessTokenRequestPropPermissionsResultType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsResult

    Permissions requested, categorized by type of permission. This field
    incorporates `permissions_added` and `permissions_upgraded`.
    """

    organization: NotRequired[
        PersonalAccessTokenRequestPropPermissionsResultPropOrganizationType
    ]
    repository: NotRequired[
        PersonalAccessTokenRequestPropPermissionsResultPropRepositoryType
    ]
    other: NotRequired[PersonalAccessTokenRequestPropPermissionsResultPropOtherType]


class PersonalAccessTokenRequestPropPermissionsResultPropOrganizationType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsResultPropOrganization"""


class PersonalAccessTokenRequestPropPermissionsResultPropRepositoryType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsResultPropRepository"""


class PersonalAccessTokenRequestPropPermissionsResultPropOtherType(TypedDict):
    """PersonalAccessTokenRequestPropPermissionsResultPropOther"""


__all__ = (
    "PersonalAccessTokenRequestType",
    "PersonalAccessTokenRequestPropRepositoriesItemsType",
    "PersonalAccessTokenRequestPropPermissionsAddedType",
    "PersonalAccessTokenRequestPropPermissionsAddedPropOrganizationType",
    "PersonalAccessTokenRequestPropPermissionsAddedPropRepositoryType",
    "PersonalAccessTokenRequestPropPermissionsAddedPropOtherType",
    "PersonalAccessTokenRequestPropPermissionsUpgradedType",
    "PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganizationType",
    "PersonalAccessTokenRequestPropPermissionsUpgradedPropRepositoryType",
    "PersonalAccessTokenRequestPropPermissionsUpgradedPropOtherType",
    "PersonalAccessTokenRequestPropPermissionsResultType",
    "PersonalAccessTokenRequestPropPermissionsResultPropOrganizationType",
    "PersonalAccessTokenRequestPropPermissionsResultPropRepositoryType",
    "PersonalAccessTokenRequestPropPermissionsResultPropOtherType",
)
