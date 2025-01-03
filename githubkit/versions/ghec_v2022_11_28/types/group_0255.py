"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class CodeScanningAutofixCommitsType(TypedDict):
    """CodeScanningAutofixCommits

    Commit an autofix for a code scanning alert
    """

    target_ref: NotRequired[str]
    message: NotRequired[str]


__all__ = ("CodeScanningAutofixCommitsType",)
