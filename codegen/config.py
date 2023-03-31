from typing import Any, Dict

from pydantic import BaseModel
import openapi_schema_pydantic as oas


class Config(BaseModel):
    rest_description_source: str
    rest_api_version: str
    webhook_schema_source: str
    class_overrides: Dict[str, str] = {}
    field_overrides: Dict[str, str] = {}
    schema_overrides: Dict[str, Dict[str, Any]] = {}

    client_output: str
    webhooks_output: str
    webhook_types_output: str
