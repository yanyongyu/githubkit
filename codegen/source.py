from dataclasses import dataclass
from functools import cache
import os
from typing import Any

import httpx
from jsonpointer import JsonPointer

REPO_COMMIT = os.getenv(
    "REPO_COMMIT",
    "https://api.github.com/repos/github/rest-api-description/commits/main",
)
RAW_SOURCE_PREFIX = os.getenv(
    "RAW_SOURCE_PREFIX",
    "https://raw.githubusercontent.com/github/rest-api-description/",
)


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

    def get_root(self: "Source") -> "Source":
        return Source(uri=self.uri.copy_with(fragment=""), root=self.root)

    def resolve_ref(self, ref: str) -> "Source":
        uri_ref = httpx.URL(ref)
        if uri_ref.scheme and uri_ref.host:
            return get_source(uri_ref)
        return Source(uri=self.uri.copy_with(fragment=uri_ref.fragment), root=self.root)

    def __truediv__(self, other: str | int) -> "Source":
        parts = [*self.pointer.get_parts(), other]
        fragment = JsonPointer.from_parts(parts).path
        return self.resolve_ref(str(httpx.URL(fragment=fragment)))


@cache
def get_content(source: str | httpx.URL) -> tuple[httpx.URL, dict]:
    if isinstance(source, str):
        sha_response = httpx.get(
            REPO_COMMIT,
            headers={
                "User-Agent": "GitHubKit Codegen",
                "Accept": "application/vnd.github.sha",
            },
            timeout=httpx.Timeout(10.0),
        )
        sha_response.raise_for_status()
        sha = sha_response.text.strip()
        source_link = httpx.URL(RAW_SOURCE_PREFIX).join(f"{sha}/{source.lstrip('/')}")
    else:
        source_link = source

    response = httpx.get(
        source_link, headers={"User-Agent": "GitHubKit Codegen"}, follow_redirects=True
    )
    response.raise_for_status()
    uri = response.url
    content = response.json()
    return uri, content


def get_source(source: str | httpx.URL, path: str | None = None) -> Source:
    uri, root = get_content(source)
    if path is not None:
        uri = uri.copy_with(fragment=path)
    return Source(uri=uri, root=root)
