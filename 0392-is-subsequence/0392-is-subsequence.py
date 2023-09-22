class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def rec(idx, string):
            if idx == len(s):
                return True
            
            if s[idx] in string:
                return rec(idx + 1, string[string.index(s[idx]) + 1 : ])
            
        return rec(0, t)