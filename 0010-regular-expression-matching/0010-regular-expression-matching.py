class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        
        @cache
        def dp(i, j):
            if i == ns and j == np:
                return True
            
            if j >= np:
                return False
            
            if  i < ns and (s[i] == p[j] or p[j] == ".") and dp(i + 1, j + 1):
                return True
            
            
            if j + 1 < np and p[j + 1] == "*":
                if dp(i, j + 2):
                    return True
                
                if p[j].isalpha():
                    for idx in range(i, ns):
                        if s[idx] == p[j]:
                            if dp(idx + 1, j + 2):
                                return True

                        else:
                            break
                    
                else:
                    for idx in range(i, ns):
                        if dp(idx + 1, j + 2):
                            return True
                    
        return dp(0, 0)        