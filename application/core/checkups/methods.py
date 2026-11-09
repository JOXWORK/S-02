from pathlib import Path

from core.config import settings

from . import exceptions


def check_source_mods_exists(path: Path = settings.app_dirs.SOURCE_MODS_DIR) -> None:
    if not path.exists():
        raise exceptions.SourceModsNotFound()


def check_fabric_installer_exists(path: Path = settings.app_dirs.FABRIC_INSTALLER_JAR) -> None:
    if not path.exists():
        raise exceptions.FabricInstallerNotFound()


def check_source_dir_exists(path: Path = settings.app_dirs.SOURCE_DIR) -> None:
    if not path.exists():
        raise exceptions.SourceDirNotfound()
