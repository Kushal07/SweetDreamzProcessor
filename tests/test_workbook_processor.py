from processor.processor import SweetDreamzProcessor


def test_workbook_processing():
    processor = SweetDreamzProcessor()

    processor.load_workbook("Sweet Dreamz.xlsx")

    result = processor.process_row(
        "Number wise arrangement",
        2,
    )

    assert result["date"] is not None
    assert len(result["numbers"]) > 0
    assert len(result["middle"]) > 0
    assert len(result["last"]) > 0