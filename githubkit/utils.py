import inspect
from typing import Any, Dict, Literal

from pydantic.json import pydantic_encoder


class Unset:
    def __repr__(self) -> str:
        return "<UNSET>"

    def __bool__(self) -> Literal[False]:
        return False

    def __copy__(self):
        return UNSET

    def __deepcopy__(self, memo: Dict[int, Any]):
        return UNSET

    @classmethod
    def __get_validators__(cls):
        yield cls._validate

    @classmethod
    def _validate(cls, value: Any):
        if value is not UNSET:
            raise ValueError(f"{value!r} is not UNSET")
        return value


UNSET = Unset()


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

    return pydantic_encoder(obj)
