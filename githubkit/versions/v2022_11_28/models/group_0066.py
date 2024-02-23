"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class CodeScanningAlertRuleSummary(GitHubModel):
    """CodeScanningAlertRuleSummary"""

    id: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="A unique identifier for the rule used to detect the alert.",
    )
    name: Missing[str] = Field(
        default=UNSET, description="The name of the rule used to detect the alert."
    )
    tags: Missing[Union[List[str], None]] = Field(
        default=UNSET, description="A set of tags applicable for the rule."
    )
    severity: Missing[Union[None, Literal["none", "note", "warning", "error"]]] = Field(
        default=UNSET, description="The severity of the alert."
    )
    security_severity_level: Missing[
        Union[None, Literal["low", "medium", "high", "critical"]]
    ] = Field(default=UNSET, description="The security severity of the alert.")
    description: Missing[str] = Field(
        default=UNSET,
        description="A short description of the rule used to detect the alert.",
    )


model_rebuild(CodeScanningAlertRuleSummary)

__all__ = ("CodeScanningAlertRuleSummary",)
