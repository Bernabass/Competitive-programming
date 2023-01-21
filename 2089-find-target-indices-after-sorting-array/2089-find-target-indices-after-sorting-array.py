class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        
        for idx, val in enumerate(nums):
            if val == target:
                res.append(idx)
                
        return res