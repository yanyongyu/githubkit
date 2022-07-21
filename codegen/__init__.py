from pathlib import Path
from typing import Any, Dict, Union

import httpx
import tomli

from .config import Config
from .source import get_source
from .parser import parse_openapi_spec


def build(spec: Union[httpx.URL, Path]):
    pyproject = tomli.loads(Path("./pyproject.toml").read_text())
    config_dict: Dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})
    config_dict = {
        k.replace("--", "").replace("-", "_"): v for k, v in config_dict.items()
    }
    config = Config.parse_obj(config_dict)
    source = get_source(spec)

    parsed_data = parse_openapi_spec(source, config)
    print(len(parsed_data.endpoints))
