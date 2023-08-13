class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        
        while a or b or c:
            if c & 1 == 1:
                if a & 1 == 0 and b & 1 == 0:
                    answer += 1
            elif c & 1 == 0:
                answer += (a & 1) + (b & 1)
            
            a >>= 1
            b >>= 1
            c >>= 1
            
        return answer
        