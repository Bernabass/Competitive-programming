class Solution:
    def countVowelPermutation(self, n: int) -> int:
        next_candidates = {"a":("e"), "e":("a", "i"), "i":("a", "e", "o", "u"), "o":("i", "u"), "u":("a")}
        
        @cache
        def back_track(arr, n):
            if not n:
                return 1
            
            ans = 0
            for char in arr:
                ans += back_track(next_candidates[char], n - 1) % (10**9 + 7)
                
            return ans
        
        return back_track(("a", "e", "i", "o", "u"), n) % (10**9 + 7)