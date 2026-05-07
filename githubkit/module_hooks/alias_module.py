from collections.abc import Sequence
from importlib.machinery import ModuleSpec, PathFinder, SourceFileLoader
import importlib.util
import re
import sys
from types import ModuleType
from typing import Any, Optional
import warnings

ALIAS_MODULES = {
    r"^githubkit\.versions\.(.+)": r"githubkit_schemas.\1",
}
WARNING_PATTERN = r"^githubkit\.versions\.([^.]+)$"


class AliasModule(ModuleType):
    __alias_fullname__: str
    __alias_module__: ModuleType

    @property
    def __all__(self) -> tuple[str, ...]:
        return getattr(self.__alias_module__, "__all__", ())

    def __dir__(self):
        result = list(super().__dir__())
        for attr in self.__all__:
            if attr not in result:
                result.append(attr)
        return result

    def __getattr__(self, name: str) -> Any:
        return getattr(self.__alias_module__, name)

    def __reduce__(self):
        return (
            self.__class__,
            (self.__name__, self.__file__, getattr(self, "__alias_fullname__", None)),
        )


class AliasModuleLoader(SourceFileLoader):
    def __init__(self, fullname: str, path: str, alias_fullname: str) -> None:
        super().__init__(fullname, path)

        self.alias_fullname = alias_fullname

    def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
        if self.name in sys.modules:
            return sys.modules[self.name]

        alias_module = importlib.import_module(self.alias_fullname)
        module = AliasModule(self.name)
        module.__alias_fullname__ = self.alias_fullname
        module.__alias_module__ = alias_module
        return module


class AliasModuleFinder(PathFinder):
    @classmethod
    def find_spec(
        cls,
        fullname: str,
        path: Optional[Sequence[str]] = None,
        target: Optional[ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        # match if the module should be aliased
        for pattern, replacement in ALIAS_MODULES.items():
            alias_fullname, count = re.subn(pattern, replacement, fullname, count=1)
            if count > 0:
                # find the alias module spec
                alias_spec = importlib.util.find_spec(alias_fullname)
                # do nothing if alias spec is not found
                if not alias_spec or not alias_spec.origin:
                    return

                # modify the alias spec to load as current module instead
                alias_spec.name = fullname
                alias_spec.loader = AliasModuleLoader(
                    fullname, alias_spec.origin, alias_fullname
                )

                if re.match(WARNING_PATTERN, fullname):
                    warnings.warn(
                        f"Importing '{fullname}' is deprecated, "
                        f"use '{alias_fullname}' instead.",
                        DeprecationWarning,
                        stacklevel=2,
                    )

                return alias_spec


def apply():
    sys.meta_path.insert(0, AliasModuleFinder())
