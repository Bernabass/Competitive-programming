class Solution:
    def largestNumber(self, nums: List[int]) -> str:     
        nums, N = list(map(str,nums)), len(nums)
        
        for i in range(N):
            for j in range(i+1, N):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                      
        return "".join(nums).lstrip("0") or "0"