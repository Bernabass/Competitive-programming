class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a = (num ^ a) & (~b)
            b = (num ^ b) & (~a)

        return a