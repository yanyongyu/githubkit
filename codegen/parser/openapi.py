from typing import List, Optional

from pydantic import BaseModel

from .schemas import SchemaData
from .endpoints import EndpointData


class GeneratorData(BaseModel):
    """All the data needed to generate a client"""

    title: str
    description: Optional[str]
    version: str
    endpoints: List[EndpointData]
    schemas: List[SchemaData]
