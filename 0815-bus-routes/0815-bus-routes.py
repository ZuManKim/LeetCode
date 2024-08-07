class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        
        bfs = [(source, 0)]
        seen = set([source])

        for stop, bus in bfs:
            if stop == target:
                return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus+1))
                        seen.add(j)
                routes[i] = []
        return -1