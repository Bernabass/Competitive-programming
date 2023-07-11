class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        info = {}
        for idx, val in enumerate(nums):
            x = target - val
            if x in info:
                return [info[x], idx]
            
            else:
                info[val] = idx