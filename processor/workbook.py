"""
Workbook Manager
================

Handles loading and validating Excel workbooks.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook

from utils.logger import get_logger
from processor.validator import WorkbookValidator


class WorkbookManager:
    """Handles workbook loading."""

    def __init__(self) -> None:
        self.logger = get_logger(__name__)
        self.workbook: Workbook | None = None
        self.file_path: Path | None = None
        self.validator = WorkbookValidator()

    def load(self, filename: str | Path) -> Workbook:
        """
        Load workbook.

        Raises
        ------
        FileNotFoundError
        ValueError
        """

        self.file_path = Path(filename)

        if not self.file_path.exists():
            raise FileNotFoundError(self.file_path)

        self.logger.info(f"Loading workbook: {self.file_path.name}")

        self.workbook = load_workbook(
            filename=self.file_path,
            data_only=False
        )
        # Validate AFTER the workbook is loaded
        self.validator.validate(self.workbook)

        self.logger.info("Workbook loaded successfully.")

        return self.workbook

    def sheet_names(self) -> List[str]:
        """Return worksheet names."""

        if self.workbook is None:
            return []

        return self.workbook.sheetnames

    def active_sheet(self):
        """Return active worksheet."""

        if self.workbook is None:
            raise RuntimeError("Workbook not loaded.")

        return self.workbook.active

    def information(self) -> dict:
        """Return workbook information."""

        if self.workbook is None:
            raise RuntimeError("Workbook not loaded.")

        ws = self.active_sheet()

        return {
            "filename": self.file_path.name,
            "worksheets": len(self.workbook.sheetnames),
            "sheet_names": self.workbook.sheetnames,
            "rows": ws.max_row,
            "columns": ws.max_column,
        }