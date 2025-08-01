"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0089 import CodeScanningAnalysisTool


class CodeScanningAnalysis(GitHubModel):
    """CodeScanningAnalysis"""

    ref: str = Field(
        description="The Git reference, formatted as `refs/pull/<number>/merge`, `refs/pull/<number>/head`,\n`refs/heads/<branch name>` or simply `<branch name>`."
    )
    commit_sha: str = Field(
        min_length=40,
        max_length=40,
        pattern="^[0-9a-fA-F]+$",
        description="The SHA of the commit to which the analysis you are uploading relates.",
    )
    analysis_key: str = Field(
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name."
    )
    environment: str = Field(
        description="Identifies the variable values associated with the environment in which this analysis was performed."
    )
    category: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code.",
    )
    error: str = Field()
    created_at: datetime = Field(
        description="The time that the analysis was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    results_count: int = Field(
        description="The total number of results in the analysis."
    )
    rules_count: int = Field(
        description="The total number of rules used in the analysis."
    )
    id: int = Field(description="Unique identifier for this analysis.")
    url: str = Field(description="The REST API URL of the analysis resource.")
    sarif_id: str = Field(description="An identifier for the upload.")
    tool: CodeScanningAnalysisTool = Field()
    deletable: bool = Field()
    warning: str = Field(description="Warning generated when processing the analysis")


model_rebuild(CodeScanningAnalysis)

__all__ = ("CodeScanningAnalysis",)
