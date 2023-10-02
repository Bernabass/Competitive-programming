class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def rec(k, start):
            if not k:
                return start
                        
            left, right = start, start + 1
            count = 0
            while left <= n:
                count += min(right, n + 1) - left
                left *= 10
                right *= 10
                
            if count <= k:
                return rec(k - count, start + 1)
            
            return rec(k - 1, start*10)
        
        return rec(k - 1, 1)