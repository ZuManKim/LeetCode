class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = [False] * len(graph)
        outbound = [set(out) for out in graph]
        inbound = [set() for _ in range(len(graph))]
        queue = collections.deque()
        
        for i, outgoing in enumerate(outbound):
            if not outgoing:
                queue.append(i)
            for j in outgoing:
                inbound[j].add(i)
                
        while queue:
            j = queue.popleft()
            safe_nodes[j] = True
            for i in inbound[j]:
                outbound[i].remove(j)
                if len(outbound[i]) == 0:
                    queue.append(i)

        return [i for i, is_safe in enumerate(safe_nodes) if is_safe]