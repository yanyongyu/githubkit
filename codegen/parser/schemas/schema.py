from typing import Any, Set, Dict, List, ClassVar, Optional

from pydantic import BaseModel


class SchemaData(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    examples: Optional[List[Any]] = None

    _type_string: ClassVar[str] = "Any"

    def get_type_string(self) -> str:
        return self._type_string

    def get_imports(self) -> Set[str]:
        return set()

    def get_default_args(self) -> Dict[str, str]:
        default = self.default
        args = {}
        if self.title:
            args["title"] = repr(self.title)
        if self.description:
            args["description"] = repr(self.description)
        if isinstance(default, (int, bool, float, str)):
            args["default"] = repr(default)
        elif isinstance(default, (list, dict)):
            args["default_factory"] = f"lambda: {default!r}"
        return args
