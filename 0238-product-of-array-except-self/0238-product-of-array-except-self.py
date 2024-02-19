class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, suf, pre = [1] * n, 1, 1
        
        for i in range(n):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1-i] *= suf
            suf *= nums[-1-i]
            
        return ans        