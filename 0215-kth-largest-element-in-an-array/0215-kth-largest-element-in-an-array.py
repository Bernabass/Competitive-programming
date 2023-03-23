class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = max(nums) - min(nums) + 1
        _min = min(nums)
        buckets = [0]*n
        target = len(nums) - k + 1
        
        for num in nums:
            buckets[num-_min] += 1
            
        count = 0   
        for idx, val in enumerate(buckets):
            count += val
            if count >= target:
                return idx + _min