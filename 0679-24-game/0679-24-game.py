from itertools import permutations
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper1(a,b,c,d):
            # a,b,c,d = arr
            if (helper2(a+b,c,d) or helper2(a-b,c,d) or helper2(a*b,c,d) or helper2(a/b,c,d)):
                return True
            if (helper2(a,b+c,d) or helper2(a,b*c,d) or helper2(a,b-c,d) or helper2(a,b/c,d)):
                return True
            if (helper2(a,b,c+d) or helper2(a,b,c-d) or helper2(a,b,c*d) or helper2(a,b,c/d)):
                return True
            return False
        
        def helper2(a,b,c):
            if (helper3(a+b,c) or helper3(a-b,c) or helper3(a*b,c) or ( b!=0 and helper3(a/b,c))):
                return True
            if (helper3(a,b+c) or helper3(a,b-c) or helper3(a,b*c) or ( c!=0 and helper3(a,b/c))):
                return True
            return False
        def helper3(a,b):
            if abs((a+b) - 24) <= (10**-5) or abs((a-b) - 24) <= (10**-5) or abs((a*b) - 24 )<= (10**-5) or ( b!=0 and abs((a/b) - 24 )<= (10**-5)) :
                return True
            return False


        permu = permutations(cards)
        permu = list(permu)
        for ele in permu:
            a,b,c,d = ele
            if helper1(a,b,c,d):
                return True
        return False

        
        

        