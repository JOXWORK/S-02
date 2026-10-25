from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ButtonSettings(BaseModel):
    text: str
    fill: str


class EntrySettings(BaseModel):
    fill: str


class MinecraftDirTKBlockSettings(BaseModel):
    MinecraftDirEntry: EntrySettings = EntrySettings(fill="x")


class InstallModsTKBlockSettings(BaseModel):
    InstallModsButton: ButtonSettings = ButtonSettings(
        text="Install mods",
        fill="x",
    )


class UISettings(BaseSettings):
    minecraft_dir_tkb: MinecraftDirTKBlockSettings = MinecraftDirTKBlockSettings()

    install_mods_tkb: InstallModsTKBlockSettings = InstallModsTKBlockSettings()


ui_settings = UISettings()
