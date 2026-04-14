
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #We can sort it and loop through finding and saving 
        #bettter way: save our array as a set, loop through the array,
        # check if it is the start of a sequence by seeing if any value is to the left of it
        # if value is the start then conitnually check if there is another one until it ends and record its length
        my_set = {}
        my_set = nums
        longest = 0
        
        for num in my_set:
            if num-1 in my_set:
                pass
            else:
                j = 1
                while (num+j) in my_set:
                    j +=1
                longest = max(j, longest)
        return longest