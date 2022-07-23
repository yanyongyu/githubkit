from typing import Any, Set, Dict, List, ClassVar, Optional

from pydantic import Field, BaseModel


class SchemaData(BaseModel):

    title: Optional[str] = Field(default=None, exclude=True)
    description: Optional[str] = Field(default=None, exclude=True)
    default: Optional[Any] = Field(default=None, exclude=True)
    examples: Optional[List[Any]] = Field(default=None, exclude=True)

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


class Property(BaseModel):
    name: str
    prop_name: str
    required: bool
    schema_data: SchemaData

    def get_type_string(self) -> str:
        type_string = self.schema_data.get_type_string()
        return type_string if self.required else f"Union[Unset, {type_string}]"

    def get_imports(self) -> Set[str]:
        imports = self.schema_data.get_imports()
        imports.add("from pydantic import Field")
        if not self.required:
            imports.add("from typing import Union")
            imports.add("from githubkit.utils import UNSET, Unset")
        return imports

    def get_default_string(self) -> str:
        args = self.schema_data.get_default_args()
        if "default" not in args and "default_factory" not in args:
            args["default"] = "..." if self.required else "UNSET"
        if self.prop_name != self.name:
            args["alias"] = repr(self.name)

        arg_string = [f"{k}={v}" for k, v in args.items()]
        return f"Field({', '.join(arg_string)})"

    def get_param_string(self) -> str:
        type_ = self.get_type_string()
        if self.schema_data.default is None:
            return f"{self.prop_name}: {type_}"
        return f"{self.prop_name}: {type_} = {self.schema_data.default!r}"

    def get_attr_string(self) -> str:
        type_ = self.get_type_string()
        default = self.get_default_string()
        return f"{self.prop_name}: {type_} = {default}"


class AnySchema(SchemaData):
    _type_string: ClassVar[str] = "Any"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
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

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args()
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

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args()
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

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args() or {}
        if self.min_length is not None:
            args["min_length"] = str(self.min_length)
        if self.max_length is not None:
            args["max_length"] = str(self.max_length)
        if self.pattern is not None:
            args["regex"] = repr(self.pattern)
        return args


class DateTimeSchema(SchemaData):
    _type_string: ClassVar[str] = "datetime"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from datetime import datetime")
        return imports


class DateSchema(SchemaData):
    _type_string: ClassVar[str] = "date"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from datetime import date")
        return imports


class FileSchema(SchemaData):
    _type_string: ClassVar[str] = "FileTypes"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from githubkit.typing import FileTypes")
        return imports


class ListSchema(SchemaData):
    item_schema: SchemaData
    min_items: Optional[int] = Field(default=None, ge=0)
    max_items: Optional[int] = Field(default=None, ge=0)
    unique_items: Optional[bool] = None

    def get_type_string(self) -> str:
        return f"List[{self.item_schema.get_type_string()}]"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from typing import List")
        return imports

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args()
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

    def is_int_enum(self) -> bool:
        return all(isinstance(value, int) for value in self.values)

    def is_float_enum(self) -> bool:
        return all(isinstance(value, (int, float)) for value in self.values)

    def get_type_string(self) -> str:
        return f"Literal[{', '.join(repr(value) for value in self.values)}]"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from typing import Literal")
        return imports


class ModelSchema(SchemaData):
    class_name: str = Field(..., exclude=True)
    properties: List[Property] = Field(default_factory=list)
    allow_extra: bool = True

    @property
    def required_properties(self) -> List[Property]:
        return [prop for prop in self.properties if prop.required]

    @property
    def optional_properties(self) -> List[Property]:
        return [prop for prop in self.properties if not prop.required]

    def get_model_dependencies(self) -> List["ModelSchema"]:
        return [
            prop.schema_data
            for prop in self.properties
            if isinstance(prop.schema_data, ModelSchema)
        ]

    def get_type_string(self) -> str:
        return self.class_name

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from pydantic import BaseModel")
        if self.allow_extra:
            imports.add("from pydantic import Extra")
        for prop in self.properties:
            imports.update(prop.get_imports())
        return imports


class UnionSchema(SchemaData):
    schemas: List[SchemaData]
    discriminator: Optional[str] = None

    def get_type_string(self) -> str:
        if len(self.schemas) == 1:
            return self.schemas[0].get_type_string()
        return (
            f"Union[{', '.join(schema.get_type_string() for schema in self.schemas)}]"
        )

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        for schema in self.schemas:
            imports.update(schema.get_imports())
        imports.add("from typing import Union")
        return imports

    def get_default_args(self) -> Dict[str, str]:
        args = {}
        for schema in self.schemas:
            args.update(schema.get_default_args())
        args.update(super().get_default_args())
        if self.discriminator:
            args["discriminator"] = self.discriminator
        return args
