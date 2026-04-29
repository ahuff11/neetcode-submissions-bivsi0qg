class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #DP / Tab
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        obstacleGrid[ROWS-1][COLS-1] = 1

        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if r == ROWS-1 and c == COLS-1:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    d = obstacleGrid[r+1][c] if r + 1 < ROWS else 0 
                    ri = obstacleGrid[r][c+1] if c + 1 < COLS else 0
                    obstacleGrid[r][c] = d + ri

        return obstacleGrid[0][0]