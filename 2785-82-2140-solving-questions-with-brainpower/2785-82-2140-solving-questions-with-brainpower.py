class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        mat = [0] * (n+1)
        for i in range(n-1,-1,-1):
            
            mat[i] = max(mat[i+1],questions[i][0])
            if questions[i][1] + i +1<n:
                mat[i] = max(mat[i+1],questions[i][0] + mat[questions[i][1] + i +1])
        # print(mat)
        return mat[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #     p,b = questions[i][0],questions[i][1]
        #     cur= p
        #     maxi = max(maxi,cur)
        #     mat[i][i] = p
        #     j = i+1
        #     pen =b
        #     while j<n:
                
        #         if pen>0:
        #             mat[i][j] = cur
        #             j+=1
        #             pen-=1
        #             maxi = max(maxi,cur)
                    
        #         else:
        #             cur = cur+questions[j][0]
        #             pen = questions[j][1]
        #             mat[i][j] = cur
        #             j+=1
        #             maxi = max(maxi,cur)
            
            




        # print(mat)
        # return maxi

        