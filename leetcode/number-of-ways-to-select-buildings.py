class Solution:
    def numberOfWays(self, s: str) -> int:
        one,zero=0,0
        sum_=0
        dict1=defaultdict(int)
        # if s[0]=="1":
        #     one=1
        # else:
        #     zero=1
        
        for i in range(len(s)):

            if s[i]=="0":
                zero+=1
                dict1["10"]+=one
                sum_+=dict1["01"]
            elif s[i]=="1":
                one+=1
                dict1["01"]+=zero
                sum_+=dict1["10"]
        return sum_
                   

        