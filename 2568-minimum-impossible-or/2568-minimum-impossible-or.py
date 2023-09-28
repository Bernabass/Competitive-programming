class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        pos_ans = 2
        
        for i in range(33):
            if (pos_ans ** i) not in nums:
                return pos_ans ** i