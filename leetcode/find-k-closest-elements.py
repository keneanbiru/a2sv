class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr,key = lambda ele:(abs(ele-x)))
        ans = sorted(sorted_arr[0:k])
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # arr2 = []
        # pos = bisect_left(arr,x)
        # n= len(arr)
        # if pos == 0:
        #     if 
        #     return arr[0:kk]
        
        # elif pos == n:
        #     arr_rev = reversed(arr)
        #     return arr_rev[0:kk-1].sort()
        # else:
        #     l = 0
        #     r = n -1
            
        #     while l<= r:
        #         l+=1
        #         if kk==len(arr[l:r]):
        #             return arr[l:r]
        #         r-=1                        
               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #     arr2.append(arr[pos])
        # #     for i in range(pos,(len(arr))):
        # #         if i<=pos:
        # #             arr2.append(arr[pos-1])
        # #         elif i<n-1:
        # #             arr2.append(arr[pos+1])
        # #         else:
        # #             l= pos
        # #             r= pos+1
        # #             count = 0
        # #             while l>=0 and r<=n-1:
        # #                 arr2.append(arr[l])
        # #                 arr2.append(arr[r])
        # #                 count +=2
        # #             if l==0 :
        # #                 k=(n-1) -r
        # #                 while k>0 and len(arr2) <= kk:
        # #                     arr2.append(arr[k])
        #                     k-=1
        #             elif r==0 :
        #                 k=l
        #                 while k>0 and len(arr2) <= kk:
        #                     arr2.append(arr[k])
        #                     k-=1
        # return arr2
                        





