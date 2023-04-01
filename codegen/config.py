from typing import Any, Dict, List

import openapi_schema_pydantic as oas
from pydantic import Field, BaseModel


class Overridable(BaseModel):
    class_overrides: Dict[str, str] = Field(default_factory=dict)
    field_overrides: Dict[str, str] = Field(default_factory=dict)
    schema_overrides: Dict[str, Dict[str, Any]] = Field(default_factory=dict)


class RestConfig(Overridable):
    version: str
    description_source: str
    output_dir: str


class WebhookConfig(Overridable):
    schema_source: str
    output: str
    types_output: str


class Config(Overridable):
    rest: List[RestConfig]
    webhook: WebhookConfig
