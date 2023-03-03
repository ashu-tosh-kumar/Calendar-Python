import os
from typing import Type


class _Config:
    """Base Config class"""

    # Placeholders
    ENV = None


class _DevelopmentConfig(_Config):
    """Development config class"""

    ENV = "development"


class _ProductionConfig(_Config):
    """Production config class"""

    ENV = "production"


_ENV_CONFIG_MAPPING: dict[str, Type[_ProductionConfig] | Type[_DevelopmentConfig]] = {
    "production": _ProductionConfig,
    "development": _DevelopmentConfig,
}
_curr_env: str = os.getenv("env") or "development"
config = _ENV_CONFIG_MAPPING[_curr_env]()
