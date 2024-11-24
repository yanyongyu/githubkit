from dataclasses import dataclass, field
from typing import Any, ClassVar
from typing_extensions import override


@dataclass(kw_only=True)
class SchemaData:
    title: str | None = field(default=None, compare=False)
    description: str | None = field(default=None, compare=False)
    default: Any | None = field(default=None, compare=False)
    examples: list[Any] | None = field(default=None, compare=False)

    _type_string: ClassVar[str] = "Any"

    def get_type_string(self, include_constraints: bool = True) -> str:
        """Get schema typing string in any place"""
        if include_constraints and (args := self._get_field_args()):
            return f"Annotated[{self._type_string}, {self._get_field_string(args)}]"
        return self._type_string

    def get_param_type_string(self) -> str:
        """Get type string used by client codegen"""
        return self._type_string

    def get_model_imports(self) -> set[str]:
        """Get schema needed imports for model codegen"""
        if self._get_field_args():
            return {
                "from pydantic import Field",
                "from typing import Annotated",
            }
        return set()

    def get_type_imports(self) -> set[str]:
        """Get schema needed imports for types codegen"""
        return set()

    def get_param_imports(self) -> set[str]:
        """Get schema needed imports for client param codegen"""
        return set()

    def get_using_imports(self) -> set[str]:
        """Get schema needed imports for client request codegen"""
        return set()

    def _get_field_string(self, args: dict[str, str]) -> str:
        return f"Field({', '.join(f'{k}={v}' for k, v in args.items())})"

    def _get_field_args(self) -> dict[str, str]:
        """Get pydantic field constraints"""
        return {}

    def get_model_dependencies(self) -> list["ModelSchema"]:
        return []


@dataclass(kw_only=True)
class Property:
    """Property data

    This indicates a property with its name and schema.
    """

    name: str
    prop_name: str
    required: bool
    schema_data: SchemaData

    def get_type_string(self, include_constraints: bool = True) -> str:
        """Get schema typing string in any place"""
        type_string = self.schema_data.get_type_string(
            include_constraints=include_constraints
        )
        return type_string if self.required else f"Missing[{type_string}]"

    def get_param_type_string(self) -> str:
        """Get type string used by client codegen"""
        type_string = self.schema_data.get_param_type_string()
        return type_string if self.required else f"Missing[{type_string}]"

    def get_model_defination(self) -> str:
        """Get defination used by model codegen"""
        # extract the outermost type constraints to the field
        type_ = self.get_type_string(include_constraints=False)
        args = self.schema_data._get_field_args()
        args.update(self._get_field_args())
        default = self._get_field_string(args)
        return f"{self.prop_name}: {type_} = {default}"

    def get_type_defination(self) -> str:
        """Get defination used by types codegen"""
        type_ = self.schema_data.get_param_type_string()
        return (
            f"{self.prop_name}: {type_ if self.required else f'NotRequired[{type_}]'}"
        )

    def get_param_defination(self) -> str:
        """Get defination used by client codegen"""
        type_ = self.get_param_type_string()
        return (
            (
                f"{self.prop_name}: {type_}"
                if self.schema_data.default is None
                else f"{self.prop_name}: {type_} = {self.schema_data.default!r}"
            )
            if self.required
            else f"{self.prop_name}: {type_} = UNSET"
        )

    def get_model_imports(self) -> set[str]:
        """Get schema needed imports for model codegen"""
        imports = self.schema_data.get_model_imports()
        imports.add("from pydantic import Field")
        if not self.required:
            imports.add("from githubkit.utils import UNSET")
            imports.add("from githubkit.typing import Missing")
        return imports

    def get_type_imports(self) -> set[str]:
        """Get schema needed imports for type codegen"""
        imports = self.schema_data.get_type_imports()
        if not self.required:
            imports.add("from typing_extensions import NotRequired")
        return imports

    def get_param_imports(self) -> set[str]:
        """Get schema needed imports for typing params"""
        imports = self.schema_data.get_param_imports()
        if not self.required:
            imports.add("from githubkit.utils import UNSET")
            imports.add("from githubkit.typing import Missing")
        return imports

    def _get_field_string(self, args: dict[str, str]) -> str:
        return f"Field({', '.join(f'{k}={v}' for k, v in args.items())})"

    def _get_field_args(self) -> dict[str, str]:
        args = {}
        if not self.required:
            args["default"] = "UNSET"
        elif self.required and self.schema_data.default is not None:
            args["default"] = repr(self.schema_data.default)
        if self.prop_name != self.name:
            args["alias"] = repr(self.name)
        if self.schema_data.title is not None:
            args["title"] = repr(self.schema_data.title)
        if self.schema_data.description is not None:
            args["description"] = repr(self.schema_data.description)
        return args


