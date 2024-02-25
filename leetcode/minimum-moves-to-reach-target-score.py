class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count_i=0
        count_m=0
        t_orginal=target
        if (maxDoubles==0):
            return target-1
        while target>1:
            if (count_m==maxDoubles):
                break
            if (target%2==0):
                target=target//2
                count_m+=1
            else:
                target=target//2
               
                count_i+=1
                count_m+=1
            # print(target)
            # print(count_i+count_m)

            
       # print (target)
        if(target==1):
            return  count_i+count_m
        else:
            print(target)
            return count_i+count_m+(target-1)
           
       
       
       
       
       
        #     target-=1
        #     count_i+=1
        # if (t_orginal%2==0):
        #     print("even")
        #     return count_i+count_m
        # elif(t_orginal==1):
        #     return 0
        # else:
        #     return count_i+count_m+1

        