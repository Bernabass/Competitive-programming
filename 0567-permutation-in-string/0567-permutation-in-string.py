class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s, p = s2, s1
        n = len(s)
        window_size = len(p)
        res = []
        anagram, window = Counter(p), Counter(s[:window_size])
        if window == anagram:
            res.append(0)
        
        for idx in range(window_size, n):
            front, back = s[idx-window_size], s[idx]
            window[front] -= 1
            if window[front] <= 0:
                window.pop(front)
            window[back] += 1
            
            if window == anagram:
                res.append(idx - window_size + 1)
        
        return res
        