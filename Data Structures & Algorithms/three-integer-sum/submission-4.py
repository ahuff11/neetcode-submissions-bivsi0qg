class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        #     i    l r     target = 0 0 0 
        #                      ans.append([i,l,r])
        #
        #
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l <r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    # if [nums[i], nums[l], nums[r]] in ans:
                    #     l+=1
                    # else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        # nondupeans = set(tuple(item) for item in ans)
        # ans = [list(item) for item in nondupeans]
        return ans

                  