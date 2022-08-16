class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        out=[]
        for i in matrix:
            out=[*out,*i]
        heapq.heapify(out)
        for i in range(k-1):
            heapq.heappop(out)
        return out[0]