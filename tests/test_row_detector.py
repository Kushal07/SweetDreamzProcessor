from processor.row_detector import RowDetector


def test_valid_first_prize():
    assert RowDetector.should_process(
        "12/07/2026",
        "12345",
        "",
    )


def test_valid_second_prize():
    assert RowDetector.should_process(
        "12/07/2026",
        "",
        "54321",
    )


def test_both_prizes():
    assert RowDetector.should_process(
        "12/07/2026",
        "12345",
        "54321",
    )


def test_no_date():
    assert not RowDetector.should_process(
        "",
        "12345",
        "54321",
    )


def test_blank_row():
    assert not RowDetector.should_process(
        "",
        "",
        "",
    )


def test_date_only():
    assert not RowDetector.should_process(
        "12/07/2026",
        "",
        "",
    )