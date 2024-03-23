class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = height[0], height[n-1]
        left, right = 1, n-2
        ans = 0
        
        while left <= right:
            if max_left < max_right:
                if max_left >= height[left]:
                    ans += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if max_right >= height[right]:
                    ans += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        
        return ans        