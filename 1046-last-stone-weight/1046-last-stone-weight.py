class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            heapq._heapify_max(stones)
            y = heapq.heappop(stones)
            heapq._heapify_max(stones)
            x = heapq.heappop(stones)
            heapq._heapify_max(stones)
            smashed = y - x
            
            if smashed:
                heapq.heappush(stones,smashed)
            heapq._heapify_max(stones)
            
        if not stones:
            return 0
        
        else:
            return stones[0]