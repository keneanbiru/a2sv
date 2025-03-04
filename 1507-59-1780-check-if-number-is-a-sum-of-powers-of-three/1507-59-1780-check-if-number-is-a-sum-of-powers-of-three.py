class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            # print(n)
            rem = n%3
            n //= 3
            if rem == 2:
                return False
        return True

        