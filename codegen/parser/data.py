from dataclasses import dataclass
from collections import defaultdict
from functools import cached_property
from typing import Dict, List, Union, Optional

from pydantic import BaseModel

from .endpoints import EndpointData
from .schemas import SchemaData, ModelSchema


@dataclass
class OpenAPIData:
    """All the data needed to generate a client"""

    title: str
    description: Optional[str]
    version: str
    endpoints: List[EndpointData]
    schemas: List[SchemaData]

    @cached_property
    def endpoints_by_tag(self) -> Dict[str, List[EndpointData]]:
        data: Dict[str, List[EndpointData]] = defaultdict(list)
        for endpoint in self.endpoints:
            data[endpoint.category].append(endpoint)
        return data

    @cached_property
    def models(self) -> List[ModelSchema]:
        return [schema for schema in self.schemas if isinstance(schema, ModelSchema)]


@dataclass
class WebhookData:
    schemas: List[SchemaData]
    definitions: Dict[str, Union[SchemaData, Dict[str, SchemaData]]]

    @cached_property
    def models(self) -> List[ModelSchema]:
        return [schema for schema in self.schemas if isinstance(schema, ModelSchema)]

    @cached_property
    def model_definitions(self) -> Dict[str, SchemaData]:
        return {
            name: schema
            for name, schema in self.definitions.items()
            if isinstance(schema, SchemaData)
        }

    @cached_property
    def union_definitions(self) -> Dict[str, Dict[str, SchemaData]]:
        return {
            name: schema
            for name, schema in self.definitions.items()
            if isinstance(schema, dict)
        }
