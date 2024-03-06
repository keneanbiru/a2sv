class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # mini = max(weights) #10
        # maxi = sum(weights)#55
        # mid = (maxi+mini)//2
       
        def capacity(mid,days):
            sum1=0
            count_days = 1
            for i in range(len(weights)):
                if sum1+weights[i] <= mid:
                    sum1 += weights[i]
                else:
                    count_days+=1
                    sum1 = weights[i]
            return count_days<=days
        
        l , r = max(weights), sum(weights)
        ans = r
    
        while l<=r:
            m = l+ ((r-l)//2)
            if capacity(m, days):
                ans = m
                r = m-1
            else:
                l = m+1

        return ans    


        # while mini <= maxi:
        #     mid = (mini+maxi)//2
        #     if (capacity(mid) <= days):
        #         right = mid-1
        #     else:
        #         left = mid+1
                
        # return maxi 
 

        #  def isVal(m,days):
        #     acc,day = 0,1
        #     i = 0
        #     while i<len(weights):
        #         if acc+weights[i]<=m:
        #             acc+=weights[i]
        #         else:
        #             day+=1
        #             acc= weights[i]

        #         i+=1 

        #     return day<=days

        # l , r = max(weights), sum(weights)
        # ans = r

        # while l<=r:
        #     m = l+ ((r-l)//2)
        #     if isVal(m, days):
        #         ans = m
        #         r = m-1
        #     else:
        #         l = m+1

        # return ans
        
        
        