@dataclass(kw_only=True)
class AnySchema(SchemaData):
    _type_string: ClassVar[str] = "Any"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import Any")
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.add("from typing import Any")
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.add("from typing import Any")
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from typing import Any")
        return imports


@dataclass(kw_only=True)
class NoneSchema(SchemaData):
    _type_string: ClassVar[str] = "None"


@dataclass(kw_only=True)
class BoolSchema(SchemaData):
    _type_string: ClassVar[str] = "bool"


@dataclass(kw_only=True)
class IntSchema(SchemaData):
    multiple_of: float | None = None
    maximum: float | None = None
    exclusive_maximum: float | None = None
    minimum: float | None = None
    exclusive_minimum: float | None = None

    _type_string: ClassVar[str] = "int"

    @override
    def _get_field_args(self) -> dict[str, str]:
        args = super()._get_field_args()
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


@dataclass(kw_only=True)
class FloatSchema(SchemaData):
    multiple_of: float | None = None
    maximum: float | None = None
    exclusive_maximum: float | None = None
    minimum: float | None = None
    exclusive_minimum: float | None = None

    _type_string: ClassVar[str] = "float"

    @override
    def _get_field_args(self) -> dict[str, str]:
        args = super()._get_field_args()
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


@dataclass(kw_only=True)
class StringSchema(SchemaData):
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | None = None

    _type_string: ClassVar[str] = "str"

    @override
    def _get_field_args(self) -> dict[str, str]:
        args = super()._get_field_args()
        if self.min_length is not None:
            args["min_length"] = repr(self.min_length)
        if self.max_length is not None:
            args["max_length"] = repr(self.max_length)
        if self.pattern is not None:
            args["pattern"] = repr(self.pattern)
        return args


@dataclass(kw_only=True)
class DateTimeSchema(SchemaData):
    _type_string: ClassVar[str] = "datetime"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from datetime import datetime")
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.add("from datetime import datetime")
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.add("from datetime import datetime")
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from datetime import datetime")
        return imports


@dataclass(kw_only=True)
class DateSchema(SchemaData):
    _type_string: ClassVar[str] = "date"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from datetime import date")
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.add("from datetime import date")
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.add("from datetime import date")
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from datetime import date")
        return imports


@dataclass(kw_only=True)
class FileSchema(SchemaData):
    _type_string: ClassVar[str] = "FileTypes"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from githubkit.typing import FileTypes")
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.add("from githubkit.typing import FileTypes")
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.add("from githubkit.typing import FileTypes")
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from githubkit.typing import FileTypes")
        return imports


