class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        output = deque()
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            
            if left < right:
                output.appendleft(right ** 2)
                r -= 1
            else:
                output.appendleft(left ** 2)
                l += 1
        
        return output