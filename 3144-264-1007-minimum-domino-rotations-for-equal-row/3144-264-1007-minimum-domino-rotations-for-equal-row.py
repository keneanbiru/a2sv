class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        combined = tops + bottoms
        n = len(tops)
        all_cnt = Counter(combined)
        top_cnt = Counter(tops)
        bot_cnt = Counter(bottoms)
        ans = float("inf")

        
        
        for i in range(1,7):
            if all_cnt[i] >= n:
                l = 0
                cnt = 0
                while l<n:
                    
                    if tops[l] == i:
                        if tops[l] == bottoms[l]:
                            cnt+=1
                    l+=1
                # print(cnt)
                all_cnt[i] -= 2*cnt
                top_cnt[i] -= cnt
                bot_cnt[i] -= cnt

                if all_cnt[i] >= n - cnt:
                    mini = min(n - cnt - top_cnt[i] , n - cnt - bot_cnt[i])
                    ans = min(ans ,mini)
        
        return -1 if ans == float("inf") else ans



                
