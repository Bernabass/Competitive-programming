class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        window_size = len(s1)
        permuation, window = Counter(s1), Counter(s2[:window_size])
        if window == permuation:
            return True
        
        for idx in range(window_size, n):
            front, back = s2[idx-window_size], s2[idx]
            window[front] -= 1
            if window[front] <= 0:
                window.pop(front)
            window[back] += 1
            
            if window == permuation:
                return True
        
        return False
        