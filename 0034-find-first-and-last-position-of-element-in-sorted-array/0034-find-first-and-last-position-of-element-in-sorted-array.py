class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums,target)
        right = bisect_right(nums,target)- 1
        res = [-1,-1]
        if not nums:
            return res
    
        if 0 <= left < len(nums) and nums[left] == target:
            res[0] = left
        if 0 <= right < len(nums) and nums[right] == target:
            res[1] = right
        
        return res