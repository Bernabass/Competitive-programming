class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if numOnes >= k:
            return k
    
        ans += numOnes
        k -= numOnes
        
        if numZeros >= k:
            return ans
        
        k -= numZeros
        
        return ans - k