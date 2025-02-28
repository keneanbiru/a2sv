class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        prev = [s2[:j] for j in range(n + 1)]

        for i in range(1, m + 1):
            curr = [s1[:i]] + [None] * n
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + s1[i - 1]
                else:
                    pick1, pick2 = prev[j] + s1[i - 1], curr[j - 1] + s2[j - 1]
                    curr[j] = pick1 if len(pick1) < len(pick2) else pick2
            prev = curr

        return prev[n]