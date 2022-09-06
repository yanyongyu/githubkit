import inspect
from typing import Any, Dict, Literal


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
    elif data is UNSET:
        return None
    return data


def is_async(obj: Any) -> bool:
    return inspect.isroutine(obj) and inspect.iscoroutinefunction(obj)
