from openpyxl import Workbook

from processor.workbook_mapper import WorkbookMapper


def test_map_pair_columns():

    wb = Workbook()

    ws = wb.active

    ws["D1"] = "Series"
    ws["E1"] = "00"
    ws["F1"] = "Last"

    ws["G1"] = "Series"
    ws["H1"] = "01"
    ws["I1"] = "Last"

    mapper = WorkbookMapper()

    mapping = mapper.map_pair_columns(ws)

    assert mapping["00"]["series"] == 4
    assert mapping["00"]["pair"] == 5
    assert mapping["00"]["last"] == 6

    assert mapping["01"]["series"] == 7
    assert mapping["01"]["pair"] == 8
    assert mapping["01"]["last"] == 9

    assert len(mapping) == 2

    assert "00" in mapping
    assert "01" in mapping