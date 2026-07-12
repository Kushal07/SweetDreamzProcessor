from processor.extractor import NumberExtractor

extractor = NumberExtractor()

numbers = extractor.extract("""
45231 75265
95288
11111
""")

for n in numbers:
    print(
        n.original,
        n.series,
        n.middle_pair,
        n.last_pair,
    )