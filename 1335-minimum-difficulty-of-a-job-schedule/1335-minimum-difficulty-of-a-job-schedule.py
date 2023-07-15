class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        suffix_max = [0] * (n-1) + [jobDifficulty[n - 1]]  
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(jobDifficulty[i], suffix_max[i + 1])
        
        @cache
        def back_track(idx, d):
            if n - idx == 1:
                return jobDifficulty[idx]
            
            if d == 1:
                return suffix_max[idx]
            
            ans = float("inf")
            curr_max = float("-inf")
            
            for i in range(idx, n - d + 1):
                curr_max = max(curr_max, jobDifficulty[i])
                ans = min(ans, curr_max + back_track(i + 1, d - 1))
                
            return ans
        
        return back_track(0, d)