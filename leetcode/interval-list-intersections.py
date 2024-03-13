class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 0
        ans = []
        while l<len(firstList) and r<len(secondList):
            if firstList[l][1] < secondList[r][0]:
                l+=1
            elif firstList[l][0] > secondList[r][1]:
                r+=1
            else:
                maxi = max(firstList[l][0],secondList[r][0])
                mini = min(firstList[l][1],secondList[r][1])
                
                ans.append([maxi,mini])
                if mini == firstList[l][1]:
                    l+=1
                else:
                    r+=1
        return ans
            