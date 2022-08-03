from typing import Dict

from pydantic import BaseModel


class Config(BaseModel):
    rest_descrition_source: str
    webhook_schema_source: str
    class_overrides: Dict[str, str] = {}
    field_overrides: Dict[str, str] = {}

    client_output: str
    webhooks_output: str
    webhook_types_output: str
