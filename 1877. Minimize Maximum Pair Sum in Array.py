class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        out=0
        for i in range(len(nums)//2):
            if nums[i]+nums[len(nums)-i-1]>out:
                out=nums[i]+nums[len(nums)-i-1]
        return out