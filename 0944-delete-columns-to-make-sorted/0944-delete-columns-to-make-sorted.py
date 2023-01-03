class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m , n = len(strs), len(strs[0])
        count = 0
        for j in range(n):
            for i in range(1,m):
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    count += 1
                    break
                
        return count 