"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from weakref import ref

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response
    from githubkit.typing import Missing
    from githubkit.utils import UNSET

    from ..models import (
        ActionsBillingUsage,
        BillingUsageReport,
        CombinedBillingUsage,
        PackagesBillingUsage,
    )
    from ..types import (
        ActionsBillingUsageType,
        BillingUsageReportType,
        CombinedBillingUsageType,
        PackagesBillingUsageType,
    )


class BillingClient:
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

    def get_github_billing_usage_report_org(
        self,
        org: str,
        *,
        year: Missing[int] = UNSET,
        month: Missing[int] = UNSET,
        day: Missing[int] = UNSET,
        hour: Missing[int] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[BillingUsageReport, BillingUsageReportType]:
        """See also: https://docs.github.com/rest/billing/enhanced-billing#get-billing-usage-report-for-an-organization"""

        from ..models import (
            BasicError,
            BillingUsageReport,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/organizations/{org}/settings/billing/usage"

        params = {
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=BillingUsageReport,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "500": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_github_billing_usage_report_org(
        self,
        org: str,
        *,
        year: Missing[int] = UNSET,
        month: Missing[int] = UNSET,
        day: Missing[int] = UNSET,
        hour: Missing[int] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[BillingUsageReport, BillingUsageReportType]:
        """See also: https://docs.github.com/rest/billing/enhanced-billing#get-billing-usage-report-for-an-organization"""

        from ..models import (
            BasicError,
            BillingUsageReport,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/organizations/{org}/settings/billing/usage"

        params = {
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=BillingUsageReport,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "500": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_github_actions_billing_org(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-an-organization"""

        from ..models import ActionsBillingUsage

        url = f"/orgs/{org}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    async def async_get_github_actions_billing_org(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-an-organization"""

        from ..models import ActionsBillingUsage

        url = f"/orgs/{org}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    def get_github_packages_billing_org(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-an-organization"""

        from ..models import PackagesBillingUsage

        url = f"/orgs/{org}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    async def async_get_github_packages_billing_org(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-an-organization"""

        from ..models import PackagesBillingUsage

        url = f"/orgs/{org}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    def get_shared_storage_billing_org(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-an-organization"""

        from ..models import CombinedBillingUsage

        url = f"/orgs/{org}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )

    async def async_get_shared_storage_billing_org(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-an-organization"""

        from ..models import CombinedBillingUsage

        url = f"/orgs/{org}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )

    def get_github_actions_billing_user(
        self,
        username: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-a-user"""

        from ..models import ActionsBillingUsage

        url = f"/users/{username}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    async def async_get_github_actions_billing_user(
        self,
        username: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-a-user"""

        from ..models import ActionsBillingUsage

        url = f"/users/{username}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    def get_github_packages_billing_user(
        self,
        username: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-a-user"""

        from ..models import PackagesBillingUsage

        url = f"/users/{username}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    async def async_get_github_packages_billing_user(
        self,
        username: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-a-user"""

        from ..models import PackagesBillingUsage

        url = f"/users/{username}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    def get_shared_storage_billing_user(
        self,
        username: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-a-user"""

        from ..models import CombinedBillingUsage

        url = f"/users/{username}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )

    async def async_get_shared_storage_billing_user(
        self,
        username: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-a-user"""

        from ..models import CombinedBillingUsage

        url = f"/users/{username}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )
