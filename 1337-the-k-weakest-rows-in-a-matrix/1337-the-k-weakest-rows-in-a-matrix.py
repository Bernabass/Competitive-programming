class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(row), idx) for idx, row in enumerate(mat)]
        soldiers.sort()
        ans = []
        
        for i in range(k):
            _, idx = soldiers[i]
            ans.append(idx)
            
        return ans