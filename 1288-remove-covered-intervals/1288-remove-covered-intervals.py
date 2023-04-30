class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cnt = last = 0
        for i, j in intervals:
            if j > last: cnt += 1
            last = max(j, last)
        
        return cnt