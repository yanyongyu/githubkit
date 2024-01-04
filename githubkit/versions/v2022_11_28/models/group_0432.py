"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild


class WebhookForkPropForkeeAllof0PropCustomProperties(ExtraGitHubModel):
    """WebhookForkPropForkeeAllof0PropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


class WebhookForkPropForkeeAllof0PropPermissions(GitHubModel):
    """WebhookForkPropForkeeAllof0PropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)


model_rebuild(WebhookForkPropForkeeAllof0PropCustomProperties)
model_rebuild(WebhookForkPropForkeeAllof0PropPermissions)

__all__ = (
    "WebhookForkPropForkeeAllof0PropCustomProperties",
    "WebhookForkPropForkeeAllof0PropPermissions",
)
