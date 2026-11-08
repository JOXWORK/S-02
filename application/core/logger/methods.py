import logging
import sys
from collections.abc import Callable
from functools import wraps


def dolog(msg: str | None = None, level: int = logging.INFO, *, custom_logger: logging.Logger | None = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        logger = custom_logger or logging.getLogger(func.__module__)
        func_name = func.__name__

        log = msg or f"Call {func_name}"
        if func.__name__ == "__init__" and msg is None:
            log = f"Init {func.__qualname__.replace('.__init__', '')}"

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(log)
                result = func(*args, **kwargs)

                return result
            except Exception:
                logger.exception(f"Func {func_name} finished with exception")
                sys.exit(1)

        return wrapper

    return decorator
