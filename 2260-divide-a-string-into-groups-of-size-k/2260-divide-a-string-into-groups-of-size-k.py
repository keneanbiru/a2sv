class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        if n%k !=0:
            s+=(fill * (k - n%k))
        # print(s)
        ans = []
        ls = 0
        for i in range(k ,len(s)+1,k):
            ans.append(s[ls:i])
            ls+=k
        return ans