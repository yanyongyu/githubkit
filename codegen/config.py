from typing import Dict, List

from pydantic import BaseModel


class Config(BaseModel):
    class_overrides: Dict[str, str] = {}
