class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left, max_len = 0, 0
        
        for right in range(len(s)):
            if s[right] in seen and left <= seen[s[right]]:
                left = seen[s[right]] + 1
            else:
                max_len = max(max_len, right-left+1)

            seen[s[right]] = right
        
        return max_len        