from processor.processor import SweetDreamzProcessor


def test_process_row():
    processor = SweetDreamzProcessor()

    processor.load_workbook("Sweet Dreamz.xlsx")

    result = processor.process_row(
        "Number wise arrangement",
        2,
    )

    assert "date" in result
    assert "numbers" in result
    assert "middle" in result
    assert "last" in result

    assert isinstance(result["numbers"], list)
    assert isinstance(result["middle"], dict)
    assert isinstance(result["last"], dict)

    assert len(result["numbers"]) > 0