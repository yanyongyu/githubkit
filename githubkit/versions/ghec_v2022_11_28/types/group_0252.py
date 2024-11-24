"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class CodeScanningDefaultSetupUpdateType(TypedDict):
    """CodeScanningDefaultSetupUpdate

    Configuration for code scanning default setup.
    """

    state: NotRequired[Literal["configured", "not-configured"]]
    query_suite: NotRequired[Literal["default", "extended"]]
    languages: NotRequired[
        list[
            Literal[
                "c-cpp",
                "csharp",
                "go",
                "java-kotlin",
                "javascript-typescript",
                "python",
                "ruby",
                "swift",
            ]
        ]
    ]


__all__ = ("CodeScanningDefaultSetupUpdateType",)
