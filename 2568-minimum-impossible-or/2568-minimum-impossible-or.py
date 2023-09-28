class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(33):
            ans = 1 << i
            if ans not in nums:
                return ans