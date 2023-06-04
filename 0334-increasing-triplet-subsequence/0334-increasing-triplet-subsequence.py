class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        _min, _max = nums[0], float("inf")
        
        for i in range(1, len(nums)):
            if nums[i] > _max:
                return True
            
            elif nums[i] < _min:
                _min = nums[i]
                
            elif _min < nums[i] < _max:
                _max = nums[i]
                
        return False