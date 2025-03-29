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


class CodeScanningSarifsStatus(GitHubModel):
    """CodeScanningSarifsStatus"""

    processing_status: Missing[Literal["pending", "complete", "failed"]] = Field(
        default=UNSET,
        description="`pending` files have not yet been processed, while `complete` means results from the SARIF have been stored. `failed` files have either not been processed at all, or could only be partially processed.",
    )
    analyses_url: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The REST API URL for getting the analyses associated with the upload.",
    )
    errors: Missing[Union[list[str], None]] = Field(
        default=UNSET,
        description="Any errors that ocurred during processing of the delivery.",
    )


model_rebuild(CodeScanningSarifsStatus)

__all__ = ("CodeScanningSarifsStatus",)
