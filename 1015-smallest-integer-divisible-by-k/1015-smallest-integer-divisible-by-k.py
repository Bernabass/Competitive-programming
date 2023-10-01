class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 0
        for length in range(1, k + 1):
            rem = (rem*10 + 1) % k
            
            if not rem:
                return length
            
        return -1