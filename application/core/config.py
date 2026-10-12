import sys
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    program_name: str = "I-AMInstaller"

    SOURCE_DIR_NAME: str = "source"

    HOME_DIR: Path = Path.home()
    ROOT_DIR: Path = Path(__file__).parents[1]
    SOURCE_DIR: Path = ROOT_DIR / SOURCE_DIR_NAME

    if getattr(sys, "frozen", False):
        ROOT_DIR: Path = Path(sys._MEIPASS)
        SOURCE_DIR: Path = Path(sys.executable).parent


settings = Settings()
