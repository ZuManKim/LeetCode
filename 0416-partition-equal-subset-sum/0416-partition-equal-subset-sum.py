class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        dp = [True] + [False] * s

        for num in nums:
            for curr in range(s, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
        
        return dp[s//2]