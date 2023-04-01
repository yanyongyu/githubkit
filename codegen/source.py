import json
from pathlib import Path
from functools import cache
from dataclasses import dataclass
from typing import Any, Union, Optional

import httpx
from jsonpointer import JsonPointer
from openapi_schema_pydantic import OpenAPI


@dataclass(frozen=True)
class Source:
    uri: httpx.URL
    root: Any

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


@cache
def get_content(source: Union[httpx.URL, Path]) -> dict:
    return (
        json.loads(source.read_text())
        if isinstance(source, Path)
        else httpx.get(
            source, headers={"User-Agent": "GitHubKit Codegen"}, follow_redirects=True
        ).json()
    )


def get_source(source: Union[httpx.URL, Path], path: Optional[str] = None) -> Source:
    if isinstance(source, Path):
        uri = httpx.URL(source.resolve().as_uri(), fragment=path)
    else:
        uri = source if path is None else source.copy_with(fragment=path)
    return Source(uri=uri, root=get_content(source))
