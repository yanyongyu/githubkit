"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0601 import WebhookRubygemsMetadata


class WebhookPackagePublishedPropPackagePropPackageVersion(GitHubModel):
    """WebhookPackagePublishedPropPackagePropPackageVersion"""

    author: Missing[
        Union[WebhookPackagePublishedPropPackagePropPackageVersionPropAuthor, None]
    ] = Field(default=UNSET, title="User")
    body: Missing[
        Union[str, WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1]
    ] = Field(default=UNSET)
    body_html: Missing[str] = Field(default=UNSET)
    container_metadata: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadata,
            None,
        ]
    ] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    description: str = Field()
    docker_metadata: Missing[
        list[
            WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItems
        ]
    ] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: str = Field()
    id: int = Field()
    installation_command: str = Field()
    manifest: Missing[str] = Field(default=UNSET)
    metadata: list[
        WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItems
    ] = Field()
    name: str = Field()
    npm_metadata: Missing[
        Union[WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadata, None]
    ] = Field(default=UNSET)
    nuget_metadata: Missing[
        Union[
            list[
                WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    package_files: list[
        WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItems
    ] = Field()
    package_url: Missing[str] = Field(default=UNSET)
    prerelease: Missing[bool] = Field(default=UNSET)
    release: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropRelease
    ] = Field(default=UNSET)
    rubygems_metadata: Missing[list[WebhookRubygemsMetadata]] = Field(default=UNSET)
    source_url: Missing[str] = Field(default=UNSET)
    summary: str = Field()
    tag_name: Missing[str] = Field(default=UNSET)
    target_commitish: Missing[str] = Field(default=UNSET)
    target_oid: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    version: str = Field()


class WebhookPackagePublishedPropPackagePropPackageVersionPropAuthor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1(GitHubModel):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadata(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadata"""

    labels: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabels,
            None,
        ]
    ] = Field(default=UNSET)
    manifest: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifest,
            None,
        ]
    ] = Field(default=UNSET)
    tag: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTag
    ] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabels(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLab
    els
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifest(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropMan
    ifest
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTag(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTag"""

    digest: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItems(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItems"""

    tags: Missing[list[str]] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItems(
    ExtraGitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItems"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadata(GitHubModel):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadata"""

    name: Missing[str] = Field(default=UNSET)
    version: Missing[str] = Field(default=UNSET)
    npm_user: Missing[str] = Field(default=UNSET)
    author: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthor,
            None,
        ]
    ] = Field(default=UNSET)
    bugs: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugs,
            None,
        ]
    ] = Field(default=UNSET)
    dependencies: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependencies
    ] = Field(default=UNSET)
    dev_dependencies: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependencies
    ] = Field(default=UNSET)
    peer_dependencies: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependencies
    ] = Field(default=UNSET)
    optional_dependencies: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies
    ] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    dist: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDist,
            None,
        ]
    ] = Field(default=UNSET)
    git_head: Missing[str] = Field(default=UNSET)
    homepage: Missing[str] = Field(default=UNSET)
    license_: Missing[str] = Field(default=UNSET, alias="license")
    main: Missing[str] = Field(default=UNSET)
    repository: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepository,
            None,
        ]
    ] = Field(default=UNSET)
    scripts: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScripts
    ] = Field(default=UNSET)
    id: Missing[str] = Field(default=UNSET)
    node_version: Missing[str] = Field(default=UNSET)
    npm_version: Missing[str] = Field(default=UNSET)
    has_shrinkwrap: Missing[bool] = Field(default=UNSET)
    maintainers: Missing[
        list[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItems
        ]
    ] = Field(default=UNSET)
    contributors: Missing[
        list[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItems
        ]
    ] = Field(default=UNSET)
    engines: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEngines
    ] = Field(default=UNSET)
    keywords: Missing[list[str]] = Field(default=UNSET)
    files: Missing[list[str]] = Field(default=UNSET)
    bin_: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBin
    ] = Field(default=UNSET, alias="bin")
    man: Missing[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMan
    ] = Field(default=UNSET)
    directories: Missing[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectories,
            None,
        ]
    ] = Field(default=UNSET)
    os: Missing[list[str]] = Field(default=UNSET)
    cpu: Missing[list[str]] = Field(default=UNSET)
    readme: Missing[str] = Field(default=UNSET)
    installation_command: Missing[str] = Field(default=UNSET)
    release_id: Missing[int] = Field(default=UNSET)
    commit_oid: Missing[str] = Field(default=UNSET)
    published_via_actions: Missing[bool] = Field(default=UNSET)
    deleted_by_id: Missing[int] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthor(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthor"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugs(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugs"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependencies(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependenc
    ies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependencies(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDepend
    encies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependencies(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDepen
    dencies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalD
    ependencies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDist(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDist"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepository(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepositor
    y
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScripts(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScripts"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItems(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintaine
    rsItems
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItems(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContribut
    orsItems
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEngines(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEngines"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBin(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBin"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMan(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMan"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectories(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectori
    es
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItems(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItems"""

    content_type: str = Field()
    created_at: str = Field()
    download_url: str = Field()
    id: int = Field()
    md5: Union[str, None] = Field()
    name: str = Field()
    sha1: Union[str, None] = Field()
    sha256: Union[str, None] = Field()
    size: int = Field()
    state: Union[str, None] = Field()
    updated_at: str = Field()


class WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItems(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItems"""

    id: Missing[Union[int, str]] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    value: Missing[
        Union[
            bool,
            str,
            int,
            WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3,
        ]
    ] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3(
    GitHubModel
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropVa
    lueOneof3
    """

    url: Missing[str] = Field(default=UNSET)
    branch: Missing[str] = Field(default=UNSET)
    commit: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropPackageVersionPropRelease(GitHubModel):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropRelease"""

    author: Union[
        WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthor, None
    ] = Field(title="User")
    created_at: str = Field()
    draft: bool = Field()
    html_url: str = Field()
    id: int = Field()
    name: Union[str, None] = Field()
    prerelease: bool = Field()
    published_at: str = Field()
    tag_name: str = Field()
    target_commitish: str = Field()
    url: str = Field()


class WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthor(
    GitHubModel
):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersion)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropAuthor)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadata)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabels
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifest
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTag
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItems
)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItems)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadata)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthor
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugs
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependencies
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependencies
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependencies
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDist
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepository
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScripts
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItems
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItems
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEngines
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBin
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMan
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectories
)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItems)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItems
)
model_rebuild(
    WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3
)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropRelease)
model_rebuild(WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthor)

__all__ = (
    "WebhookPackagePublishedPropPackagePropPackageVersion",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropAuthor",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadata",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabels",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifest",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTag",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItems",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItems",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadata",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthor",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBin",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugs",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItems",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependencies",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependencies",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectories",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDist",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEngines",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItems",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMan",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependencies",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependencies",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepository",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScripts",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItems",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItems",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropRelease",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthor",
)
