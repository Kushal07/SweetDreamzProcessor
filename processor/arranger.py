"""
SweetDreamzProcessor
Arranger Module
"""

from __future__ import annotations

from collections import defaultdict

from processor.models import LotteryNumber


class NumberArranger:
    """
    Creates Number Wise and Last Digit arrangements.
    """

    def arrange_middle_pair(
        self,
        numbers: list[LotteryNumber]
    ) -> dict[str, dict[str, str]]:

        grouped = defaultdict(list)

        for number in numbers:
            grouped[number.middle_pair].append(number)

        result = {}

        for pair in sorted(grouped.keys()):

            group = grouped[pair]

            result[pair] = {
                "series": ",".join(n.series for n in group),
                "pair": ",".join(n.middle_pair for n in group),
                "blank": ",".join(n.last_pair for n in group),
            }

        return result

    def arrange_last_pair(
        self,
        numbers: list[LotteryNumber]
    ) -> dict[str, dict[str, str]]:

        grouped = defaultdict(list)

        for number in numbers:
            grouped[number.last_pair].append(number)

        result = {}

        for pair in sorted(grouped.keys()):

            group = grouped[pair]

            result[pair] = {
                "series": ",".join(n.series for n in group),
                "blank": ",".join(n.middle_pair for n in group),
                "pair": ",".join(n.last_pair for n in group),
            }

        return result