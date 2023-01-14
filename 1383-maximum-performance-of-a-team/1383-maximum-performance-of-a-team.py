class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        performance = speed_sum = 0

        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, s)
            speed_sum += s
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            performance = max(performance, speed_sum * e)

        return performance % (10**9+7)