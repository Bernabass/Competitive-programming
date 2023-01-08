class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        window_size = len(p)
        if window_size > n:
            return []
        check = Counter(p)
        window = deque()
        res = []
        for _ in range(window_size):
            window.append(s[_])
        if Counter(window) == check:
            res.append(0)
    
        for i in range(window_size,n):
            window.popleft()
            window.append(s[i])
            if Counter(window) == check:
                res.append(i-window_size+1)
        
        return res