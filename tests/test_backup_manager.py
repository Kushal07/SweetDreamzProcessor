from pathlib import Path

from processor.backup_manager import BackupManager


def test_create_backup(tmp_path):
    source = tmp_path / "sample.xlsx"
    source.write_text("dummy workbook")

    backup_dir = tmp_path / "backup"

    manager = BackupManager(str(backup_dir))

    backup = manager.create_backup(str(source))

    assert backup.exists()
    assert backup.parent == backup_dir
    assert backup.read_text() == "dummy workbook"