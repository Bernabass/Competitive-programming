class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        dictionary = set(dictionary)
        
        @cache
        def dp(start):
            min_extras = N - start
            for i in range(start, N):
                for j in range(i, N):
                    curr = s[i : j + 1]
                    if curr in dictionary:
                        min_extras = min(min_extras, i - start + dp(j + 1))
                        
            return min_extras
        
        return dp(0)