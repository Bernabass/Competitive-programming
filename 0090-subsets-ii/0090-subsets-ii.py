class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        def back_track(idx, collected):
            if idx == len(nums):
                ans.add(tuple(collected))
                return
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                    
                back_track(i + 1, collected + [nums[i]])
                back_track(i + 1, collected)
                
        back_track(0, [])
                
        return ans