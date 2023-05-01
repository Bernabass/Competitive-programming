class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = y = 0
        
        for num in nums:
            a = (x & ~num) | (~x & y & num)
            b = ~x & (y ^ num)
            x, y = a, b
            
        return x | y
