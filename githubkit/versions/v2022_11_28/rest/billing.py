"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from collections.abc import Mapping
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
        BillingUsageReportUser,
        CombinedBillingUsage,
        PackagesBillingUsage,
    )
    from ..types import (
        ActionsBillingUsageType,
        BillingUsageReportType,
        BillingUsageReportUserType,
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
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[BillingUsageReport, BillingUsageReportType]:
        """billing/get-github-billing-usage-report-org

        GET /organizations/{org}/settings/billing/usage

        Gets a report of the total usage for an organization. To use this endpoint, you must be an administrator of an organization within an enterprise or an organization account.

        **Note:** This endpoint is only available to organizations with access to the enhanced billing platform. For more information, see "[About the enhanced billing platform](https://docs.github.com/billing/using-the-new-billing-platform)."

        See also: https://docs.github.com/rest/billing/enhanced-billing#get-billing-usage-report-for-an-organization
        """

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
            stream=stream,
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
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[BillingUsageReport, BillingUsageReportType]:
        """billing/get-github-billing-usage-report-org

        GET /organizations/{org}/settings/billing/usage

        Gets a report of the total usage for an organization. To use this endpoint, you must be an administrator of an organization within an enterprise or an organization account.

        **Note:** This endpoint is only available to organizations with access to the enhanced billing platform. For more information, see "[About the enhanced billing platform](https://docs.github.com/billing/using-the-new-billing-platform)."

        See also: https://docs.github.com/rest/billing/enhanced-billing#get-billing-usage-report-for-an-organization
        """

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
            stream=stream,
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
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """billing/get-github-actions-billing-org

        GET /orgs/{org}/settings/billing/actions

        Gets the summary of the free and paid GitHub Actions minutes used.

        Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-an-organization
        """

        from ..models import ActionsBillingUsage

        url = f"/orgs/{org}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=ActionsBillingUsage,
        )

    async def async_get_github_actions_billing_org(
        self,
        org: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """billing/get-github-actions-billing-org

        GET /orgs/{org}/settings/billing/actions

        Gets the summary of the free and paid GitHub Actions minutes used.

        Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-an-organization
        """

        from ..models import ActionsBillingUsage

        url = f"/orgs/{org}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=ActionsBillingUsage,
        )

    def get_github_packages_billing_org(
        self,
        org: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """billing/get-github-packages-billing-org

        GET /orgs/{org}/settings/billing/packages

        Gets the free and paid storage used for GitHub Packages in gigabytes.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-an-organization
        """

        from ..models import PackagesBillingUsage

        url = f"/orgs/{org}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=PackagesBillingUsage,
        )

    async def async_get_github_packages_billing_org(
        self,
        org: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """billing/get-github-packages-billing-org

        GET /orgs/{org}/settings/billing/packages

        Gets the free and paid storage used for GitHub Packages in gigabytes.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-an-organization
        """

        from ..models import PackagesBillingUsage

        url = f"/orgs/{org}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=PackagesBillingUsage,
        )

    def get_shared_storage_billing_org(
        self,
        org: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """billing/get-shared-storage-billing-org

        GET /orgs/{org}/settings/billing/shared-storage

        Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-an-organization
        """

        from ..models import CombinedBillingUsage

        url = f"/orgs/{org}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=CombinedBillingUsage,
        )

    async def async_get_shared_storage_billing_org(
        self,
        org: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """billing/get-shared-storage-billing-org

        GET /orgs/{org}/settings/billing/shared-storage

        Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-an-organization
        """

        from ..models import CombinedBillingUsage

        url = f"/orgs/{org}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=CombinedBillingUsage,
        )

    def get_github_actions_billing_user(
        self,
        username: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """billing/get-github-actions-billing-user

        GET /users/{username}/settings/billing/actions

        Gets the summary of the free and paid GitHub Actions minutes used.

        Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-a-user
        """

        from ..models import ActionsBillingUsage

        url = f"/users/{username}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=ActionsBillingUsage,
        )

    async def async_get_github_actions_billing_user(
        self,
        username: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[ActionsBillingUsage, ActionsBillingUsageType]:
        """billing/get-github-actions-billing-user

        GET /users/{username}/settings/billing/actions

        Gets the summary of the free and paid GitHub Actions minutes used.

        Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-actions-billing-for-a-user
        """

        from ..models import ActionsBillingUsage

        url = f"/users/{username}/settings/billing/actions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=ActionsBillingUsage,
        )

    def get_github_packages_billing_user(
        self,
        username: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """billing/get-github-packages-billing-user

        GET /users/{username}/settings/billing/packages

        Gets the free and paid storage used for GitHub Packages in gigabytes.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-a-user
        """

        from ..models import PackagesBillingUsage

        url = f"/users/{username}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=PackagesBillingUsage,
        )

    async def async_get_github_packages_billing_user(
        self,
        username: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[PackagesBillingUsage, PackagesBillingUsageType]:
        """billing/get-github-packages-billing-user

        GET /users/{username}/settings/billing/packages

        Gets the free and paid storage used for GitHub Packages in gigabytes.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-github-packages-billing-for-a-user
        """

        from ..models import PackagesBillingUsage

        url = f"/users/{username}/settings/billing/packages"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=PackagesBillingUsage,
        )

    def get_shared_storage_billing_user(
        self,
        username: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """billing/get-shared-storage-billing-user

        GET /users/{username}/settings/billing/shared-storage

        Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-a-user
        """

        from ..models import CombinedBillingUsage

        url = f"/users/{username}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=CombinedBillingUsage,
        )

    async def async_get_shared_storage_billing_user(
        self,
        username: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[CombinedBillingUsage, CombinedBillingUsageType]:
        """billing/get-shared-storage-billing-user

        GET /users/{username}/settings/billing/shared-storage

        Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.

        Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

        See also: https://docs.github.com/rest/billing/billing#get-shared-storage-billing-for-a-user
        """

        from ..models import CombinedBillingUsage

        url = f"/users/{username}/settings/billing/shared-storage"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            stream=stream,
            response_model=CombinedBillingUsage,
        )

    def get_github_billing_usage_report_user(
        self,
        username: str,
        *,
        year: Missing[int] = UNSET,
        month: Missing[int] = UNSET,
        day: Missing[int] = UNSET,
        hour: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[BillingUsageReportUser, BillingUsageReportUserType]:
        """billing/get-github-billing-usage-report-user

        GET /users/{username}/settings/billing/usage

        Gets a report of the total usage for a user.

        **Note:** This endpoint is only available to users with access to the enhanced billing platform.

        See also: https://docs.github.com/rest/billing/enhanced-billing#get-billing-usage-report-for-a-user
        """

        from ..models import (
            BasicError,
            BillingUsageReportUser,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/users/{username}/settings/billing/usage"

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
            stream=stream,
            response_model=BillingUsageReportUser,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "500": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_github_billing_usage_report_user(
        self,
        username: str,
        *,
        year: Missing[int] = UNSET,
        month: Missing[int] = UNSET,
        day: Missing[int] = UNSET,
        hour: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
        stream: bool = False,
    ) -> Response[BillingUsageReportUser, BillingUsageReportUserType]:
        """billing/get-github-billing-usage-report-user

        GET /users/{username}/settings/billing/usage

        Gets a report of the total usage for a user.

        **Note:** This endpoint is only available to users with access to the enhanced billing platform.

        See also: https://docs.github.com/rest/billing/enhanced-billing#get-billing-usage-report-for-a-user
        """

        from ..models import (
            BasicError,
            BillingUsageReportUser,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = f"/users/{username}/settings/billing/usage"

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
            stream=stream,
            response_model=BillingUsageReportUser,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "500": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )
