class Solution:
    def countArrangement(self, n: int) -> int:
        count, nums = [0], list(range(1, n+1))
        
        def back_track(pos, nums):
            if not nums:
                count[0] += 1           
            
            for i in range(len(nums)):
                if not(pos % nums[i]) or not(nums[i] % pos):
                    back_track(pos+1, nums[:i] + nums[i+1:])
                    
                       
        back_track(1, nums)
        
        return count[0]