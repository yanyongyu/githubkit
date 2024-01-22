"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from weakref import ref
from typing_extensions import Annotated
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import Field, BaseModel

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import Union, Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..types import InteractionLimitType
    from ..models import (
        InteractionLimitResponse,
        UserInteractionLimitsGetResponse200Anyof1,
        OrgsOrgInteractionLimitsGetResponse200Anyof1,
        ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
    )


class InteractionsClient:
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

    def get_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[
        Union[InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1]
    ]:
        """See also: https://docs.github.com/rest/interactions/orgs#get-interaction-restrictions-for-an-organization"""

        from typing import Union

        from ..models import (
            InteractionLimitResponse,
            OrgsOrgInteractionLimitsGetResponse200Anyof1,
        )

        url = f"/orgs/{org}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Union[
                InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1
            ],
        )

    async def async_get_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[
        Union[InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1]
    ]:
        """See also: https://docs.github.com/rest/interactions/orgs#get-interaction-restrictions-for-an-organization"""

        from typing import Union

        from ..models import (
            InteractionLimitResponse,
            OrgsOrgInteractionLimitsGetResponse200Anyof1,
        )

        url = f"/orgs/{org}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Union[
                InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1
            ],
        )

    @overload
    def set_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: InteractionLimitType,
    ) -> Response[InteractionLimitResponse]:
        ...

    @overload
    def set_restrictions_for_org(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Missing[
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
        ] = UNSET,
    ) -> Response[InteractionLimitResponse]:
        ...

    def set_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[InteractionLimitType] = UNSET,
        **kwargs,
    ) -> Response[InteractionLimitResponse]:
        """See also: https://docs.github.com/rest/interactions/orgs#set-interaction-restrictions-for-an-organization"""

        from ..models import ValidationError, InteractionLimit, InteractionLimitResponse

        url = f"/orgs/{org}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(InteractionLimit, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_set_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: InteractionLimitType,
    ) -> Response[InteractionLimitResponse]:
        ...

    @overload
    async def async_set_restrictions_for_org(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Missing[
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
        ] = UNSET,
    ) -> Response[InteractionLimitResponse]:
        ...

    async def async_set_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[InteractionLimitType] = UNSET,
        **kwargs,
    ) -> Response[InteractionLimitResponse]:
        """See also: https://docs.github.com/rest/interactions/orgs#set-interaction-restrictions-for-an-organization"""

        from ..models import ValidationError, InteractionLimit, InteractionLimitResponse

        url = f"/orgs/{org}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(InteractionLimit, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    def remove_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/interactions/orgs#remove-interaction-restrictions-for-an-organization"""

        url = f"/orgs/{org}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
        )

    async def async_remove_restrictions_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/interactions/orgs#remove-interaction-restrictions-for-an-organization"""

        url = f"/orgs/{org}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
        )

    def get_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[
        Union[
            InteractionLimitResponse,
            ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
        ]
    ]:
        """See also: https://docs.github.com/rest/interactions/repos#get-interaction-restrictions-for-a-repository"""

        from typing import Union

        from ..models import (
            InteractionLimitResponse,
            ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
        )

        url = f"/repos/{owner}/{repo}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Union[
                InteractionLimitResponse,
                ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
            ],
        )

    async def async_get_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[
        Union[
            InteractionLimitResponse,
            ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
        ]
    ]:
        """See also: https://docs.github.com/rest/interactions/repos#get-interaction-restrictions-for-a-repository"""

        from typing import Union

        from ..models import (
            InteractionLimitResponse,
            ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
        )

        url = f"/repos/{owner}/{repo}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Union[
                InteractionLimitResponse,
                ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
            ],
        )

    @overload
    def set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: InteractionLimitType,
    ) -> Response[InteractionLimitResponse]:
        ...

    @overload
    def set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Missing[
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
        ] = UNSET,
    ) -> Response[InteractionLimitResponse]:
        ...

    def set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[InteractionLimitType] = UNSET,
        **kwargs,
    ) -> Response[InteractionLimitResponse]:
        """See also: https://docs.github.com/rest/interactions/repos#set-interaction-restrictions-for-a-repository"""

        from ..models import InteractionLimit, InteractionLimitResponse

        url = f"/repos/{owner}/{repo}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(InteractionLimit, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=InteractionLimitResponse,
            error_models={},
        )

    @overload
    async def async_set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: InteractionLimitType,
    ) -> Response[InteractionLimitResponse]:
        ...

    @overload
    async def async_set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Missing[
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
        ] = UNSET,
    ) -> Response[InteractionLimitResponse]:
        ...

    async def async_set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[InteractionLimitType] = UNSET,
        **kwargs,
    ) -> Response[InteractionLimitResponse]:
        """See also: https://docs.github.com/rest/interactions/repos#set-interaction-restrictions-for-a-repository"""

        from ..models import InteractionLimit, InteractionLimitResponse

        url = f"/repos/{owner}/{repo}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(InteractionLimit, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=InteractionLimitResponse,
            error_models={},
        )

    def remove_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/interactions/repos#remove-interaction-restrictions-for-a-repository"""

        url = f"/repos/{owner}/{repo}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={},
        )

    async def async_remove_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/interactions/repos#remove-interaction-restrictions-for-a-repository"""

        url = f"/repos/{owner}/{repo}/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={},
        )

    def get_restrictions_for_authenticated_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[
        Union[InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1]
    ]:
        """See also: https://docs.github.com/rest/interactions/user#get-interaction-restrictions-for-your-public-repositories"""

        from typing import Union

        from ..models import (
            InteractionLimitResponse,
            UserInteractionLimitsGetResponse200Anyof1,
        )

        url = "/user/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Union[
                InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1
            ],
        )

    async def async_get_restrictions_for_authenticated_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[
        Union[InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1]
    ]:
        """See also: https://docs.github.com/rest/interactions/user#get-interaction-restrictions-for-your-public-repositories"""

        from typing import Union

        from ..models import (
            InteractionLimitResponse,
            UserInteractionLimitsGetResponse200Anyof1,
        )

        url = "/user/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Union[
                InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1
            ],
        )

    @overload
    def set_restrictions_for_authenticated_user(
        self, *, headers: Optional[Dict[str, str]] = None, data: InteractionLimitType
    ) -> Response[InteractionLimitResponse]:
        ...

    @overload
    def set_restrictions_for_authenticated_user(
        self,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Missing[
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
        ] = UNSET,
    ) -> Response[InteractionLimitResponse]:
        ...

    def set_restrictions_for_authenticated_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[InteractionLimitType] = UNSET,
        **kwargs,
    ) -> Response[InteractionLimitResponse]:
        """See also: https://docs.github.com/rest/interactions/user#set-interaction-restrictions-for-your-public-repositories"""

        from ..models import ValidationError, InteractionLimit, InteractionLimitResponse

        url = "/user/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(InteractionLimit, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_set_restrictions_for_authenticated_user(
        self, *, headers: Optional[Dict[str, str]] = None, data: InteractionLimitType
    ) -> Response[InteractionLimitResponse]:
        ...

    @overload
    async def async_set_restrictions_for_authenticated_user(
        self,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Missing[
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
        ] = UNSET,
    ) -> Response[InteractionLimitResponse]:
        ...

    async def async_set_restrictions_for_authenticated_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[InteractionLimitType] = UNSET,
        **kwargs,
    ) -> Response[InteractionLimitResponse]:
        """See also: https://docs.github.com/rest/interactions/user#set-interaction-restrictions-for-your-public-repositories"""

        from ..models import ValidationError, InteractionLimit, InteractionLimitResponse

        url = "/user/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(InteractionLimit, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    def remove_restrictions_for_authenticated_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/interactions/user#remove-interaction-restrictions-from-your-public-repositories"""

        url = "/user/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
        )

    async def async_remove_restrictions_for_authenticated_user(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/interactions/user#remove-interaction-restrictions-from-your-public-repositories"""

        url = "/user/interaction-limits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
        )
