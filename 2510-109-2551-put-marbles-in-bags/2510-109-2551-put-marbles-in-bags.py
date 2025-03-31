class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        num_weights = len(weights)
        adjacent_sums = [weights[i] + weights[i + 1] for i in range(num_weights - 1)]

        adjacent_sums.sort()

        max_difference = 0
        for i in range(k - 1):
            max_difference += adjacent_sums[num_weights - 2 - i] - adjacent_sums[i]

        return max_difference