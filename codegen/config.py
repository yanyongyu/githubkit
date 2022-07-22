from typing import Dict

from pydantic import BaseModel


class Config(BaseModel):
    schema_source: str
    class_overrides: Dict[str, str] = {}
