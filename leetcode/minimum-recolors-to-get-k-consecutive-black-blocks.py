class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = l+k
        count = blocks[0:k].count('W')
        mini = count 
        while r<len(blocks):
            if blocks[l] == 'W':
                count-=1
            if blocks[r] == 'W':
                count +=1
            l+=1
            r+=1
            mini = min(mini,count)
        return mini
