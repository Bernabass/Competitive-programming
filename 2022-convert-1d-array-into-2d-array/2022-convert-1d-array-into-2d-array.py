class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        res = [[0]*n for _ in range(m)]
        for idx, val in enumerate(original):
            i, j = idx // n, idx % n
            res[i][j] = val
            
        return res