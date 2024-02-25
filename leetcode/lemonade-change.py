class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
         
        count_5 = 0
        count_10 = 0
        
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 >= 1:
                    count_5 -= 1
                    count_10 += 1
                else:
                    return False
            elif bill == 20:
                if count_10 >= 1 and count_5 >= 1:
                    count_10 -= 1
                    count_5 -= 1
                elif count_5 >= 3:
                    count_5 -= 3
                else:
                    return False
        
        return True

        #count=0
#         sum1=0
#         for i in bills:
#             if(i==5):
#                 count+=1
#                 sum1+=5
#             if(i==10 ):
#                 if count>=1:
#                     count-=1
#                     sum1+=5
#                 else:
#                     return False
#             if (i==20 ):
#                 if (sum1>=15 and count>=1):
#                     sum1+=5
#                     count-=1
#                 else :
#                     return False
#         return True

