"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBodyType(TypedDict):
    """EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBody"""

    advanced_security_enabled_for_new_repositories: NotRequired[bool]
    dependabot_alerts_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_push_protection_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_push_protection_custom_link: NotRequired[Union[str, None]]
    secret_scanning_validity_checks_enabled: NotRequired[Union[bool, None]]


__all__ = ("EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBodyType",)
