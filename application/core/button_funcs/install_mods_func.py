import shutil
from datetime import datetime

from core.config import settings


def install_mods_func():
    MINECRAFT_MODS_DIR = settings.app_dirs.MINECRAFT_MODS_DIR

    if MINECRAFT_MODS_DIR.exists():
        rename_datetime_str = str(datetime.now())
        restruct_datetime_str = rename_datetime_str.replace(" ", "_").replace(":", "-")

        MINECRAFT_MODS_DIR.rename(f"{MINECRAFT_MODS_DIR}.old.{restruct_datetime_str}")

    shutil.copytree(
        settings.app_dirs.SOURCE_MODS_DIR,
        settings.app_dirs.MINECRAFT_MODS_DIR,
    )
