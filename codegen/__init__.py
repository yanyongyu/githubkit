import shutil
from typing import Any
from pathlib import Path

import httpx
import tomli
from jinja2 import Environment, PackageLoader

from .config import Config
from .source import get_source
from .log import logger as logger
from .parser.schemas import ModelSchema
from .parser import (
    WebhookData,
    sanitize,
    kebab_case,
    snake_case,
    pascal_case,
    parse_openapi_spec,
)

env = Environment(
    loader=PackageLoader("codegen"),
    trim_blocks=True,
    lstrip_blocks=True,
    extensions=["jinja2.ext.loopcontrols"],
)
env.globals.update(
    {
        "repr": repr,
        "sanitize": sanitize,
        "snake_case": snake_case,
        "pascal_case": pascal_case,
        "kebab_case": kebab_case,
    }
)


def load_config() -> Config:
    pyproject = tomli.loads(Path("./pyproject.toml").read_text())
    config_dict: dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})

    return Config.model_validate(config_dict)


def build_models(dir: Path, models: list[ModelSchema]):
    logger.info("Start generating models...")
    models_template = env.get_template("models/models.py.jinja")
    models_path = dir / "__init__.py"
    models_path.write_text(models_template.render(models=models))
    logger.info("Successfully generated models!")


def build_types(dir: Path, models: list[ModelSchema]):
    logger.info("Start generating types...")
    types_template = env.get_template("models/types.py.jinja")
    types_path = dir / "__init__.py"
    types_path.write_text(types_template.render(models=models))
    logger.info("Successfully generated types!")


# def build_rest_api(description: DescriptionConfig, data: ...):
#     logger.info("Start generating rest api codes...")

#     # build models
#     logger.info("Building models...")
#     models_template = env.get_template("models/models.py.jinja")
#     models_path = version_path / "models.py"
#     models_path.write_text(models_template.render(models=data.models))
#     logger.info("Successfully built models!")

#     # build types
#     logger.info("Building types...")
#     types_template = env.get_template("models/types.py.jinja")
#     types_path = version_path / "types.py"
#     types_path.write_text(types_template.render(models=data.models))
#     logger.info("Successfully built types!")

#     # build endpoints
#     logger.info("Building endpoints...")
#     client_template = env.get_template("client/client.py.jinja")
#     for tag, endpoints in data.endpoints_by_tag.items():
#         logger.info(f"Building endpoints for tag {tag}...")
#         tag_path = version_path / f"{tag}.py"
#         tag_path.write_text(
#             client_template.render(
#                 tag=tag, endpoints=endpoints, rest_api_version=rest.version
#             )
#         )
#         logger.info(f"Successfully built endpoints for tag {tag}!")
#     logger.info("Successfully built endpoints!")

#     # build namespace
#     logger.info("Building namespace...")
#     namespace_template = env.get_template("namespace/namespace.py.jinja")
#     namespace_path = version_path / "__init__.py"
#     namespace_path.write_text(
#         namespace_template.render(tags=data.endpoints_by_tag.keys())
#     )
#     logger.info("Successfully built namespace!")

#     logger.info("Successfully generated rest api codes!")


def build_webhooks(dir: Path, all_webhooks: dict[str, list[WebhookData]]):
    logger.info("Start generating webhooks...")

    # build events
    for name, webhooks in all_webhooks.items():
        logger.info(f"Building webhooks for event {name}...")
        event_template = env.get_template("webhooks/event.py.jinja")
        event_path = dir / f"{name}.py"
        event_path.write_text(event_template.render(name=name, webhooks=webhooks))
        logger.info(f"Successfully built webhooks for event {name}!")

    # build types
    logger.info("Building webhook types...")
    types_template = env.get_template("webhooks/_types.py.jinja")
    types_path = dir / "_types.py"
    types_path.write_text(types_template.render(event_names=list(all_webhooks.keys())))
    logger.info("Successfully built webhook types!")

    # build namespace
    logger.info("Building webhooks namespace...")
    namespace_template = env.get_template("webhooks/_namespace.py.jinja")
    namespace_path = dir / "_namespace.py"
    namespace_path.write_text(
        namespace_template.render(event_names=list(all_webhooks.keys()))
    )

    # build __init__.py
    logger.info("Building webhooks __init__.py...")
    init_template = env.get_template("webhooks/__init__.py.jinja")
    init_path = dir / "__init__.py"
    init_path.write_text(init_template.render(event_names=list(all_webhooks.keys())))

    logger.info("Successfully generated webhooks!")


def build_versions(dir: Path, versions: dict[str, str], latest_version: str):
    logger.info("Start generating versions...")

    # build __init__.py
    logger.info("Building versions __init__.py...")
    init_template = env.get_template("versions.py.jinja")
    init_path = dir / "__init__.py"
    init_path.write_text(
        init_template.render(versions=versions, latest_version=latest_version)
    )

    logger.info("Successfully generated versions!")


# def _patch_openapi_spec(spec: dict[str, Any]):
#     spec.pop("webhooks", None)
#     for name in list(spec["components"]["schemas"].keys()):
#         if name.startswith("webhook-config"):
#             continue
#         elif name.startswith("webhook"):
#             del spec["components"]["schemas"][name]


def build():
    config = load_config()
    logger.info(f"Loaded config: {config!r}")

    # clean output dir
    if config.output_dir.exists():
        logger.warning(f"Output dir {config.output_dir} already exists, deleting...")
        shutil.rmtree(config.output_dir)
        config.output_dir.mkdir(parents=True, exist_ok=True)

    versions: dict[str, str] = {}
    latest_version: str | None = None

    for description in config.descriptions:
        logger.info(
            f"Start getting OpenAPI source for version {description.version}..."
        )
        source = get_source(httpx.URL(description.source))
        logger.info(f"Getting schema from {source.uri} succeeded!")

        logger.info(f"Start parsing OpenAPI spec for {description.version}...")
        override = config.get_override_config_for_version(description.version)
        # _patch_openapi_spec(source.root)
        parsed_data = parse_openapi_spec(source, override)
        logger.info(
            f"Successfully parsed OpenAPI spec {description.version}: "
            f"{len(parsed_data.models)} models, "
            f"{len(parsed_data.endpoints)} endpoints, "
            f"{len(parsed_data.webhooks)} webhooks"
        )

        logger.info(f"Start generating codes for {description.version}...")
        version_module = f"{config.version_prefix}{snake_case(description.version)}"
        versions[description.version] = version_module
        if description.is_latest:
            if latest_version is not None:
                raise RuntimeError(
                    "Found multiple latest versions: "
                    f"{latest_version}, {description.version}"
                )
            latest_version = description.version

        version_path = config.output_dir / version_module
        version_path.mkdir(parents=True, exist_ok=True)
        # generate models
        model_path = version_path / "models"
        model_path.mkdir(parents=True, exist_ok=True)
        build_models(model_path, parsed_data.models)
        type_path = version_path / "types"
        type_path.mkdir(parents=True, exist_ok=True)
        build_types(type_path, parsed_data.models)
        # generate rest api codes
        # TODO
        # build_rest_api(description, parsed_data)
        # generate webhook codes
        webhook_path = version_path / "webhooks"
        webhook_path.mkdir(parents=True, exist_ok=True)
        build_webhooks(webhook_path, parsed_data.webhooks_by_event)
        logger.info(f"Successfully generated codes for {description.version}!")

        del source, override, parsed_data

    # generate versions
    if latest_version is None:
        raise RuntimeError("No latest version found!")
    build_versions(config.output_dir, versions, latest_version)
