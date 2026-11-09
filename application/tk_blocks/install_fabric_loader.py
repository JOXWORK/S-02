import logging

logger = logging.getLogger(__name__)

import subprocess
import tkinter as tk

from core.config import settings
from core.logger.methods import dolog

from .ui_config import ui_settings


class InstallFabricLoaderTKBlock:
    @dolog()
    def __init__(self):
        self.root: tk.Tk

        self.install_fabric_loader_button = tk.Button(
            self.root,
            text=ui_settings.install_fabric_loader.InstallFabricLoaderButton.text,
            command=self.install_fabric_loader_func,
        )

        self.install_fabric_loader_button.pack(fill=ui_settings.install_fabric_loader.InstallFabricLoaderButton.fill)

        super().__init__()

    @dolog()
    def install_fabric_loader_func(self):
        with subprocess.Popen(
            [
                "java",
                "-jar",
                settings.app_dirs.FABRIC_INSTALLER_JAR,
                "client",
                "-dir",
                settings.app_dirs.minecraft.MINECRAFT_DIR,
                "-mcversion",
                settings.fabric_installer.mcversion,
                "-loader",
                settings.fabric_installer.loader,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        ) as process:
            for line in process.stdout:
                logger.info(line.strip())
