class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        q =deque(senate)
        r = 0
        dp = 0
        rp = 0
        while len(set(q))!=1:
            poped= q.popleft()
            if poped=="R" :
                if rp==0:
                    q.append(poped)
                    dp+=1
                else:
                    rp-=1
            if poped=="D" :
                if dp==0:
                    q.append(poped)
                    rp+=1
                else:
                    dp-=1
        if "R" in set(q):
            return "Radiant"
        else:
            return "Dire"
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in senate:
        #     if i=="R" :
        #         if rp==0:
        #             q.append(q.popleft())
        #             dp+=1
        #         else:
        #             q.popleft()
        #             rp-=1
        #     if i=="D": 
        #         if dp==0:
        #             q.append(q.popleft())
        #             rp+=1
        #         else:
        #             q.popleft()
        #             dp-=1
        #     print()
        #     if len(set(q)) == 1:
        #         if "R" in set(q):
        #             return "Radiant"
        #         else:
        #             return "Dire"
            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in senate:
        #     if count["R"] ==0:
        #         return "Dire"
        #     elif count["D"] ==0:
        #         return "Radiant"
               
        #     elif i=="R" and count["D"]>0:
        #         count["D"] -=1
        #     elif i=="D" and count["R"]>0:
        #         count["R"] -=1            
                
            