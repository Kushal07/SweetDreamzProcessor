from processor.processor import SweetDreamzProcessor


def test_process_and_write_row():
    processor = SweetDreamzProcessor()

    processor.load_workbook("Sweet Dreamz.xlsx")

    result = processor.process_and_write_row(
        source_sheet="Number wise arrangement",
        number_wise_sheet="Number wise arrangement",
        last_digit_sheet="Last digit arrangement",
        row=2,
    )

    assert result["date"] is not None
    assert len(result["numbers"]) > 0
    assert len(result["middle"]) > 0

    worksheet = processor.workbook.get_sheet("Number wise arrangement")

    # At least one mapped block should now contain written data.
    wrote_data = False

    mapping = processor.sheet_mappings["Number wise arrangement"]

    for pair, data in result["middle"].items():

        column = mapping[pair]["series"]

        if worksheet.cell(row=2, column=column).value == data["series"]:
            wrote_data = True
            break

    assert wrote_data

def test_missing_middle_header_is_created():
    """
    ARR-004

    Verify that a missing Number Wise arrangement
    header can be recreated without modifying the
    source worksheet columns.
    """