class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        subsequence, ans = [], []
        
        for obs in obstacles:
            k = bisect.bisect_right(subsequence, obs)
            
            if len(subsequence) == k: 
                subsequence.append(obs)
            else: 
                subsequence[k] = obs
                
            ans.append(k+1)
            
        return ans