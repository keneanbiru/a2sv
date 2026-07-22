class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.decode(s)
    def decode(self, s: str) -> str:
        res, num = "", 0
        while self.i < len(s):
            c = s[self.i]
            if c.isdigit():
                num = num * 10 + int(c)
                self.i += 1
            elif c == '[':
                self.i += 1
                inn = self.decode(s)
                res += inn * num
                num = 0
            elif c == ']':
                self.i += 1
                return res
            else:
                res += c
                self.i += 1
        return res