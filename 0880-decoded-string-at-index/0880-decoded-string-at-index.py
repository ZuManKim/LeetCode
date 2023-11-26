class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_len = 0
        
        for char in s:
            if char.isdigit():
                decoded_len *= int(char)
            else:
                decoded_len += 1
        
        for char in s[::-1]:
            if char.isdigit():
                decoded_len //= int(char)
                k %= decoded_len
            elif k == 0 or decoded_len == k:
                return char
            else:
                decoded_len -= 1        