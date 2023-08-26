class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        
        @cache
        def dp(idx, prev):            
            max_len = 0
            for i in range(len(pairs)):
                if pairs[i][0] > prev:
                    max_len = max(max_len, dp(i + 1, pairs[i][1]) + 1)
                    
            return max_len
                    
        return dp(0, -inf)