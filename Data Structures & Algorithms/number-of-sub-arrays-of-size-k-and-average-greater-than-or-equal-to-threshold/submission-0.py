class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        runningSum = 0
        L = 0
        count = 0

        for R in range(len(arr)):
            
            if R -L+1> k:
                runningSum -= arr[L]
                L +=1
            runningSum += arr[R]
            if runningSum /k >= threshold and R-L+1 ==k:
                count += 1
            
        return count