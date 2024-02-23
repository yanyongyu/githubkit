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

from .group_0356 import EnterpriseWebhooks
from .group_0357 import SimpleInstallation
from .group_0358 import OrganizationSimpleWebhooks
from .group_0359 import RepositoryWebhooks
from .group_0360 import SimpleUserWebhooks


class WebhookSecurityAdvisoryWithdrawn(GitHubModel):
    """security_advisory withdrawn event"""

    action: Literal["withdrawn"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
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
    security_advisory: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory = Field(
        description="The details of the security advisory, including summary, description, and severity."
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory(GitHubModel):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory

    The details of the security advisory, including summary, description, and
    severity.
    """

    cvss: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss = Field()
    cwes: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems
    ] = Field()
    description: str = Field()
    ghsa_id: str = Field()
    identifiers: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems
    ] = Field()
    published_at: str = Field()
    references: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems
    ] = Field()
    severity: str = Field()
    summary: str = Field()
    updated_at: str = Field()
    vulnerabilities: List[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems
    ] = Field()
    withdrawn_at: str = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss(GitHubModel):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss"""

    score: float = Field()
    vector_string: Union[str, None] = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems(GitHubModel):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems"""

    cwe_id: str = Field()
    name: str = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems(
    GitHubModel
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems"""

    type: str = Field()
    value: str = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems(
    GitHubModel
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems"""

    url: str = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems(
    GitHubModel
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems"""

    first_patched_version: Union[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion,
        None,
    ] = Field()
    package: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage = Field()
    severity: str = Field()
    vulnerable_version_range: str = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion(
    GitHubModel
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    FirstPatchedVersion
    """

    identifier: str = Field()


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage(
    GitHubModel
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    Package
    """

    ecosystem: str = Field()
    name: str = Field()


model_rebuild(WebhookSecurityAdvisoryWithdrawn)
model_rebuild(WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory)
model_rebuild(WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss)
model_rebuild(WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems)
model_rebuild(WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems)
model_rebuild(WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems)
model_rebuild(
    WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems
)
model_rebuild(
    WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion
)
model_rebuild(
    WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage
)

__all__ = (
    "WebhookSecurityAdvisoryWithdrawn",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackage",
)
