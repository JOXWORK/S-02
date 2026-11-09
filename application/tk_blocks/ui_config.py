from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ButtonSettings(BaseModel):
    text: str
    fill: str


class WidgetSet(BaseModel):
    text: str | None = None
    fill: str | None = None
    width: int | None = None
    height: int | None = None


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


class LogPanelTKBlockSettings(BaseModel):
    LogPanel: WidgetSet = WidgetSet(fill="x", width=1, height=10)


class UISettings(BaseSettings):
    minecraft_dir: MinecraftDirTKBlockSettings = MinecraftDirTKBlockSettings()

    install_mods: InstallModsTKBlockSettings = InstallModsTKBlockSettings()

    install_fabric_loader: InstallFabricLoaderTKBlockSettings = InstallFabricLoaderTKBlockSettings()

    log_panel: LogPanelTKBlockSettings = LogPanelTKBlockSettings()


ui_settings = UISettings()
