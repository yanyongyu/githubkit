from typing import TYPE_CHECKING, Any, Dict, Union, Literal

from githubkit.compat import GitHubModel
from githubkit.versions.latest.webhooks import WebhookNamespace

if TYPE_CHECKING:
    from githubkit.versions.latest.webhooks import WebhookEvent


def parse_without_name(payload: Union[str, bytes]) -> "WebhookEvent":
    """Parse the webhook payload without event name.

    Note:
        Parse the payload without event name is not recommended.

        The parser may take more time to parse the payload and
        the result may not be the correct type as expected.

    Args:
        payload (Union[str, bytes]): webhook payload.
    """
    return WebhookNamespace.parse_without_name(payload)


def parse(name: str, payload: Union[str, bytes]) -> "WebhookEvent":
    """Parse the webhook payload with event name.

    Args:
        name (str): event name.
        payload (Union[str, bytes]): webhook payload.
    """
    return WebhookNamespace.parse(name, payload)


def parse_obj_without_name(payload: Dict[str, Any]) -> "WebhookEvent":
    """Parse the webhook payload dict without event name.

    Note:
        Parse the payload without event name is not recommended.

        The parser may take more time to parse the payload and
        the result may not be the correct type as expected.

    Args:
        payload (Dict[str, Any]): webhook payload dict.
    """
    return WebhookNamespace.parse_obj_without_name(payload)


def parse_obj(name: str, payload: Dict[str, Any]) -> "WebhookEvent":
    """Parse the webhook payload dict with event name.

    Args:
        name (str): event name.
        payload (Dict[str, Any]): webhook payload dict.
    """
    return WebhookNamespace.parse_obj(name, payload)


def normalize_payload(payload: Union[GitHubModel, Dict[str, Any]]) -> str:
    """Normalize the webhook payload to string.

    Note:
        This function may not behave the same way as GitHub Webhooks.

        Always use raw data posted by GitHub Webhooks.

    Args:
        payload (Union[GitHubModel, Dict[str, Any]]): webhook payload.

    Returns:
        str: normalized payload string.
    """
    return WebhookNamespace.normalize_payload(payload)


def sign(
    secret: str,
    payload: Union[GitHubModel, Dict[str, Any], str, bytes],
    method: Literal["sha256", "sha1"] = "sha256",
) -> str:
    """Sign the webhook payload.

    Args:
        secret (str): webhook secret.
        payload (Union[GitHubModel, Dict[str, Any], str, bytes]): webhook payload.
        method (str): sha256 or sha1. Defaults to sha256.

    Returns:
        str: signed payload string.
    """
    return WebhookNamespace.sign(secret, payload, method)


def verify(
    secret: str,
    payload: Union[GitHubModel, Dict[str, Any], str, bytes],
    signature: str,
) -> bool:
    """Verify the webhook payload.

    See: https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#validating-payloads-from-github

    Note:
        Always use raw data posted by GitHub Webhooks.

    Args:
        secret (str): webhook secret.
        payload (Union[GitHubModel, Dict[str, Any], str, bytes]): webhook payload.
        signature (str): webhook signature.

    Returns:
        bool: True if verified, False otherwise.
    """
    return WebhookNamespace.verify(secret, payload, signature)
