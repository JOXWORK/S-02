import os
import sys
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AppDirs(BaseModel):
    SOURCE_DIR_NAME: str = "source"

    ROOT_DIR: Path = Path(__file__).parents[1]
    SOURCE_DIR: Path = ROOT_DIR / SOURCE_DIR_NAME

    if getattr(sys, "frozen", False):
        ROOT_DIR: Path = Path(sys._MEIPASS)
        SOURCE_DIR: Path = Path(sys.executable).parent

    MINECRAFT_DIR_NAME: str = ".minecraft"

    APPDATA_ROAMING_DIR: Path = Path(os.environ["APPDATA"])
    MINECRAFT_DIR: Path = APPDATA_ROAMING_DIR / MINECRAFT_DIR_NAME


class WindowSettings(BaseModel):
    geometry: str = "500x500"


class Settings(BaseSettings):
    program_name: str = "I-AMInstaller"

    app_dirs: AppDirs = AppDirs()

    window_settings: WindowSettings = WindowSettings()


settings = Settings()


if __name__ == "__main__":
    pass
