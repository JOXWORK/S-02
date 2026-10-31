import tkinter as tk

from core.button_funcs.install_fabric_loader import install_fabric_loader

from .ui_config import ui_settings


class InstallFabricLoaderTKBlock:
    def __init__(self):
        self.root: tk.Tk

        self.install_fabric_loader_button = tk.Button(
            self.root,
            text=ui_settings.install_fabric_loader.InstallFabricLoaderButton.text,
            command=install_fabric_loader,
        )
        self.install_fabric_loader_button.pack(fill=ui_settings.install_fabric_loader.InstallFabricLoaderButton.fill)

        super().__init__()
