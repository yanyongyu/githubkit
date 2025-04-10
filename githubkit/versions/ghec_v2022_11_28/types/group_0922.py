"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType(
    TypedDict
):
    """EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutBody"""

    default_for_new_repos: NotRequired[
        Literal["all", "none", "private_and_internal", "public"]
    ]


__all__ = (
    "EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutBodyType",
)
