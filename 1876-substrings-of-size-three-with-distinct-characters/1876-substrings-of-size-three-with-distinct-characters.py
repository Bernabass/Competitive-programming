class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        goods = 0
        
        for i in range(n-2):
            if len(set(s[i:i+3])) == 3:
                goods += 1
            
        return goods