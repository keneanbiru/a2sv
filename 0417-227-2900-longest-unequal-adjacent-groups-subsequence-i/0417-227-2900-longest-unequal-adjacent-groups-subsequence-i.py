class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        array=[]
        array.append(words[0])
        for i in range(len(groups)-1):
            if groups[i]!=groups[i+1]:
                array.append(words[i+1])
        return array