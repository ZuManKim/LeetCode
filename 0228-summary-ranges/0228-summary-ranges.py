class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        i = 0
        
        while i < len(nums):
            s = e = i
            
            while e < len(nums)-1 and nums[e]+1 == nums[e+1]:
                e += 1
            
            if s == e:
                output.append(f"{nums[e]}")
            else:
                output.append(f"{nums[s]}->{nums[e]}")
                
            i = e + 1
        
        return output