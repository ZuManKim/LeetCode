class Solution:
    def myAtoi(self, s: str) -> int:
        ans, state, sign = 0, 0, 1

        if len(s) == 0:
            return 0
        
        for char in s:
            if state == 0:
                if char == " ":
                    state = 0
                elif char in '+-':
                    state = 1
                    sign = 1 if char == '+' else -1
                elif char.isdigit():
                    state = 2
                    ans = ans * 10 + int(char)
                else:
                    return 0
            elif state == 1:
                if char.isdigit():
                    state = 2
                    ans = ans * 10 + int(char)
                else:
                    return 0
            else:
                if char.isdigit():
                    state = 2
                    ans = ans * 10 + int(char)
                else:
                    break
        
        ans = sign * ans
        ans = min(ans, 2 ** 31 - 1)
        ans = max(ans, -2 ** 31)

        return ans