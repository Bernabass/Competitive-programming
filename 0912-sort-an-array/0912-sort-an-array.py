class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_array = []
        heapq.heapify(nums)
        
        while nums:
            sorted_array.append(heapq.heappop(nums))
            
        return sorted_array