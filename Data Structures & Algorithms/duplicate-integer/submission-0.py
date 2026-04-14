class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        
        for n in nums:
            hashy[n] = hashy.get(n,0)+1
            if hashy[n] >1:
                return True
        return False
