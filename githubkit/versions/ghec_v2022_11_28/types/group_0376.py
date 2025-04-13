"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class PageType(TypedDict):
    """GitHub Pages

    The configuration for GitHub Pages for a repository.
    """

    url: str
    status: Union[None, Literal["built", "building", "errored"]]
    cname: Union[str, None]
    protected_domain_state: NotRequired[
        Union[None, Literal["pending", "verified", "unverified"]]
    ]
    pending_domain_unverified_at: NotRequired[Union[datetime, None]]
    custom_404: bool
    html_url: NotRequired[str]
    build_type: NotRequired[Union[None, Literal["legacy", "workflow"]]]
    source: NotRequired[PagesSourceHashType]
    public: bool
    https_certificate: NotRequired[PagesHttpsCertificateType]
    https_enforced: NotRequired[bool]


class PagesSourceHashType(TypedDict):
    """Pages Source Hash"""

    branch: str
    path: str


class PagesHttpsCertificateType(TypedDict):
    """Pages Https Certificate"""

    state: Literal[
        "new",
        "authorization_created",
        "authorization_pending",
        "authorized",
        "authorization_revoked",
        "issued",
        "uploaded",
        "approved",
        "errored",
        "bad_authz",
        "destroy_pending",
        "dns_changed",
    ]
    description: str
    domains: list[str]
    expires_at: NotRequired[date]


__all__ = (
    "PageType",
    "PagesHttpsCertificateType",
    "PagesSourceHashType",
)
