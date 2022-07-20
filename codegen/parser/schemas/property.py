from typing import Set

from pydantic import BaseModel

from .schema import SchemaData
from ..utils import sanitize, snake_case


class Property(BaseModel):
    name: str
    required: bool
    schema_data: SchemaData

    @property
    def snake_name(self) -> str:
        return snake_case(sanitize(self.name))

    def get_type_string(self) -> str:
        type_string = self.schema_data.get_type_string()
        return type_string if self.required else f"Union[Unset, {type_string}]"

    def get_imports(self) -> Set[str]:
        imports = self.schema_data.get_imports()
        imports.add("from pydantic import Field")
        if not self.required:
            imports.add("from typing import Union")
            imports.add("from .types import UNSET, Unset")
        return imports

    def get_default_string(self) -> str:
        args = self.schema_data.get_default_args()
        if "default" not in args and "default_factory" not in args:
            args["default"] = "..." if self.required else "UNSET"
        if self.snake_name != self.name:
            args["alias"] = self.name

        arg_string = [f"{k}={v!r}" for k, v in args.items()]
        return f"Field({', '.join(arg_string)})"

    def get_param_string(self) -> str:
        type_ = self.get_type_string()
        if self.schema_data.default is None:
            return f"{self.snake_name}: {type_}"
        return f"{self.snake_name}: {type_} = {self.schema_data.default!r}"

    def get_attr_string(self) -> str:
        type_ = self.get_type_string()
        default = self.get_default_string()
        return f"{self.snake_name}: {type_} = {default}"

    def get_docstring(self) -> str:
        doc = f"{self.name} ({self.get_type_string()}): {self.schema_data.description or ''}."
        if self.schema_data.default:
            doc += f" Default: {self.schema_data.default}."
        if self.schema_data.examples:
            doc += f" Examples: {self.schema_data.examples}."
        return doc
