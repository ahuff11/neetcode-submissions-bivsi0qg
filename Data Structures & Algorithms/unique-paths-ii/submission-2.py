class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dfs memo
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        memo = [[-1] * COLS for _ in range(ROWS)]

        def dfs(row, col):
            if row == ROWS or col == COLS or obstacleGrid[row][col] == 1:
                return 0
            if memo[row][col] > 0:
                return memo[row][col]
            if row == ROWS-1 and col == COLS -1:
                return 1

            memo[row][col] = dfs(row+1,col) + dfs(row,col+1)

            return memo[row][col]
        return dfs(0,0)
             
            
