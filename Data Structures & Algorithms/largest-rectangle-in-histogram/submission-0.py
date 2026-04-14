class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # loop through, what can we keep in our stack and what condition do we need to fill to pop or add 
        # maybe I can use the stack for the indicies <- this was right im goated(dont know how to implement it)
        # loop through and store on a stack using a pair of (index, height)
        # while the height is less the top element on our stack we calculate if this is max area
        # and pop(while checking the area) until the top of our stack is greater then our continue our iteration

        
        stack =  []
        maxarea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxarea = max((i-index)*height, maxarea)
                start = index
            stack.append((start,h))

        for i, h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))

        return maxarea