class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones)-heapq.heappop(stones))
        return -1*stones[0]