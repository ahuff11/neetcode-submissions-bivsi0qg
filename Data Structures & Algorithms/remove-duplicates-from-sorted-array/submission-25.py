class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #loop through and since it is sorted we just need to count how many 
        # if i = i+1 then loop until i /= i+1, 
        nums2 = {}
        for i in range(len(nums)):
            if nums[i] in nums2:
                nums2[nums[i]] +=1
            else:
                nums2[nums[i]] =1

        # for i in nums:
        #     value = nums2[i]
        #     while value > 1:
        #         nums.remove(i)
        #         value -=1
        nums[:] = nums2.keys()
      
        return len(nums2)

