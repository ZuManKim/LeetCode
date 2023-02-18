class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                delete_left = s[left:right]
                delete_right = s[left+1:right+1]
                return delete_left == delete_left[::-1] or delete_right == delete_right[::-1]
            
            left += 1
            right -= 1
        
        return True