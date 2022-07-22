from pathlib import Path
from typing import Any, Dict, Union, Optional

import httpx
import tomli

from .log import logger
from .config import Config
from .source import get_source
from .parser import parse_openapi_spec


def build(spec: Optional[Union[httpx.URL, Path]] = None):
    pyproject = tomli.loads(Path("./pyproject.toml").read_text())
    config_dict: Dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})
    config_dict = {
        k.replace("--", "").replace("-", "_"): v for k, v in config_dict.items()
    }
    config = Config.parse_obj(config_dict)
    logger.info(f"Loaded config: {config!r}")

    source = get_source(spec or httpx.URL(config.schema_source))
    logger.info(f"Getting schema from {source.uri} succeeded!")

    logger.info("Start parsing OpenAPI spec")
    parsed_data = parse_openapi_spec(source, config)
    logger.info(
        "Successfully parsed OpenAPI spec: "
        f"{len(parsed_data.schemas)} schemas, {len(parsed_data.endpoints)} endpoints"
    )
