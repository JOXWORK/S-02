import tkinter as tk
from pathlib import Path

from core.config import MinecraftDirs, settings

from .ui_config import ui_settings


class MinecraftDirTKBlock:
    def __init__(self):
        self.root: tk.Tk

        self.entry_value = tk.StringVar(value=settings.app_dirs.minecraft.MINECRAFT_DIR)

        self.minecraft_dir_entry = tk.Entry(
            self.root,
            textvariable=self.entry_value,
        )
        self.minecraft_dir_entry.bind("<Return>", self.minecraft_dir_entry_bind_enter)
        self.minecraft_dir_entry.bind("<Escape>", self.minecraft_dir_entry_bind_esc)

        self.minecraft_dir_entry.pack(fill=ui_settings.minecraft_dir.MinecraftDirEntry.fill)

        super().__init__()

    def minecraft_dir_entry_bind_enter(self, event: tk.Event):
        user_input = self.minecraft_dir_entry.get()

        new_minecraft_root = Path(user_input)
        if not new_minecraft_root.exists() or not new_minecraft_root.is_dir():
            self._set_entry_value_and_focus()
            return

        new_minecraft_dirs = MinecraftDirs(MINECRAFT_DIR=new_minecraft_root)
        settings.app_dirs.minecraft = new_minecraft_dirs

        self.root.focus()

    def minecraft_dir_entry_bind_esc(self, event: tk.Event):
        self._set_entry_value_and_focus()

    def _set_entry_value_and_focus(self):
        self.entry_value.set(settings.app_dirs.minecraft.MINECRAFT_DIR)
        self.root.focus()
