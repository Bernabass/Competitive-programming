class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def back_track(idx, prev):
            if idx == len(nums):
                ans.append(prev[:])
                return
            
            
            back_track(idx + 1, prev)
            back_track(idx + 1, prev + [nums[idx]])
          
        back_track(0, [])
                
        return ans     