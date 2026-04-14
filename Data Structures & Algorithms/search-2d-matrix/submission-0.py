class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search with more conditions 
        
        for row in range(len(matrix)):
            if matrix[row][-1] < target:
                continue
            elif matrix[row][-1] > target:
                #go trhough with binary search the number is in this list
                l, r = 0, len(matrix[row])-1
                
                while l <= r:
                    mid = (l+r)//2
                    if matrix[row][mid] <target:
                        l = mid +1
                    elif matrix[row][mid] > target:
                        r = mid-1
                    else:
                        return True
            else:
                return True
        return False