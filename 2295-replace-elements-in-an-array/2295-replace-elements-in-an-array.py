class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums = dict(zip(nums,range(len(nums))))
        res = [[]] * len(nums)
        
        for idx, new_idx in operations:
            nums[new_idx] = nums[idx]
            del nums[idx]

        for val, idx in nums.items():
            res[idx] = val
            
        return res