class Solution:
    def strangePrinter(self, s: str) -> int:
        
        @cache
        def dp(i, j):
            if i > j:
                return 0

            ans = dp(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    ans = min(ans, dp(i, k - 1) + dp(k, j - 1))
                
            return ans
        
        s = re.sub(r'(.)\1*', r'\1', s)
        
        return dp(0, len(s) - 1)