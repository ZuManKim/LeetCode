class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        neg_idx = len(grid[0]) - 1
        
        for row in grid:
            
            while neg_idx >= 0 and row[neg_idx] < 0:
                neg_idx -= 1
            
            count += (len(row) - (neg_idx + 1))
        
        return count