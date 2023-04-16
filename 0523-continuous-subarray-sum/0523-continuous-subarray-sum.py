class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_dict = {0: 0}
        s = 0
        
        for i, n in enumerate(nums):
            s += n
            
            if s % k not in mod_dict:
                mod_dict[s % k] = i + 1
            elif mod_dict[s % k] < i:
                return True
        
        return False