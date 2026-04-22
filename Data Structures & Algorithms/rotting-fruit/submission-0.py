class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruit = 0
        q = deque()
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshFruit += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        neighbors = [[0,1], [0,-1], [1, 0], [-1, 0]]
        time = 0
        while freshFruit > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                
                for dr, dc in neighbors:
                    if min(r+dr, c+dc) < 0 or r+dr == ROWS or c+dc == COLS or grid[r+dr][c+dc] == 2 or grid[r+dr][c+dc] == 0:
                        continue
                    grid[r+dr][c+dc] = 2
                    freshFruit -= 1
                    q.append((r+dr, c+dc))

            time += 1

        if freshFruit == 0:
            return time
        return -1