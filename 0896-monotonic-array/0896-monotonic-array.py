class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr = decr = False
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incr = True
                if decr: return False
            elif nums[i] < nums[i-1]:
                decr = True
                if incr: return False
        
        return True        