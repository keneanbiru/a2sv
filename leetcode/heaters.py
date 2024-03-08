class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        n = len(houses)
        nt = len(heaters)
        ans = []
        
        # if len(heaters)==1:
        #     return 0
        houses.sort()
        heaters.sort()
        for i in houses:
            pos = bisect.bisect_left(heaters,i)
            if pos==0:
                ans.append(heaters[0] - i)
            elif pos == len(heaters):
                ans.append(i - heaters[nt - 1])
            else:
                dif_1 = abs( i - heaters[pos - 1])
                dif_2 = abs(i - heaters[pos ])
                ans.append(min(dif_1,dif_2))
        return(max(ans))
                
               
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #     heater2 = bisect.bisect_left(houses,heaters[left+1])
            #     # print(heater1)
            #     # print(heater2)
            #     # print(abs(room - heater1))
            #     if heater1 == len(houses):
            #         dif1 = heaters1 - room
            #     else:
            #         dif1 = abs (room - hetaer1)
            #     mini = min(room - heater1,room - heater2)
            #     ans.append(mini)
            # if (i>heaters[left]):
            #     left+=1
            #while left+1 < len(heaters):
    #         for i in houses:
    #         # print(left,len(heaters))
            
    #             # mini_org = mini
    #             room = bisect.bisect_left(houses,i)
    #         #     
        
    #     return max(ans)

    # heater1 = bisect.bisect_left(houses,heaters[left])
            
            
            


        