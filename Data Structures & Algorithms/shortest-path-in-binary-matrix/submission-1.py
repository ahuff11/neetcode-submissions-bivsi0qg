class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            visit = set()
            q = deque()
            q.append((0,0))
            visit.add((0,0))
            if grid[0][0] == 1:
                return -1

            length = 1
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if r == ROWS-1 and c == COLS-1:
                        return length
                #              up    down   right  left     tl      bl      tr      bl
                    neighbors = [[0,1], [0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
                    for dr, dc in neighbors:
                        if min(r+dr, c+dc) < 0 or r+dr == ROWS or c+dc == COLS or grid[r+dr][c+ dc] == 1 or (r+dr, c+dc) in visit:
                            continue 
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
                length += 1
            
            return -1

        return bfs(grid)