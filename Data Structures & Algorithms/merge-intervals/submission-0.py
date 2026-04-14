class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for s, e in intervals:
            lastend = output[-1][1]

            if s<= lastend:
                output[-1][1] = max(lastend,e)
            else:
                output.append([s, e])

        return output