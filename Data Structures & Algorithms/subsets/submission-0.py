class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # remember create two arrays and use copy() function on one of them
        ans = []
        subsets = []

        def dfs(i):

            if i == len(nums):
                ans.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i+1)
            subsets.pop()
            dfs(i+1)

        dfs(0)
        return ans
