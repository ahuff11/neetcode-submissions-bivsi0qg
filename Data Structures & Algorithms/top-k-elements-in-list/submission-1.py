class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}    
        ans = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            hashy[nums[i]] = 1 + hashy.get(nums[i],0)
        for num, count in hashy.items():
            ans[count].append(num)
        
        res = []
        for i in range(len(ans)-1, 0, -1):
            for num in ans[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        

        

        