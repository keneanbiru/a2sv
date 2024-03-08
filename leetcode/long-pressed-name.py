class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        r = 0
        if len(name) > len(typed):
            return False
        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l += 1
                r += 1
            elif r > 0 and typed[r] == typed[r - 1]:
                r += 1
            else:
                return False

        if l < len(name):
            return False

        while r < len(typed) and typed[r] == typed[r - 1]:
            r += 1

        return r == len(typed)

            
            