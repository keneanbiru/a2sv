class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        index_dict = {}
        for i in range(len(arr2)):
            index_dict[arr2[i]] = i

    
        def compare(element):
        
            if element in index_dict:
                return index_dict[element]
       
            else:
                return len(arr2) + element

   
        arr1.sort(key=compare)

        return arr1
