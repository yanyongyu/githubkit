"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

import importlib
from typing import TYPE_CHECKING, Any, Dict, Literal, overload

from . import VERSIONS, VERSION_TYPE, LATEST_VERSION

if TYPE_CHECKING:
    from githubkit import GitHubCore

    from .v2022_11_28.rest import RestNamespace as V20221128RestNamespace

if TYPE_CHECKING:

    class _VersionProxy(V20221128RestNamespace):
        ...

else:
    _VersionProxy = object


class RestVersionSwitcher(_VersionProxy):
    _cached_namespaces: Dict[VERSION_TYPE, Any] = {}

    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> Any:
            namespace = self()
            return getattr(namespace, name)

    def __init__(self, github: "GitHubCore"):
        self._github = github

    @overload
    def __call__(self, version: Literal["2022-11-28"]) -> "V20221128RestNamespace":
        ...

    @overload
    def __call__(self) -> "V20221128RestNamespace":
        ...

    def __call__(self, version: VERSION_TYPE = LATEST_VERSION) -> Any:
        if version in self._cached_namespaces:
            return self._cached_namespaces[version]
        module = importlib.import_module(f".{VERSIONS[version]}.rest", __package__)
        namespace = module.RestNamespace(self._github)
        self._cached_namespaces[version] = namespace
        return namespace
