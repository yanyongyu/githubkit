from typing import Any


class Unset:
    def __str__(self) -> str:
        return "<UNSET>"

    def __bool__(self) -> bool:
        return False


UNSET = Unset()


def exclude_unset(data: Any) -> Any:
    if isinstance(data, dict):
        return data.__class__(
            (k, exclude_unset(v)) for k, v in data.items() if v is not UNSET
        )
    return data
