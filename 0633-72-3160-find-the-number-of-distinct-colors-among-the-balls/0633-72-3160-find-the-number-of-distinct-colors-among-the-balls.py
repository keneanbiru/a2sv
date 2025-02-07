class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mapp = {}  
        balls = {}  
        res = []
        cnt = 0

        for query in queries:
            ball, col = query

            if ball in balls:
                mapp[balls[ball]] -= 1
                if mapp[balls[ball]] == 0:
                    cnt -= 1

            balls[ball] = col
            mapp[col] = mapp.get(col, 0) + 1

            if mapp[col] == 1:
                cnt += 1

            res.append(cnt)

        return res