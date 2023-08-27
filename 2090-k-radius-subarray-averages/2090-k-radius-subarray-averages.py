class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        output = [-1] * len(nums)
        window = 2 * k + 1
        n = len(nums)
        
        if not k:
            return nums
        
        if window > len(nums):
            return output
        
        window_sum = sum(nums[:window])
        output[k] = window_sum // window
        
        for i in range(window, n):
            window_sum += nums[i] - nums[i-window]
            output[i-k] = window_sum // window
            
        return output