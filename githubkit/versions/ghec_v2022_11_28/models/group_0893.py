"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class EnterprisesEnterpriseActionsHostedRunnersPostBody(GitHubModel):
    """EnterprisesEnterpriseActionsHostedRunnersPostBody"""

    name: str = Field(
        description="Name of the runner. Must be between 1 and 64 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'."
    )
    image: EnterprisesEnterpriseActionsHostedRunnersPostBodyPropImage = Field(
        description="The image of runner. To list all available images, use `GET /actions/hosted-runners/images/github-owned` or `GET /actions/hosted-runners/images/partner`."
    )
    size: str = Field(
        description="The machine size of the runner. To list available sizes, use `GET actions/hosted-runners/machine-sizes`"
    )
    runner_group_id: int = Field(
        description="The existing runner group to add this runner to."
    )
    maximum_runners: Missing[int] = Field(
        default=UNSET,
        description="The maximum amount of runners to scale up to. Runners will not auto-scale above this number. Use this setting to limit your cost.",
    )
    enable_static_ip: Missing[bool] = Field(
        default=UNSET,
        description="Whether this runner should be created with a static public IP. Note limit on account. To list limits on account, use `GET actions/hosted-runners/limits`",
    )


class EnterprisesEnterpriseActionsHostedRunnersPostBodyPropImage(GitHubModel):
    """EnterprisesEnterpriseActionsHostedRunnersPostBodyPropImage

    The image of runner. To list all available images, use `GET /actions/hosted-
    runners/images/github-owned` or `GET /actions/hosted-runners/images/partner`.
    """

    id: Missing[str] = Field(
        default=UNSET, description="The unique identifier of the runner image."
    )
    source: Missing[Literal["github", "partner", "custom"]] = Field(
        default=UNSET, description="The source of the runner image."
    )


model_rebuild(EnterprisesEnterpriseActionsHostedRunnersPostBody)
model_rebuild(EnterprisesEnterpriseActionsHostedRunnersPostBodyPropImage)

__all__ = (
    "EnterprisesEnterpriseActionsHostedRunnersPostBody",
    "EnterprisesEnterpriseActionsHostedRunnersPostBodyPropImage",
)
