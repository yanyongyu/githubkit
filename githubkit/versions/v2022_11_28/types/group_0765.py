"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookSecurityAdvisoryUpdatedType(TypedDict):
    """security_advisory updated event"""

    action: Literal["updated"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    security_advisory: WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryType
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryType(TypedDict):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisory

    The details of the security advisory, including summary, description, and
    severity.
    """

    cvss: WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCvssType
    cwes: List[WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCwesItemsType]
    description: str
    ghsa_id: str
    identifiers: List[
        WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropIdentifiersItemsType
    ]
    published_at: str
    references: List[
        WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropReferencesItemsType
    ]
    severity: str
    summary: str
    updated_at: str
    vulnerabilities: List[
        WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsType
    ]
    withdrawn_at: Union[str, None]


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCvssType(TypedDict):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCvss"""

    score: float
    vector_string: Union[str, None]


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCwesItemsType(TypedDict):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCwesItems"""

    cwe_id: str
    name: str


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropIdentifiersItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropIdentifiersItems"""

    type: str
    value: str


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropReferencesItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropReferencesItems"""

    url: str


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItems"""

    first_patched_version: Union[
        WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType,
        None,
    ]
    package: WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType
    severity: str
    vulnerable_version_range: str


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType(
    TypedDict
):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFi
    rstPatchedVersion
    """

    identifier: str


class WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType(
    TypedDict
):
    """WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPa
    ckage
    """

    ecosystem: str
    name: str


__all__ = (
    "WebhookSecurityAdvisoryUpdatedType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCvssType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropCwesItemsType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropIdentifiersItemsType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropReferencesItemsType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType",
    "WebhookSecurityAdvisoryUpdatedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType",
)
