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
    from typing import List

    from githubkit import GitHubCore
    from githubkit.response import Response

    from ..types import OidcCustomSubType
    from ..models import EmptyObject, OidcCustomSub


class OidcClient:
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

    def get_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[OidcCustomSub]:
        from ..models import OidcCustomSub

        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OidcCustomSub,
        )

    async def async_get_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[OidcCustomSub]:
        from ..models import OidcCustomSub

        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OidcCustomSub,
        )

    @overload
    def update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OidcCustomSubType,
    ) -> Response[EmptyObject]:
        ...

    @overload
    def update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        include_claim_keys: List[str],
    ) -> Response[EmptyObject]:
        ...

    def update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OidcCustomSubType] = UNSET,
        **kwargs,
    ) -> Response[EmptyObject]:
        from ..models import BasicError, EmptyObject, OidcCustomSub

        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OidcCustomSub, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    @overload
    async def async_update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OidcCustomSubType,
    ) -> Response[EmptyObject]:
        ...

    @overload
    async def async_update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        include_claim_keys: List[str],
    ) -> Response[EmptyObject]:
        ...

    async def async_update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OidcCustomSubType] = UNSET,
        **kwargs,
    ) -> Response[EmptyObject]:
        from ..models import BasicError, EmptyObject, OidcCustomSub

        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(OidcCustomSub, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )
