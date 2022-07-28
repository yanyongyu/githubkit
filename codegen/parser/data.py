from collections import defaultdict
from typing import Dict, List, Optional

from pydantic import BaseModel

from .endpoints import EndpointData
from .schemas import SchemaData, ModelSchema


class GeneratorData(BaseModel):
    """All the data needed to generate a client"""

    title: str
    description: Optional[str]
    version: str
    endpoints: List[EndpointData]
    schemas: List[SchemaData]

    @property
    def endpoints_by_tag(self) -> Dict[str, List[EndpointData]]:
        data: Dict[str, List[EndpointData]] = defaultdict(list)
        for endpoint in self.endpoints:
            data[endpoint.category].append(endpoint)
        return data

    @property
    def models(self) -> List[ModelSchema]:
        return [schema for schema in self.schemas if isinstance(schema, ModelSchema)]
