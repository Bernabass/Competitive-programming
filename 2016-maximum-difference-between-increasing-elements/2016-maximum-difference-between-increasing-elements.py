class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = nums[-1]
        res = -1
        
        for i in range(n-2,-1,-1):
            if nums[i] < maxx:
                res = max(res,maxx - nums[i])
                
            maxx = max(maxx,nums[i])
            
        return res       