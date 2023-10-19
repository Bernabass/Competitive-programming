class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        
        @cache
        def dp(i, j):
            if i == N1:
                return N2 - j
            
            if j == N2:
                return N1 - i

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)

            insert = dp(i, j + 1) + 1
            delete = dp(i + 1, j) + 1
            replace = dp(i + 1, j + 1) + 1

            return min(insert, delete, replace)

        return dp(0, 0)