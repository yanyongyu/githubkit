from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Type,
    TypeVar,
    Callable,
    Protocol,
    Generator,
)

from pydantic import VERSION

T = TypeVar("T")

PYDANTIC_V2 = int(VERSION.split(".", 1)[0]) == 2

if TYPE_CHECKING:

    class ModelBeforeValidator(Protocol):
        def __call__(self, cls: Any, values: Any) -> Any: ...

    class CustomValidationClass(Protocol):
        @classmethod
        def __get_validators__(cls) -> Generator[Callable[..., Any], None, None]: ...

    CVC = TypeVar("CVC", bound=CustomValidationClass)


if PYDANTIC_V2:  # pragma: pydantic-v2
    from pydantic_core import CoreSchema, core_schema
    from pydantic_core import to_jsonable_python as to_jsonable_python
    from pydantic import (
        BaseModel,
        ConfigDict,
        TypeAdapter,
        GetCoreSchemaHandler,
        model_validator,
    )

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

    def model_rebuild(model: Type[BaseModel]):
        model.model_rebuild()

    def model_before_validator(func: "ModelBeforeValidator"):
        return model_validator(mode="before")(func)

    def __get_pydantic_core_schema__(
        cls: Type["CustomValidationClass"],
        source_type: Any,
        handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        validators = list(cls.__get_validators__())
        if len(validators) == 1:
            return core_schema.no_info_plain_validator_function(validators[0])
        return core_schema.chain_schema(
            [core_schema.no_info_plain_validator_function(func) for func in validators]
        )

    def custom_validation(class_: Type["CVC"]) -> Type["CVC"]:
        setattr(
            class_,
            "__get_pydantic_core_schema__",
            classmethod(__get_pydantic_core_schema__),
        )
        return class_

else:  # pragma: pydantic-v1
    from pydantic.json import pydantic_encoder
    from pydantic import Extra, BaseModel, parse_obj_as, parse_raw_as, root_validator

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

    def to_jsonable_python(obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: to_jsonable_python(v) for k, v in obj.items()}

        if isinstance(obj, (list, tuple)):
            return [to_jsonable_python(item) for item in obj]

        if obj is None or isinstance(obj, (int, float, str, bool)):
            return obj

        return pydantic_encoder(obj)

    def model_dump(model: BaseModel, by_alias: bool = True) -> Dict[str, Any]:
        return model.dict(by_alias=by_alias)

    def model_rebuild(model: Type[BaseModel]):
        return model.update_forward_refs()

    def model_before_validator(func: "ModelBeforeValidator"):
        return root_validator(pre=True)(func)

    def custom_validation(class_: Type["CVC"]) -> Type["CVC"]:
        return class_
