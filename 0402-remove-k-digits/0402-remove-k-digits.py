class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for char in num:
            while k and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            stack.append(char)
        
        if k:
            stack = stack[:-k]
        
        return ''.join(stack).lstrip('0') or "0"