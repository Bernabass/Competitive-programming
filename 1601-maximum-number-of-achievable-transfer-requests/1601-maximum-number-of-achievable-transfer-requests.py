class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        N = len(requests)
        self.max_achievable = 0
        
        def back_track(idx, info, achieved):
            if idx == N:
                if not any(info):
                    self.max_achievable = max(self.max_achievable, achieved)
                    
                return
            
            _from, _to = requests[idx]
            info[_from] += 1
            info[_to] -= 1
            achieved += 1
            back_track(idx+1, info, achieved)
            info[_from] -= 1
            info[_to] += 1
            achieved -= 1
            back_track(idx+1, info, achieved)
            
            return
        
        back_track(0, [0]*n, 0)
        
        return self.max_achievable