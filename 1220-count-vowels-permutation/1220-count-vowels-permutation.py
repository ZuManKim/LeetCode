class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        aeiou = [1] * 5
        for _ in range(1, n):
            a, e, i, o, u = aeiou
            aeiou[0] = (e + i + u) % MOD
            aeiou[1] = (a + i) % MOD
            aeiou[2] = (e + o) % MOD
            aeiou[3] = i
            aeiou[4] = (i + o) % MOD
        
        return sum(aeiou) % MOD        