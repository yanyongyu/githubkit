import inspect
from enum import Enum
from typing_extensions import TypeAlias
from typing import Any, Dict, Union, Literal, TypeVar, final

from pydantic_core import to_jsonable_python

T = TypeVar("T")


@final
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
Missing: TypeAlias = Union[Literal[UNSET], T]


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


def obj_to_jsonable(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: obj_to_jsonable(v) for k, v in obj.items()}

    if isinstance(obj, (list, tuple)):
        return [obj_to_jsonable(item) for item in obj]

    if obj is None or isinstance(obj, (int, float, str, bool)):
        return obj

    return to_jsonable_python(obj)
