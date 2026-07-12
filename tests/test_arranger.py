from processor.extractor import NumberExtractor
from processor.arranger import NumberArranger


def test_arrange_middle_and_last_pair():
    extractor = NumberExtractor()
    arranger = NumberArranger()

    numbers = extractor.extract(
        """
45231
75265
95288
16341
36389
"""
    )

    middle = arranger.arrange_middle_pair(numbers)

    assert "52" in middle

    assert middle["52"]["series"] == "4,7,9"
    assert middle["52"]["pair"] == "52,52,52"
    assert middle["52"]["blank"] == "31,65,88"

    last = arranger.arrange_last_pair(numbers)

    assert "31" in last
    assert last["31"]["series"] == "4"
    assert last["31"]["pair"] == "31"
    assert last["31"]["blank"] == "52"

    assert "89" in last
    assert last["89"]["series"] == "3"
    assert last["89"]["pair"] == "89"
    assert last["89"]["blank"] == "63"