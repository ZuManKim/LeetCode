class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        counter = collections.Counter()
        MOD = 10**9 + 7
        
        for num in nums:
            rev = int(str(num)[::-1])
            ans = (ans + counter[num - rev]) % MOD
            counter[num - rev] += 1
        
        return ans        