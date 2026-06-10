class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
            

    def sumRange(self, left: int, right: int) -> int:
        pre = [0]
        for i in self.nums:
            pre.append(pre[-1]+i)
        return pre[right+1] - pre[left]

        