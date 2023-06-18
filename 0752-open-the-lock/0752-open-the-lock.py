class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            output = []
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff) % 10
                    output.append(code[:i] + str(y) + code[i+1:])
            
            return output
        
        dead_set = set(deadends)
        if '0000' in dead_set: return -1
        q = deque(['0000'])
        cnt = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return cnt
                for neighbor in neighbors(curr):
                    if neighbor in dead_set: 
                        continue
                    dead_set.add(neighbor)
                    q.append(neighbor)
            
            cnt += 1
        
        return -1