class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        window_size = len(p)
        if window_size > n:
            return []
        anagram = Counter(p)
        window, res = defaultdict(int), []
        for i in range(window_size):
            window[s[i]] += 1
            if window == anagram:
                res.append(0)
        
    
        for idx in range(window_size,n):
            window[s[idx-window_size]] -= 1
            if window[s[idx-window_size]] <= 0:
                window.pop(s[idx-window_size])
            window[s[idx]] += 1
            if window == anagram:
                res.append(idx-window_size+1)
        
        return res