import os
from _version import __version__
from shared.logging import logger, tracer


VERSION = __version__


def get_config() -> dict:
    with tracer.start_as_current_span("get_config"):
        config = {}       
        arm_environment = os.environ.get("ARM_ENVIRONMENT", "public")
        print(f"ARM_ENVIRONMENT variable value: {arm_environment}")
        config["arm_environment"] = arm_environment        
    return config
