class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        #  
        # right pointer travels to find valid trapment. once valid trapment is found iterate left point to calc
        # area. if not valid trapment set l = r until l gets to the end
        #  calc trapment buy doing saving min height of the valid    
        ans = 0   
        l, r =0, len(height) -1
        leftmax = rightmax = 0
        leftmax = max(height[l], leftmax)
        rightmax = max(height[r], rightmax)
        while l < r:

            if leftmax < rightmax:
                l+=1
                leftmax = max(height[l], leftmax)
                ans += leftmax - height[l]
            else:
                r-=1
                rightmax = max(height[r], rightmax)
                ans +=rightmax - height[r]
        return ans