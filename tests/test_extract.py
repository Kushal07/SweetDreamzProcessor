from processor.extractor import NumberExtractor


def test_extract_numbers():
    extractor = NumberExtractor()

    numbers = extractor.extract(
        """
45231 75265
95288
11111
"""
    )

    assert len(numbers) == 4

    # First number
    assert numbers[0].original == "45231"
    assert numbers[0].series == "4"
    assert numbers[0].middle_pair == "52"
    assert numbers[0].last_pair == "31"

    # Second number
    assert numbers[1].original == "75265"
    assert numbers[1].series == "7"
    assert numbers[1].middle_pair == "52"
    assert numbers[1].last_pair == "65"

    # Third number
    assert numbers[2].original == "95288"
    assert numbers[2].series == "9"
    assert numbers[2].middle_pair == "52"
    assert numbers[2].last_pair == "88"

    # Fourth number
    assert numbers[3].original == "11111"
    assert numbers[3].series == "1"
    assert numbers[3].middle_pair == "11"
    assert numbers[3].last_pair == "11"