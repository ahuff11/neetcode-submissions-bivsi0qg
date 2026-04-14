class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j =0, len(numbers)-1
        if len(numbers) ==2:
            return [1, 2]
        
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j-=1
            if numbers[i] + numbers[j] < target:
                i+=1
        return[i+1, j+1]
