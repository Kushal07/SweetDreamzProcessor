import re, math
class NumberExtractor:
    def extract_numbers(self, val):
        return re.findall(r'\b\d{5}\b', str(val or ""))
    def format_prize_text(self, val, lines_count):
        nums = self.extract_numbers(val)
        if not nums: return ""
        n = len(nums)
        per_line = math.ceil(n / lines_count)
        lines = []
        for i in range(0, n, per_line):
            lines.append(" ".join(nums[i:i + per_line]))
        return "\n".join(lines[:lines_count]).strip()
