class Solution:
    def totalNQueens(self, n: int) -> int:

        diag = set()
        anti_diag = set()
        used_cols = set()
        
        return self.helper(n, diag, anti_diag, used_cols, 0)

    def helper(self, n, diag, anti_diag, used_cols, row):
        if row == n:
            return 1
        
        solutions = 0
        
        for col in range(n):
            if row + col in diag or row - col in anti_diag or col in used_cols:
                continue
                
            diag.add(row + col)
            anti_diag.add(row - col)
            used_cols.add(col)
            
            solutions += self.helper(n, diag, anti_diag, used_cols, row + 1)
        
            diag.remove(row + col)
            anti_diag.remove(row - col)
            used_cols.remove(col)
        
        return solutions