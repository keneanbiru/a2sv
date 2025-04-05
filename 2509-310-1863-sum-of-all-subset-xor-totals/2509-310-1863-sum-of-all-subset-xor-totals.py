class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        def backtrack(index, path, arr):
            if index == len(arr):
                ans.append(path)
                return
         
            backtrack(index + 1, path + [arr[index]], arr)
            
            backtrack(index + 1, path, arr)
        backtrack(0,[],nums)
        res = 0
        # print(ans)
        for array in ans:
            
            one = 0
            for i in array:
                one^=i
            # print(one)
            res+=one


        return res
