class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev, cur, counter = 0, 0, Counter(nums)
        
        for num in range(min(counter.keys()), max(counter.keys()) + 1):
            prev, cur = cur, max(num * counter[num] + prev, cur)            
        
        return cur        