class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mi, ma, n, nums = min(arr), max(arr), len(arr), set(arr)
        
        if (ma - mi) % (n - 1) != 0: return False
        
        diff = (ma - mi) / (n - 1)
        
        for i in range(n):
            if mi + i * diff not in nums:
                return False
        
        return True