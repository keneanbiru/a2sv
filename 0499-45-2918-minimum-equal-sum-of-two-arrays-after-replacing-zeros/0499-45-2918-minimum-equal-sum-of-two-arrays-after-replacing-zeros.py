class Solution:
    def minSum(self, nums1, nums2):
        sum1 = sum(x if x != 0 else 1 for x in nums1)
        sum2 = sum(x if x != 0 else 1 for x in nums2)

        nums1_zeros = nums1.count(0)
        nums2_zeros = nums2.count(0)

        if (nums1_zeros == 0 and sum2 > sum1) or \
           (nums2_zeros == 0 and sum1 > sum2):
            return -1
        return max(sum1, sum2)