class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calCost(mid):
            return sum(abs(num - mid) * cost for num, cost in zip(nums, cost))
        
        left, right = min(nums), max(nums)
        result = calCost(left)
        
        while left < right:
            mid = (left + right) // 2
            cost1, cost2 = calCost(mid), calCost(mid+1)
            result = min(cost1, cost2)
            if cost1 < cost2:
                right = mid
            else:
                left = mid + 1
        
        return result        