class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(i, currentlist, total):
            
            if total == target:
                ans.append(currentlist.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            currentlist.append(nums[i])
            dfs(i, currentlist, total + nums[i])
            currentlist.pop()
            dfs(i+1, currentlist, total)
        
        dfs(0, [], 0)

        return ans