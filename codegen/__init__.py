import shutil
from pathlib import Path
from typing import Any, Dict

import httpx
import tomli
from jinja2 import Environment, PackageLoader

from .log import logger
from .source import get_source
from .config import Config, RestConfig, WebhookConfig
from .parser import (
    OpenAPIData,
    WebhookData,
    sanitize,
    kebab_case,
    snake_case,
    pascal_case,
    parse_openapi_spec,
    parse_webhook_schema,
)

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
    config_dict: Dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})

    return Config.model_validate(config_dict)


def build_rest_api(data: OpenAPIData, rest: RestConfig):
    logger.info("Start generating rest api codes...")

    client_path = Path(rest.output_dir)
    shutil.rmtree(client_path)
    client_path.mkdir(parents=True, exist_ok=True)

    # build models
    logger.info("Building models...")
    models_template = env.get_template("models/models.py.jinja")
    models_path = client_path / "models.py"
    models_path.write_text(models_template.render(models=data.models))
    logger.info("Successfully built models!")

    # build types
    logger.info("Building types...")
    types_template = env.get_template("models/types.py.jinja")
    types_path = client_path / "types.py"
    types_path.write_text(types_template.render(models=data.models))
    logger.info("Successfully built types!")

    # build endpoints
    logger.info("Building endpoints...")
    client_template = env.get_template("client/client.py.jinja")
    for tag, endpoints in data.endpoints_by_tag.items():
        logger.info(f"Building endpoints for tag {tag}...")
        tag_path = client_path / f"{tag}.py"
        tag_path.write_text(
            client_template.render(
                tag=tag, endpoints=endpoints, rest_api_version=rest.version
            )
        )
        logger.info(f"Successfully built endpoints for tag {tag}!")
    logger.info("Successfully built endpoints!")

    # build namespace
    logger.info("Building namespace...")
    namespace_template = env.get_template("namespace/namespace.py.jinja")
    namespace_path = client_path / "__init__.py"
    namespace_path.write_text(
        namespace_template.render(tags=data.endpoints_by_tag.keys())
    )
    logger.info("Successfully built namespace!")

    logger.info("Successfully generated rest api codes!")


def build_webhook(data: WebhookData, webhook: WebhookConfig):
    logger.info("Start generating webhook codes...")

    # build models
    logger.info("Building webhook models...")
    models_template = env.get_template("models/webhooks.py.jinja")
    models_path = Path(webhook.output)
    models_path.parent.mkdir(parents=True, exist_ok=True)
    models_path.write_text(models_template.render(models=data.models))
    logger.info("Successfully built webhook models!")

    # build types
    logger.info("Building webhook types...")
    types_template = env.get_template("models/webhook_types.py.jinja")
    types_path = Path(webhook.types_output)
    types_path.parent.mkdir(parents=True, exist_ok=True)
    types_path.write_text(
        types_template.render(
            definitions=data.definitions,
            model_definitions=data.model_definitions,
            union_definitions=data.union_definitions,
        )
    )
    logger.info("Successfully built webhook models!")

    logger.info("Successfully generated webhook codes!")


def _patch_openapi_spec(spec: Dict[str, Any]):
    spec.pop("webhooks", None)
    for name in list(spec["components"]["schemas"].keys()):
        if name.startswith("webhook-config"):
            continue
        elif name.startswith("webhook"):
            del spec["components"]["schemas"][name]


def build():
    config = load_config()
    logger.info(f"Loaded config: {config!r}")

    for versioned_rest in config.rest:
        logger.info(f"Start getting OpenAPI source for {versioned_rest.version}...")
        source = get_source(httpx.URL(versioned_rest.description_source))
        logger.info(f"Getting schema from {source.uri} succeeded!")

        logger.info(f"Start parsing OpenAPI spec for {versioned_rest.version}...")
        _patch_openapi_spec(source.root)
        parsed_data = parse_openapi_spec(source, versioned_rest, config)
        logger.info(
            f"Successfully parsed OpenAPI spec {versioned_rest.version}: "
            f"{len(parsed_data.schemas)} schemas, "
            f"{len(parsed_data.endpoints)} endpoints"
        )

        build_rest_api(parsed_data, versioned_rest)

        del parsed_data

    logger.info("Start getting Webhook source...")
    source = get_source(httpx.URL(config.webhook.schema_source))
    logger.info(f"Getting schema from {source.uri} succeeded!")

    logger.info("Start parsing Webhook spec...")
    parsed_data = parse_webhook_schema(source, config.webhook, config)
    logger.info(
        f"Successfully parsed Webhook spec: {len(parsed_data.definitions)} schemas"
    )

    build_webhook(parsed_data, config.webhook)
