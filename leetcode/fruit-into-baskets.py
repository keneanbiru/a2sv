class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        
        l = 0
        for num in fruits:
            count[num]+=1
            if len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    count.pop(fruits[l])
                l+=1
            # print(count)
        return len(fruits) - l

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(fruits)
        # l = 0
        # r = l + 2
        # count  = len(Counter(fruits[l:r]))
        # # print(count)
        # maxi = 0
        # if n == 1 or n ==2:
        #     return n
        # while r<n:
        #     if fruits[r] not in fruits[l:r]:
        #         count+=1
        #         # print(count,fruits[r])
        #         if count>2:
        #             num = fruits[l]
        #             maxi = max(maxi,r-l+1)
        #             l+=1
        #             while num in fruits[l:r]:
        #                 l+=1
        #             count = len(Counter(fruits[l:r+1]))
        #             print(count,fruits[r],l)
        #     # print(r,l)
        #     maxi = max(maxi,r-l+1)
        #     r+=1
            
        # return maxi




               


                

