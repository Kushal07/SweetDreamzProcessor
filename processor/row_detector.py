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