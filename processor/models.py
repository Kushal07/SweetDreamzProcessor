"""
SweetDreamzProcessor
Core Data Models
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LotteryNumber:
    """
    Represents one 5-digit lottery number.

    Example
    -------
    Original Number : 45231

    Series       : 4
    Middle Pair  : 52
    Last Pair    : 31
    """

    original: str
    series: str
    middle_pair: str
    last_pair: str

    @classmethod
    def from_string(cls, number: str) -> "LotteryNumber":
        """
        Create a LotteryNumber from a 5-digit string.
        """

        number = number.strip()

        if len(number) != 5:
            raise ValueError(
                f"{number} is not a valid 5-digit number."
            )

        if not number.isdigit():
            raise ValueError(
                f"{number} contains non-numeric characters."
            )

        return cls(
            original=number,
            series=number[0],
            middle_pair=number[1:3],
            last_pair=number[3:5],
        )

    def __str__(self) -> str:
        return self.original