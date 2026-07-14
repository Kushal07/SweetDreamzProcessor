from dataclasses import dataclass
@dataclass
class LotteryNumber:
    full_number: str; series: str; middle_pair: str; last_pair: str
    @classmethod
    def from_str(cls, value):
        v = str(value).strip().zfill(5)
        if len(v) == 5 and v.isdigit(): return cls(v, v[0], v[1:3], v[3:5])
        return None
