from typing import Any, Dict, Type, TypeVar

from pydantic import VERSION

T = TypeVar("T")

PYDANTIC_V2 = int(VERSION.split(".", 1)[0]) == 2

if PYDANTIC_V2:
    from pydantic import BaseModel, ConfigDict, TypeAdapter

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

else:
    from pydantic import Extra, BaseModel, parse_obj_as, parse_raw_as

    class GitHubModel(BaseModel):
        class Config:
            allow_population_by_field_name = True

    class ExtraGitHubModel(BaseModel):
        class Config:
            extra = Extra.allow

    def type_validate_python(type_: Type[T], data: Any) -> T:
        return parse_obj_as(type_, data)

    def type_validate_json(type_: Type[T], data: Any) -> T:
        return parse_raw_as(type_, data)

    def model_dump(model: BaseModel, by_alias: bool = True) -> Dict[str, Any]:
        return model.dict(by_alias=by_alias)

    def model_rebuild(model: BaseModel):
        return model.update_forward_refs()
