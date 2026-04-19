from collections.abc import Sequence
import importlib
from importlib.abc import Loader
from importlib.machinery import ModuleSpec, PathFinder, SourceFileLoader
from itertools import chain
import os
import re
import sys
from types import ModuleType
from typing import Any, Optional

GITHUBKIT_LAZY_DISABLE_FLAG = "GITHUBKIT_LAZY_DISABLE_FLAG"

LAZY_MODULES = (
    r"^githubkit\.rest$",
    r"^githubkit\.versions\.[^.]+\.models$",
    r"^githubkit\.versions\.[^.]+\.types$",
    r"^githubkit\.versions\.[^.]+\.webhooks$",
    # r"^githubkit\.versions\.latest\.models$",
    # r"^githubkit\.versions\.latest\.types$",
    # r"^githubkit\.versions\.latest\.webhooks$",
)


class LazyModule(ModuleType):
    __lazy_vars__: dict[str, list[str]]
    __lazy_vars_validated__: Optional[dict[str, list[str]]]
    __lazy_vars_mapping__: dict[str, str]

    @property
    def __all__(self) -> tuple[str, ...]:
        lazy_vars = self.__lazy_vars_validated__
        if lazy_vars is None:
            return ()
        return tuple(chain.from_iterable(lazy_vars.values()))

    def __dir__(self):
        result = list(super().__dir__())
        for attr in self.__all__:
            if attr not in result:
                result.append(attr)
        return result

    def __getattr__(self, name: str) -> Any:
        lazy_vars = self.__lazy_vars_validated__
        # module may not initialized or not valid
        if lazy_vars is None:
            raise AttributeError(f"module '{self.__name__}' has no attribute '{name}'")

        # check if the attribute is a lazy variable
        if name in self.__lazy_vars_mapping__:
            module = self._get_module(self.__lazy_vars_mapping__[name])
            value = getattr(module, name)
        else:
            raise AttributeError(f"module '{self.__name__}' has no attribute '{name}'")

        # cache the value
        setattr(self, name, value)
        return value

    def _get_module(self, module_name: str) -> ModuleType:
        try:
            return importlib.import_module(module_name, self.__name__)
        except Exception as e:
            raise RuntimeError(
                f"Failed to import {module_name} from {self.__name__}"
            ) from e

    def __reduce__(self):
        return (
            self.__class__,
            (self.__name__, self.__file__, getattr(self, "__lazy_vars__", None)),
        )


class LazyModuleLoader(SourceFileLoader):
    def __init__(
        self, fullname: str, path: str, origin_loader: Optional[Loader] = None
    ) -> None:
        super().__init__(fullname, path)

        self.origin_loader = origin_loader

    def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
        if self.name in sys.modules:
            return sys.modules[self.name]

        # create a simple empty lazy module
        module = LazyModule(spec.name)
        # pre-initialize the module to avoid infinite recursion
        module.__lazy_vars_validated__ = None
        module.__lazy_vars_mapping__ = {}
        return module

    def exec_module(self, module: ModuleType) -> None:
        # execute the module code
        if self.origin_loader is not None:
            self.origin_loader.exec_module(module)
        else:
            super().exec_module(module)

        # initialize the module's lazy vars structure
        if (
            isinstance(module, LazyModule)
            and getattr(module, "__lazy_vars_validated__", None) is None
        ):
            structure = getattr(module, "__lazy_vars__", None)
            if isinstance(structure, dict) and all(
                isinstance(key, str) and isinstance(value, (list, tuple, set))
                for key, value in structure.items()
            ):
                module.__lazy_vars_validated__ = structure
                module.__lazy_vars_mapping__ = {
                    var: module
                    for module, vars in module.__lazy_vars_validated__.items()
                    for var in vars
                }
            else:
                raise RuntimeError(
                    f"Invalid lazy module structure for {module.__name__}"
                )


class LazyModuleFinder(PathFinder):
    @classmethod
    def find_spec(
        cls,
        fullname: str,
        path: Optional[Sequence[str]] = None,
        target: Optional[ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        # match if the module should be loaded lazily
        if any(re.match(pattern, fullname) for pattern in LAZY_MODULES):
            # find the module spec
            module_spec = super().find_spec(fullname, path, target)
            # do nothing if spec is not found
            if not module_spec or not module_spec.origin:
                return

            # wraps the module's loader to change the module into LazyModule
            # NOTE: module may have custom loader in some environment (e.g. pyinstaller)
            module_spec.loader = LazyModuleLoader(
                module_spec.name, module_spec.origin, module_spec.loader
            )
            return module_spec


def is_lazy_disabled() -> bool:
    return bool(os.getenv(GITHUBKIT_LAZY_DISABLE_FLAG))


def apply():
    sys.meta_path.insert(0, LazyModuleFinder())
