class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for key, val in num_dict.items():
            if val == 1:
                return key