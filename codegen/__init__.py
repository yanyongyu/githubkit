from pathlib import Path
import shutil
import sys
from typing import Any

import httpx
from jinja2 import Environment, PackageLoader

from .config import Config
from .log import logger as logger
from .parser import (
    EndpointData,
    ModelGroup,
    WebhookData,
    kebab_case,
    parse_openapi_spec,
    pascal_case,
    sanitize,
    snake_case,
)
from .parser.schemas import UnionSchema
from .source import get_source

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

env = Environment(
    loader=PackageLoader("codegen"),
    trim_blocks=True,
    lstrip_blocks=True,
    extensions=["jinja2.ext.loopcontrols"],
)

_funcs = {
    "repr": repr,
    "sanitize": sanitize,
    "snake_case": snake_case,
    "pascal_case": pascal_case,
    "kebab_case": kebab_case,
    "is_union_schema": lambda x: isinstance(x, UnionSchema),
}
env.globals.update(_funcs)
env.filters.update(_funcs)


def load_config() -> Config:
    pyproject = tomllib.loads(Path("./pyproject.toml").read_text(encoding="utf-8"))
    config_dict: dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})

    return Config.model_validate(config_dict)


def group_name(group: ModelGroup, groups: list[ModelGroup]) -> str:
    count = len(str(len(groups)))
    return f"group_{groups.index(group):0{count}d}"


def build_models(dir: Path, groups: list[ModelGroup]):
    logger.info("Start generating models...")
    models_template = env.get_template("models/models.py.jinja")
    models_path = dir / "__init__.py"
    models_path.write_text(models_template.render(groups=groups, group_name=group_name))

    group_template = env.get_template("models/group.py.jinja")
    for group in groups:
        group_path = dir / f"{group_name(group, groups)}.py"
        group_path.write_text(
            group_template.render(group=group, groups=groups, group_name=group_name)
        )
    logger.info("Successfully generated models!")


def build_types(dir: Path, groups: list[ModelGroup]):
    logger.info("Start generating types...")
    types_template = env.get_template("models/types.py.jinja")
    types_path = dir / "__init__.py"
    types_path.write_text(types_template.render(groups=groups, group_name=group_name))

    group_template = env.get_template("models/type_group.py.jinja")
    for group in groups:
        group_path = dir / f"{group_name(group, groups)}.py"
        group_path.write_text(
            group_template.render(group=group, groups=groups, group_name=group_name)
        )
    logger.info("Successfully generated types!")


def build_rest_api(
    dir: Path, version: str, all_endpoints: dict[str, list[EndpointData]]
):
    logger.info("Start generating rest api codes...")

    # build endpoints
    logger.info("Building rest endpoints...")
    client_template = env.get_template("rest/client.py.jinja")
    for tag, endpoints in all_endpoints.items():
        logger.info(f"Building rest endpoints for tag {tag}...")
        tag_path = dir / f"{tag}.py"
        tag_path.write_text(
            client_template.render(
                tag=tag, endpoints=endpoints, rest_api_version=version
            )
        )
        logger.info(f"Successfully built rest endpoints for tag {tag}!")
    logger.info("Successfully built rest endpoints!")

    # build namespace
    logger.info("Building rest namespace...")
    namespace_template = env.get_template("rest/__init__.py.jinja")
    namespace_path = dir / "__init__.py"
    namespace_path.write_text(
        namespace_template.render(tags=list(all_endpoints.keys()))
    )
    logger.info("Successfully built rest namespace!")

    logger.info("Successfully generated rest api codes!")


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


def build_latest_version(
    dir: Path,
    output_module: str,
    latest_version_module: str,
    model_names: list[str],
    event_names: list[str],
):
    logger.info("Start generating latest version...")

    # build pkg
    logger.info("Building latest __init__.py...")
    init_template = env.get_template("__init__.py.jinja")
    init_path = dir / "__init__.py"
    init_path.write_text(init_template.render())

    # build models
    logger.info("Building latest models...")
    latest_template = env.get_template("latest/models.py.jinja")
    latest_path = dir / "models.py"
    latest_path.write_text(
        latest_template.render(
            output_module=output_module,
            latest_version_module=latest_version_module,
            model_names=model_names,
        )
    )

    # build types
    logger.info("Building latest types...")
    latest_template = env.get_template("latest/types.py.jinja")
    latest_path = dir / "types.py"
    latest_path.write_text(
        latest_template.render(
            output_module=output_module,
            latest_version_module=latest_version_module,
            model_names=model_names,
        )
    )

    # build webhooks
    logger.info("Building latest webhooks...")
    latest_template = env.get_template("latest/webhooks.py.jinja")
    latest_path = dir / "webhooks.py"
    latest_path.write_text(
        latest_template.render(
            output_module=output_module,
            latest_version_module=latest_version_module,
            event_names=event_names,
        )
    )

    logger.info("Successfully generated latest version!")


