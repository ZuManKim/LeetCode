class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, candidates, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return        
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target-candidates[i], path+[candidates[i]], ret)