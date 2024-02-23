"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class EnterprisesEnterpriseActionsRunnersRunnerIdLabelsPostBody(GitHubModel):
    """EnterprisesEnterpriseActionsRunnersRunnerIdLabelsPostBody"""

    labels: List[str] = Field(
        max_length=100,
        min_length=1,
        description="The names of the custom labels to add to the runner.",
    )


model_rebuild(EnterprisesEnterpriseActionsRunnersRunnerIdLabelsPostBody)

__all__ = ("EnterprisesEnterpriseActionsRunnersRunnerIdLabelsPostBody",)
