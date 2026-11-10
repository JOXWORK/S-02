from pydantic import BaseModel
from pydantic_settings import BaseSettings


class WidgetSet(BaseModel):
    text: str | None = None
    fill: str | None = None
    width: int | None = None
    height: int | None = None


class MinecraftDirTKBlockSettings(BaseModel):
    MinecraftDirEntry: WidgetSet = WidgetSet(fill="x")


class InstallModsTKBlockSettings(BaseModel):
    InstallModsButton: WidgetSet = WidgetSet(
        text="Install mods",
        fill="x",
    )


class InstallFabricLoaderTKBlockSettings(BaseModel):
    InstallFabricLoaderButton: WidgetSet = WidgetSet(
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
