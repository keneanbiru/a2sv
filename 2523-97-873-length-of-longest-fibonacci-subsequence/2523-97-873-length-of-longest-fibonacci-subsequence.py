class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s=set(arr)
        result=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev,cur=arr[i],arr[j]
                nxt=prev+cur
                l=2
                while nxt in s:
                    l+=1
                    prev,cur=cur,nxt
                    nxt=prev+cur
                    result=max(result,l)
        return result


        