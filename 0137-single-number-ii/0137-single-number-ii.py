class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0

        for num in nums:
            twos = twos | (ones & num)
            ones = ones ^ num
            num = ~(ones & twos)
            ones &= num
            twos &= num
            
        return ones