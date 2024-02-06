"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookBranchProtectionRuleEdited,
    WebhookBranchProtectionRuleCreated,
    WebhookBranchProtectionRuleDeleted,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookBranchProtectionRuleCreated,
        WebhookBranchProtectionRuleDeleted,
        WebhookBranchProtectionRuleEdited,
    ],
    Field(discriminator="action"),
]

BranchProtectionRuleEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "created": WebhookBranchProtectionRuleCreated,
    "deleted": WebhookBranchProtectionRuleDeleted,
    "edited": WebhookBranchProtectionRuleEdited,
}

branch_protection_rule_action_types = action_types

__all__ = (
    "Event",
    "BranchProtectionRuleEvent",
    "action_types",
    "branch_protection_rule_action_types",
)
