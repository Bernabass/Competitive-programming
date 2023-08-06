class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        @cache
        def dp(uniques, repeats, rem, x):
            if x == 0:
                repeats += 1
                x = 1
                
            if uniques > rem:
                return 0
            
            if rem == 0:
                return 1
            
            res = 0
            if uniques > 0:
                res += dp(uniques - 1, repeats, rem - 1, x - 1) * uniques
                
            if repeats > 0:
                res += dp(uniques, repeats - 1, rem - 1, x - 1) * repeats
                
            return res

        
        return dp(n, 0, goal, k + 1) % (10 ** 9 + 7)