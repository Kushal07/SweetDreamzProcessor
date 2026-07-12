"""
SweetDreamzProcessor
Workbook Mapper
"""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet


class WorkbookMapper:
    """
    Builds a mapping of Pair -> Worksheet Columns.

    Example:

    {
        "52": {
            "series": 154,
            "pair": 155,
            "last": 156,
        }
    }
    """

    def map_pair_columns(
        self,
        worksheet: Worksheet,
        header_row: int = 1,
    ) -> dict[str, dict[str, int]]:

        mapping: dict[str, dict[str, int]] = {}

        max_col = worksheet.max_column

        column = 1

        while column <= max_col - 2:

            series = worksheet.cell(row=header_row, column=column).value
            pair = worksheet.cell(row=header_row, column=column + 1).value

            header = str(series).strip().lower()

            if header == "series" and pair is not None:

                # Convert Excel numeric values like 0.0 -> "00"
                try:
                    pair_key = f"{int(float(pair)):02d}"
                except (TypeError, ValueError):
                    pair_key = str(pair).strip().zfill(2)

                mapping[pair_key] = {
                    "series": column,
                    "pair": column + 1,
                    "last": column + 2,
                }

                column += 3

            else:
                column += 1

        return mapping