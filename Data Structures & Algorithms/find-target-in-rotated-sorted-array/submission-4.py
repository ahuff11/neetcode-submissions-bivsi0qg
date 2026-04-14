class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # think of it as two sorted portions of the array 
        # set left right and middle for normal binary search
        # find which sorted portion we are in my checking the middle against the edges
        # see where target is according to middle, then we need to check where it is according to left and right
        # if target is < nums[left], then we can eliminate the left side and search the right 
        #

        l, r = 0, len(nums)-1
        
        while l <= r:
            mid =(l+r) //2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid+1




        return -1