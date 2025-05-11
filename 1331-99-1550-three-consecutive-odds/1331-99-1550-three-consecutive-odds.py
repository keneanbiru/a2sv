class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False

        
        coc = 0

        
        for n in arr:
            
            if n % 2 != 0:
                coc += 1
                
                if coc == 3:
                    return True
            
            else:
                coc = 0

        
        return False