
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        result = 0
        end = 0
        
        for meet in meetings:
            if meet[0] > end:
                result += meet[0] - end - 1
            end = max(end, meet[1])

        if days > end:
            result += days - end
        
        return result







# class Solution:
#     def countDays(self, days: int, meeting: List[List[int]]) -> int:
#         ans = 0
#         meeting  = sorted(meeting, key = lambda x:x[0])
#         n  = len(meeting)
#         i = 0
#         f = False
#         for i in range(n-1):
#             f = True
#             ans+=min(meeting[i+1][0] , meeting[i][1]) - meeting[i][0] + 1
#         print(ans,i)
#         if not f:
#             ans+=meeting[i][1] - meeting[i][0]+1
#         else:
#             ans+=meeting[i+1][1] - meeting[i+1][0]+1

#         res = days-ans
#         return res if res >=0 else 0