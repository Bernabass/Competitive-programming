class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        max_heap, min_heap = [], []
        
        for i in range(len(weights) - 1):
            val = weights[i] + weights[i + 1]
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
            
            if len(min_heap) > k - 1:
                heapq.heappop(min_heap)
                heapq.heappop(max_heap)
                
        return sum(min_heap) + sum(max_heap)