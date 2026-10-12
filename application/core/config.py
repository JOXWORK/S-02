import os
import sys
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class SysDirs(BaseModel):
    APPDATA_ROAMING_DIR: Path = Path(os.environ["APPDATA"])


class AppDirs(BaseModel):
    SOURCE_DIR_NAME: str = "source"

    ROOT_DIR: Path = Path(__file__).parents[1]
    SOURCE_DIR: Path = ROOT_DIR / SOURCE_DIR_NAME

    if getattr(sys, "frozen", False):
        ROOT_DIR: Path = Path(sys._MEIPASS)
        SOURCE_DIR: Path = Path(sys.executable).parent


class Settings(BaseSettings):
    program_name: str = "I-AMInstaller"

    sys_dirs: SysDirs = SysDirs()

    app_dirs: AppDirs = AppDirs()


settings = Settings()


if __name__ == "__main__":
    pass
