class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = n.bit_length()
        
        for _ in range(length):
            prev = 1 & n
            n >>= 1
            curr = 1 & n
            
            if prev == curr:
                return False
            
        return True