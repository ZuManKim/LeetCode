class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        r, c = len(grid), len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        
        while rotten and fresh:    
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    xx, yy = x + dx, y + dy
                    
                    if xx < 0 or yy < 0 or xx >= r or yy >= c: 
                        continue
                    
                    if grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        fresh -= 1
                        rotten.append((xx, yy))
            
            minutes += 1
        
        return minutes if not fresh else -1
        
                