class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = ''
        while True:
            s.sort()
            
            i = 1 if len(ans) >= 2 and ans[-2]== ans[-1] == s[2][1] else 2
            if s[i][0]:
                ans += s[i][1]
                s[i][0] -= 1
            else:
                break
        
        return ans