import os
import sys
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppDirs(BaseModel):
    SOURCE_DIR_NAME: str = "source"

    ROOT_DIR: Path = Path(__file__).parents[2]
    SOURCE_DIR: Path = ROOT_DIR / SOURCE_DIR_NAME

    if getattr(sys, "frozen", False):
        ROOT_DIR: Path = Path(sys._MEIPASS)
        SOURCE_DIR: Path = Path(sys.executable).parent

    ENV_FILE_NAME: str = ".env"
    ENV_TEMPLATE_FILE_NAME: str = ".env.template"

    ENV_FILE: Path = ROOT_DIR / ENV_FILE_NAME
    ENV_TEMPLATE_FILE: Path = ROOT_DIR / ENV_TEMPLATE_FILE_NAME

    MINECRAFT_DIR_NAME: str = ".minecraft"
    MODS_DIR_NAME: str = "mods"

    APPDATA_ROAMING_DIR: Path = Path(os.environ["APPDATA"])
    SOURCE_MODS_DIR: Path = SOURCE_DIR / MODS_DIR_NAME

    MINECRAFT_DIR: Path = APPDATA_ROAMING_DIR / MINECRAFT_DIR_NAME
    MINECRAFT_MODS_DIR: Path = MINECRAFT_DIR / MODS_DIR_NAME


class WindowSettings(BaseModel):
    geometry: str = "500x500"


class FabricInstallerSettings(BaseModel):
    mcversion: str
    loader: str


class Settings(BaseSettings):
    app_dirs: AppDirs = AppDirs()

    model_config = SettingsConfigDict(
        env_file=[
            app_dirs.ENV_FILE,
            app_dirs.ENV_TEMPLATE_FILE,
        ],
        env_file_encoding="UTF-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APPLICATION__",
    )

    program_name: str = "I-AMInstaller"

    window: WindowSettings = WindowSettings()

    fabric_installer: FabricInstallerSettings


settings = Settings()


if __name__ == "__main__":
    pass
