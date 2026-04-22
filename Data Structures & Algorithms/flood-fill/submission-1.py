class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #bfs
        if image[sr][sc] == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        q = deque()
        q.append((sr, sc))
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        temp = image[sr][sc]
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                
                image[r][c] = color
            
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or image[nr][nc] != temp:
                        continue
                    q.append((nr, nc))
        return image