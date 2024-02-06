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
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import License, LicenseSimple, LicenseContent


class LicensesClient:
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

    def get_all_commonly_used(
        self,
        featured: Missing[bool] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[LicenseSimple]]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-all-commonly-used-licenses"""

        from typing import List

        from ..models import LicenseSimple

        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[LicenseSimple],
        )

    async def async_get_all_commonly_used(
        self,
        featured: Missing[bool] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[LicenseSimple]]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-all-commonly-used-licenses"""

        from typing import List

        from ..models import LicenseSimple

        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[LicenseSimple],
        )

    def get(
        self,
        license_: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[License]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-a-license"""

        from ..models import License, BasicError

        url = f"/licenses/{license}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get(
        self,
        license_: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[License]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-a-license"""

        from ..models import License, BasicError

        url = f"/licenses/{license}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[LicenseContent]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository"""

        from ..models import BasicError, LicenseContent

        url = f"/repos/{owner}/{repo}/license"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=LicenseContent,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[LicenseContent]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository"""

        from ..models import BasicError, LicenseContent

        url = f"/repos/{owner}/{repo}/license"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=LicenseContent,
            error_models={
                "404": BasicError,
            },
        )
