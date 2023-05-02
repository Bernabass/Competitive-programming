class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = math.prod(nums)
        if not prod:
            return 0
        
        return prod//(abs(prod))