"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import BaseModel

from githubkit.typing import Missing, UnsetType
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import List, Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import (
        CodeSecurityConfiguration,
        CodeSecurityConfigurationRepositories,
        CodeSecurityConfigurationForRepository,
        CodeSecurityDefaultConfigurationsItems,
        AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200,
    )
    from ..types import (
        OrgsOrgCodeSecurityConfigurationsPostBodyType,
        OrgsOrgCodeSecurityConfigurationsDetachDeleteBodyType,
        OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType,
        OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBodyType,
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType,
        OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptionsType,
        OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType,
    )


class CodeSecurityClient:
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

    def get_configurations_for_org(
        self,
        org: str,
        target_type: Missing[Literal["global", "all"]] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeSecurityConfiguration]]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-code-security-configurations-for-an-organization"""

        from typing import List

        from ..models import BasicError, CodeSecurityConfiguration

        url = f"/orgs/{org}/code-security/configurations"

        params = {
            "target_type": target_type,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeSecurityConfiguration],
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_configurations_for_org(
        self,
        org: str,
        target_type: Missing[Literal["global", "all"]] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeSecurityConfiguration]]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-code-security-configurations-for-an-organization"""

        from typing import List

        from ..models import BasicError, CodeSecurityConfiguration

        url = f"/orgs/{org}/code-security/configurations"

        params = {
            "target_type": target_type,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeSecurityConfiguration],
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def create_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsPostBodyType,
    ) -> Response[CodeSecurityConfiguration]: ...

    @overload
    def create_configuration(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: str,
        description: str,
        advanced_security: Missing[Literal["enabled", "disabled"]] = UNSET,
        dependency_graph: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependency_graph_autosubmit_action: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        dependency_graph_autosubmit_action_options: Missing[
            OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptionsType
        ] = UNSET,
        dependabot_alerts: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependabot_security_updates: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        code_scanning_default_setup: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        secret_scanning_push_protection: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_validity_checks: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_non_provider_patterns: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        private_vulnerability_reporting: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        enforcement: Missing[Literal["enforced", "unenforced"]] = UNSET,
    ) -> Response[CodeSecurityConfiguration]: ...

    def create_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCodeSecurityConfigurationsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[CodeSecurityConfiguration]:
        """See also: https://docs.github.com/rest/code-security/configurations#create-a-code-security-configuration"""

        from ..models import (
            CodeSecurityConfiguration,
            OrgsOrgCodeSecurityConfigurationsPostBody,
        )

        url = f"/orgs/{org}/code-security/configurations"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCodeSecurityConfigurationsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfiguration,
        )

    @overload
    async def async_create_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsPostBodyType,
    ) -> Response[CodeSecurityConfiguration]: ...

    @overload
    async def async_create_configuration(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: str,
        description: str,
        advanced_security: Missing[Literal["enabled", "disabled"]] = UNSET,
        dependency_graph: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependency_graph_autosubmit_action: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        dependency_graph_autosubmit_action_options: Missing[
            OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptionsType
        ] = UNSET,
        dependabot_alerts: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependabot_security_updates: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        code_scanning_default_setup: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        secret_scanning_push_protection: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_validity_checks: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_non_provider_patterns: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        private_vulnerability_reporting: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        enforcement: Missing[Literal["enforced", "unenforced"]] = UNSET,
    ) -> Response[CodeSecurityConfiguration]: ...

    async def async_create_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCodeSecurityConfigurationsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[CodeSecurityConfiguration]:
        """See also: https://docs.github.com/rest/code-security/configurations#create-a-code-security-configuration"""

        from ..models import (
            CodeSecurityConfiguration,
            OrgsOrgCodeSecurityConfigurationsPostBody,
        )

        url = f"/orgs/{org}/code-security/configurations"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(OrgsOrgCodeSecurityConfigurationsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfiguration,
        )

    def get_default_configurations(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeSecurityDefaultConfigurationsItems]]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-default-code-security-configurations"""

        from typing import List

        from ..models import BasicError, CodeSecurityDefaultConfigurationsItems

        url = f"/orgs/{org}/code-security/configurations/defaults"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeSecurityDefaultConfigurationsItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_default_configurations(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeSecurityDefaultConfigurationsItems]]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-default-code-security-configurations"""

        from typing import List

        from ..models import BasicError, CodeSecurityDefaultConfigurationsItems

        url = f"/orgs/{org}/code-security/configurations/defaults"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeSecurityDefaultConfigurationsItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def detach_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsDetachDeleteBodyType,
    ) -> Response: ...

    @overload
    def detach_configuration(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_repository_ids: Missing[List[int]] = UNSET,
    ) -> Response: ...

    def detach_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCodeSecurityConfigurationsDetachDeleteBodyType] = UNSET,
        **kwargs,
    ) -> Response:
        """See also: https://docs.github.com/rest/code-security/configurations#detach-configurations-from-repositories"""

        from ..models import (
            BasicError,
            OrgsOrgCodeSecurityConfigurationsDetachDeleteBody,
        )

        url = f"/orgs/{org}/code-security/configurations/detach"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsDetachDeleteBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    @overload
    async def async_detach_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsDetachDeleteBodyType,
    ) -> Response: ...

    @overload
    async def async_detach_configuration(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_repository_ids: Missing[List[int]] = UNSET,
    ) -> Response: ...

    async def async_detach_configuration(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCodeSecurityConfigurationsDetachDeleteBodyType] = UNSET,
        **kwargs,
    ) -> Response:
        """See also: https://docs.github.com/rest/code-security/configurations#detach-configurations-from-repositories"""

        from ..models import (
            BasicError,
            OrgsOrgCodeSecurityConfigurationsDetachDeleteBody,
        )

        url = f"/orgs/{org}/code-security/configurations/detach"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsDetachDeleteBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    def get_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CodeSecurityConfiguration]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-a-code-security-configuration"""

        from ..models import BasicError, CodeSecurityConfiguration

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfiguration,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CodeSecurityConfiguration]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-a-code-security-configuration"""

        from ..models import BasicError, CodeSecurityConfiguration

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfiguration,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    def delete_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/code-security/configurations#delete-a-code-security-configuration"""

        from ..models import BasicError

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    async def async_delete_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/code-security/configurations#delete-a-code-security-configuration"""

        from ..models import BasicError

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    @overload
    def update_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType,
    ) -> Response[CodeSecurityConfiguration]: ...

    @overload
    def update_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: Missing[str] = UNSET,
        description: Missing[str] = UNSET,
        advanced_security: Missing[Literal["enabled", "disabled"]] = UNSET,
        dependency_graph: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependency_graph_autosubmit_action: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        dependency_graph_autosubmit_action_options: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType
        ] = UNSET,
        dependabot_alerts: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependabot_security_updates: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        code_scanning_default_setup: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        secret_scanning_push_protection: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_validity_checks: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_non_provider_patterns: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        private_vulnerability_reporting: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        enforcement: Missing[Literal["enforced", "unenforced"]] = UNSET,
    ) -> Response[CodeSecurityConfiguration]: ...

    def update_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[CodeSecurityConfiguration]:
        """See also: https://docs.github.com/rest/code-security/configurations#update-a-code-security-configuration"""

        from ..models import (
            CodeSecurityConfiguration,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBody,
        )

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfiguration,
        )

    @overload
    async def async_update_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType,
    ) -> Response[CodeSecurityConfiguration]: ...

    @overload
    async def async_update_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: Missing[str] = UNSET,
        description: Missing[str] = UNSET,
        advanced_security: Missing[Literal["enabled", "disabled"]] = UNSET,
        dependency_graph: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependency_graph_autosubmit_action: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        dependency_graph_autosubmit_action_options: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType
        ] = UNSET,
        dependabot_alerts: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        dependabot_security_updates: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        code_scanning_default_setup: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning: Missing[Literal["enabled", "disabled", "not_set"]] = UNSET,
        secret_scanning_push_protection: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_validity_checks: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        secret_scanning_non_provider_patterns: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        private_vulnerability_reporting: Missing[
            Literal["enabled", "disabled", "not_set"]
        ] = UNSET,
        enforcement: Missing[Literal["enforced", "unenforced"]] = UNSET,
    ) -> Response[CodeSecurityConfiguration]: ...

    async def async_update_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[CodeSecurityConfiguration]:
        """See also: https://docs.github.com/rest/code-security/configurations#update-a-code-security-configuration"""

        from ..models import (
            CodeSecurityConfiguration,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBody,
        )

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfiguration,
        )

    @overload
    def attach_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBodyType,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]: ...

    @overload
    def attach_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        scope: Literal["all", "public", "private_or_internal", "selected"],
        selected_repository_ids: Missing[List[int]] = UNSET,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]: ...

    def attach_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]:
        """See also: https://docs.github.com/rest/code-security/configurations#attach-a-configuration-to-repositories"""

        from ..models import (
            AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBody,
        )

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}/attach"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
        )

    @overload
    async def async_attach_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBodyType,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]: ...

    @overload
    async def async_attach_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        scope: Literal["all", "public", "private_or_internal", "selected"],
        selected_repository_ids: Missing[List[int]] = UNSET,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]: ...

    async def async_attach_configuration(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[AppHookDeliveriesDeliveryIdAttemptsPostResponse202]:
        """See also: https://docs.github.com/rest/code-security/configurations#attach-a-configuration-to-repositories"""

        from ..models import (
            AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBody,
        )

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}/attach"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsConfigurationIdAttachPostBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=AppHookDeliveriesDeliveryIdAttemptsPostResponse202,
        )

    @overload
    def set_configuration_as_default(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType,
    ) -> Response[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
    ]: ...

    @overload
    def set_configuration_as_default(
        self,
        org: str,
        configuration_id: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        default_for_new_repos: Missing[
            Literal["all", "none", "private_and_internal", "public"]
        ] = UNSET,
    ) -> Response[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
    ]: ...

    def set_configuration_as_default(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
    ]:
        """See also: https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBody,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200,
        )

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}/defaults"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_set_configuration_as_default(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType,
    ) -> Response[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
    ]: ...

    @overload
    async def async_set_configuration_as_default(
        self,
        org: str,
        configuration_id: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        default_for_new_repos: Missing[
            Literal["all", "none", "private_and_internal", "public"]
        ] = UNSET,
    ) -> Response[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
    ]: ...

    async def async_set_configuration_as_default(
        self,
        org: str,
        configuration_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType
        ] = UNSET,
        **kwargs,
    ) -> Response[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
    ]:
        """See also: https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBody,
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200,
        )

        url = f"/orgs/{org}/code-security/configurations/{configuration_id}/defaults"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutBody, json
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_repositories_for_configuration(
        self,
        org: str,
        configuration_id: int,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        status: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeSecurityConfigurationRepositories]]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-repositories-associated-with-a-code-security-configuration"""

        from typing import List

        from ..models import BasicError, CodeSecurityConfigurationRepositories

        url = (
            f"/orgs/{org}/code-security/configurations/{configuration_id}/repositories"
        )

        params = {
            "per_page": per_page,
            "before": before,
            "after": after,
            "status": status,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeSecurityConfigurationRepositories],
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_repositories_for_configuration(
        self,
        org: str,
        configuration_id: int,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        status: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CodeSecurityConfigurationRepositories]]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-repositories-associated-with-a-code-security-configuration"""

        from typing import List

        from ..models import BasicError, CodeSecurityConfigurationRepositories

        url = (
            f"/orgs/{org}/code-security/configurations/{configuration_id}/repositories"
        )

        params = {
            "per_page": per_page,
            "before": before,
            "after": after,
            "status": status,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeSecurityConfigurationRepositories],
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_configuration_for_repository(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CodeSecurityConfigurationForRepository]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-the-code-security-configuration-associated-with-a-repository"""

        from ..models import BasicError, CodeSecurityConfigurationForRepository

        url = f"/repos/{owner}/{repo}/code-security-configuration"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfigurationForRepository,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_configuration_for_repository(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CodeSecurityConfigurationForRepository]:
        """See also: https://docs.github.com/rest/code-security/configurations#get-the-code-security-configuration-associated-with-a-repository"""

        from ..models import BasicError, CodeSecurityConfigurationForRepository

        url = f"/repos/{owner}/{repo}/code-security-configuration"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeSecurityConfigurationForRepository,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )
