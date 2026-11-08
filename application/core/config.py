import logging
import os
import sys
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class FSNames(BaseModel):
    SOURCE_DIR_NAME: str = "source"

    ENV_FILE_NAME: str = ".env"
    ENV_TEMPLATE_FILE_NAME: str = ".env.template"

    MINECRAFT_DIR_NAME: str = ".minecraft"
    MODS_DIR_NAME: str = "mods"

    FABRIC_INSTALLER_JAR_NAME: str = "fabric-installer.jar"


class MinecraftDirs(BaseModel):
    fsnames: FSNames = FSNames()

    APPDATA_ROAMING_DIR: Path = Path(os.environ["APPDATA"])

    MINECRAFT_DIR: Path = APPDATA_ROAMING_DIR / fsnames.MINECRAFT_DIR_NAME

    @property
    def MINECRAFT_MODS_DIR(self):
        return self.MINECRAFT_DIR / self.fsnames.MODS_DIR_NAME


class AppDirs(BaseModel):
    fsnames: FSNames = FSNames()

    minecraft: MinecraftDirs = MinecraftDirs(fsnames=fsnames)

    ROOT_DIR: Path = Path(__file__).parents[2]
    SOURCE_DIR: Path = ROOT_DIR / fsnames.SOURCE_DIR_NAME

    if getattr(sys, "frozen", False):
        ROOT_DIR: Path = Path(sys._MEIPASS)
        SOURCE_DIR: Path = Path(sys.executable).parent

    ENV_FILE: Path = ROOT_DIR / fsnames.ENV_FILE_NAME
    ENV_TEMPLATE_FILE: Path = ROOT_DIR / fsnames.ENV_TEMPLATE_FILE_NAME

    SOURCE_MODS_DIR: Path = SOURCE_DIR / fsnames.MODS_DIR_NAME

    FABRIC_INSTALLER_JAR: Path = SOURCE_DIR / fsnames.FABRIC_INSTALLER_JAR_NAME


class WindowSettings(BaseModel):
    geometry: str = "500x500"


class FabricInstallerSettings(BaseModel):
    mcversion: str
    loader: str


class LoggerSettings(BaseModel):
    filename: str = "app.log"
    level: int = logging.DEBUG


class Settings(BaseSettings):
    app_dirs: AppDirs = AppDirs()

    model_config = SettingsConfigDict(
        env_file=[
            app_dirs.ENV_TEMPLATE_FILE,
            app_dirs.ENV_FILE,
        ],
        env_file_encoding="UTF-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APPLICATION__",
        validate_assignment=True,
    )

    program_name: str = "I-AMInstaller"

    window: WindowSettings = WindowSettings()

    fabric_installer: FabricInstallerSettings

    logger: LoggerSettings = LoggerSettings()


settings = Settings()


if __name__ == "__main__":
    pass
