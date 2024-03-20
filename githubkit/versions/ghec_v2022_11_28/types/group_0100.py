"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict


class RepositoryFineGrainedPermissionType(TypedDict):
    """Repository Fine-Grained Permission

    A fine-grained permission that protects repository resources.
    """

    name: str
    description: str


__all__ = ("RepositoryFineGrainedPermissionType",)