import logging

from core.config import settings


def init_logger():
    logging.basicConfig(
        filename=settings.logger.filename,
        level=settings.logger.level,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    )

    logging.getLogger().info("Logger config inited")
