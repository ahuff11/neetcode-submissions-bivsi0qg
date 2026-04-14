class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left and right pointer: use the min of both pointers and multiply by r-l+1 to get width
        #find when to iterate left or right 
        ans = 0
        tempmax = 0
        l ,r = 0, len(heights)-1
        while l<r:
            tempmax = min(heights[l], heights[r])*(r-l)
            ans = max(ans,tempmax)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return ans