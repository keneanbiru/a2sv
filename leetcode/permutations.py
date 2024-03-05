class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       
        ans = []
        n = len(nums)

        def backtrack(state):
            # print("Backtrack call happening")
            if len(state) == n:
                ans.append(state.copy())
                return
            
            for i in nums:
                if i not in state:
                    state.append(i)
                    # print("Going to child: The current state is:", state)
                    backtrack(state)
                    state.remove(i)
                    # print("Going to parent: The current state is:", state)


        backtrack([])
        return ans