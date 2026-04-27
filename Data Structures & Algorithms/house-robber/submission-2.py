class Solution:
    def rob(self, nums: List[int]) -> int:
        #DP Top-Down
        cache = [-1] * len(nums)
        def memo(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(memo(i+1), nums[i] + memo(i+2))
            return cache[i]
        return memo(0)