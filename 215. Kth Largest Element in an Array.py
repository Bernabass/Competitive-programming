class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        for j in range(k):
            out=heapq.heappop(nums)
        return -out