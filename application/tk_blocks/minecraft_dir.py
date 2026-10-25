import tkinter as tk

from core.config import settings

from .ui_config import ui_settings


class MinecraftDirTKBlock:
    def __init__(self):
        self.root: tk.Tk

        entry_value = tk.StringVar(value=settings.sys_dirs.MINECRAFT_DIR)

        self.minecraft_dir_entry = tk.Entry(
            self.root,
            textvariable=entry_value,
        )

        self.minecraft_dir_entry.pack(fill=ui_settings.minecraft_dir_tkb.fill)
