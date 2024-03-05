class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
           
        ans = []
        def backtrack(state, start):
            if len(state) == k:
                ans.append(state.copy())
                return
            
            for candidate in range(start, n + 1):
                state.append(candidate)
                # print("Going to child: - The current state is:", state)
                backtrack(state, candidate + 1)
                state.remove(candidate)
                # print("Going back to parent - The current state is:", state)

        

        backtrack([], 1)
        return ans

  
  
  
  
   #to optimize
   # need = k - len(state) #how many i need to reach k from the current state
            # remain = n - start + 1  #how many remains to k
            # available = remain - need
            
            
            # for candidate in range(start, start+available+1):
            #     state.append(candidate)
            #     print("Going to child: - The current state is:", state)
            #     start += 1
            #     backtrack(state, start)
            #     state.remove(candidate)
            #     print("Going back to parent - The current state is:", state)
