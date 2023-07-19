class Solution:
    def numTilings(self, n: int) -> int:
        even_2 = odd_2 = 1
        even_1 = odd_1 = 2
        mod = 10**9 + 7

        for i in range(3, n + 2):
            prev_even_1, prev_odd_1 = even_1, odd_1
            odd_1 += even_1 % mod
            even_1 += (even_2 + 2 * odd_2) % mod
            odd_2, even_2 = prev_odd_1, prev_even_1
            
        return even_2 % mod