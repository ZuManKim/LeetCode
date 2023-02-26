class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col = len(grid[0])
        flatten = sum(grid, [])
        k %= len(flatten)
        flatten = flatten[-k:] + flatten[:-k]
        return [flatten[i:i+col] for i in range(0, len(flatten), col)]