class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def back_track(target):
            if target < 0:
                return 0
            
            if target == 0:
                return 1
            
            count = 0
            for num in nums:
                count += back_track(target - num)
                
            return count
        
        return back_track(target)