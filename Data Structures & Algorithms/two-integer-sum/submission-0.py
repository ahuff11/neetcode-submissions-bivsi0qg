class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        
        # iterate through nums list wiht two pointers, as we go target- the i = j
        # save shit so we dont have to re iterate through stuff
        #two pointers through save positions to hash map  when target - nums[i] = nums[j]
        # {4: 0, 3: 1, 2: 2, 1: 3}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_dict:
                return [my_dict[difference], i]
            else:
                my_dict[nums[i]] = i