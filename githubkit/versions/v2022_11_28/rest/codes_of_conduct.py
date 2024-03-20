"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Optional


from githubkit.utils import exclude_unset

if TYPE_CHECKING:
    from typing import List

    from githubkit import GitHubCore
    from githubkit.response import Response

    from ..models import CodeOfConduct


class CodesOfConductClient:
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

    def get_all_codes_of_conduct(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeOfConduct]]:
        """See also: https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-all-codes-of-conduct"""

        from typing import List

        from ..models import CodeOfConduct

        url = "/codes_of_conduct"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeOfConduct],
        )

    async def async_get_all_codes_of_conduct(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeOfConduct]]:
        """See also: https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-all-codes-of-conduct"""

        from typing import List

        from ..models import CodeOfConduct

        url = "/codes_of_conduct"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeOfConduct],
        )

    def get_conduct_code(
        self,
        key: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CodeOfConduct]:
        """See also: https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-a-code-of-conduct"""

        from ..models import BasicError, CodeOfConduct

        url = f"/codes_of_conduct/{key}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeOfConduct,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_conduct_code(
        self,
        key: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CodeOfConduct]:
        """See also: https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-a-code-of-conduct"""

        from ..models import BasicError, CodeOfConduct

        url = f"/codes_of_conduct/{key}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeOfConduct,
            error_models={
                "404": BasicError,
            },
        )
