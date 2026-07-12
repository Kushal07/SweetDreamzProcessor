"""
SweetDreamzProcessor
Main Processing Engine
"""

from processor.workbook import WorkbookManager
from processor.extractor import NumberExtractor
from processor.arranger import NumberArranger
from processor.workbook_mapper import WorkbookMapper
from processor.workbook_verifier import WorkbookVerifier
from processor.backup_manager import BackupManager
from processor.writer import WorkbookWriter

from processor.row_detector import RowDetector
from processor.block_detector import (
    BlockDetector,
    BlockState,
)

from utils.logger import get_logger
from processor.processing_statistics import ProcessingStatistics

class SweetDreamzProcessor:

    def __init__(self):

        
        self.workbook = WorkbookManager()
        self.extractor = NumberExtractor()
        self.arranger = NumberArranger()
        self.mapper = WorkbookMapper()
        self.writer = WorkbookWriter()

        self.backup_manager = BackupManager()

        self.block_detector = BlockDetector()
        self.statistics = ProcessingStatistics()
        self.logger = get_logger(__name__)
        self.sheet_mappings: dict[str, dict[str, dict[str, int]]] = {}

    def load_workbook(self, filename):

        self.workbook.load(filename)

        self._build_sheet_mappings()


    def _build_sheet_mappings(self) -> None:
        """
        Build and cache workbook mappings for all worksheets.
        """

        self.sheet_mappings.clear()

        for sheet_name in self.workbook.sheet_names():

            worksheet = self.workbook.get_sheet(sheet_name)

            self.sheet_mappings[sheet_name] = (
                self.mapper.map_pair_columns(worksheet)
            )



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
    
    def write_middle_pair(
        self,
        worksheet_name: str,
        row: int,
        pair: str,
        data: dict,
    ) -> None:
        """
        Write one middle-pair block using WorkbookMapper.
        """

        worksheet = self.workbook.get_sheet(worksheet_name)

        mapping = self.sheet_mappings.get(worksheet_name)

        if mapping is None:
            raise RuntimeError(
                f"No cached mapping for worksheet '{worksheet_name}'."
            )

        if pair not in mapping:
            raise KeyError(
                f"Pair '{pair}' not found in worksheet mapping."
            )

        columns = mapping[pair]

        state = self.block_detector.detect(
            worksheet=worksheet,
            row=row,
            start_column=columns["series"],
        )

        # COMPLETE → Skip
        if state is BlockState.COMPLETE:
            self.statistics.complete_blocks_skipped += 1
            self.workbook.logger.info(
                f"Row {row}, Pair {pair}: skipped (already complete)."
            )
            return

        # PARTIAL → Rewrite and log warning
        if state is BlockState.PARTIAL:
            self.statistics.partial_blocks_rewritten += 1
            self.workbook.logger.warning(
                f"Row {row}, Pair {pair}: partially filled block detected. Rewriting block."
            )

        # EMPTY or PARTIAL → Write
        self.writer.write_middle_block(
            worksheet=worksheet,
            row=row,
            start_column=columns["series"],
            data=data,
        )

        if state is BlockState.EMPTY:
            self.statistics.empty_blocks_written += 1
            self.workbook.logger.info(
                f"Row {row}, Pair {pair}: empty block filled."
            )

    def write_middle_arrangement(
        self,
        worksheet_name: str,
        row: int,
        arrangement: dict[str, dict[str, str]],
    ) -> None:
        """
        Write all middle-pair blocks for a single worksheet row.
        """

        for pair, data in arrangement.items():

            self.write_middle_pair(
                worksheet_name=worksheet_name,
                row=row,
                pair=pair,
                data=data,
            )

    def process_and_write_row(
        self,
        source_sheet: str,
        destination_sheet: str,
        row: int,
    ) -> dict:
        """
        Process one workbook row and write the
        middle-pair arrangement into the destination sheet.

        Returns the processed result.
        """
        self.statistics.total_rows_scanned += 1

        result = self.process_row(
            
            source_sheet,
            row,
        )
        self.statistics.rows_processed += 1

        self.write_middle_arrangement(
            worksheet_name=destination_sheet,
            row=row,
            arrangement=result["middle"],
        )


        return result
    
    def process_workbook(
        self,
        source_sheet: str,
        destination_sheet: str,
    ) -> ProcessingStatistics:
        """
        Process all eligible rows in a workbook.
        """

        WorkbookVerifier.verify(
            workbook_manager=self.workbook,
            sheet_mappings=self.sheet_mappings,
            source_sheet=source_sheet,
            destination_sheet=destination_sheet,
        )

        if self.workbook.file_path is None:
            raise RuntimeError("Workbook path is not available.")

        backup_path = self.backup_manager.create_backup(
            self.workbook.file_path
        )

        self.logger.info(
            "Workbook backup created: %s",
            backup_path,
        )

        worksheet = self.workbook.get_sheet(source_sheet)

        self.statistics.start()

        try:
            for row_number in range(2, worksheet.max_row + 1):

                row = self.workbook.get_row_data(
                    source_sheet,
                    row_number,
                )

                if not RowDetector.should_process(
                    row["date"],
                    row["first_prize"],
                    row["second_prize"],
                ):
                    continue

                self.process_and_write_row(
                    source_sheet=source_sheet,
                    destination_sheet=destination_sheet,
                    row=row_number,
                )

        finally:
            self.statistics.finish()

        return self.statistics