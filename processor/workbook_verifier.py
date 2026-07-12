"""
Workbook Verifier

Verifies that the processor is ready to process a workbook.
"""

from __future__ import annotations

from processor.workbook import WorkbookManager


class WorkbookVerifier:
    """
    Verifies workbook state before processing.
    """

    @staticmethod
    def verify(
        workbook_manager: WorkbookManager,
        sheet_mappings: dict,
        source_sheet: str,
        destination_sheet: str,
    ) -> None:
        """
        Verify workbook readiness.

        Raises
        ------
        RuntimeError
        KeyError
        """

        if workbook_manager.workbook is None:
            raise RuntimeError("Workbook not loaded.")

        sheets = workbook_manager.sheet_names()

        if source_sheet not in sheets:
            raise KeyError(
                f"Source worksheet '{source_sheet}' not found."
            )

        if destination_sheet not in sheets:
            raise KeyError(
                f"Destination worksheet '{destination_sheet}' not found."
            )

        if source_sheet not in sheet_mappings:
            raise KeyError(
                f"No cached mapping for '{source_sheet}'."
            )

        if destination_sheet not in sheet_mappings:
            raise KeyError(
                f"No cached mapping for '{destination_sheet}'."
            )