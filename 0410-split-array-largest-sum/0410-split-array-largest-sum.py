class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low+high)//2
            sum_sub, cnt_sub = 0, 1
            
            for num in nums:
                if sum_sub + num <= mid:
                    sum_sub += num
                else:
                    sum_sub = num
                    cnt_sub += 1
            
            if cnt_sub > k:
                low = mid + 1
            else:
                high = mid
        
        return high