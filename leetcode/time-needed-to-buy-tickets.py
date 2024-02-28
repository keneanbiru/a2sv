class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        count=0
        for i in tickets:
            q.append(i)
        # print(q)
        while q[k]!=0:
            # print(q)
            for i in range(len(tickets)):
                # print(q[0])
                if i==k and q[0]==1:
                    return count+1

                if (q[0]!=0):
                    popped=q.popleft()
                    q.append(popped-1)
                    count+=1
                else:
                    popped=q.popleft()
                    q.append(popped)
            # print(q)
        # return count