@dataclass(kw_only=True)
class ListSchema(SchemaData):
    item_schema: SchemaData
    min_length: int | None = None
    max_length: int | None = None

    _type_string: ClassVar[str] = "list"

    @override
    def get_type_string(self, include_constraints: bool = True) -> str:
        type_string = f"list[{self.item_schema.get_type_string()}]"
        if include_constraints and (args := self._get_field_args()):
            return f"Annotated[{type_string}, {self._get_field_string(args)}]"
        return type_string

    @override
    def get_param_type_string(self) -> str:
        return f"list[{self.item_schema.get_param_type_string()}]"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from githubkit.compat import PYDANTIC_V2")
        imports.update(self.item_schema.get_model_imports())
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.update(self.item_schema.get_type_imports())
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.update(self.item_schema.get_param_imports())
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from githubkit.compat import PYDANTIC_V2")
        imports.update(self.item_schema.get_using_imports())
        return imports

    @override
    def _get_field_args(self) -> dict[str, str]:
        args = super()._get_field_args()
        # pydantic v1 uses min_items/max_items list constraints
        # but this will cause error when using forwardref
        # See https://github.com/samuelcolvin/pydantic/issues/3745
        # So remove constraints when using pydantic v1
        if self.max_length is not None:
            # args["max_items"] = f"{self.max_length!r} if not PYDANTIC_V2 else None"
            args["max_length"] = f"{self.max_length!r} if PYDANTIC_V2 else None"
        if self.min_length is not None:
            # args["min_items"] = f"{self.min_length!r} if not PYDANTIC_V2 else None"
            args["min_length"] = f"{self.min_length!r} if PYDANTIC_V2 else None"
        return args

    @override
    def get_model_dependencies(self) -> list["ModelSchema"]:
        if isinstance(self.item_schema, ModelSchema):
            return [self.item_schema]
        return self.item_schema.get_model_dependencies()


@dataclass(kw_only=True)
class UniqueListSchema(SchemaData):
    item_schema: SchemaData
    min_length: int | None = None
    max_length: int | None = None

    _type_string: ClassVar[str] = "UniqueList"

    @override
    def get_type_string(self, include_constraints: bool = True) -> str:
        type_string = f"UniqueList[{self.item_schema.get_type_string()}]"
        if include_constraints and (args := self._get_field_args()):
            return f"Annotated[{type_string}, {self._get_field_string(args)}]"
        return type_string

    @override
    def get_param_type_string(self) -> str:
        return f"UniqueList[{self.item_schema.get_param_type_string()}]"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from githubkit.typing import UniqueList")
        imports.add("from githubkit.compat import PYDANTIC_V2")
        imports.update(self.item_schema.get_model_imports())
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        # imports = super().get_type_imports()
        imports = {"from githubkit.typing import UniqueList"}
        imports.update(self.item_schema.get_type_imports())
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        # imports = super().get_param_imports()
        imports = {"from githubkit.typing import UniqueList"}
        imports.update(self.item_schema.get_param_imports())
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        # imports = super().get_using_imports()
        imports = {"from githubkit.typing import UniqueList"}
        imports.update(self.item_schema.get_using_imports())
        return imports

    @override
    def _get_field_args(self) -> dict[str, str]:
        args = super()._get_field_args()
        # pydantic v1 uses min_items/max_items list constraints
        # but this will cause error when using forwardref
        # See https://github.com/samuelcolvin/pydantic/issues/3745
        # So remove constraints when using pydantic v1
        if self.max_length is not None:
            # args["max_items"] = f"{self.max_length!r} if not PYDANTIC_V2 else None"
            args["max_length"] = f"{self.max_length!r} if PYDANTIC_V2 else None"
        if self.min_length is not None:
            # args["min_items"] = f"{self.min_length!r} if not PYDANTIC_V2 else None"
            args["min_length"] = f"{self.min_length!r} if PYDANTIC_V2 else None"
        return args

    @override
    def get_model_dependencies(self) -> list["ModelSchema"]:
        if isinstance(self.item_schema, ModelSchema):
            return [self.item_schema]
        return self.item_schema.get_model_dependencies()


@dataclass(kw_only=True)
class EnumSchema(SchemaData):
    values: list[Any]

    def is_str_enum(self) -> bool:
        return all(isinstance(value, str) for value in self.values)

    def is_bool_enum(self) -> bool:
        return all(isinstance(value, bool) for value in self.values)

    def is_int_enum(self) -> bool:
        return all(isinstance(value, int) for value in self.values)

    def is_float_enum(self) -> bool:
        return all(isinstance(value, int | float) for value in self.values)

    @override
    def get_type_string(self, include_constraints: bool = True) -> str:
        type_string = f"Literal[{', '.join(repr(value) for value in self.values)}]"
        if include_constraints and (args := self._get_field_args()):
            return f"Annotated[{type_string}, {self._get_field_string(args)}]"
        return type_string

    @override
    def get_param_type_string(self) -> str:
        return f"Literal[{', '.join(repr(value) for value in self.values)}]"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import Literal")
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.add("from typing import Literal")
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.add("from typing import Literal")
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from typing import Literal")
        return imports


