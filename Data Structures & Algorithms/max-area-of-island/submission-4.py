class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs 
        bisland = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        direc = [[0,1], [0,-1], [1,0], [-1,0]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = 0
                    q.append((i, j))
                    
                    while q:
                        for k in range(len(q)):
                            r, c = q.popleft()

                            area += 1
                            grid[r][c] = 0

                            for dr, dc in direc:
                                nr, nc = r+dr, c+dc
                                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0:
                                    continue
                                q.append((nr, nc))
                                grid[nr][nc] = 0
                                
                    bisland = max(area, bisland)

        return bisland
        