import inspect
from enum import Enum
from typing import Any, Dict, Type, Generic, Literal, TypeVar, final

from pydantic import BaseModel

from .compat import PYDANTIC_V2, custom_validation, type_validate_python

if PYDANTIC_V2:  # pragma: pydantic-v2
    from pydantic_core import core_schema
    from pydantic import GetCoreSchemaHandler

T = TypeVar("T")


@final
@custom_validation
class Unset(Enum):
    _UNSET = "<UNSET>"

    def __repr__(self) -> str:
        return "<UNSET>"

    def __str__(self) -> str:
        return self.__repr__()

    def __bool__(self) -> Literal[False]:
        return False

    def __copy__(self):
        return self._UNSET

    def __deepcopy__(self, memo: Dict[int, Any]):
        return self._UNSET

    @classmethod
    def __get_validators__(cls):
        yield cls._validate

    @classmethod
    def _validate(cls, value: Any):
        if value is not cls._UNSET:
            raise ValueError(f"{value!r} is not UNSET")
        return value


UNSET = Unset._UNSET


def exclude_unset(data: Any) -> Any:
    if isinstance(data, dict):
        return data.__class__(
            (k, exclude_unset(v)) for k, v in data.items() if v is not UNSET
        )
    elif isinstance(data, list):
        return data.__class__(exclude_unset(i) for i in data)
    elif data is UNSET:
        return None
    return data


def is_async(obj: Any) -> bool:
    if inspect.isroutine(obj):
        return inspect.iscoroutinefunction(obj)
    if inspect.isclass(obj):
        return False
    func_ = getattr(obj, "__call__", None)
    return inspect.iscoroutinefunction(func_)


class TaggedUnion(Generic[T]):
    __slots__ = ("type_", "discriminator", "tag")

    def __init__(self, type_: Type[T], discriminator: str, tag: str) -> None:
        self.type_ = type_
        self.discriminator = discriminator
        self.tag = tag

    def _validate(self, value: Any) -> T:
        return type_validate_python(self.type_, value)

    if PYDANTIC_V2:  # pragma: pydantic-v2

        def __get_pydantic_core_schema__(
            self, _source_type: Any, _handler: "GetCoreSchemaHandler"
        ) -> "core_schema.CoreSchema":
            return core_schema.no_info_before_validator_function(
                self._validate,
                core_schema.model_schema(
                    BaseModel,
                    schema=core_schema.model_fields_schema(
                        {
                            self.discriminator: core_schema.model_field(
                                core_schema.literal_schema([self.tag])
                            )
                        }
                    ),
                ),
            )
