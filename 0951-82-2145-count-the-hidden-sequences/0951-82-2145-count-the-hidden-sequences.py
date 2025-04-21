from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pre_sum = 0
        min_val = 0
        max_val = 0

        for diff in differences:
            pre_sum += diff
            min_val = min(min_val, pre_sum)
            max_val = max(max_val, pre_sum)

        range_span = upper - lower

        if max_val - min_val > range_span:
            return 0

        return range_span - (max_val - min_val) + 1
