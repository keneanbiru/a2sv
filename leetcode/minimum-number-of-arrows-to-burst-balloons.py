class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        count=1
        points.sort(key=lambda x:x[1])
           
        end = points[0][1]
        for i in range(1,n):
            if  end<points[i][0]:
                count+=1
                end = points[i][1]
        return count 
        
        