class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #check if this is a starter for a consecutive seqeunce check if number -1 exists in nums
        # if it does just continue 
        hashy = {}
        hashy = nums
        count = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] -1 in hashy:
                pass
            else:
                k = 1
                while (nums[i]+k) in hashy:
                    
                    k +=1
                count = max(k, count)
        return count

