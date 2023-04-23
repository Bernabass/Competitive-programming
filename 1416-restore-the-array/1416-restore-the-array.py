class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n= len(s)

        @cache
        def dfs(idx):
            if not idx:
                return 1

            ans = 0
            for i in range(idx-1, -1, -1):
                if s[i] == "0": 
                    continue
                    
                elif int(s[i:idx]) <= k:
                    ans += dfs(i) % (10**9 + 7)
                    
                elif int(s[i:idx]) > k:
                    break

            return ans

        return dfs(n) % (10**9+7)