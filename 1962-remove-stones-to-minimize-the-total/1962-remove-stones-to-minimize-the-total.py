class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for _ in range(k):
            largest = heapq.heappop(piles)
            largest -= int(largest / 2)
            heapq.heappush(piles,largest)
            
        return -(sum(list(piles)))