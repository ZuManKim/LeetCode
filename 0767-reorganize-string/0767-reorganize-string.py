class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = []
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(pq)
        
        prev_count, prev_char = heapq.heappop(pq)
        res += [prev_char]
        
        while pq:
            cur_count, cur_char = heapq.heappop(pq)
            res += [cur_char]
            prev_count += 1
            if prev_count < 0:
                heapq.heappush(pq, (prev_count, prev_char))

            prev_count, prev_char = cur_count, cur_char
        
        return ''.join(res) if len(res) == len(s) else ''