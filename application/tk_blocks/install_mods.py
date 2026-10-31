import tkinter as tk

from core.button_funcs.install_mods import install_mods_func

from .ui_config import ui_settings


class InstallModsTKBlock:
    def __init__(self):
        self.root: tk.Tk

        self.install_mods_button = tk.Button(
            self.root,
            text=ui_settings.install_mods.InstallModsButton.text,
            command=install_mods_func,
        )

        self.install_mods_button.pack(fill=ui_settings.install_mods.InstallModsButton.fill)

        super().__init__()
