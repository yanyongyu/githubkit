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
from .parser import sanitize, kebab_case, snake_case, pascal_case, parse_openapi_spec

env = Environment(
    loader=PackageLoader("codegen"),
    trim_blocks=True,
    lstrip_blocks=True,
    extensions=["jinja2.ext.loopcontrols"],
)
env.globals.update(
    {
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


# def build_webhook(data: WebhookData, webhook: WebhookConfig):
#     logger.info("Start generating webhook codes...")

#     # build models
#     logger.info("Building webhook models...")
#     models_template = env.get_template("models/webhooks.py.jinja")
#     models_path = Path(webhook.output)
#     models_path.parent.mkdir(parents=True, exist_ok=True)
#     models_path.write_text(models_template.render(models=data.models))
#     logger.info("Successfully built webhook models!")

#     # build types
#     logger.info("Building webhook types...")
#     types_template = env.get_template("models/webhook_types.py.jinja")
#     types_path = Path(webhook.types_output)
#     types_path.parent.mkdir(parents=True, exist_ok=True)
#     types_path.write_text(
#         types_template.render(
#             definitions=data.definitions,
#             model_definitions=data.model_definitions,
#             union_definitions=data.union_definitions,
#         )
#     )
#     logger.info("Successfully built webhook models!")

#     logger.info("Successfully generated webhook codes!")


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
        version_path = (
            config.output_dir
            / f"{config.version_prefix}{snake_case(description.version)}"
        )
        version_path.mkdir(parents=True, exist_ok=True)
        # generate models
        model_path = version_path / "models"
        build_models(model_path, parsed_data.models)
        type_path = version_path / "types"
        build_types(type_path, parsed_data.models)
        # generate rest api codes
        # build_rest_api(description, parsed_data)
        # generate webhook codes
        # build_webhook()
        # TODO
        logger.info(f"Successfully generated codes for {description.version}!")

        del source, override, parsed_data
