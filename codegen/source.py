import json
from pathlib import Path
from functools import cache
from dataclasses import dataclass
from typing import Any, Union, Optional, Sequence

import httpx
from pydantic import BaseModel
from jsonpointer import EndOfList
from openapi_schema_pydantic import OpenAPI
from jsonpointer import JsonPointerException
from jsonpointer import JsonPointer as BasePointer


class JsonPointer(BasePointer):
    def walk(self, doc, part):
        """Walks one step in doc and returns the referenced part"""

        part = self.get_part(dict(doc) if isinstance(doc, BaseModel) else doc, part)

        if isinstance(doc, Sequence):
            if part == "-":
                return EndOfList(doc)

            try:
                return doc[part]
            except IndexError as e:
                raise JsonPointerException(
                    "index '%s' is out of bounds" % (part,)
                ) from e

        if isinstance(doc, BaseModel):
            try:
                return getattr(doc, str(part))
            except KeyError as e:
                raise JsonPointerException(
                    f"member '{part}' not found in {doc}"
                ) from None

        try:
            return doc[part]
        except KeyError as e:
            raise JsonPointerException(f"member '{part}' not found in {doc}") from None


@dataclass(frozen=True)
class Source:
    uri: httpx.URL
    root: OpenAPI

    @property
    def pointer(self) -> JsonPointer:
        return JsonPointer(self.uri.fragment)

    @property
    def data(self) -> Any:
        return self.pointer.resolve(self.root)

    def get_root(self) -> "Source":
        return Source(uri=self.uri.copy_with(fragment=""), root=self.root)

    def resolve_ref(self, ref: str) -> "Source":
        uri_ref = httpx.URL(ref)
        if uri_ref.scheme and uri_ref.host:
            return get_source(uri_ref)
        return Source(uri=self.uri.copy_with(fragment=uri_ref.fragment), root=self.root)

    def __truediv__(self, other: Union[str, int]) -> "Source":
        parts = self.pointer.get_parts() + [other]
        fragment = JsonPointer.from_parts(parts).path
        return self.resolve_ref(str(httpx.URL(fragment=fragment)))


def pre_process(spec: Any) -> Any:
    """Patch to official rest api description"""
    if isinstance(spec, dict):
        # remove uncomplated webhook description
        spec.pop("webhooks", None)
    return spec


@cache
def get_spec(source: Union[httpx.URL, Path]) -> OpenAPI:
    if isinstance(source, Path):
        content = json.loads(source.read_text())
    else:
        content = httpx.get(source).json()
    return OpenAPI.parse_obj(pre_process(content))


def get_source(source: Union[httpx.URL, Path], path: Optional[str] = None) -> Source:
    if isinstance(source, Path):
        uri = httpx.URL(source.resolve().as_uri(), fragment=path)
    else:
        uri = source if path is None else source.copy_with(fragment=path)
    return Source(uri=uri, root=get_spec(source))
