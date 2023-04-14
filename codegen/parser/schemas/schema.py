from typing import Any, Set, Dict, List, ClassVar, Optional

from pydantic import Field, BaseModel


class SchemaData(BaseModel):
    title: Optional[str] = Field(default=None, exclude=True)
    description: Optional[str] = Field(default=None, exclude=True)
    default: Optional[Any] = Field(default=None, exclude=True)
    examples: Optional[List[Any]] = Field(default=None, exclude=True)

    _type_string: ClassVar[str] = "Any"

    def get_type_string(self) -> str:
        """Get schema typing string in any place"""
        return self._type_string

    def get_param_type_string(self) -> str:
        """Get type string used by client codegen"""
        return self.get_type_string()

    def get_model_imports(self) -> Set[str]:
        """Get schema needed imports for model codegen"""
        return set()

    def get_type_imports(self) -> Set[str]:
        """Get schema needed imports for types codegen"""
        return self.get_model_imports()

    def get_param_imports(self) -> Set[str]:
        """Get schema needed imports for client param codegen"""
        return self.get_model_imports()

    def get_using_imports(self) -> Set[str]:
        """Get schema needed imports for client request codegen"""
        return self.get_model_imports()

    def _get_default_args(self) -> Dict[str, str]:
        """Get pydantic field info args"""
        args = {}
        if self.title:
            args["title"] = repr(self.title)
        if self.description:
            args["description"] = repr(self.description)
        if self.default is not None:
            args["default"] = repr(self.default)
        return args


class Property(BaseModel):
    name: str
    prop_name: str
    required: bool
    schema_data: SchemaData

    def get_type_string(self) -> str:
        """Get schema typing string in any place"""
        type_string = self.schema_data.get_type_string()
        return type_string if self.required else f"Missing[{type_string}]"

    def get_param_type_string(self) -> str:
        """Get type string used by client codegen"""
        type_string = self.schema_data.get_param_type_string()
        return type_string if self.required else f"Missing[{type_string}]"

    def get_model_imports(self) -> Set[str]:
        """Get schema needed imports for model codegen"""
        imports = self.schema_data.get_model_imports()
        imports.add("from pydantic import Field")
        if not self.required:
            imports.add("from githubkit.utils import UNSET, Missing")
        return imports

    def get_type_imports(self) -> Set[str]:
        """Get schema needed imports for type codegen"""
        imports = self.schema_data.get_type_imports()
        if not self.required:
            imports.add("from typing_extensions import NotRequired")
        return imports

    def get_param_imports(self) -> Set[str]:
        """Get schema needed imports for typing params"""
        imports = self.schema_data.get_param_imports()
        if not self.required:
            imports.add("from githubkit.utils import UNSET, Missing")
        return imports

    def _get_default_string(self) -> str:
        args = self.schema_data._get_default_args()
        if "default" not in args and "default_factory" not in args:
            args["default"] = "..." if self.required else "UNSET"
        if self.prop_name != self.name:
            args["alias"] = repr(self.name)

        arg_string = [f"{k}={v}" for k, v in args.items()]
        return f"Field({', '.join(arg_string)})"

    def get_param_defination(self) -> str:
        """Get defination used by client codegen"""
        type_ = self.get_param_type_string()
        if self.schema_data.default is None:
            return (
                f"{self.prop_name}: {type_}"
                if self.required
                else f"{self.prop_name}: {type_} = UNSET"
            )
        return f"{self.prop_name}: {type_} = {self.schema_data.default!r}"

    def get_model_defination(self) -> str:
        """Get defination used by model codegen"""
        type_ = self.get_type_string()
        default = self._get_default_string()
        return f"{self.prop_name}: {type_} = {default}"

    def get_type_defination(self) -> str:
        """Get defination used by types codegen"""
        type_ = self.schema_data.get_param_type_string()
        return (
            f"{self.prop_name}: {type_ if self.required else f'NotRequired[{type_}]'}"
        )


class AnySchema(SchemaData):
    _type_string: ClassVar[str] = "Any"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import Any")
        return imports


class NoneSchema(SchemaData):
    _type_string: ClassVar[str] = "None"


class BoolSchema(SchemaData):
    _type_string: ClassVar[str] = "bool"


class IntSchema(SchemaData):
    multiple_of: Optional[float] = None
    maximum: Optional[float] = None
    exclusive_maximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusive_minimum: Optional[float] = None

    _type_string: ClassVar[str] = "int"

    def _get_default_args(self) -> Dict[str, str]:
        args = super()._get_default_args()
        if self.multiple_of is not None:
            args["multiple_of"] = repr(self.multiple_of)
        if self.maximum is not None:
            args["le"] = repr(self.maximum)
        if self.exclusive_maximum is not None:
            args["lt"] = repr(self.exclusive_maximum)
        if self.minimum is not None:
            args["ge"] = repr(self.minimum)
        if self.exclusive_minimum is not None:
            args["gt"] = repr(self.exclusive_minimum)
        return args


class FloatSchema(SchemaData):
    multiple_of: Optional[float] = None
    maximum: Optional[float] = None
    exclusive_maximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusive_minimum: Optional[float] = None

    _type_string: ClassVar[str] = "float"

    def _get_default_args(self) -> Dict[str, str]:
        args = super()._get_default_args()
        if self.multiple_of is not None:
            args["multiple_of"] = str(self.multiple_of)
        if self.maximum is not None:
            args["le"] = str(self.maximum)
        if self.exclusive_maximum is not None:
            args["lt"] = str(self.exclusive_maximum)
        if self.minimum is not None:
            args["ge"] = str(self.minimum)
        if self.exclusive_minimum is not None:
            args["gt"] = str(self.exclusive_minimum)
        return args


