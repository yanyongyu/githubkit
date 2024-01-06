"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhookSecretScanningAlertLocationCreatedFormEncoded(GitHubModel):
    """Secret Scanning Alert Location Created Event"""

    payload: str = Field(
        description="A URL-encoded string of the secret_scanning_alert_location.created JSON payload. The decoded payload is a JSON object."
    )


model_rebuild(WebhookSecretScanningAlertLocationCreatedFormEncoded)

__all__ = ("WebhookSecretScanningAlertLocationCreatedFormEncoded",)