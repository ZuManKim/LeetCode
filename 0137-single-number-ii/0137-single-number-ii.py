class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)
        
        return ones        