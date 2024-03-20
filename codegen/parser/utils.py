import re
import builtins
from keyword import iskeyword
from typing import TYPE_CHECKING, TypeVar

import openapi_pydantic as oas
from pydantic import TypeAdapter

from . import get_override_config

if TYPE_CHECKING:
    from ..source import Source


T = TypeVar("T")

DELIMITERS = r"\. _-"

RESERVED_WORDS = (
    set(dir(builtins)) | {"self", "true", "false", "datetime", "validate"}
) - {
    "type",
    "id",
}

UNSET_KEY = "<unset>"


def sanitize(value: str) -> str:
    """Replace every character that isn't 0-9, A-Z, a-z, or a known delimiter"""
    return re.sub(rf"[^\w{DELIMITERS}]+", "_", value)


def split_words(value: str) -> list[str]:
    """Split a string on words and known delimiters"""
    # We can't guess words if there is no capital letter
    if any(c.isupper() for c in value):
        value = " ".join(re.split("([A-Z]?[a-z]+)", value))
    return re.findall(rf"[^{DELIMITERS}]+", value)


def fix_reserved_words(value: str) -> str:
    """
    Using reserved Python words as identifiers in generated code causes problems,
    so this function renames them.

    Args:
        value: The identifier to-be that should be renamed if it's a reserved word.

    Returns:
        `value` suffixed with `_` if it was a reserved word.
    """
    return f"{value}_" if value in RESERVED_WORDS or iskeyword(value) else value


def snake_case(value: str) -> str:
    """Converts to snake_case"""
    words = split_words(sanitize(value))
    return "_".join(words).lower()


def pascal_case(value: str) -> str:
    """Converts to PascalCase"""
    words = split_words(sanitize(value))
    return "".join(word if word.isupper() else word.capitalize() for word in words)


def kebab_case(value: str) -> str:
    """Converts to kebab-case"""
    words = split_words(sanitize(value))
    return "-".join(words).lower()


def remove_string_escapes(value: str) -> str:
    return value.replace('"', r"\"")


def concat_snake_name(*names: str) -> str:
    return "_".join(snake_case(name) for name in names)


def build_boolean(value: bool | str) -> bool:
    if isinstance(value, bool):
        return value
    return value.lower() not in {"false", "f", "no", "n", "0"}


def build_class_name(name: str) -> str:
    override = get_override_config()
    class_name = fix_reserved_words(pascal_case(name))
    if overrided_name := override.class_overrides.get(class_name):
        return overrided_name
    return class_name


def build_prop_name(name: str) -> str:
    override = get_override_config()
    if overrided_name := override.field_overrides.get(name):
        name = overrided_name
    return fix_reserved_words(snake_case(name))


def merge_dict(old: dict, new: dict):
    # make change inplace to make json point correct
    for key, value in new.items():
        if value == UNSET_KEY:
            if key not in old:
                raise ValueError(f"Key {key} not found in {old}")
            del old[key]
        else:
            old[key] = (
                merge_dict(old[key], value)
                if isinstance(value, dict) and isinstance(old[key], dict)
                else value
            )


def schema_from_source(source: "Source") -> oas.Schema:
    data = source.data

    try:
        return TypeAdapter(oas.Schema).validate_python(data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e


def type_ref_from_source(source: "Source", type_: type[T]) -> oas.Reference | T:
    data = source.data

    try:
        return TypeAdapter(oas.Reference | type_).validate_python(data)
    except Exception as e:
        raise TypeError(f"Invalid {type_} from {source.uri}") from e
