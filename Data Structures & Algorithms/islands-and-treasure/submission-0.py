from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs!
        row = len(grid)
        col = len(grid[0])
        visited = set()
        q = deque([])

        # find gates, add em to the queue
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))

        # bfs function
        def marker(r,c):
            if r >= row or c >= col or r < 0 or c < 0 or grid[r][c] == -1 or grid[r][c] == 0 or (r,c) in visited:
                return
            visited.add((r,c))
            q.append((r,c))
            grid[r][c] = curr
            return

        curr = 1
        # bfsing
        while q:
            amt = len(q)
            for _ in range(amt):
                r,c = q.popleft()
                marker(r+1, c)
                marker(r, c+1)
                marker(r-1, c)
                marker(r, c-1)
            curr += 1

        return


        