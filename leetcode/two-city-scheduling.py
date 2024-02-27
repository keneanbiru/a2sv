class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:-abs(x[0]-x[1]))
        b=a=len(costs)//2
        total=0
        for bcost, acost in costs:
            if b==0 or (a and acost<bcost):
                total+=acost
                a-=1
            else:
                total+=bcost
                b-=1
        return total


        