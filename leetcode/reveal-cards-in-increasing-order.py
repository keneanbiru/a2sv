class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck=sorted(deck)
        q=deque(i for i in range(n))
        lu=[None] * n
        t=0
        while len(q) > 0:
            top = q.popleft()
            lu[top] = t
            t+=1
            if len(q) > 0:
                top = q.popleft()
                q.append(top)
        print(lu)
         
        return [deck[i] for i in lu]


        