"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0075 import SecurityAndAnalysis


class WebhookSecurityAndAnalysisPropChangesPropFrom(GitHubModel):
    """WebhookSecurityAndAnalysisPropChangesPropFrom"""

    security_and_analysis: Missing[Union[SecurityAndAnalysis, None]] = Field(
        default=UNSET
    )


model_rebuild(WebhookSecurityAndAnalysisPropChangesPropFrom)

__all__ = ("WebhookSecurityAndAnalysisPropChangesPropFrom",)