class StringSchema(SchemaData):
    min_length: Optional[int] = Field(default=None, ge=0)
    max_length: Optional[int] = Field(default=None, ge=0)
    pattern: Optional[str] = None

    _type_string: ClassVar[str] = "str"

    def _get_default_args(self) -> Dict[str, str]:
        args = super()._get_default_args()
        if self.min_length is not None:
            args["min_length"] = str(self.min_length)
        if self.max_length is not None:
            args["max_length"] = str(self.max_length)
        if self.pattern is not None:
            args["regex"] = repr(self.pattern)
        return args


class DateTimeSchema(SchemaData):
    _type_string: ClassVar[str] = "datetime"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from datetime import datetime")
        return imports


class DateSchema(SchemaData):
    _type_string: ClassVar[str] = "date"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from datetime import date")
        return imports


class FileSchema(SchemaData):
    _type_string: ClassVar[str] = "FileTypes"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from githubkit.typing import FileTypes")
        return imports


class ListSchema(SchemaData):
    item_schema: SchemaData
    min_items: Optional[int] = Field(default=None, ge=0)
    max_items: Optional[int] = Field(default=None, ge=0)
    unique_items: Optional[bool] = None

    def get_type_string(self) -> str:
        return f"List[{self.item_schema.get_type_string()}]"

    def get_param_type_string(self) -> str:
        return f"List[{self.item_schema.get_param_type_string()}]"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import List")
        imports.update(self.item_schema.get_model_imports())
        return imports

    def get_type_imports(self) -> Set[str]:
        imports = {"from typing import List"}
        imports.update(self.item_schema.get_type_imports())
        return imports

    def get_param_imports(self) -> Set[str]:
        imports = {"from typing import List"}
        imports.update(self.item_schema.get_param_imports())
        return imports

    def get_using_imports(self) -> Set[str]:
        imports = {"from typing import List"}
        imports.update(self.item_schema.get_using_imports())
        return imports

    def _get_default_args(self) -> Dict[str, str]:
        args = super()._get_default_args()
        # FIXME: remove list constraints due to forwardref not supported
        # See https://github.com/samuelcolvin/pydantic/issues/3745
        if isinstance(self.item_schema, (ModelSchema, UnionSchema)):
            return args
        if self.max_items is not None:
            args["max_items"] = repr(self.max_items)
        if self.min_items is not None:
            args["min_items"] = repr(self.min_items)
        if self.unique_items is not None:
            args["unique_items"] = repr(self.unique_items)
        return args


class EnumSchema(SchemaData):
    values: List[Any]

    def is_str_enum(self) -> bool:
        return all(isinstance(value, str) for value in self.values)

    def is_bool_enum(self) -> bool:
        return all(isinstance(value, bool) for value in self.values)

    def is_int_enum(self) -> bool:
        return all(isinstance(value, int) for value in self.values)

    def is_float_enum(self) -> bool:
        return all(isinstance(value, (int, float)) for value in self.values)

    def get_type_string(self) -> str:
        return f"Literal[{', '.join(repr(value) for value in self.values)}]"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import Literal")
        return imports


class ModelSchema(SchemaData):
    class_name: str = Field(..., exclude=True)
    properties: List[Property] = Field(default_factory=list)
    allow_extra: bool = True

    def get_type_string(self) -> str:
        return self.class_name

    def get_param_type_string(self) -> str:
        return f"{self.class_name}Type"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from pydantic import BaseModel")
        if self.allow_extra:
            imports.add("from pydantic import Extra")
        for prop in self.properties:
            imports.update(prop.get_model_imports())
        return imports

    def get_type_imports(self) -> Set[str]:
        imports = {"from typing_extensions import TypedDict"}
        for prop in self.properties:
            imports.update(prop.get_type_imports())
        return imports

    def get_param_imports(self) -> Set[str]:
        return {f"from .types import {self.class_name}Type"}

    def get_using_imports(self) -> Set[str]:
        return {f"from .models import {self.class_name}"}


class UnionSchema(SchemaData):
    schemas: List[SchemaData]
    discriminator: Optional[str] = None

    def get_type_string(self) -> str:
        if len(self.schemas) == 0:
            return "Any"
        elif len(self.schemas) == 1:
            return self.schemas[0].get_type_string()
        return (
            f"Union[{', '.join(schema.get_type_string() for schema in self.schemas)}]"
        )

    def get_param_type_string(self) -> str:
        if len(self.schemas) == 1:
            return self.schemas[0].get_param_type_string()
        return f"Union[{', '.join(schema.get_param_type_string() for schema in self.schemas)}]"

    def get_model_imports(self) -> Set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import Union")
        for schema in self.schemas:
            imports.update(schema.get_model_imports())
        return imports

    def get_type_imports(self) -> Set[str]:
        imports = {"from typing import Union"}
        for schema in self.schemas:
            imports.update(schema.get_type_imports())
        return imports

    def get_param_imports(self) -> Set[str]:
        imports = {"from typing import Union"}
        for schema in self.schemas:
            imports.update(schema.get_param_imports())
        return imports

    def get_using_imports(self) -> Set[str]:
        imports = {"from typing import Union"}
        for schema in self.schemas:
            imports.update(schema.get_using_imports())
        return imports

    def _get_default_args(self) -> Dict[str, str]:
        args = {}
        for schema in self.schemas:
            args.update(schema._get_default_args())
        args.update(super()._get_default_args())
        if self.discriminator:
            args["discriminator"] = self.discriminator
        return args
