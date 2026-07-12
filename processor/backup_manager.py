from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil


class BackupManager:
    """
    Creates timestamped backups of workbook files.
    """

    def __init__(self, backup_directory: str = "backup") -> None:
        self.backup_directory = Path(backup_directory)
        self.backup_directory.mkdir(parents=True, exist_ok=True)

    def create_backup(self, workbook_path: str) -> Path:
        """
        Create a timestamped backup of the workbook and return its path.
        """

        source = Path(workbook_path)

        if not source.exists():
            raise FileNotFoundError(source)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        destination = (
            self.backup_directory
            / f"{source.stem}_{timestamp}{source.suffix}"
        )

        shutil.copy2(source, destination)

        return destination