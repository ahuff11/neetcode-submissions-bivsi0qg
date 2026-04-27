class Solution:
    def rob(self, nums: List[int]) -> int:
        #optimized
        i = 0
        rob1 = 0
        rob2 = 0

        while i < len(nums):
            
            newrob = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = newrob
            i +=1
        return rob2