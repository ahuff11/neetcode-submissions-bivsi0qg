class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(r, c, ogColor):
            
            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != ogColor:
                return
            
            image[r][c] = color

            dfs(r+1,c, ogColor)
            dfs(r-1,c, ogColor)
            dfs(r,c+1, ogColor)
            dfs(r,c-1, ogColor)

        dfs(sr, sc, image[sr][sc])
        return image