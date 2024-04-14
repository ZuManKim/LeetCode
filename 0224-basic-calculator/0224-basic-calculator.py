class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in '+-':
                res += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + sign * num        