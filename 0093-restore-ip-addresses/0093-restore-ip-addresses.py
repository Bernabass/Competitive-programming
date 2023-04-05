class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12:
            return []
        
        ans = set()
        
        def back_track(start, prev):
            if start == n:
                if len(prev) == 4:
                    ans.add(".".join(prev))
                    
                return
            
            for i in range(start, n):
                if len(prev) < 3:
                    curr = int(s[start:i+1])
                    if str(curr) != s[start:i+1]:
                        break
                    
                else:
                    curr = int(s[start:])
                    if str(curr) != s[start:]:
                        break
                    i = n - 1
                
                if 0 <= curr <= 255:
                    prev.append(str(curr))
                    back_track(i+1, prev)
                    prev.pop()
                    
                else:
                    return
                    
            return
        
        back_track(0, [])
        
        return ans