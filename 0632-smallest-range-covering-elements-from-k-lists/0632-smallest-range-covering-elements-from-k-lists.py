class Solution:
    def smallestRange(self, nums):
        k = len(nums)

        # Step 1: flatten
        arr = []
        for i in range(k):
            for val in nums[i]:
                arr.append((val, i))

        # Step 2: sort by value
        arr.sort()

        # Sliding window
        count = [0] * k
        covered = 0
        l = 0

        best_l = 0
        best_r = float("inf")

        for r in range(len(arr)):
            val_r, idx_r = arr[r]

            if count[idx_r] == 0:
                covered += 1
            count[idx_r] += 1

            # Try to shrink
            while covered == k:
                val_l, idx_l = arr[l]

                # Update best range
                if (val_r - val_l < best_r - best_l) or \
                   (val_r - val_l == best_r - best_l and val_l < best_l):
                    best_l, best_r = val_l, val_r

                # Shrink window
                count[idx_l] -= 1
                if count[idx_l] == 0:
                    covered -= 1
                l += 1

        return [best_l, best_r]
