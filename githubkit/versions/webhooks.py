"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import TYPE_CHECKING, Any, Literal, ClassVar, overload
import importlib

from . import VERSIONS, VERSION_TYPE, LATEST_VERSION

if TYPE_CHECKING:
    from .v2022_11_28.webhooks import WebhookNamespace as V20221128WebhookNamespace
    from .ghec_v2022_11_28.webhooks import (
        WebhookNamespace as GhecV20221128WebhookNamespace,
    )

if TYPE_CHECKING:

    class _VersionProxy(V20221128WebhookNamespace): ...

else:
    _VersionProxy = object


class WebhooksVersionSwitcher(_VersionProxy):
    _cached_namespaces: ClassVar[dict[VERSION_TYPE, Any]] = {}

    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> Any:
            if name.startswith("_"):
                raise AttributeError(
                    f"'{self.__class__.__name__}' object has no attribute '{name}'"
                )
            namespace = self()
            return getattr(namespace, name)

    @overload
    def __call__(
        self, version: Literal["2022-11-28"]
    ) -> "V20221128WebhookNamespace": ...
    @overload
    def __call__(
        self, version: Literal["ghec-2022-11-28"]
    ) -> "GhecV20221128WebhookNamespace": ...

    @overload
    def __call__(self) -> "V20221128WebhookNamespace": ...

    def __call__(self, version: VERSION_TYPE = LATEST_VERSION) -> Any:
        if version in self._cached_namespaces:
            return self._cached_namespaces[version]
        module = importlib.import_module(f".{VERSIONS[version]}.webhooks", __package__)
        namespace = module.WebhookNamespace()
        self._cached_namespaces[version] = namespace
        return namespace
