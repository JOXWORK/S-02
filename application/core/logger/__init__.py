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

    logger = logging.getLogger()

    logger.info("-" * 50)
    logger.debug("Logger config inited")


init_logger()
