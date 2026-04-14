class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #find the middle of the array, check we are greater then or equal to target
        #if we are less then targert
            #two pointers at both ends and shrink end pointer or increase based on whatever
        if len(numbers) == 2:
            return [1,2]
        i = 0 
        j = len(numbers)-1
        
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j-=1
            if numbers[i] + numbers[j] < target:
                i +=1

        return [i+1, j+1]