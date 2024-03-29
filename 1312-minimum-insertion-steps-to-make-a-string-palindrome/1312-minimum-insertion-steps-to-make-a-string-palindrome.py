class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(l, r):
            if r <= l:
                return 0
            if s[l] == s[r]:
                return rec(l + 1, r - 1)
            else:
                return min(rec(l, r - 1), rec(l + 1, r)) + 1
            
        return rec(0, len(s) - 1)