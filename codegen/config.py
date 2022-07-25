from typing import Dict

from pydantic import BaseModel


class Config(BaseModel):
    schema_source: str
    class_overrides: Dict[str, str] = {}
    field_overrides: Dict[str, str] = {}

    models_output: str
    types_output: str
    client_output: str
    namespace_output: str
