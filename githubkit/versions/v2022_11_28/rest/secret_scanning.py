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
    from typing import List, Union, Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..types import ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
    from ..models import (
        SecretScanningAlert,
        SecretScanningLocation,
        OrganizationSecretScanningAlert,
    )


class SecretScanningClient:
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

    def list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[OrganizationSecretScanningAlert]]:
        from typing import List

        from ..models import (
            BasicError,
            OrganizationSecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[OrganizationSecretScanningAlert]]:
        from typing import List

        from ..models import (
            BasicError,
            OrganizationSecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_org(
        self,
        org: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[OrganizationSecretScanningAlert]]:
        from typing import List

        from ..models import (
            BasicError,
            OrganizationSecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[OrganizationSecretScanningAlert]]:
        from typing import List

        from ..models import (
            BasicError,
            OrganizationSecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SecretScanningAlert]]:
        from typing import List

        from ..models import (
            SecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SecretScanningAlert]]:
        from typing import List

        from ..models import (
            SecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SecretScanningAlert]:
        from ..models import (
            SecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SecretScanningAlert]:
        from ..models import (
            SecretScanningAlert,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> Response[SecretScanningAlert]:
        ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        state: Literal["open", "resolved"],
        resolution: Missing[
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ]
        ] = UNSET,
        resolution_comment: Missing[Union[str, None]] = UNSET,
    ) -> Response[SecretScanningAlert]:
        ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[SecretScanningAlert]:
        from ..models import (
            SecretScanningAlert,
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> Response[SecretScanningAlert]:
        ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        state: Literal["open", "resolved"],
        resolution: Missing[
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ]
        ] = UNSET,
        resolution_comment: Missing[Union[str, None]] = UNSET,
    ) -> Response[SecretScanningAlert]:
        ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[SecretScanningAlert]:
        from ..models import (
            SecretScanningAlert,
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SecretScanningLocation]]:
        from typing import List

        from ..models import (
            SecretScanningLocation,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SecretScanningLocation]]:
        from typing import List

        from ..models import (
            SecretScanningLocation,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )
