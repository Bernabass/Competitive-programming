class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator = 0
        for i in range(len(nums)):
            nums[i] += accumulator
            accumulator = nums[i]
            
        return nums