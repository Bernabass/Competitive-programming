class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if i == len(s) and j == len(p):
                return True

            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                return (dp(i, j + 2) or (match and dp(i + 1, j)))

            return match and dp(i + 1, j + 1)

        return dp(0, 0)