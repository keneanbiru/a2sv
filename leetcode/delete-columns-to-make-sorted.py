class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r=len(strs)
        c=len(strs[0])
        count=[]
        for i in range(r-1):
             for j in range(c):
                 if strs[i][j]>strs[i+1][j]:
                     count.append(j)
        return len(set(count))

                



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # zipped = list(zip(*strs))
        # print(zipped)
        # count = 0
        # for i in range(len(zipped)):
        #     for j in range(len(zipped[i])-1):
        #         if ord(zipped[i][j]) > ord(zipped[i][j+1]):
        #             count += 1
        #             break
        # return count