class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)


        while len(stones) > 1:
            
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)

            c = a-b

            if c == 0:
                pass
            else:
                heapq.heappush_max(stones,c)
        
        if stones:
            return stones[0]
        return 0