class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Initialize pointers for both arrays
        i, j = 0, 0
        res = []
        
        # Traverse both arrays with two pointers
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 < id2:
                # Id1 is smaller, add it to res
                res.append([id1, val1])
                i += 1
            elif id2 < id1:
                # Id2 is smaller, add it to res
                res.append([id2, val2])
                j += 1
            else:
                # Ids are equal, sum the values
                res.append([id1, val1 + val2])
                i += 1
                j += 1
        
        # Add remaining elements from nums1, if any
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2, if any
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        
        return res