from typing import Any, Dict


class Unset:
    def __str__(self) -> str:
        return "<UNSET>"

    __repr__ = __str__

    def __bool__(self) -> bool:
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
