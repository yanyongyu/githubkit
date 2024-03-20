"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0001 import SimpleUser


class PersonalAccessTokenRequest(GitHubModel):
    """Personal Access Token Request

    Details of a Personal Access Token Request.
    """

    id: int = Field(
        description="Unique identifier of the request for access via fine-grained personal access token. Used as the `pat_request_id` parameter in the list and review API calls."
    )
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    permissions_added: PersonalAccessTokenRequestPropPermissionsAdded = Field(
        description="New requested permissions, categorized by type of permission."
    )
    permissions_upgraded: PersonalAccessTokenRequestPropPermissionsUpgraded = Field(
        description="Requested permissions that elevate access for a previously approved request for access, categorized by type of permission."
    )
    permissions_result: PersonalAccessTokenRequestPropPermissionsResult = Field(
        description="Permissions requested, categorized by type of permission. This field incorporates `permissions_added` and `permissions_upgraded`."
    )
    repository_selection: Literal["none", "all", "subset"] = Field(
        description="Type of repository selection requested."
    )
    repository_count: Union[int, None] = Field(
        description="The number of repositories the token is requesting access to. This field is only populated when `repository_selection` is `subset`."
    )
    repositories: Union[
        List[PersonalAccessTokenRequestPropRepositoriesItems], None
    ] = Field(
        description="An array of repository objects the token is requesting access to. This field is only populated when `repository_selection` is `subset`."
    )
    created_at: str = Field(
        description="Date and time when the request for access was created."
    )
    token_expired: bool = Field(
        description="Whether the associated fine-grained personal access token has expired."
    )
    token_expires_at: Union[str, None] = Field(
        description="Date and time when the associated fine-grained personal access token expires."
    )
    token_last_used_at: Union[str, None] = Field(
        description="Date and time when the associated fine-grained personal access token was last used for authentication."
    )


class PersonalAccessTokenRequestPropRepositoriesItems(GitHubModel):
    """PersonalAccessTokenRequestPropRepositoriesItems"""

    full_name: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    private: bool = Field(description="Whether the repository is private or public.")


class PersonalAccessTokenRequestPropPermissionsAdded(GitHubModel):
    """PersonalAccessTokenRequestPropPermissionsAdded

    New requested permissions, categorized by type of permission.
    """

    organization: Missing[
        PersonalAccessTokenRequestPropPermissionsAddedPropOrganization
    ] = Field(default=UNSET)
    repository: Missing[
        PersonalAccessTokenRequestPropPermissionsAddedPropRepository
    ] = Field(default=UNSET)
    other: Missing[PersonalAccessTokenRequestPropPermissionsAddedPropOther] = Field(
        default=UNSET
    )


class PersonalAccessTokenRequestPropPermissionsAddedPropOrganization(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsAddedPropOrganization"""


class PersonalAccessTokenRequestPropPermissionsAddedPropRepository(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsAddedPropRepository"""


class PersonalAccessTokenRequestPropPermissionsAddedPropOther(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsAddedPropOther"""


class PersonalAccessTokenRequestPropPermissionsUpgraded(GitHubModel):
    """PersonalAccessTokenRequestPropPermissionsUpgraded

    Requested permissions that elevate access for a previously approved request for
    access, categorized by type of permission.
    """

    organization: Missing[
        PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganization
    ] = Field(default=UNSET)
    repository: Missing[
        PersonalAccessTokenRequestPropPermissionsUpgradedPropRepository
    ] = Field(default=UNSET)
    other: Missing[PersonalAccessTokenRequestPropPermissionsUpgradedPropOther] = Field(
        default=UNSET
    )


class PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganization(
    ExtraGitHubModel
):
    """PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganization"""


class PersonalAccessTokenRequestPropPermissionsUpgradedPropRepository(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsUpgradedPropRepository"""


class PersonalAccessTokenRequestPropPermissionsUpgradedPropOther(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsUpgradedPropOther"""


class PersonalAccessTokenRequestPropPermissionsResult(GitHubModel):
    """PersonalAccessTokenRequestPropPermissionsResult

    Permissions requested, categorized by type of permission. This field
    incorporates `permissions_added` and `permissions_upgraded`.
    """

    organization: Missing[
        PersonalAccessTokenRequestPropPermissionsResultPropOrganization
    ] = Field(default=UNSET)
    repository: Missing[
        PersonalAccessTokenRequestPropPermissionsResultPropRepository
    ] = Field(default=UNSET)
    other: Missing[PersonalAccessTokenRequestPropPermissionsResultPropOther] = Field(
        default=UNSET
    )


class PersonalAccessTokenRequestPropPermissionsResultPropOrganization(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsResultPropOrganization"""


class PersonalAccessTokenRequestPropPermissionsResultPropRepository(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsResultPropRepository"""


class PersonalAccessTokenRequestPropPermissionsResultPropOther(ExtraGitHubModel):
    """PersonalAccessTokenRequestPropPermissionsResultPropOther"""


model_rebuild(PersonalAccessTokenRequest)
model_rebuild(PersonalAccessTokenRequestPropRepositoriesItems)
model_rebuild(PersonalAccessTokenRequestPropPermissionsAdded)
model_rebuild(PersonalAccessTokenRequestPropPermissionsAddedPropOrganization)
model_rebuild(PersonalAccessTokenRequestPropPermissionsAddedPropRepository)
model_rebuild(PersonalAccessTokenRequestPropPermissionsAddedPropOther)
model_rebuild(PersonalAccessTokenRequestPropPermissionsUpgraded)
model_rebuild(PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganization)
model_rebuild(PersonalAccessTokenRequestPropPermissionsUpgradedPropRepository)
model_rebuild(PersonalAccessTokenRequestPropPermissionsUpgradedPropOther)
model_rebuild(PersonalAccessTokenRequestPropPermissionsResult)
model_rebuild(PersonalAccessTokenRequestPropPermissionsResultPropOrganization)
model_rebuild(PersonalAccessTokenRequestPropPermissionsResultPropRepository)
model_rebuild(PersonalAccessTokenRequestPropPermissionsResultPropOther)

__all__ = (
    "PersonalAccessTokenRequest",
    "PersonalAccessTokenRequestPropRepositoriesItems",
    "PersonalAccessTokenRequestPropPermissionsAdded",
    "PersonalAccessTokenRequestPropPermissionsAddedPropOrganization",
    "PersonalAccessTokenRequestPropPermissionsAddedPropRepository",
    "PersonalAccessTokenRequestPropPermissionsAddedPropOther",
    "PersonalAccessTokenRequestPropPermissionsUpgraded",
    "PersonalAccessTokenRequestPropPermissionsUpgradedPropOrganization",
    "PersonalAccessTokenRequestPropPermissionsUpgradedPropRepository",
    "PersonalAccessTokenRequestPropPermissionsUpgradedPropOther",
    "PersonalAccessTokenRequestPropPermissionsResult",
    "PersonalAccessTokenRequestPropPermissionsResultPropOrganization",
    "PersonalAccessTokenRequestPropPermissionsResultPropRepository",
    "PersonalAccessTokenRequestPropPermissionsResultPropOther",
)