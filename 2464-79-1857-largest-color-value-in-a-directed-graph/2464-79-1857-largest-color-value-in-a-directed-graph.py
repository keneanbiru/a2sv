
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

       
        dp = [[0] * 26 for _ in range(n)]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        vis = 0
        max_color_value = 0

        while queue:
            u = queue.popleft()
            vis += 1

            for v in graph[u]:
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0))
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

            max_color_value = max(max_color_value, max(dp[u]))

        return max_color_value if vis == n else -1