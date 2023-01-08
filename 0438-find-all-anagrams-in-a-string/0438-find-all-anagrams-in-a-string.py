class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        window_size = len(p)
        if window_size > n:
            return []
        anagram = Counter(p)
        window, res = defaultdict(int), []
        for _ in range(window_size):
            window[s[_]] += 1
            if window == anagram:
                res.append(0)
    
        for idx in range(window_size,n):
            window[s[idx-window_size]] -= 1
            window[s[idx]] += 1
            if Counter(window) == anagram:
                res.append(idx-window_size+1)
        
        return res