class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rlen=len(mat)
        clen=len(mat[0])
    

        list1=[]
        dict1=defaultdict(list)
        for i in range(rlen):
            for j in range(clen):
                dict1[i+j].append(mat[i][j])
        
        for key in range(len(dict1)):
            if key%2==0:
                dict1[key].reverse()
                list1.extend(dict1[key])
                
            else:
                list1.extend(dict1[key])
                
        return list1
