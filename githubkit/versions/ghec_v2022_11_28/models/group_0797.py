"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0392 import OrganizationSimpleWebhooks
from .group_0393 import RepositoryWebhooks
from .group_0394 import SimpleUserWebhooks


class WebhookSecurityAdvisoryPublished(GitHubModel):
    """security_advisory published event"""

    action: Literal["published"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    security_advisory: WebhookSecurityAdvisoryPublishedPropSecurityAdvisory = Field(
        description="The details of the security advisory, including summary, description, and severity."
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisory(GitHubModel):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisory

    The details of the security advisory, including summary, description, and
    severity.
    """

    cvss: WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCvss = Field()
    cwes: List[
        WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCwesItems
    ] = Field()
    description: str = Field()
    ghsa_id: str = Field()
    identifiers: List[
        WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropIdentifiersItems
    ] = Field()
    published_at: str = Field()
    references: List[
        WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropReferencesItems
    ] = Field()
    severity: str = Field()
    summary: str = Field()
    updated_at: str = Field()
    vulnerabilities: List[
        WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItems
    ] = Field()
    withdrawn_at: Union[str, None] = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCvss(GitHubModel):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCvss"""

    score: float = Field()
    vector_string: Union[str, None] = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCwesItems(GitHubModel):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCwesItems"""

    cwe_id: str = Field()
    name: str = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropIdentifiersItems(
    GitHubModel
):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropIdentifiersItems"""

    type: str = Field()
    value: str = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropReferencesItems(
    GitHubModel
):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropReferencesItems"""

    url: str = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItems(
    GitHubModel
):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItems"""

    first_patched_version: Union[
        WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion,
        None,
    ] = Field()
    package: WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage = Field()
    severity: str = Field()
    vulnerable_version_range: str = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion(
    GitHubModel
):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    FirstPatchedVersion
    """

    identifier: str = Field()


class WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage(
    GitHubModel
):
    """WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    Package
    """

    ecosystem: str = Field()
    name: str = Field()


model_rebuild(WebhookSecurityAdvisoryPublished)
model_rebuild(WebhookSecurityAdvisoryPublishedPropSecurityAdvisory)
model_rebuild(WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCvss)
model_rebuild(WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCwesItems)
model_rebuild(WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropIdentifiersItems)
model_rebuild(WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropReferencesItems)
model_rebuild(
    WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItems
)
model_rebuild(
    WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion
)
model_rebuild(
    WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage
)

__all__ = (
    "WebhookSecurityAdvisoryPublished",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisory",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCvss",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropCwesItems",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropIdentifiersItems",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropReferencesItems",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItems",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion",
    "WebhookSecurityAdvisoryPublishedPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage",
)
