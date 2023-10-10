class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        LPS = [0] * N
        i, j = 1, 0
        while i < N:
            if s[i] == s[j]:
                i += 1
                j += 1
                LPS[i - 1] = j

            elif j:
                j = LPS[j - 1]

            else:
                i += 1
                                    
        return s[0 :LPS[-1]]