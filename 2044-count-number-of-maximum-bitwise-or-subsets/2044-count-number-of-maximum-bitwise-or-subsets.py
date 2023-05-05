class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_OR = reduce(or_, nums)
        
        def back_track(idx, prev, count):
            if idx == len(nums):
                return 0
            
            for i in range(idx, len(nums)):
                if prev|nums[i] == max_OR:
                    count += 1
                    
                count += back_track(i+1, prev|nums[i], 0)
                   
            return count
        
        return back_track(0, 0, 0)