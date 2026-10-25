from pydantic import BaseModel
from pydantic_settings import BaseSettings


class MinecraftDirTKBlockSettings(BaseModel):
    fill: str = "x"


class UISettings(BaseSettings):
    minecraft_dir_tkb: MinecraftDirTKBlockSettings = MinecraftDirTKBlockSettings()


ui_settings = UISettings()
