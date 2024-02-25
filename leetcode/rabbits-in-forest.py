class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        max1=0
        
        count=0
        answers.sort()
        
        sum1=answers.count (0)
        #print(sum1)
        for i in range(sum1):
            answers.remove(0)
        #print (answers)
        for i in answers:
            if max1!=i:
                count=0
            
            if i>max1 :
                
                max1=i
                
                sum1=sum1+i+1
            
             
            count+=1
            
            if count>i:
                max1=i-1
                count=0
                
            

            # else:
            #     count+=1
        return sum1
