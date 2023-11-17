from typing import Any, Type, Union, Callable, Optional

from pydantic import BaseModel, Discriminator

from githubkit.webhooks.models import GitHubWebhookModel


def _get_field_getter(v: Union[dict, BaseModel]) -> Callable[[str], Optional[Any]]:
    if isinstance(v, dict):
        return v.get

    def _getter(field: str) -> Optional[Any]:
        return getattr(v, field, None)

    return _getter


def SchemaDiscriminator(*schemas: Type[GitHubWebhookModel]) -> Discriminator:
    def _discriminator(v: Any) -> Optional[str]:
        if not isinstance(v, (dict, BaseModel)):
            return None

        field_getter = _get_field_getter(v)

        for schema in schemas:
            for field_name, field_info in schema.model_fields.items():
                if field_info.is_required() and field_getter(field_name) is None:
                    break
            return schema.__name__

        return None

    return Discriminator(_discriminator)
