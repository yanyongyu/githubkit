"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0224 import Metadata


class Dependency(GitHubModel):
    """Dependency"""

    package_url: Missing[Annotated[str, Field(pattern="^pkg")]] = Field(
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
    dependencies: Missing[List[str]] = Field(
        default=UNSET,
        description="Array of package-url (PURLs) of direct child dependencies.",
    )


model_rebuild(Dependency)

__all__ = ("Dependency",)
