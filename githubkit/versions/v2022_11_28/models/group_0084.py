"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class CodeScanningAlertInstance(GitHubModel):
    """CodeScanningAlertInstance"""

    ref: Missing[str] = Field(
        default=UNSET,
        description="The Git reference, formatted as `refs/pull/<number>/merge`, `refs/pull/<number>/head`,\n`refs/heads/<branch name>` or simply `<branch name>`.",
    )
    analysis_key: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name.",
    )
    environment: Missing[str] = Field(
        default=UNSET,
        description="Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed.",
    )
    category: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code.",
    )
    state: Missing[Union[None, Literal["open", "dismissed", "fixed"]]] = Field(
        default=UNSET, description="State of a code scanning alert."
    )
    commit_sha: Missing[str] = Field(default=UNSET)
    message: Missing[CodeScanningAlertInstancePropMessage] = Field(default=UNSET)
    location: Missing[CodeScanningAlertLocation] = Field(
        default=UNSET, description="Describe a region within a file for the alert."
    )
    html_url: Missing[str] = Field(default=UNSET)
    classifications: Missing[
        list[
            Union[
                None, Literal["source", "generated", "test", "library", "documentation"]
            ]
        ]
    ] = Field(
        default=UNSET,
        description="Classifications that have been applied to the file that triggered the alert.\nFor example identifying it as documentation, or a generated file.",
    )


class CodeScanningAlertLocation(GitHubModel):
    """CodeScanningAlertLocation

    Describe a region within a file for the alert.
    """

    path: Missing[str] = Field(default=UNSET)
    start_line: Missing[int] = Field(default=UNSET)
    end_line: Missing[int] = Field(default=UNSET)
    start_column: Missing[int] = Field(default=UNSET)
    end_column: Missing[int] = Field(default=UNSET)


class CodeScanningAlertInstancePropMessage(GitHubModel):
    """CodeScanningAlertInstancePropMessage"""

    text: Missing[str] = Field(default=UNSET)


model_rebuild(CodeScanningAlertInstance)
model_rebuild(CodeScanningAlertLocation)
model_rebuild(CodeScanningAlertInstancePropMessage)

__all__ = (
    "CodeScanningAlertInstance",
    "CodeScanningAlertInstancePropMessage",
    "CodeScanningAlertLocation",
)
