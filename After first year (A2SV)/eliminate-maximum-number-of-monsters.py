class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = [math.ceil(dist[i] / speed[i]) for i in range(len(dist))]
        arr.sort()

        for idx, num in enumerate(arr):
            if idx >= num:
                return max(1, idx)

        return max(1, len(dist))