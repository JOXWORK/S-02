import tkinter as tk

from core.config import settings
from tk_blocks.install_mods import InstallModsTKBlock
from tk_blocks.minecraft_dir import MinecraftDirTKBlock


class App(MinecraftDirTKBlock, InstallModsTKBlock):
    def __init__(self, root: tk.Tk):
        self.root = root

        self.root.geometry(settings.window_settings.geometry)

        super().__init__()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()

    app = App(root)
    app.start()
