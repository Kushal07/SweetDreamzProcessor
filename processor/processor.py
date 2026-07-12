"""
SweetDreamzProcessor
Main Processing Engine
"""

from processor.workbook import WorkbookManager
from processor.extractor import NumberExtractor
from processor.arranger import NumberArranger


class SweetDreamzProcessor:

    def __init__(self):

        self.workbook = WorkbookManager()
        self.extractor = NumberExtractor()
        self.arranger = NumberArranger()

    def load_workbook(self, filename):

        self.workbook.load(filename)

    def process_row(
        self,
        sheet_name: str,
        row_number: int,
    ):

        row = self.workbook.get_row_data(
            sheet_name,
            row_number,
        )

        combined = f"{row['first_prize'] or ''}\n{row['second_prize'] or ''}"

        numbers = self.extractor.extract(combined)

        middle = self.arranger.arrange_middle_pair(numbers)
        last = self.arranger.arrange_last_pair(numbers)

        return {
            "date": row["date"],
            "numbers": numbers,
            "middle": middle,
            "last": last,
        }