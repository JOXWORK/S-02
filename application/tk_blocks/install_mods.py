import tkinter as tk

from core.button_funcs.install_mods_func import install_mods_func

from .ui_config import ui_settings


class InstallModsTKBlock:
    def __init__(self):
        self.root: tk.Tk

        self.InstallModsButton = ui_settings.install_mods_tkb.InstallModsButton

        self.install_mods_button = tk.Button(
            self.root,
            text=self.InstallModsButton.text,
            command=install_mods_func,
        )

        self.install_mods_button.pack(fill=self.InstallModsButton.fill)

        super().__init__()
