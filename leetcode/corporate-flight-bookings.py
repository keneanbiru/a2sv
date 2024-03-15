class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = 0
        ans = [0]*(n+1)
        for i in (bookings):
            ans[i[0]-1] += i[2]
            ans[i[1]] -= i[2]
        for i in range(len(ans)) :
            prefix += ans[i]
            ans[i]= prefix
        ans.pop()
        return ans

        
        