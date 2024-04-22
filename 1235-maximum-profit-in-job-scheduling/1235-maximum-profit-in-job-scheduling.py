class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        startTime = [jobs[i][0] for i in range(n)]

        @lru_cache(None)
        def dp(i):
            if i == n: return 0 
            ans = dp(i + 1)

            j = bisect_left(startTime, jobs[i][1])
            ans = max(ans, dp(j) + jobs[i][2])

            return ans
        
        return dp(0)