@dataclass(kw_only=True)
class ModelSchema(SchemaData):
    class_name: str = field(compare=False)
    properties: list[Property] = field(default_factory=list)
    allow_extra: bool = True

    _type_string: ClassVar[str] = "dict"

    @override
    def get_type_string(self, include_constraints: bool = True) -> str:
        if include_constraints and (args := self._get_field_args()):
            return f"Annotated[{self.class_name}, {self._get_field_string(args)}]"
        return self.class_name

    @override
    def get_param_type_string(self) -> str:
        return f"{self.class_name}Type"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        if self.allow_extra:
            imports.add("from githubkit.compat import ExtraGitHubModel")
        else:
            imports.add("from githubkit.compat import GitHubModel")
        for prop in self.properties:
            imports.update(prop.get_model_imports())
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = {"from typing_extensions import TypedDict"}
        for prop in self.properties:
            imports.update(prop.get_type_imports())
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        return {f"from ..types import {self.get_param_type_string()}"}

    @override
    def get_using_imports(self) -> set[str]:
        return {f"from ..models import {self.class_name}"}

    @override
    def get_model_dependencies(self) -> list["ModelSchema"]:
        result: list[ModelSchema] = []
        for prop in self.properties:
            if isinstance(prop.schema_data, ModelSchema):
                if id(prop.schema_data) not in set(map(id, result)):
                    result.append(prop.schema_data)
            else:
                for model in prop.schema_data.get_model_dependencies():
                    if id(model) not in set(map(id, result)):
                        result.append(model)
        return result


@dataclass(kw_only=True)
class UnionSchema(SchemaData):
    schemas: list[SchemaData]
    discriminator: str | None = None

    @override
    def get_type_string(self, include_constraints: bool = True) -> str:
        if len(self.schemas) == 0:
            return "Any"
        elif len(self.schemas) == 1:
            return self.schemas[0].get_type_string()
        type_string = (
            f"Union[{', '.join(schema.get_type_string() for schema in self.schemas)}]"
        )
        if include_constraints and (args := self._get_field_args()):
            return f"Annotated[{type_string}, {self._get_field_string(args)}]"
        return type_string

    @override
    def get_param_type_string(self) -> str:
        if len(self.schemas) == 0:
            return "Any"
        elif len(self.schemas) == 1:
            return self.schemas[0].get_param_type_string()
        types = ", ".join(schema.get_param_type_string() for schema in self.schemas)
        return f"Union[{types}]"

    @override
    def get_model_imports(self) -> set[str]:
        imports = super().get_model_imports()
        imports.add("from typing import Union")
        for schema in self.schemas:
            imports.update(schema.get_model_imports())
        return imports

    @override
    def get_type_imports(self) -> set[str]:
        imports = super().get_type_imports()
        imports.add("from typing import Union")
        for schema in self.schemas:
            imports.update(schema.get_type_imports())
        return imports

    @override
    def get_param_imports(self) -> set[str]:
        imports = super().get_param_imports()
        imports.add("from typing import Union")
        for schema in self.schemas:
            imports.update(schema.get_param_imports())
        return imports

    @override
    def get_using_imports(self) -> set[str]:
        imports = super().get_using_imports()
        imports.add("from typing import Union")
        for schema in self.schemas:
            imports.update(schema.get_using_imports())
        return imports

    def _get_field_args(self) -> dict[str, str]:
        args = super()._get_field_args()
        if self.discriminator:
            args["discriminator"] = repr(self.discriminator)
        return args

    @override
    def get_model_dependencies(self) -> list[ModelSchema]:
        result: list[ModelSchema] = []
        for schema in self.schemas:
            if isinstance(schema, ModelSchema):
                if id(schema) not in set(map(id, result)):
                    result.append(schema)
            else:
                for model in schema.get_model_dependencies():
                    if id(model) not in set(map(id, result)):
                        result.append(model)
        return result
