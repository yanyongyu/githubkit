from typing import Any, Dict, Type, TypeVar

from pydantic import BaseModel, ConfigDict, TypeAdapter

T = TypeVar("T")


class GitHubModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


class ExtraGitHubModel(GitHubModel):
    model_config = ConfigDict(extra="allow")


def type_validate_python(type_: Type[T], data: Any) -> T:
    return TypeAdapter(type_).validate_python(data)


def type_validate_json(type_: Type[T], data: Any) -> T:
    return TypeAdapter(type_).validate_json(data)


def model_dump(model: BaseModel, by_alias: bool = True) -> Dict[str, Any]:
    return model.model_dump(by_alias=by_alias)


def model_rebuild(model: BaseModel):
    model.model_rebuild()
