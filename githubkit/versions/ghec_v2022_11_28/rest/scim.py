"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Optional, overload

from pydantic import BaseModel

from githubkit.typing import Missing, UnsetType
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import List

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import ScimUser, ScimUserList
    from ..types import (
        ScimV2OrganizationsOrgUsersPostBodyType,
        ScimV2OrganizationsOrgUsersPostBodyPropNameType,
        ScimV2OrganizationsOrgUsersScimUserIdPutBodyType,
        ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType,
        ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType,
        ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType,
        ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType,
        ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsType,
    )


class ScimClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def list_provisioned_identities(
        self,
        org: str,
        start_index: Missing[int] = UNSET,
        count: Missing[int] = UNSET,
        filter_: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ScimUserList]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#list-scim-provisioned-identities"""

        from ..models import ScimError, ScimUserList

        url = f"/scim/v2/organizations/{org}/Users"

        params = {
            "startIndex": start_index,
            "count": count,
            "filter": filter_,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ScimUserList,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": ScimError,
            },
        )

    async def async_list_provisioned_identities(
        self,
        org: str,
        start_index: Missing[int] = UNSET,
        count: Missing[int] = UNSET,
        filter_: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ScimUserList]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#list-scim-provisioned-identities"""

        from ..models import ScimError, ScimUserList

        url = f"/scim/v2/organizations/{org}/Users"

        params = {
            "startIndex": start_index,
            "count": count,
            "filter": filter_,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ScimUserList,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": ScimError,
            },
        )

    @overload
    def provision_and_invite_user(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ScimV2OrganizationsOrgUsersPostBodyType,
    ) -> Response[ScimUser]: ...

    @overload
    def provision_and_invite_user(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        user_name: str,
        display_name: Missing[str] = UNSET,
        name: ScimV2OrganizationsOrgUsersPostBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType],
        schemas: Missing[List[str]] = UNSET,
        external_id: Missing[str] = UNSET,
        groups: Missing[List[str]] = UNSET,
        active: Missing[bool] = UNSET,
    ) -> Response[ScimUser]: ...

    def provision_and_invite_user(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ScimV2OrganizationsOrgUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#provision-and-invite-a-scim-user"""

        from ..models import ScimUser, ScimError, ScimV2OrganizationsOrgUsersPostBody

        url = f"/scim/v2/organizations/{org}/Users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(ScimV2OrganizationsOrgUsersPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "500": ScimError,
                "409": ScimError,
                "400": ScimError,
            },
        )

    @overload
    async def async_provision_and_invite_user(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ScimV2OrganizationsOrgUsersPostBodyType,
    ) -> Response[ScimUser]: ...

    @overload
    async def async_provision_and_invite_user(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        user_name: str,
        display_name: Missing[str] = UNSET,
        name: ScimV2OrganizationsOrgUsersPostBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType],
        schemas: Missing[List[str]] = UNSET,
        external_id: Missing[str] = UNSET,
        groups: Missing[List[str]] = UNSET,
        active: Missing[bool] = UNSET,
    ) -> Response[ScimUser]: ...

    async def async_provision_and_invite_user(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ScimV2OrganizationsOrgUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#provision-and-invite-a-scim-user"""

        from ..models import ScimUser, ScimError, ScimV2OrganizationsOrgUsersPostBody

        url = f"/scim/v2/organizations/{org}/Users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(ScimV2OrganizationsOrgUsersPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "500": ScimError,
                "409": ScimError,
                "400": ScimError,
            },
        )

    def get_provisioning_information_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#get-scim-provisioning-information-for-a-user"""

        from ..models import ScimUser, ScimError

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_get_provisioning_information_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#get-scim-provisioning-information-for-a-user"""

        from ..models import ScimUser, ScimError

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    @overload
    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ScimV2OrganizationsOrgUsersScimUserIdPutBodyType,
    ) -> Response[ScimUser]: ...

    @overload
    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        schemas: Missing[List[str]] = UNSET,
        display_name: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        groups: Missing[List[str]] = UNSET,
        active: Missing[bool] = UNSET,
        user_name: str,
        name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType],
    ) -> Response[ScimUser]: ...

    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ScimV2OrganizationsOrgUsersScimUserIdPutBodyType] = UNSET,
        **kwargs,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#update-a-provisioned-organization-membership"""

        from ..models import (
            ScimUser,
            ScimError,
            ScimV2OrganizationsOrgUsersScimUserIdPutBody,
        )

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(ScimV2OrganizationsOrgUsersScimUserIdPutBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    @overload
    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ScimV2OrganizationsOrgUsersScimUserIdPutBodyType,
    ) -> Response[ScimUser]: ...

    @overload
    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        schemas: Missing[List[str]] = UNSET,
        display_name: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        groups: Missing[List[str]] = UNSET,
        active: Missing[bool] = UNSET,
        user_name: str,
        name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType],
    ) -> Response[ScimUser]: ...

    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ScimV2OrganizationsOrgUsersScimUserIdPutBodyType] = UNSET,
        **kwargs,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#update-a-provisioned-organization-membership"""

        from ..models import (
            ScimUser,
            ScimError,
            ScimV2OrganizationsOrgUsersScimUserIdPutBody,
        )

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(ScimV2OrganizationsOrgUsersScimUserIdPutBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    def delete_user_from_org(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#delete-a-scim-user-from-an-organization"""

        from ..models import ScimError

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_delete_user_from_org(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#delete-a-scim-user-from-an-organization"""

        from ..models import ScimError

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    @overload
    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType,
    ) -> Response[ScimUser]: ...

    @overload
    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        schemas: Missing[List[str]] = UNSET,
        operations: List[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsType
        ],
    ) -> Response[ScimUser]: ...

    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType] = UNSET,
        **kwargs,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#update-an-attribute-for-a-scim-user"""

        from ..models import (
            ScimUser,
            ScimError,
            BasicError,
            ScimV2OrganizationsOrgUsersScimUserIdPatchBody,
        )

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            ScimV2OrganizationsOrgUsersScimUserIdPatchBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": BasicError,
            },
        )

    @overload
    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType,
    ) -> Response[ScimUser]: ...

    @overload
    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        schemas: Missing[List[str]] = UNSET,
        operations: List[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsType
        ],
    ) -> Response[ScimUser]: ...

    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType] = UNSET,
        **kwargs,
    ) -> Response[ScimUser]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/scim/scim#update-an-attribute-for-a-scim-user"""

        from ..models import (
            ScimUser,
            ScimError,
            BasicError,
            ScimV2OrganizationsOrgUsersScimUserIdPatchBody,
        )

        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            ScimV2OrganizationsOrgUsersScimUserIdPatchBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": BasicError,
            },
        )
