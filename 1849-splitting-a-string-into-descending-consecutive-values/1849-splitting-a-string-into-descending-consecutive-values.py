class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def split(prev, start):
            for idx in range(start, n):
                curr = int(s[start:idx+1])
                
                if not start:
                    if split(curr, idx+1):
                        return True
                
                elif prev - curr == 1:
                    if idx == n-1:
                        return True
                    
                    if not curr:
                        if int(s[idx+1:]):
                            return False

                        return True
                    
                    return split(curr, idx+1)
                    
                elif curr - prev > 1:
                    return False
                    
            return False
        
        return split([], 0)