class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, step, boundary = len(grid), 0, set()

        def get_first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        return i, j

        def dfs(i, j):
            grid[i][j] = -1
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        dfs(x, y)
                    elif not grid[x][y]:
                        boundary.add((i, j))
        dfs(*get_first())

        while boundary:
            new_boundary = []
            for i, j in boundary:
                for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return step
                        elif not grid[x][y]:
                            grid[x][y] = -1
                            new_boundary.append((x, y))
            step += 1
            boundary = new_boundary