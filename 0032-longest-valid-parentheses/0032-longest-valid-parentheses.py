class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp, stack = [0] * (n+1), []

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i+1] = dp[p] + i - p + 1
        
        return max(dp)
