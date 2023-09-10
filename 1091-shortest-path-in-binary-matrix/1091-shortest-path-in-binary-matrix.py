class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def is_clear(cell):
            return grid[cell[0]][cell[1]] == 0

        def get_neighbours(cell):
            (i, j) = cell
            return (
                (i + a, j + b)
                for a in (-1, 0, 1)
                for b in (-1, 0, 1)
                if a != 0 or b != 0
                if 0 <= i + a < N
                if 0 <= j + b < N
                if is_clear( (i + a, j + b) )
            )

        start = (0, 0)
        goal = (N - 1, N - 1)

        queue = deque()
        if is_clear(start):
            queue.append(start)
        visited = set()
        path_len = {start: 1}

        while queue:
            cell = queue.popleft()
            if cell in visited:
                continue
            if cell == goal:
                return path_len[cell]
            visited.add(cell)
            for neighbour in get_neighbours(cell):
                if neighbour not in path_len:
                    path_len[neighbour] = path_len[cell] + 1
                queue.append(neighbour)

        return -1