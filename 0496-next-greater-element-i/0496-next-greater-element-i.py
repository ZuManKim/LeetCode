class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_greater_dict = {}
        ans = []
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                first_greater_dict[stack[-1]] = num
                stack.pop()
            stack.append(num)
        
        for remainder in stack:
            first_greater_dict[remainder] = -1
        
        for num in nums1:
            ans.append(first_greater_dict[num])
        
        return ans