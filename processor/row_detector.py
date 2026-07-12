from __future__ import annotations

from typing import Any


class RowDetector:
    """
    Determines whether a workbook row should be processed.
    """

    @staticmethod
    def should_process(
        date_value: Any,
        first_prize: Any,
        second_prize: Any,
    ) -> bool:
        """
        Return True if the row contains data that should be processed.

        Rules (Version 1):

        - Date must exist.
        - At least one prize column must contain data.
        """

        has_date = str(date_value).strip() != ""

        has_first = str(first_prize).strip() != ""

        has_second = str(second_prize).strip() != ""

        return has_date and (has_first or has_second)
    
    @staticmethod
    def detect_rows(
        workbook_manager,
        sheet_name: str,
        start_row: int = 2,
    ) -> list[int]:
        """
        Return a list of row numbers that should be processed.

        The decision is delegated to should_process().
        """

        worksheet = workbook_manager.get_sheet(sheet_name)

        rows: list[int] = []

        for row_number in range(start_row, worksheet.max_row + 1):

            row = workbook_manager.get_row_data(
                sheet_name,
                row_number,
            )

            if RowDetector.should_process(
                row["date"],
                row["first_prize"],
                row["second_prize"],
            ):
                rows.append(row_number)

        return rows