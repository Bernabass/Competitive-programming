class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = left = 0
        valids = defaultdict(int)
        
        for right in range(n):
            valids[s[right]] += 1
            
            while len(valids) == 3:
                ans += n - right
                
                valids[s[left]] -= 1
                if not valids[s[left]]:
                    del valids[s[left]]
                    
                left += 1
                
                
        return ans