class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        paths = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, prev):
            
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0
            
            if paths[i][j] != -1:
                return paths[i][j]
            
            cur = matrix[i][j]
            left = dfs(i-1, j, cur)
            right = dfs(i+1, j, cur)
            top = dfs(i, j-1, cur)
            bottom = dfs(i, j+1, cur)
            
            paths[i][j] = max(left, right, top, bottom) + 1
            
            return paths[i][j]
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
        
        return max(map(max, paths))