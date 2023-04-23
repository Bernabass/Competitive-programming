class Solution:
    def twoEggDrop(self, n: int) -> int:
        count = 0
        res = 0
        
        while (n - count) > 0:
            n -= count
            res += 1
            count += 1
            
        return res