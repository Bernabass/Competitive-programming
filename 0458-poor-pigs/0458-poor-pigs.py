class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        """
        buckets = 8
        
        A      B      C
        
        1457   2467   3567
        
        ""
        A
        B
        C
        AB
        AC
        BC
        ABC
         
        so, with n pig = [2**(n - 1) + 1, 2**n]
        
        """

        
        def pigs(n):
            return log2(n)
        
        ratio = ceil(minutesToTest / minutesToDie)
        
        if ratio == 1:
            return ceil(pigs(buckets))
            
        return ceil(pigs(buckets) / log2(ratio + 1))