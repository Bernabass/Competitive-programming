class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        children = [0]*k
        min_unfairness = [float("inf")]
        
        if n == k:
            return max(cookies)
        
        def back_track(start):
            if start == n:
                min_unfairness[0] = min(min_unfairness[0], max(children))
                    
                return
            
            for idx in range(k):
                children[idx] += cookies[start]
                back_track(start+1)
                children[idx] -= cookies[start]
                    
            return
        
        back_track(0)
        
        return min_unfairness[0]