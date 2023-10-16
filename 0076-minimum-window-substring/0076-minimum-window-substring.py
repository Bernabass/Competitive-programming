class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        left, N = 0, len(s)
        window = Counter()
        ans = [inf, inf]
        
        def good(dict1):
            if len(dict1) != len(target):
                return False
            
            for key in dict1:
                if key not in target or dict1[key] < target[key]:
                    return False
                
            return True
    
        for right, char in enumerate(s):
            if char in target:
                window += Counter(char)
                
            while left < N and good(window):
                if right - left + 1 < ans[1]:
                    ans = [left, right - left + 1]
                window -= Counter(s[left])
                if window[s[left]] == 0:
                    del window[s[left]]
                    
                left += 1
                      
        index, length = ans
        if index == inf:
            return ""
        
        return s[index:index + length]
            
        
            
            