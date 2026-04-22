class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        islands = 0
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]

        for i in range(ROWS):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands +=1
                    q.append((i, j))

                    while q:
                        for k in range(len(q)):

                            r, c =  q.popleft()

                            grid[r][c] = "0"

                            for dr, dc in neighbors:
                                nr, nc = r+dr, c+dc
                                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == "0":
                                    continue
                                q.append((nr,nc))
        return islands