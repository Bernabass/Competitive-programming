class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp_matrix = [[0]*len(s) for i in range(n)]
        
        k = 0
        while k < n:
            for i in range(n-k):
                j = i + k
                if i == j:
                    dp_matrix[i][j] = 1
                elif s[i] == s[j]:
                    dp_matrix[i][j] = dp_matrix[i+1][j-1] + 2
                else:
                    dp_matrix[i][j] = max(dp_matrix[i][j-1], dp_matrix[i+1][j])
                    
            k += 1
                 
        return dp_matrix[0][n-1]