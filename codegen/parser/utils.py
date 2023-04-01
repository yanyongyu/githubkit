import re
import builtins
from copy import deepcopy
from keyword import iskeyword
from typing import Any, Dict, List, Union, Optional

from pydantic import parse_obj_as
import openapi_schema_pydantic as oas

from ..source import Source
from . import get_override_config

DELIMITERS = r"\. _-"


def sanitize(value: str) -> str:
    """Replace every character that isn't 0-9, A-Z, a-z, or a known delimiter"""
    return re.sub(rf"[^\w{DELIMITERS}]+", "_", value)


def split_words(value: str) -> List[str]:
    """Split a string on words and known delimiters"""
    # We can't guess words if there is no capital letter
    if any(c.isupper() for c in value):
        value = " ".join(re.split("([A-Z]?[a-z]+)", value))
    return re.findall(rf"[^{DELIMITERS}]+", value)


RESERVED_WORDS = (
    set(dir(builtins)) | {"self", "true", "false", "datetime", "validate"}
) - {
    "type",
    "id",
}


def fix_reserved_words(value: str) -> str:
    """
    Using reserved Python words as identifiers in generated code causes problems, so this function renames them.

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
    return "".join((word if word.isupper() else word.capitalize() for word in words))


def kebab_case(value: str) -> str:
    """Converts to kebab-case"""
    words = split_words(sanitize(value))
    return "-".join(words).lower()


def remove_string_escapes(value: str) -> str:
    return value.replace('"', r"\"")


def concat_snake_name(*names: str) -> str:
    return "_".join(snake_case(name) for name in names)


def build_boolean(value: Union[bool, str]) -> bool:
    if isinstance(value, bool):
        return value
    return value.lower() not in {"false", "f", "no", "n", "0"}


def build_class_name(name: str) -> str:
    sources = get_override_config()
    class_name = fix_reserved_words(pascal_case(name))
    for override_source in sources:
        if override := override_source.class_overrides.get(class_name):
            return override
    return class_name


def build_prop_name(name: str) -> str:
    sources = get_override_config()
    for override_source in sources:
        if override := override_source.field_overrides.get(name):
            name = override
            break
    return fix_reserved_words(snake_case(name))


def get_schema_override(source: Source) -> Optional[Dict[str, Any]]:
    sources = get_override_config()
    for override_source in sources:
        if schema := override_source.schema_overrides.get(source.pointer.path):
            return schema
    return None


def merge_dict(old: dict, new: dict):
    # make change inplace to make json point correct
    for key, value in new.items():
        old[key] = (
            merge_dict(old[key], value)
            if isinstance(value, dict) and isinstance(old[key], dict)
            else value
        )


def schema_from_source(source: Source) -> oas.Schema:
    data = source.data
    try:
        assert isinstance(data, dict)
        if overrides := get_schema_override(source):
            merge_dict(data, overrides)
        return parse_obj_as(oas.Schema, data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e
