class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(set(pattern)) != len(set(s)) or len(s) != len(pattern):
            return False
        info = dict(zip(pattern,s))
        
        for i in range(len(pattern)):
            if info[pattern[i]] != s[i]:
                return False
        
        return True