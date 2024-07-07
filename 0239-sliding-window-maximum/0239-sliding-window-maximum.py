class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([0])
        result = []
        for i in range(len(nums)):
            
            if q[0] == i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)
            result.append(nums[q[0]])
            
        return result[k-1:]        