"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class EnterprisesEnterpriseNetworkConfigurationsNetworkConfigurationIdPatchBodyType(
    TypedDict
):
    """EnterprisesEnterpriseNetworkConfigurationsNetworkConfigurationIdPatchBody"""

    name: NotRequired[str]
    compute_service: NotRequired[Literal["none", "actions"]]
    network_settings_ids: NotRequired[list[str]]


__all__ = (
    "EnterprisesEnterpriseNetworkConfigurationsNetworkConfigurationIdPatchBodyType",
)
