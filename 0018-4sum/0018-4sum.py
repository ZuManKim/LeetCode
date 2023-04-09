class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
    
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        result = []
        
        if not nums:
            return result
        
        if target // k < nums[0] or target // k > nums[-1]:
            return result
        
        if k == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subSet in self.kSum(nums[i+1:], target - nums[i], k - 1):
                    result.append([nums[i]] + subSet)
        
        return result
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        s = set()
        
        for num in nums:
            if len(result) == 0 or result[-1][1] != num:
                if target - num in s:
                    result.append([target - num, num])
            s.add(num)
        
        return result