import logging
from logging.handlers import MemoryHandler, RotatingFileHandler

from core.config import settings

console_handler = logging.StreamHandler()
rotating_file_handler = RotatingFileHandler(
    filename=settings.logger.filename,
    maxBytes=settings.logger.rotating.max_bytes,
    backupCount=settings.logger.rotating.backup_count,
    encoding=settings.logger.rotating.encoding,
)
memory_handler = MemoryHandler(capacity=500)


def init_logger():
    logging.basicConfig(
        handlers=[
            console_handler,
            rotating_file_handler,
            memory_handler,
        ],
        level=settings.logger.level,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    )

    logger = logging.getLogger()

    logger.info("-" * 50)
    logger.debug("Logger config inited")


init_logger()
