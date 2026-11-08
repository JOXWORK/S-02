import logging

from core.config import settings


def init_logger():
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=settings.logger.filename)

    logging.basicConfig(
        handlers=[console_handler, file_handler],
        level=settings.logger.level,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    )

    logging.getLogger().info("Logger config inited")
