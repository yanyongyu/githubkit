"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict


class SimpleInstallationType(TypedDict):
    """Simple Installation

    The GitHub App installation. Webhook payloads contain the `installation`
    property when the event is configured
    for and sent to a GitHub App. For more information,
    see "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-
    github-apps/registering-a-github-app/using-webhooks-with-github-apps)."
    """

    id: int
    node_id: str


__all__ = ("SimpleInstallationType",)
