import os
from pathlib import Path
from typing import Dict, Any

import yaml
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

def load_config() -> Dict[str, Any]:
    """Loads the configuration from the config.yaml file."""
    
    config = {}
    config_file = BASE_DIR / "config" / "config.yaml"
    if config_file.exists():
        with open(config_file, "r") as f:
            yaml_config = yaml.safe_load(f)
            if yaml_config:
                _deep_merge(config, yaml_config)
    
    return config


def _deep_merge(dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge(s) two distinct dictionaries, overwriting if necessary."""

    for key, value in dict_b.items():
        if key in dict_a and isinstance(dict_a[key], dict) and isinstance(value, dict):
            _deep_merge(dict_a[key], value)
        else:
            dict_a[key] = value
    return dict_a
