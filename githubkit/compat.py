from typing import Any, Type, TypeVar

from pydantic import BaseModel, ConfigDict, TypeAdapter

T = TypeVar("T")


class GitHubModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


class ExtraGitHubModel(GitHubModel):
    model_config = ConfigDict(extra="allow")


def type_validate_python(type_: Type[T], data: Any) -> T:
    return TypeAdapter(type_).validate_python(data)


def type_validate_strings(type_: Type[T], data: Any) -> T:
    return TypeAdapter(type_).validate_strings(data)


def model_rebuild(model: BaseModel):
    model.model_rebuild()
