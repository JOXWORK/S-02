from pydantic import BaseModel
from pydantic_settings import BaseSettings


class MinecraftDirTKBlockSettings(BaseModel):
    fill: str = "x"


class InstallModsTKBlockSettings(BaseModel):
    text: str = "Install mods"
    fill: str = "x"


class UISettings(BaseSettings):
    minecraft_dir_tkb: MinecraftDirTKBlockSettings = MinecraftDirTKBlockSettings()

    install_mods_tkb: InstallModsTKBlockSettings = InstallModsTKBlockSettings()


ui_settings = UISettings()
