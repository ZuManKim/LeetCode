class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cumsum = 0
        for i in range(len(nums)):
            total -= nums[i]
            
            if cumsum == total:
                return i
            
            cumsum += nums[i]
        
        return -1