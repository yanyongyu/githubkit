from collections import defaultdict
from typing import Dict, List, Optional

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

    @property
    def endpoints_by_tag(self) -> Dict[str, List[EndpointData]]:
        data: Dict[str, List[EndpointData]] = defaultdict(list)
        for endpoint in self.endpoints:
            if endpoint.tags:
                data[endpoint.tags[0]].append(endpoint)
            else:
                data["default"].append(endpoint)
        return data
