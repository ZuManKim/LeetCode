class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        seen = set()
        def dfs(node):
            for neighbor, adjacent in enumerate(isConnected[node]):
                if adjacent and neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans