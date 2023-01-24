class Solution:
    def largestNumber(self, nums: List[int]) -> str:     
        nums = list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]>nums[i]+nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                
                    
        output="".join(nums).lstrip("0")
        return output or "0"