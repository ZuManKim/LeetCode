class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        left, sum_window = 0, 0
        
        for right in range(len(nums)):
            sum_window += nums[right]
            
            while sum_window >= target:
                res = min(res, right - left + 1)
                sum_window -= nums[left]
                left += 1
                
        return res % (len(nums) + 1)