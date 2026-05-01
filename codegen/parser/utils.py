import builtins
from keyword import iskeyword
import re
from typing import TYPE_CHECKING, Any, TypeVar

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

COPY_KEY = "<copy>"
UNSET_KEY = "<unset>"
ADD_KEY = "<add>"
REMOVE_KEY = "<remove>"


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


def _handle_copy(source: "Source", new: dict):
    if COPY_KEY not in new:
        return
    copy_from = new.pop(COPY_KEY)
    if not isinstance(copy_from, str):
        raise TypeError(f"{COPY_KEY} value must be a reference string")
    copy_source = source.resolve_ref(copy_from)
    target_name = source.pointer.parts[-1]
    source.parent.data[target_name] = copy_source.data


def merge_dict(source: "Source", new: dict):
    old = source.data
    # make change inplace to make json point correct
    for key, value in new.items():
        # remove a field
        if value == UNSET_KEY:
            if key not in old:
                raise ValueError(f"Key {key} not found in {old}")
            del old[key]
        else:
            if key not in old:
                old[key] = value
            else:
                try:
                    merge_inplace(source / key, value)
                except TypeError:
                    old[key] = value


def merge_list(source: "Source", new: list | dict):
    old = source.data
    if isinstance(new, list):
        old.clear()
        old.extend(new)
    else:
        if REMOVE_KEY in new:
            for item in new[REMOVE_KEY]:
                old.remove(item)
        if ADD_KEY in new:
            old.extend(new[ADD_KEY])


def merge_inplace(source: "Source", new: Any):
    if isinstance(new, dict):
        _handle_copy(source, new)
        if not new:
            return

    if isinstance(source.data, dict) and isinstance(new, dict):
        merge_dict(source, new)
    elif isinstance(source.data, list) and isinstance(new, list | dict):
        merge_list(source, new)
    else:
        raise TypeError(f"Cannot merge type {type(source.data)} with {type(new)}")


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
