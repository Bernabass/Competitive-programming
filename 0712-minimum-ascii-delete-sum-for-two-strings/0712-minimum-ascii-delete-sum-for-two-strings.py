class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        sum1 = self.suffix_sum(s1) + [0]
        sum2 = self.suffix_sum(s2) + [0]

        @cache
        def dp(i, j):
            if i == n1:
                return sum2[j]
            
            if j == n2:
                return sum1[i]
            
            
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            
            else:
                return min(ord(s1[i]) + dp(i + 1, j), ord(s2[j]) + dp(i, j + 1))
            
            
        return dp(0, 0)
            
               
            
    def suffix_sum(self, string):
        result = [0] * len(string)
        result[-1] = ord(string[-1])
        for i in range(len(string)-2, -1, -1):
            result[i] = result[i+1] + ord(string[i])
            
        return result