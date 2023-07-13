class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def back_track(target):
            if target in memo:
                return memo[target]
            
            if target < 0:
                return 0
            
            if target == 0:
                return 1
            
            count = 0
            for num in nums:
                count += back_track(target - num)
                
                
            memo[target] = count
                
            return count
        
        return back_track(target)