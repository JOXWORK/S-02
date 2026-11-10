import logging
from logging.handlers import MemoryHandler

from core.config import settings

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename=settings.logger.filename, encoding="UTF-8")
memory_handler = MemoryHandler(capacity=500)


def init_logger():
    logging.basicConfig(
        handlers=[
            console_handler,
            file_handler,
            memory_handler,
        ],
        level=settings.logger.level,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    )

    logger = logging.getLogger()

    logger.info("-" * 50)
    logger.debug("Logger config inited")


init_logger()
