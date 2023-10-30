class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        output = 0
        prev = nums[-1]
        
        for num in reversed(nums):
            k = ceil(num / prev)
            output += k - 1
            prev = num // k
        
        return output