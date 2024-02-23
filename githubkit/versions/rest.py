"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import TYPE_CHECKING, Any, Dict, Literal, overload
from weakref import WeakKeyDictionary, ref
import importlib

from . import VERSIONS, VERSION_TYPE, LATEST_VERSION

if TYPE_CHECKING:
    from githubkit import GitHubCore

    from .v2022_11_28.rest import RestNamespace as V20221128RestNamespace
    from .ghec_v2022_11_28.rest import RestNamespace as GhecV20221128RestNamespace

if TYPE_CHECKING:

    class _VersionProxy(V20221128RestNamespace):
        ...

else:
    _VersionProxy = object


class RestVersionSwitcher(_VersionProxy):
    _cached_namespaces: "WeakKeyDictionary[GitHubCore, Dict[VERSION_TYPE, Any]]" = (
        WeakKeyDictionary()
    )

    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> Any:
            if name.startswith("_"):
                raise AttributeError(
                    f"'{self.__class__.__name__}' object has no attribute '{name}'"
                )
            namespace = self()
            return getattr(namespace, name)

    def __init__(self, github: "GitHubCore"):
        self._github_ref = ref(github)

    @property
    def _github(self) -> "GitHubCore":
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use the namespace after the client has been collected."
        )

    @overload
    def __call__(self, version: Literal["2022-11-28"]) -> "V20221128RestNamespace":
        ...

    @overload
    def __call__(
        self, version: Literal["ghec-2022-11-28"]
    ) -> "GhecV20221128RestNamespace":
        ...

    @overload
    def __call__(self) -> "V20221128RestNamespace":
        ...

    def __call__(self, version: VERSION_TYPE = LATEST_VERSION) -> Any:
        g = self._github
        cache = self._cached_namespaces.setdefault(g, {})
        if version in cache:
            return cache[version]
        module = importlib.import_module(f".{VERSIONS[version]}.rest", __package__)
        namespace = module.RestNamespace(g)
        cache[version] = namespace
        return namespace
