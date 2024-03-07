class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        first = [i[0] for i in intervals]
        second = [i[1] for i in intervals]
        dict1 = {}
        for i in range(len(first)):
            dict1[first[i]] = i
        first.sort()
        n = len(first)
        left = 0
        right = len(first) - 1
        ans = []
        for i in second:
            if i > first[n - 1]:
                ans.append(-1)
            # elif i == first[n - 1]:
            #     ans.append(dict1[first[right]])
            # elif i == first[left]:
            #     ans.append(dict1[first[left]])
            else:
                chk = right
                while left <= right:
                    mid = (left + right) // 2
                    if first[mid] > i:
                        chk = mid
                        right = mid - 1
                    elif first[mid] < i:
                        left = mid + 1
                    else:
                        ans.append(dict1[first[mid]])
                        break
                else:
                    ans.append(dict1[first[chk]])
                left = 0
                right = len(first) - 1
        return ans           
                
             