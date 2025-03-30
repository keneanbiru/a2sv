class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = set()
        f = {}
        l = {}
        ranges = []
        for i in range(len(s)):
            letter = s[i]
            letters.add(letter)
            if letter not in f:
                f[letter] = i
                l[letter] = i
            else:
                l[letter] = i
        for letter in letters:
            ranges.append([f[letter], l[letter]])
        ranges.sort()
        merged = [ranges[0]]
        for r in ranges[1:]:
            start, end = merged[-1]
            new_start, new_end = r
            
            if new_start < end:
                merged[-1] = [start, max(end, new_end)]
            else:
                merged.append(r)
        return [end - start + 1 for start, end in merged]
