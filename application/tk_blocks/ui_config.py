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


class InstallFabricLoaderTKBlockSettings(BaseModel):
    InstallFabricLoaderButton: ButtonSettings = ButtonSettings(
        text="Install Fabric Loader",
        fill="x",
    )


class UISettings(BaseSettings):
    minecraft_dir: MinecraftDirTKBlockSettings = MinecraftDirTKBlockSettings()

    install_mods: InstallModsTKBlockSettings = InstallModsTKBlockSettings()

    install_fabric_loader: InstallFabricLoaderTKBlockSettings = InstallFabricLoaderTKBlockSettings()


ui_settings = UISettings()
