from processor.extractor import NumberExtractor
from processor.arranger import NumberArranger

extractor = NumberExtractor()
arranger = NumberArranger()

numbers = extractor.extract("""
45231
75265
95288
16341
36389
""")

middle = arranger.arrange_middle_pair(numbers)

print("NUMBER WISE")
print()

for pair, value in middle.items():
    print(pair, value)

print()

last = arranger.arrange_last_pair(numbers)

print("LAST DIGIT")
print()

for pair, value in last.items():
    print(pair, value)