"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

import hmac
import json
import importlib
from typing import TYPE_CHECKING, Any, Dict, Union, Literal

from githubkit.exception import WebhookTypeNotFound
from githubkit.compat import (
    GitHubModel,
    model_dump,
    type_validate_python,
    type_validate_strings,
)

if TYPE_CHECKING:
    from ._types import WebhookEvent


VALID_EVENT_NAMES = {
    "branch_protection_configuration",
    "branch_protection_rule",
    "check_run",
    "check_suite",
    "code_scanning_alert",
    "commit_comment",
    "create",
    "custom_property",
    "custom_property_values",
    "delete",
    "dependabot_alert",
    "deploy_key",
    "deployment",
    "deployment_protection_rule",
    "deployment_review",
    "deployment_status",
    "discussion",
    "discussion_comment",
    "fork",
    "github_app_authorization",
    "gollum",
    "installation",
    "installation_repositories",
    "installation_target",
    "issue_comment",
    "issues",
    "label",
    "marketplace_purchase",
    "member",
    "membership",
    "merge_group",
    "meta",
    "milestone",
    "org_block",
    "organization",
    "package",
    "page_build",
    "personal_access_token_request",
    "ping",
    "project_card",
    "project",
    "project_column",
    "projects_v2",
    "projects_v2_item",
    "public",
    "pull_request",
    "pull_request_review_comment",
    "pull_request_review",
    "pull_request_review_thread",
    "push",
    "registry_package",
    "release",
    "repository_advisory",
    "repository",
    "repository_dispatch",
    "repository_import",
    "repository_ruleset",
    "repository_vulnerability_alert",
    "secret_scanning_alert",
    "secret_scanning_alert_location",
    "security_advisory",
    "security_and_analysis",
    "sponsorship",
    "star",
    "status",
    "team_add",
    "team",
    "watch",
    "workflow_dispatch",
    "workflow_job",
    "workflow_run",
}


class WebhookNamespace:
    @staticmethod
    def parse_without_name(payload: Union[str, bytes]) -> "WebhookEvent":
        """Parse the webhook payload without event name.

        Note:
            Parse the payload without event name is not recommended.

            The parser may take more time to parse the payload and
            the result may not be the correct type as expected.

        Args:
            payload (Union[str, bytes]): webhook payload.
        """
        from ._types import WebhookEvent

        return type_validate_strings(WebhookEvent, payload)

    @staticmethod
    def parse(name: str, payload: Union[str, bytes]) -> "WebhookEvent":
        """Parse the webhook payload with event name.

        Args:
            name (str): event name.
            payload (Union[str, bytes]): webhook payload.
        """
        if name not in VALID_EVENT_NAMES:
            raise WebhookTypeNotFound(name)
        module = importlib.import_module(f".{name}", __name__)
        Event = getattr(module, "Event")
        return type_validate_strings(Event, payload)

    @staticmethod
    def parse_obj_without_name(payload: Dict[str, Any]) -> "WebhookEvent":
        """Parse the webhook payload dict without event name.

        Note:
            Parse the payload without event name is not recommended.

            The parser may take more time to parse the payload and
            the result may not be the correct type as expected.

        Args:
            payload (Dict[str, Any]): webhook payload dict.
        """

        from ._types import WebhookEvent

        return type_validate_python(WebhookEvent, payload)

    @staticmethod
    def parse_obj(name: str, payload: Dict[str, Any]) -> "WebhookEvent":
        """Parse the webhook payload dict with event name.

        Args:
            name (str): event name.
            payload (Dict[str, Any]): webhook payload dict.
        """

        if name not in VALID_EVENT_NAMES:
            raise WebhookTypeNotFound(name)
        module = importlib.import_module(f".{name}", __name__)
        Event = getattr(module, "Event")
        return type_validate_python(Event, payload)

    @staticmethod
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
        payload = model_dump(payload) if isinstance(payload, GitHubModel) else payload
        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

    @staticmethod
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
        norm_payload = (
            payload
            if isinstance(payload, (str, bytes))
            else WebhookNamespace.normalize_payload(payload)
        )
        hmac_hex = hmac.new(
            secret.encode("utf-8"),
            norm_payload.encode("utf-8")
            if isinstance(norm_payload, str)
            else norm_payload,
            method,
        ).hexdigest()
        return f"{method}={hmac_hex}"

    @staticmethod
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
        signed = WebhookNamespace.sign(
            secret, payload, "sha256" if signature.startswith("sha256=") else "sha1"
        )

        # use time safe comparison
        return hmac.compare_digest(signed, signature)
