"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ReposOwnerRepoCodeScanningSarifsPostBody(GitHubModel):
    """ReposOwnerRepoCodeScanningSarifsPostBody"""

    commit_sha: str = Field(
        min_length=40,
        max_length=40,
        pattern="^[0-9a-fA-F]+$",
        description="The SHA of the commit to which the analysis you are uploading relates.",
    )
    ref: str = Field(
        pattern="^refs/(heads|tags|pull)/.*$",
        description="The full Git reference, formatted as `refs/heads/<branch name>`,\n`refs/tags/<tag>`, `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.",
    )
    sarif: str = Field(
        description='A Base64 string representing the SARIF file to upload. You must first compress your SARIF file using [`gzip`](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate the contents of the file into a Base64 encoding string. For more information, see "[SARIF support for code scanning](https://docs.github.com/enterprise-cloud@latest//code-security/secure-coding/sarif-support-for-code-scanning)."'
    )
    checkout_uri: Missing[str] = Field(
        default=UNSET,
        description="The base directory used in the analysis, as it appears in the SARIF file.\nThis property is used to convert file paths from absolute to relative, so that alerts can be mapped to their correct location in the repository.",
    )
    started_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time that the analysis run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    tool_name: Missing[str] = Field(
        default=UNSET,
        description='The name of the tool used to generate the code scanning analysis. If this parameter is not used, the tool name defaults to "API". If the uploaded SARIF contains a tool GUID, this will be available for filtering using the `tool_guid` parameter of operations such as `GET /repos/{owner}/{repo}/code-scanning/alerts`.',
    )
    validate_: Missing[bool] = Field(
        default=UNSET,
        alias="validate",
        description="Whether the SARIF file will be validated according to the code scanning specifications.\nThis parameter is intended to help integrators ensure that the uploaded SARIF files are correctly rendered by code scanning.",
    )


model_rebuild(ReposOwnerRepoCodeScanningSarifsPostBody)

__all__ = ("ReposOwnerRepoCodeScanningSarifsPostBody",)
