"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Optional

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import ServerStatisticsItems


class ServerStatisticsClient:
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

    def get_server_statistics(
        self,
        enterprise_or_org: str,
        date_start: Missing[str] = UNSET,
        date_end: Missing[str] = UNSET,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[list[ServerStatisticsItems]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/enterprise-admin/admin-stats#get-github-enterprise-server-statistics"""

        from ..models import ServerStatisticsItems

        url = f"/enterprise-installation/{enterprise_or_org}/server-statistics"

        params = {
            "date_start": date_start,
            "date_end": date_end,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=list[ServerStatisticsItems],
        )

    async def async_get_server_statistics(
        self,
        enterprise_or_org: str,
        date_start: Missing[str] = UNSET,
        date_end: Missing[str] = UNSET,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[list[ServerStatisticsItems]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/enterprise-admin/admin-stats#get-github-enterprise-server-statistics"""

        from ..models import ServerStatisticsItems

        url = f"/enterprise-installation/{enterprise_or_org}/server-statistics"

        params = {
            "date_start": date_start,
            "date_end": date_end,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=list[ServerStatisticsItems],
        )
