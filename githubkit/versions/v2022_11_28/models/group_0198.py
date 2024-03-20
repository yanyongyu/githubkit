"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class CodeScanningDefaultSetup(GitHubModel):
    """CodeScanningDefaultSetup

    Configuration for code scanning default setup.
    """

    state: Missing[Literal["configured", "not-configured"]] = Field(
        default=UNSET,
        description="Code scanning default setup has been configured or not.",
    )
    languages: Missing[
        List[
            Literal[
                "c-cpp",
                "csharp",
                "go",
                "java-kotlin",
                "javascript-typescript",
                "javascript",
                "python",
                "ruby",
                "typescript",
                "swift",
            ]
        ]
    ] = Field(default=UNSET, description="Languages to be analyzed.")
    query_suite: Missing[Literal["default", "extended"]] = Field(
        default=UNSET, description="CodeQL query suite to be used."
    )
    updated_at: Missing[Union[datetime, None]] = Field(
        default=UNSET, description="Timestamp of latest configuration update."
    )
    schedule: Missing[Union[None, Literal["weekly"]]] = Field(
        default=UNSET, description="The frequency of the periodic analysis."
    )


model_rebuild(CodeScanningDefaultSetup)

__all__ = ("CodeScanningDefaultSetup",)
