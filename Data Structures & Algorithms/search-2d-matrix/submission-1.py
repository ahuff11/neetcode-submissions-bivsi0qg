class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search the rows 
        # binary search the rows[i]
        top, bot = 0,len(matrix)-1
        foundrow = 0
        while top <= bot:
            mid = (top+bot)//2
            if target < matrix[mid][0]:
                bot = mid -1
            elif target > matrix[mid][-1]:
                top = mid +1
            else:
                break

        if not (top <= bot):
            return False
        mid = (top + bot) //2
        left, right = 0,len(matrix[foundrow])-1
        while left <= right:
            mid2 = (left+right)//2
            if target < matrix[mid][mid2]:
                right = mid2 -1
            elif target > matrix[mid][mid2]:
                left = mid2+1
            else:
                return True
        return False 
