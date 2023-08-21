class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            max_diff = max(curr_diff, max_diff)
            
        return max_diff