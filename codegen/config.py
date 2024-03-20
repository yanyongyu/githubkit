from typing import Any
from pathlib import Path

from pydantic import Field, BaseModel


class Override(BaseModel):
    class_overrides: dict[str, str] = Field(default_factory=dict)
    field_overrides: dict[str, str] = Field(default_factory=dict)
    schema_overrides: dict[str, dict[str, Any]] = Field(default_factory=dict)


class VersionedOverride(Override):
    target_descriptions: list[str] = Field(default_factory=list)


class DescriptionConfig(BaseModel):
    version: str
    """The version name used in the rest api header."""
    identifier: str
    """The identifier used in githubkit api versioning."""
    module: str
    """The module name used in githubkit versions."""
    is_latest: bool = False
    """If true, the description will be used as the default description."""
    source: str


class Config(BaseModel):
    output_dir: Path
    legacy_rest_models: Path
    descriptions: list[DescriptionConfig]
    overrides: list[VersionedOverride] = Field(default_factory=list)

    def get_override_config_for_version(self, version_id: str) -> Override:
        selected_overrides = [
            override
            for override in self.overrides
            if version_id in override.target_descriptions
            or not override.target_descriptions
        ]
        return Override(
            class_overrides={
                key: value
                for override in selected_overrides
                for key, value in override.class_overrides.items()
            },
            field_overrides={
                key: value
                for override in selected_overrides
                for key, value in override.field_overrides.items()
            },
            schema_overrides={
                key: value
                for override in selected_overrides
                for key, value in override.schema_overrides.items()
            },
        )
