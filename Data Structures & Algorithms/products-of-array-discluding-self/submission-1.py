class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for loop through and calculate the total product of the array 
        #for loop through again and divide product by nums[i] to get total product while saving that to an array 
        #[2,2,4,6] product = 96
        #[48,48,24,16]
        product = nums[0]
        zeroproduct = False
        zerocount = 0
        pos = 0
        for i in range(1,len(nums)):
            if nums[i] == 0:
                zerocount +=1
                pos = i
                if zerocount >1:
                    nums = [0] * len(nums)
                    return nums
            else:
                product *=nums[i]
        
        
        if zerocount == 0:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
        elif zerocount == 1:
            nums = [0] * len(nums)
            nums[pos] = product
            return nums
                
        
        return nums
