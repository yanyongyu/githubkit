import hmac
import json
from typing import Any, Dict, Union, Literal

from .models import GitHubWebhookModel


def normalize_payload(payload: Union[GitHubWebhookModel, Dict[str, Any]]) -> str:
    """Normalize the webhook payload to string.

    Note:
        This function may not behave the same way as GitHub Webhooks.

        Always use raw data posted by GitHub Webhooks.

    Args:
        payload (Union[GitHubWebhookModel, Dict[str, Any]]): webhook payload.

    Returns:
        str: normalized payload string.
    """
    payload = (
        payload.dict(by_alias=True)
        if isinstance(payload, GitHubWebhookModel)
        else payload
    )
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def sign(
    secret: str,
    payload: Union[GitHubWebhookModel, Dict[str, Any], str],
    method: Literal["sha256", "sha1"] = "sha256",
) -> str:
    """Sign the webhook payload.

    Args:
        secret (str): webhook secret.
        payload (Union[GitHubWebhookModel, Dict[str, Any], str]): webhook payload.
        method (str): sha256 or sha1. Defaults to sha256.

    Returns:
        str: signed payload string.
    """
    payload = payload if isinstance(payload, str) else normalize_payload(payload)
    hmac_hex = hmac.new(
        secret.encode("utf-8"), payload.encode("utf-8"), method
    ).hexdigest()
    return f"{method}={hmac_hex}"


def verify(
    secret: str, payload: Union[GitHubWebhookModel, Dict[str, Any], str], signature: str
) -> bool:
    """Verify the webhook payload.

    See: https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#validating-payloads-from-github

    Note:
        Always use raw data posted by GitHub Webhooks.

    Args:
        secret (str): webhook secret.
        payload (Union[GitHubWebhookModel, Dict[str, Any], str]): webhook payload.
        signature (str): webhook signature.

    Returns:
        bool: True if verified, False otherwise.
    """
    signed = sign(
        secret, payload, "sha256" if signature.startswith("sha256=") else "sha1"
    )

    # use time safe comparison
    return hmac.compare_digest(signed, signature)
