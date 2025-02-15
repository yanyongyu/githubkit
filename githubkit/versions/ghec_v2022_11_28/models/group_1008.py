"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgSettingsNetworkConfigurationsPostBody(GitHubModel):
    """OrgsOrgSettingsNetworkConfigurationsPostBody"""

    name: str = Field(
        description="Name of the network configuration. Must be between 1 and 100 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'."
    )
    compute_service: Missing[Literal["none", "actions"]] = Field(
        default=UNSET,
        description="The hosted compute service to use for the network configuration.",
    )
    network_settings_ids: list[str] = Field(
        max_length=1 if PYDANTIC_V2 else None,
        min_length=1 if PYDANTIC_V2 else None,
        description="The identifier of the network settings to use for the network configuration. Exactly one network settings must be specified.",
    )


model_rebuild(OrgsOrgSettingsNetworkConfigurationsPostBody)

__all__ = ("OrgsOrgSettingsNetworkConfigurationsPostBody",)
