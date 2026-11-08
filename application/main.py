import logging
import tkinter as tk

from core.config import settings
from core.logger.methods import dolog

logger = logging.getLogger("app")
logger.info("Start app")

from tk_blocks.install_fabric_loader import InstallFabricLoaderTKBlock
from tk_blocks.install_mods import InstallModsTKBlock
from tk_blocks.minecraft_dir import MinecraftDirTKBlock


class App(MinecraftDirTKBlock, InstallModsTKBlock, InstallFabricLoaderTKBlock):
    @dolog(custom_logger=logger)
    def __init__(self, root: tk.Tk):
        self.root = root

        self.root.geometry(settings.window.geometry)

        super().__init__()

    def start(self):
        logger.info("Start tk loop")
        self.root.mainloop()


if __name__ == "__main__":
    logger.info("Create tk loop")
    root = tk.Tk()

    app = App(root)
    app.start()
    logger.info("Shut down")
