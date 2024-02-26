class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        dict1={}
        for i in range(n):
            while(len(stack)!=0 and stack[-1][0]<temperatures[i]):
               stacktop=stack.pop()
               dict1[stacktop[1]]=i
               #ans[stacktop]=i
            stack.append([temperatures[i],i])
       
        dict_sorted=dict(sorted(dict1.items()))
        print(dict_sorted)
        for key,value in dict_sorted.items():
            ans[key]=(value-key)
        return ans
