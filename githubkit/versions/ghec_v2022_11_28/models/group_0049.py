"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class AzureBlobConfig(GitHubModel):
    """AzureBlobConfig

    Azure Blob Config for audit log streaming configuration.
    """

    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )
    encrypted_sas_url: str = Field()


class AzureHubConfig(GitHubModel):
    """AzureHubConfig

    Azure Event Hubs Config for audit log streaming configuration.
    """

    name: str = Field(description="Instance name of Azure Event Hubs")
    encrypted_connstring: str = Field(
        description="Encrypted Connection String for Azure Event Hubs"
    )
    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )


class AmazonS3AccessKeysConfig(GitHubModel):
    """AmazonS3AccessKeysConfig

    Amazon S3 Access Keys Config for audit log streaming configuration.
    """

    bucket: str = Field(description="Amazon S3 Bucket Name.")
    region: str = Field(description="Amazon S3 Bucket Name.")
    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )
    authentication_type: Literal["access_keys"] = Field(
        description="Authentication Type for Amazon S3."
    )
    encrypted_secret_key: str = Field(description="Encrypted AWS Secret Key.")
    encrypted_access_key_id: str = Field(description="Encrypted AWS Access Key ID.")


class HecConfig(GitHubModel):
    """HecConfig

    Hec Config for Audit Log Stream Configuration
    """

    domain: str = Field(description="Domain of Hec instance.")
    port: int = Field(description="The port number for connecting to HEC.")
    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )
    encrypted_token: str = Field(description="Encrypted Token.")
    path: str = Field(description="Path to send events to.")
    ssl_verify: bool = Field(
        description="SSL verification helps ensure your events are sent to your HEC endpoint securely."
    )


class DatadogConfig(GitHubModel):
    """DatadogConfig

    Datadog Config for audit log streaming configuration.
    """

    encrypted_token: str = Field(description="Encrypted Splunk token.")
    site: Literal["US", "US3", "US5", "EU1", "US1-FED", "AP1"] = Field(
        description="Datadog Site to use."
    )
    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )


model_rebuild(AzureBlobConfig)
model_rebuild(AzureHubConfig)
model_rebuild(AmazonS3AccessKeysConfig)
model_rebuild(HecConfig)
model_rebuild(DatadogConfig)

__all__ = (
    "AmazonS3AccessKeysConfig",
    "AzureBlobConfig",
    "AzureHubConfig",
    "DatadogConfig",
    "HecConfig",
)
