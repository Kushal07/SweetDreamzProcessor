"""
Lottery Number Extractor
"""

from __future__ import annotations

import re
from typing import List

from processor.models import LotteryNumber


class NumberExtractor:
    """
    Extracts all 5-digit numbers from prize cells.
    """

    NUMBER_PATTERN = re.compile(r"\b\d{5}\b")

    def extract(self, text: str | None) -> List[LotteryNumber]:
        """
        Extract every valid 5-digit number from a cell.

        Supports:
        - spaces
        - multiple spaces
        - line breaks
        """

        if not text:
            return []

        numbers = self.NUMBER_PATTERN.findall(str(text))

        return [
            LotteryNumber.from_string(num)
            for num in numbers
        ]