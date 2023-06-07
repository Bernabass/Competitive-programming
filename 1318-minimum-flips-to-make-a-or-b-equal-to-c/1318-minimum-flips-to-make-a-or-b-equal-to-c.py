class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        operation = 0
        while a or b or c:
            curr_bit_a = a & 1
            curr_bit_b = b & 1
            curr_bit_c = c & 1
            
            if curr_bit_c:
                operation += not(curr_bit_a or curr_bit_b)
                
            else:
                operation += curr_bit_a + curr_bit_b
                
            a >>= 1
            b >>= 1
            c >>= 1
            
        return operation