class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[len(digits)-1]+=1
       # print(digits[len(digits)-1])
        for i in range(len(digits)-1,-1,-1):
            
            
            if (digits[i]//10==1):
                if (i!=0):
                    digits[i]=0
                    digits[i-1]+=1
                    #print(digits[i-1])
                else:
                    res=[1] + [0]*len(digits)
                   
                    return res
            else :
                return digits
            
       
       
       
       
       
       
       
       
       
       
       
       
       
        # x = 0
        # for digit in digits:
        #     x *= 10
        #     x += digit
        # x += 1
        # ans = list()
        # while (x != 0):
        #     p = x%10
        #     ans.append(p)
        #     x //= 10
        # return reversed(ans)