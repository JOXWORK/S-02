import tkinter as tk

from core.logger.methods import dolog

from tk_blocks.ui_config import ui_settings


class LogPanelTKBlock:
    @dolog()
    def __init__(self):
        self.root: tk.Tk

        self.log_panel = tk.Listbox(
            self.root,
            width=ui_settings.log_panel.LogPanel.width,
            height=ui_settings.log_panel.LogPanel.height,
        )

        self.log_panel.pack(fill=ui_settings.log_panel.LogPanel.fill)

        super().__init__()
