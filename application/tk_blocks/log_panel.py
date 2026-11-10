import logging

logger = logging.getLogger(__name__)

import sys
import tkinter as tk

from core.logger import memory_handler
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

        self.log_index = 0
        self.update_log_panel()

        super().__init__()

    def update_log_panel(self):
        try:
            buffer_last_index = len(memory_handler.buffer) - 1

            if self.log_index < buffer_last_index:
                for record in memory_handler.buffer[self.log_index :]:
                    self.log_panel.insert(tk.END, f"[log] - {record.getMessage()}")
                    self.log_panel.see(tk.END)

                self.log_index = buffer_last_index

            self.root.after(100, self.update_log_panel)
        except Exception:
            logger.exception("Update log panel exception")
            sys.exit(1)
