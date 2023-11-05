class Solution:
    def integerBreak(self, n: int) -> int:
        if n <=3: return n-1
        product = 1
        while n > 4:
            n -= 3
            product *= 3
        
        return product * n        