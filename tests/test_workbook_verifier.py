from openpyxl import Workbook

from processor.workbook import WorkbookManager
from processor.workbook_verifier import WorkbookVerifier


def test_verify_success():
    wb = Workbook()

    ws = wb.active
    ws.title = "Number"

    wb.create_sheet("Last")

    manager = WorkbookManager()
    manager.workbook = wb

    mappings = {
        "Number": {},
        "Last": {},
    }

    WorkbookVerifier.verify(
        manager,
        mappings,
        "Number",
        "Last",
    )