def build_legacy_rest_models(
    file: Path, output_module: str, latest_version_module: str, model_names: list[str]
):
    logger.info("Start generating legacy rest models...")
    models_template = env.get_template("latest/models.py.jinja")
    file.write_text(
        models_template.render(
            output_module=output_module,
            latest_version_module=latest_version_module,
            model_names=model_names,
        )
    )
    logger.info("Successfully generated legacy rest models!")


def build_versions(dir: Path, versions: dict[str, str], latest_version: str):
    logger.info("Start generating versions...")

    # build __init__.py
    logger.info("Building versions __init__.py...")
    init_template = env.get_template("versions/__init__.py.jinja")
    init_path = dir / "__init__.py"
    init_path.write_text(
        init_template.render(versions=versions, latest_version=latest_version)
    )

    # build rest.py
    logger.info("Building versions rest.py...")
    rest_template = env.get_template("versions/rest.py.jinja")
    rest_path = dir / "rest.py"
    rest_path.write_text(
        rest_template.render(versions=versions, latest_version=latest_version)
    )

    # build webhooks.py
    logger.info("Building versions webhooks.py...")
    webhooks_template = env.get_template("versions/webhooks.py.jinja")
    webhooks_path = dir / "webhooks.py"
    webhooks_path.write_text(
        webhooks_template.render(versions=versions, latest_version=latest_version)
    )

    logger.info("Successfully generated versions!")


def build():
    config = load_config()
    logger.info(f"Loaded config: {config!r}")

    # clean output dir
    if config.output_dir.exists():
        logger.warning(f"Output dir {config.output_dir} already exists, deleting...")
        shutil.rmtree(config.output_dir)
        config.output_dir.mkdir(parents=True, exist_ok=True)

    output_module = ".".join(config.output_dir.parts)
    versions: dict[str, str] = {}
    latest_version: str | None = None
    latest_model_names: list[str] = []
    latest_event_names: list[str] = []

    for description in config.descriptions:
        logger.info(f"Start getting OpenAPI source for {description.identifier}...")
        source = get_source(httpx.URL(description.source))
        logger.info(f"Getting schema from {source.uri} succeeded!")

        logger.info(f"Start parsing OpenAPI spec for {description.identifier}...")
        override = config.get_override_config_for_version(description.identifier)
        parsed_data = parse_openapi_spec(source, override)
        logger.info(
            f"Successfully parsed OpenAPI spec {description.identifier}: "
            f"{len(parsed_data.model_groups)} model groups, "
            f"{len(parsed_data.models)} models, "
            f"{len(parsed_data.endpoints)} endpoints, "
            f"{len(parsed_data.webhooks)} webhooks"
        )

        logger.info(f"Start generating codes for {description.identifier}...")
        versions[description.identifier] = description.module
        if description.is_latest:
            if latest_version is not None:
                raise RuntimeError(
                    "Found multiple latest versions: "
                    f"{latest_version}, {description.identifier}"
                )
            latest_version = description.identifier
            latest_model_names = [model.class_name for model in parsed_data.models]
            latest_event_names = list(parsed_data.webhooks_by_event.keys())

        version_path = config.output_dir / description.module
        version_path.mkdir(parents=True, exist_ok=True)

        # generate __init__.py
        init_template = env.get_template("__init__.py.jinja")
        init_path = version_path / "__init__.py"
        init_path.write_text(init_template.render())

        # generate models
        model_path = version_path / "models"
        model_path.mkdir(parents=True, exist_ok=True)
        build_models(model_path, parsed_data.model_groups)
        type_path = version_path / "types"
        type_path.mkdir(parents=True, exist_ok=True)
        build_types(type_path, parsed_data.model_groups)

        # generate rest api codes
        rest_path = version_path / "rest"
        rest_path.mkdir(parents=True, exist_ok=True)
        build_rest_api(rest_path, description.version, parsed_data.endpoints_by_tag)

        # generate webhook codes
        webhook_path = version_path / "webhooks"
        webhook_path.mkdir(parents=True, exist_ok=True)
        build_webhooks(webhook_path, parsed_data.webhooks_by_event)

        logger.info(f"Successfully generated codes for {description.identifier}!")

        del source, override, parsed_data

    # generate versions
    if latest_version is None:
        raise RuntimeError("No latest version found!")

    latest_path = config.output_dir / "latest"
    latest_path.mkdir(parents=True, exist_ok=True)
    build_latest_version(
        latest_path,
        output_module,
        versions[latest_version],
        latest_model_names,
        latest_event_names,
    )
    build_versions(config.output_dir, versions, latest_version)
    build_legacy_rest_models(
        config.legacy_rest_models,
        output_module,
        versions[latest_version],
        latest_model_names,
    )
