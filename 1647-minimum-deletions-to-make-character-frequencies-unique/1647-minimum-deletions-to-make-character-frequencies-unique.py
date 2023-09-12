class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        arr = sorted(freq.values())
        used, ans = set(), 0
        
        for count in arr:
            while count and count in used:
                count -= 1
                ans += 1
                
            if count:
                used.add(count)
                
        return ans
                
            