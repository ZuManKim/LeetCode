class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1] * (maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            if maxMove < 0: return 0
            if i < 0 or i >= m or j < 0 or j >= n: return 1
            
            if dp[i][j][maxMove] != -1: return dp[i][j][maxMove]
            
            left = solve(i-1, j, maxMove-1)
            right = solve(i+1, j, maxMove-1)
            up = solve(i, j-1, maxMove-1)
            down = solve(i, j+1, maxMove-1)
            
            dp[i][j][maxMove] = left + right + up + down
            
            return dp[i][j][maxMove]
            
        return solve(startRow, startColumn, maxMove) % (10 ** 9 + 7)        