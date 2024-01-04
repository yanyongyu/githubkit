"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleCreation(GitHubModel):
    """creation

    Only allow users with bypass permission to create matching refs.
    """

    type: Literal["creation"] = Field()


class RepositoryRuleDeletion(GitHubModel):
    """deletion

    Only allow users with bypass permissions to delete matching refs.
    """

    type: Literal["deletion"] = Field()


class RepositoryRuleRequiredSignatures(GitHubModel):
    """required_signatures

    Commits pushed to matching refs must have verified signatures.
    """

    type: Literal["required_signatures"] = Field()


class RepositoryRuleNonFastForward(GitHubModel):
    """non_fast_forward

    Prevent users with push access from force pushing to refs.
    """

    type: Literal["non_fast_forward"] = Field()


model_rebuild(RepositoryRuleCreation)
model_rebuild(RepositoryRuleDeletion)
model_rebuild(RepositoryRuleRequiredSignatures)
model_rebuild(RepositoryRuleNonFastForward)

__all__ = (
    "RepositoryRuleCreation",
    "RepositoryRuleDeletion",
    "RepositoryRuleRequiredSignatures",
    "RepositoryRuleNonFastForward",
)
