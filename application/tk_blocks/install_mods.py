import shutil
import tkinter as tk
from datetime import datetime

from core.config import settings

from .ui_config import ui_settings


class InstallModsTKBlock:
    def __init__(self):
        self.root: tk.Tk

        self.install_mods_button = tk.Button(
            self.root,
            text=ui_settings.install_mods.InstallModsButton.text,
            command=self.install_mods_func,
        )

        self.install_mods_button.pack(fill=ui_settings.install_mods.InstallModsButton.fill)

        super().__init__()

    def install_mods_func(self):
        MINECRAFT_MODS_DIR = settings.app_dirs.minecraft.MINECRAFT_MODS_DIR

        if MINECRAFT_MODS_DIR.exists():
            rename_datetime_str = str(datetime.now())
            restruct_datetime_str = rename_datetime_str.replace(" ", "_").replace(":", "-")

            MINECRAFT_MODS_DIR.rename(f"{MINECRAFT_MODS_DIR}.old.{restruct_datetime_str}")

        shutil.copytree(
            settings.app_dirs.SOURCE_MODS_DIR,
            settings.app_dirs.minecraft.MINECRAFT_MODS_DIR,
        )
