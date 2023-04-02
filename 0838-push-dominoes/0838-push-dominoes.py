class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pushes = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        pushes = [(-1, 'L')] + pushes + [(len(dominoes), 'R')]
        
        ans = list(dominoes)
        for (i, x), (j, y) in zip(pushes, pushes[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i+1, j):
                    ans[k] = '.LR'[(k-i > j-k) - (k-i < j-k)]
        
        return "".join(ans)
                