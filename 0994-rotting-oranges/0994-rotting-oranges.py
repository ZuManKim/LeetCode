class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        fresh_cnt, num_min = 0, 0
        rotten = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        while rotten and fresh_cnt > 0:
            num_min += 1
            
            for _ in range(len(rotten)):
                x, y  = rotten.popleft()
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    
                    if xx < 0 or xx == m or yy < 0 or yy == n:
                        continue
                    
                    if grid[xx][yy] in [0, 2]:
                        continue
                    
                    rotten.append((xx, yy))
                    fresh_cnt -= 1
                    grid[xx][yy] = 2
        
        return -1 if fresh_cnt > 0 else num_min
        
                