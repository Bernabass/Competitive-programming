class Solution:
    def splitString(self, s: str) -> bool:
        s = s.lstrip()
        prev = -1
        level, n = 0, len(s)
        
        def split(idx, prev, level):
            if idx == n:
                return level >= 2
            
            for i in range(idx, n):
                curr = int(s[idx:i+1])
                
                if prev == -1 or prev - curr == 1:
                    if split(i+1, curr, level+1):
                        return True
                    
            return False
        
        return split(0, prev, level)