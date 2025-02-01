"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0306 import Metadata


class Dependency(GitHubModel):
    """Dependency"""

    package_url: Missing[str] = Field(
        pattern="^pkg",
        default=UNSET,
        description="Package-url (PURL) of dependency. See https://github.com/package-url/purl-spec for more details.",
    )
    metadata: Missing[Metadata] = Field(
        default=UNSET,
        title="metadata",
        description="User-defined metadata to store domain-specific information limited to 8 keys with scalar values.",
    )
    relationship: Missing[Literal["direct", "indirect"]] = Field(
        default=UNSET,
        description="A notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.",
    )
    scope: Missing[Literal["runtime", "development"]] = Field(
        default=UNSET,
        description="A notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.",
    )
    dependencies: Missing[list[str]] = Field(
        default=UNSET,
        description="Array of package-url (PURLs) of direct child dependencies.",
    )


model_rebuild(Dependency)

__all__ = ("Dependency",)
