import subprocess

from core.config import settings


def install_fabric_loader():
    subprocess.run(
        [
            "java",
            "-jar",
            settings.app_dirs.FABRIC_INSTALLER_JAR,
            "client",
            "-dir",
            settings.app_dirs.MINECRAFT_DIR,
            "-mcversion",
            settings.fabric_installer.mcversion,
            "-loader",
            settings.fabric_installer.loader,
        ],
        check=True,
    )
