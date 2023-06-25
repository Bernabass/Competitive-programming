class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        @cache
        def dfs(diff,idx):
            if idx >= n:
                return -inf if diff else 0

            curr = rods[idx]
            
            return max(dfs(diff-curr, idx+1), dfs(diff+curr, idx+1) + curr, dfs(diff, idx+1))

        return dfs(0, 0)