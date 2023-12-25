class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans = 1
        idxs = []
        MOD = 10 ** 9 + 7
        
        for i, char in enumerate(corridor):
            if char == 'S':
                idxs.append(i)
        
        if len(idxs) % 2 == 1 or not idxs: return 0
        elif len(idxs) == 2: return 1
        
        for j in range(2, len(idxs), 2):
            ans = ans * (idxs[j] - idxs[j - 1]) % MOD
        
        return ans