class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # solution is most likely max/min stack and as we go through the array 
        #[1,4,1,2,1,40,28]
        #                n
        #[0, 1, 2, 3, 4, 5, 6]
        #                   i
        #[40 28]           stack
        stack = []
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<num:
                index = stack.pop()
                temperatures[index] = i-index
            
            stack.append(i)
        while stack:
            index = stack.pop()
            temperatures[index] = 0
        return temperatures